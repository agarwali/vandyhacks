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
@app.route('/user/open/<int:EID>', methods = ['GET','POST'])
def openBallot (EID):
  if request.method == "GET":
    return render_template("views/user/userFormView.html", config = config)
  elif request.method == "POST":
    return redirect("user/rateIssues") 