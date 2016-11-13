from application.models.util import *
from application.models.userModel import User
class Issues (Model):
  IID                 = PrimaryKeyField()
  user                = ForeignKeyField(User,null=True)
  womenAndMinorities  = IntegerField(default=1)
  sameSexMarriage     = IntegerField(default=1)
  guns                = IntegerField(default=1)
  obamacare           = IntegerField(default=1)
  immigration         = IntegerField(default=1)
  
  # Integer field means it can only be pro or against
  # Float field means it can be anywhere between pro, against or neutral

  class Meta:
    database = getDB("dmz")

