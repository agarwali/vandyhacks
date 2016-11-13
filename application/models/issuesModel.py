from application.models.util import *
from application.models.userModel import User
class Issues (Model):
  IID                 = PrimaryKeyField()
  user                = ForeignKeyField(User,null=True)
  abortion            = IntegerField(default=1)
  womenAndMinorities  = IntegerField(default=1)
  sameSexMarriage     = IntegerField(default=1)
  publicFaith         = IntegerField(default=1)
  environment         = IntegerField(default=1)
  campaignFinance     = IntegerField(default=1)
  crime               = IntegerField(default=1)
  guns                = IntegerField(default=1)
  obamacare           = IntegerField(default=1)
  schools             = IntegerField(default=1)
  energy              = IntegerField(default=1)
  drugs               = IntegerField(default=1)
  stimulus            = IntegerField(default=1)
  taxes               = IntegerField(default=1)
  immigration         = IntegerField(default=1)
  socialSecurity      = IntegerField(default=1)
  trade               = IntegerField(default=1)
  military            = IntegerField(default=1) 
  america             = IntegerField(default=1) 
  foreignPolicy       = IntegerField(default=1)
  
  # Integer field means it can only be pro or against
  # Float field means it can be anywhere between pro, against or neutral

  class Meta:
    database = getDB("dmz")

