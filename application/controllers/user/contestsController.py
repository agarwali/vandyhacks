from application import app
from application.config import *
from application.util.electionInfo import ElectionInfo
from application.models import getModelFromName
from application.models import model
from application.models.userModel import User


import datetime
import os
import random
import re
import time
import uuid
import sys

from flask import \
  redirect, \
  render_template, \
  url_for, \
  abort,\
  request


@app.route('/user/contests/<eid>', methods = ['GET'])
def contests (eid):
  if request.method == "GET":
    elect = ElectionInfo(config['keys']['googleapi'])
    user = User.select().where(User.UID==0).get()
    address = "{0} {1} {2} {3} {4}".format(user.address1, user.address2, user.city, user.state)
    elections = elect.get_voterInfo(address, eid)
    #elections=[{"EID":"1","name":"First", "date":"12/12/12"},{"EID":"2","name":"Second", "date":"13/13/13"},{"EID":"3","name":"Third", "date":"14/14/14"}]
    return render_template("views/user/contestsView.html", config = config, elections=elections)
