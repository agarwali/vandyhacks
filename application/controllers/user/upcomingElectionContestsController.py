from application import app
from application.config import *
from application.models import getModelFromName
from application.models.userModel import User
from application.models.issuesModel import Issues
from application.util.electionInfo import ElectionInfo
from application.util.sentimentAnalyzer import SentimentAnalyzer
from random import random

from flask import \
  redirect, \
  render_template, \
  request \

from playhouse.shortcuts import model_to_dict

from application.models.userModel import User
from application.models.issuesModel import Issues

@app.route('/contests/<election_id>/<int:index>', methods = ['GET'])
def ballot (election_id, index):
    user = User.select().where(User.UID==1).get()
    issue = Issues.get(Issues.user==1)
    issue = model_to_dict(issue)
    print issue
    address = "{0} {1} {2} {3}".format(user.address1, user.address2, user.city, user.state)
    electionInfo = ElectionInfo(config['keys']['googleapi'])
    sentimentAnalyzer = SentimentAnalyzer(config['keys']['ibmapi'])
    contests = electionInfo.get_voterInfo(address, election_id)
    contest = contests[index-1]
    data = []
    count = 0
    for issue in config['issuesList']:
        dic = {}
        dic['option'] = issue['option']
        dic['explanation'] = issue['explanation']
        dic['candidates'] = []

        for candidate in contest['candidates']:
            cand = {}
            cand['name'] = candidate['name']
            cand['party'] = candidate['party']
            cand['url'] = candidate['candidateUrl']
            cand['score'] = random()*2.0
            #cand['score'] = (sentimentAnalyzer.get_sentiment(issue['explanation'].split(),candidate['name'])+1)
            dic['candidates'].append(cand)
        data.append(dic)
    return render_template("views/user/ballotView.html", config = config, contest = data)
