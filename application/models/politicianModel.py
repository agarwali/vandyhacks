from application.models.util import *

class Politician (Model):
  PID           = PrimaryKeyField()
  name          = TextField(null=True)
  party         = TextField(null=True)
  url           = TextField(null=True)
  

  class Meta:
    database = getDB("dmz")

