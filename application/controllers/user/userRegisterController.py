from application import app
from flask import abort

# Use individual models as:
# s = models.Student()
# assuming Student is a class in studentModel.py
from application.models import *
from application.models.userModel import User 
from application.config import *
from application.logic.validation import check_session
from application.controllers.login.loginController import handleTokenRequest
from flask import \
    render_template, \
    request, \
    redirect, \
    url_for, \
    session

# PURPOSE: Lets an employer view their posted internship.
@app.route('/user/userRegister/', methods = ['GET','POST'])
def userRegister():
    if request.method=="GET":
        return render_template("views/user/userRegisterView.html", config = config)
    if request.method=="POST":
        data=request.form
        new_user=User.create(first_name=data['first_name'], last_name=data['last_name'], email=data['email'],time=0, token=0)
        new_user.save()
        return handleTokenRequest()

