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
@app.route('/user/rateIssues', methods = ['GET','POST'])
def rateIssues ():
  if request.method == "GET":
    return render_template("views/user/rateIssuesView.html", config = config)
  elif request.method == "POST":
    data=request.form
    if data['button'] == "save":
      issuesList = request.form.getlist('issueChoices')
      x=1
      issues=', '.join(issuesList)
      return render_template("views/user/rateIssuesView.html", config = config,x=x, il=issuesList, issuesSTR = issues)
     
    elif data['button'] == "post":
      issue=Issues.create()
      for key in data:
        if key=="Women":
          issue.womenAndMinorities=data[key] 
        elif key=="Same-Sex":
          issue.abortion=data[key] 
        elif key=="Guns":
          issue.guns=data[key] 
        elif key=="Obamacare":
          issue.obamacare=data[key]
        elif key=="Immigration":
          issue.immigration=data[key]
        issue.user=1
      issue.save()
      
      return redirect("user/upcomingElections") 