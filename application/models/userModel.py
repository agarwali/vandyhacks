from application.models.util import *

class User (Model):
  UID           = PrimaryKeyField()
  first_name    = TextField(null=True)
  middle_initial= TextField(null=True)
  last_name     = TextField(null=True)
  address1     = CharField(null=True)
  address2     = CharField(null=True)
  city         = CharField(null=True)
  state        = CharField(null=True)
  zip_code     = CharField(null=True)
  time          = TextField(null = True)
  token         = TextField(null=True)
  

  class Meta:
    database = getDB("dmz")

