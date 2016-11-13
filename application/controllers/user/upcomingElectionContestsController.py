from application import app
from application.config import *
from application.models import getModelFromName
from application.models.userModel import User
from application.models.politicianModel import Politician
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
    userIssue = Issues.get(Issues.user==1)
    address = "{0} {1} {2} {3}".format(user.address1, user.address2, user.city, user.state)
    electionInfo = ElectionInfo(config['keys']['googleapi'])
    sentimentAnalyzer = SentimentAnalyzer(config['keys']['ibmapi'])
    contests = electionInfo.get_voterInfo(address, election_id)
    contest = contests[index-1]
    count = 0
    politicianIssues = []

    for candidate in contest['candidates']:
        name = candidate['name']
        # print name
        is_pol=Politician.select().where(Politician.name == name)
        # print is_pol
        if is_pol.exists():

           is_pol=is_pol.get()
           print "exists: ", is_pol.name
           issues=Issues.get(Issues.politician==is_pol.PID)
           politicianIssues.append(issues)
        else:
           pol=Politician.create(name=candidate['name'], party=candidate['party'], url=candidate['candidateUrl'])
           pol.save()
           issue=Issues.create()
           issue.politician=pol.PID
           for iss in config['issuesList']:
                # score=1
                s = sentimentAnalyzer.get_sentiment(iss['explanation'].split(),candidate['name'])
                print "value is {}".format(s)
                score = int(((s+1)/2) *100)
                print score
                setattr(issue, iss['option'],score)

           issue.save()
           politicianIssues.append(issue)
           #cand['score'] = int(random()*100)
    return render_template("views/user/ballotView.html", config = config, data=politicianIssues, userIssue=userIssue)
