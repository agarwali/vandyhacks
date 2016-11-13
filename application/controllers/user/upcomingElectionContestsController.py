from application import app
from application.config import *
from application.models import getModelFromName
from application.models.userModel import User
from application.models.issuesModel import Issues
from application.util.electionInfo import ElectionInfo
from application.util.sentimentAnalyzer import SentimentAnalyzer

from flask import \
  redirect, \
  render_template, \
  request \


@app.route('/contests/<election_id>/<int:index>', methods = ['GET'])
def ballot (election_id, index):
    user = User.select().where(User.UID==1).get()
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
        dic['candidate'] = []
        for candidate in contest['candidates']:
            cand = {}
            cand['name'] = candidate['name']
            cand['party'] = candidate['party']
            cand['url'] = candidate['candidateUrl']
            cand['score'] = (sentimentAnalyzer.get_sentiment(issue['explanation'].split(),candidate['name'])+1)
            dic['candidate'].append(cand)
        data.append(dic)
        if count == 5:
            break
        count += 1
    return render_template("views/user/ballotView.html", config = config, contest = data)
