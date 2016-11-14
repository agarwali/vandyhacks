# WARNING
# This script deletes the database file and configures empty
# tables for the models defined in the models module.
from application.models import classes
from application.config import *
from application.models import model
from application.models.userModel import User
from application.models.issuesModel import Issues
def init_db ():
  # First, we create the databases.
  for database in config.databases:
    filename = config.databases[database].filename

    """Initializes the database."""
    # Remove the DB
    if os.path.isfile(filename):
      os.remove(filename)

    # Create an empty DB file
    open(filename, 'a').close()

  # Now, go through the modules we've discovered in the models directory.
  # Create tables for each model.
  for c in classes:
    c.create_table(True)


  print 'Initialized the database.'

def add_dummy_users():
  T = model.User
  new_user = model.User( first_name="Aleksandra",address1="101 Chestnut St.", city="Berea", state="KY", address2="", last_name="Long", time=1476377751.49,token="oasda",email="employer@gmail.com").save()
  new_user = model.User(first_name="Cody",last_name="Myers",phone="8659347353",time=0,token="lsdjf",email="admin@gmail.com").save()
  new_issueLis = model.Issues(user = 1, womenAndMinorities = 50, abortion = 70, guns=30, sameSexMarriage = 90).save()
if __name__ == "__main__":
  init_db()
  add_dummy_users()
