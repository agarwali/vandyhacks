from application import app, getMailer
from flask_mail import Message
from application.config import *
from application.models import getModelFromName
from application.models import model
from application.models.userModel import User
from application.models.issuesModel import Issues
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
@app.route('/user/', methods = ['GET','POST'])
def userForm ():
  if request.method == "GET":
    return render_template("views/user/userFormView.html", config = config)
  elif request.method == "POST":
    data=request.form
    new_user=User.create(first_name=data['first_name'],
                         last_name=data['last_name'],
                         middle_initial=data['middle_initial'],
                         address1=data['address1'],
                         address2=data['address2'],
                         city=data['city'],
                         zip_code=data['zip_code'],
                         state=data['state'])
    new_user.save()
    return redirect("user/rateIssues") 