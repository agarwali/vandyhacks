from application import app, getMailer
from flask_mail import Message
from application.config import *
from application.models import getModelFromName
from application.models import model
from urlparse import urlparse

import datetime
import os
import random
import re
import time
import uuid
import sys

from flask import \
  flash, \
  make_response, \
  redirect, \
  render_template, \
  request, \
  session, \
  url_for, \
  abort
 
from application.logic.validation import \
  tokenOk, \
  getUserFromEmail, \
  getUserFromToken, \
  setSessionVariables

THECOOKIE = 'internshipcatalog'

# PURPOSE: The initial login page/handler.
@app.route('/', methods = ['GET'])
def getEmail ():
  session['gurumeditation'] = re.sub("-", "", str(str(uuid.uuid4())[:8])).upper()
  session['token'] = None
  session['email'] = None
  resp = make_response(render_template("views/login/emailForm.html", config = config))
  return resp

def checkIfDevUser(email):
  if email == "admin@gmail.com" or email == "employer@gmail.com":
    try:
      newToken = uuid.uuid4()
      T = model.User
      #Update Database
      query = T.update(token = newToken, time = time.time()).where(T.email == email)
      query.execute()
      #Set Session Variables
      setSessionVariables(newToken)
      return True
    except Exception as e:
      return "Fail"
  else:
    return False
    
# PURPOSE: Handle the token request.
@app.route('/gt', methods = ['POST'])
def handleTokenRequest ():
  emailAddr = request.form['email']
  
  '''TODO: Remove the line of code below before going to production'''
  check = checkIfDevUser(emailAddr)
  if check == True:
    return redirect(url_for('upcomingElections'))
  elif check == "Fail":
    flash("Could Not Access Dev account.")
    return redirect(url_for("getEmail"))
    
  returnUser = getUserFromEmail(emailAddr)
  # Check to see if the User is in the system
  if returnUser == False:
    return redirect(url_for("userRegister"))
    
  else:
    T                = model.User
    now              = time.time()
    newToken         = uuid.uuid4()
    query = T.update(token = newToken, time = now).where(T.email == emailAddr)
    query.execute()
    user = getUserFromToken(newToken)
  # Create the URL's
  o = urlparse(request.url)
  target = "http://"
  target += o.hostname
  if o.port:
    target += ":{0}".format(o.port)
  target += "/s/{0}".format(newToken)
  employerIndex = "{0}/s/{1}".format(config.application.url, newToken)
  adminIndex    = "{0}/a/{1}".format(config.application.url, newToken)
  urls = { "employer" : employerIndex}
  # Try to send email if not running locally
  try:
    if not os.getenv("InternshipCatalog"):
      msg = Message("Access Internship Catalog @ {0}".format(datetime.datetime.now().strftime("%Y %m %d - %H:%M")),
        sender = "internshipCatalog@GoIntern.berea.us",
        recipients = [emailAddr]
      )
      msg.body = ""
      
      msg.html = render_template("views/email/employer.html",
          config = config,
          urls   = urls,
          signature = config.signature
        )
      with app.app_context():
        mail = getMailer()
        mail.send(msg)
      # Set Flags and render template
      flags = {}
      flags["local"] = os.getenv("InternshipCatalog")
      resp = make_response(
      render_template("views/login/handleTokenRequestView.html",
        config = config,
        urls = urls,
        flags = flags,
        session = session,
        email = emailAddr
        ))
      return resp
  except Exception as e:
    print e
    flash ("It looks like you might need to try again.")
    return redirect(url_for("getEmail"))
# PURPOSE: Log in with a valid token.
@app.route('/s/<string:tok>', methods = ['GET'])
def login(tok):
  if tokenOk(tok):
    setSessionVariables(tok)
    #print 'email before going into session: {0}'.format(email)
    return redirect(url_for('upcomingElections'))
  else:
    abort(403)