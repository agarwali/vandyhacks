from application import app
from application.config import *
from application.models import getModelFromName
from application.models.userModel import User
from application.models.issuesModel import Issues
from application.utils.electionInfo import ElectionInfo

from flask import \
  redirect, \
  render_template, \
  request, \
 

@app.route('/contests/<election_id>/<index>', methods = ['GET'])
def userForm (election_id, office):
    user = User.select().where(User.id=1).get()
    electionInfo = ElectionInfo(cfg['keys']['googleapi'])
    constests = electionInfo.get_voteInfo(user.address, election_id)['contests']
    contest = constests[index-1]
    

    return render_template("views/user/contest.html", config = config, contest = constest)
