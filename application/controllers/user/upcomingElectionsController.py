from application import app, getMailer
from flask_mail import Message
from application.config import *
from application.models import getModelFromName
from application.models import model
from application.models.userModel import User
from application.models.issuesModel import Issues
from urlparse import urlparse
from application.util.electionInfo import ElectionInfo

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
@app.route('/user/upcomingElections/', methods = ['GET'])
def upcomingElections ():
  if request.method == "GET":

    elect = ElectionInfo(config['keys']['googleapi'])
    elections = elect.get_elections()
    #elections=[{"EID":"1","name":"First", "date":"12/12/12"},{"EID":"2","name":"Second", "date":"13/13/13"},{"EID":"3","name":"Third", "date":"14/14/14"}]
    return render_template("views/user/upcomingElectionsView.html", config = config, elections=elections)
