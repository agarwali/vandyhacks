# WARNING
# This script deletes the database file and configures empty
# tables for the models defined in the models module.
from application.models import classes
from application.config import *
from application.models import model
    
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
  new_user = model.User(first_name="Aleksandra",last_name="Long",phone="9568565255",time=1476377751.49,token="oasda",email="employer@gmail.com").save()
  new_user = model.User(first_name="Cody",last_name="Myers",phone="8659347353",time=0,token="lsdjf",email="admin@gmail.com",isAdmin=1).save()    

if __name__ == "__main__":
  init_db()
  add_dummy_users()
  

