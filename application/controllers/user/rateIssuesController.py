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
    issue=Issues.get(Issues.user==1)
    return render_template("views/user/rateIssuesView.html", config = config, issue = issue)
  elif request.method == "POST":
    data=request.form
    if data['button'] == "save":
      user=User.get(User.UID==1)
      issue=Issues.get(Issues.user==1)
      issuesList = request.form.getlist('issueChoices')
      x=1
      issues=', '.join(issuesList)
      print issues
      return render_template("views/user/rateIssuesView.html", config = config,x=x, issue=issue, il=issuesList, issuesSTR = issues)

    elif data['button'] == "post":
      user=User.get(User.UID==1)
      issue=Issues.get(Issues.user==1)
      for key in data:
        if key=="Legally":
          issue.womenAndMinorities=int((data[key]/2)*100)
        elif key=="Homosexuality":
          issue.sameSexMarriage=int((data[key]/2)*100)
        elif key=="Gun":
          issue.guns=int((data[key]/2)*100)
        elif key=="Abortion":
          issue.abortion=int((data[key]/2)*100)
        issue.user=1
      issue.save()

      return redirect("user/upcomingElections")
