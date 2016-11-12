# Import the Flask instance (app) from the application
from application import app
# Import all of our configuration
from application.config import *

# Run the web application.
app.run(host = config.sys.host, port = config.sys.port)
