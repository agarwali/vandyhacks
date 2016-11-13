from application import app
from application.config import *
from application.models import getModelFromName
from application.models.userModel import User
from application.models.issuesModel import Issues
from application.util.electionInfo import ElectionInfo
from application.util.sentimentAnalyzer import SentimentAnalyzer
from random import random
import gviz_api

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
    issue_dict = model_to_dict(issue)
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
        dic['score'] = (issue_dict[issue['key']]/2)*100
        for candidate in contest['candidates']:
            cand = {}
            cand['name'] = candidate['name']
            cand['party'] = candidate['party']
            cand['url'] = candidate['candidateUrl']
            cand['score'] = int(random()*100)
            #cand['score'] = (sentimentAnalyzer.get_sentiment(issue['explanation'].split(),candidate['name'])+1)
            dic['candidates'].append(cand)
        data.append(dic)
    description = {"name": ("string", "Name"),
                 "salary": ("number", "Salary"),
                 "full_time": ("boolean", "Full Time Employee")}
    data = [{"name": "Mike", "salary": (10000, "$10,000"), "full_time": True},
          {"name": "Jim", "salary": (800, "$800"), "full_time": False},
          {"name": "Alice", "salary": (12500, "$12,500"), "full_time": True},
          {"name": "Bob", "salary": (7000, "$7,000"), "full_time": True}]
    # Loading it into gviz_api.DataTable
    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)
      # Create a JavaScript code string.
    jscode = data_table.ToJSCode("jscode_data",
                               columns_order=("name", "salary", "full_time"),
                               order_by="salary")
    # Create a JSON string.
    json = data_table.ToJSon(columns_order=("name", "salary", "full_time"),
                           order_by="salary")
    return render_template("views/user/ballotView.html", config = config, contest = data, jscode=jscode, json = json)
