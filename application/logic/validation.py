# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from configure import Configuration
from datetime import timedelta
from application.config import config
from application.models import getModelFromName
from functools import wraps
from flask import request, redirect, url_for, session, abort, flash, app
import os, re, time
from application.models import model
from application import app

roleConfig = Configuration.from_file('config/roles.yaml').configure()
#WE don't use roles.yaml anymore
### FOR PASSWORDLESS LOGIN -CDM 20161004 ###

def getUserFromEmail(email):
  T = model.User
  q = model.User.select().where(T.email == email)
  if q.exists():
    for row in q:
      return row
  else:
    return False

def tokenExsist(tok):
  '''Checks to make sure that the token exist in our system'''
  T = model.User
  q = model.User.select().where(T.token == tok)
  if q.exists():
    return True
  else:
    return False

def tokenOk(tok):
  token = tokenExsist(tok)
  if token != False:
    T = model.User
    user = T.get(T.token == tok)
    now  = time.time()
    isTokenValid = False
    timeLeft     = (now - float(user.time))
   
    isTokenVaild = timeLeft < (config.application.tokenTimeout * 60)
    if isTokenVaild:
      print "We have {0} left.".format(timeLeft)
      return True
  return False

def getUserFromToken(tok):
  acceptToken = tokenExsist(tok)
  if acceptToken == True:
    try:
      T = model.User
      for row in T.select().where(T.token==tok):
        return row
    except Exception as e:
      print e
  return None
  
def setSessionVariables(tok):
  user  = getUserFromToken(tok)
  session['email'] = user.email
  session['token']   = tok
  return True
  
def check_session ():
  def decorator (fun):
    @wraps(fun)
    def decorated_fun (*args, **kwargs):
      if session.get('token') and session.get('email'):
        session.permanent=True
        app.permanent_session_lifetime = timedelta(minutes=60)
        return fun(*args, **kwargs)
      else:
        flash("System could not find session, may be expired.")
        return redirect(url_for("getEmail"), code = 302)
    return decorated_fun
  return decorator
  
  
  
'''Can we possibly remove all the template default validation stuff???'''
### THIS IS FROM THE TEMPLATE ###
def getUsernameFromEnv():
  # FIXME: This is wrong.
  return os.getenv("USER")
  
def getRoles(username):
  roles = []
  for role in roleConfig:
    # print "Checking role '{0}'".format(role)
    if userHasRole (username, role):
      roles.append(role)
  return roles

def doesUserHaveRole (role):
  username = getUsernameFromEnv()
  roles = getRoles(username)
  result = (role in roles)
  # print "User '{0}' has roles {1}; returning {2}".format(username, roles, result)
  return result

def userHasRole (username, role):
  # print "Checking role '{0}' for '{1}'".format(role, username)
  # print "There are {0} things in role '{1}'".format(len(roleConfig[role]), roleConfig[role])
  for ug in roleConfig[role]:
    
    # We may be referencing another "group," which is a role.
    # Recursively search.
    # print "Handing user/group: '{0}'".format(ug)
    
    # If the ug is an exact match for the username, it means we 
    # have directly coded a username into a group. We should 
    # return True, because we want them to have access. 
    if ug == config.flask.username:
      return True
    
    if re.match('group', ug):
      superRole = re.split(" ", ug)[1]
      return userHasRole (username, superRole)
      
    # We may find it is a database lookup.
    if re.match('database', ug):
      # Get the name of the database
      db = re.split(" ", ug)[1]
      print "DB is '{0}'".format(db)
      # Get the actual model from the name of the model.
      m = getModelFromName(db)
      print "Model: {0}".format(m)
      
      # Do a "get", and require that their username and role are both
      # set. For example, look for {jadudm, admin}, not just the username.
      result = m.select().where(m.username == username, m.role == role).count()
      if result > 0:
        print "User '{0}' validated via database {1}".format(username, db) 
        return True
      else:
        print "User '{0}' not found in database {1}".format(username, db)
        return False
    
    # Check if they are in the Active Directory
    if re.match('AD', ug):
      # FIXME: Implement this.
      return False
      
    # If the keyword "ANY" appears, it means anyone 
    # is good to go.
    if re.match("ANY", ug):
      return True
      
# https://realpython.com/blog/python/primer-on-python-decorators/
def checkValidUser (fun):
  @wraps(fun)
  def wrapper (*args, **kwargs):
    print "Is Valid User"
    return fun(*args, **kwargs)
  return wrapper

def require_role (requiredRole):
  def decorator (fun):
    @wraps(fun)
    def decorated_fun (*args, **kwargs):
      # print "Is Valid Role: %s" % expected_args[0]
      if userHasRole (getUsernameFromEnv(), requiredRole):
        print "User has role."
        return fun(*args, **kwargs)
      else:
        print "User does not have role."
        return redirect(url_for(config.application.default), code = 302)
        # return config.application.noRoleHandler
    return decorated_fun
  return decorator
  
