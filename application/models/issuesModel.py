from application.models.util import *
from application.models.userModel import User
class Issues (Model):
  IID                 = PrimaryKeyField(null=True)
  user                = ForeignKeyField(User)
  abortion            = FloatField(null=True)
  womenAndMinorities  = FloatField(null=True)
  sameSexMarriage     = FloatField(null=True)
  publicFaith         = FloatField(null=True)
  environment         = FloatField(null=True)
  campaignFinance     = FloatField(null=True)
  crime               = FloatField(null=True)
  guns                = IntegerField(null=True)
  obamaCare           = FloatField(null=True)
  schools             = FloatField(null=True)
  energy              = IntegerField(null=True)
  drugs               = FloatField(default=False)
  stimulus            = IntegerField(null=True)
  taxes               = FloatField(null=True)
  immigration         = FloatField(null=True)
  socialSecurity      = FloatField(default=True)
  trade               = FloatField(default=False)
  military            = FloatField(null=True) 
  america             = FloatField(null=True) 
  foreignPolicy       = FloatField(null=True)
  
  # Integer field means it can only be pro or against
  # Float field means it can be anywhere between pro, against or neutral

  class Meta:
    database = getDB("dmz")

