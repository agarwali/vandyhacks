from application.models.util import *
from application.models.userModel import User
from application.models.politicianModel import Politician

class Issues (Model):
  IID                 = PrimaryKeyField()
  user                = ForeignKeyField(User,null=True)
  womenAndMinorities  = FloatField(default=1.00)
  sameSexMarriage     = FloatField(default=1.00)
  guns                = FloatField(default=1.00)
  abortion            = FloatField(default=1.00)
  politician          = ForeignKeyField(Politician, null=True)
  
  # Integer field means it can only be pro or against
  # Float field means it can be anywhere between pro, against or neutral

  class Meta:
    database = getDB("dmz")

