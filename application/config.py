# See the configure documentation for more about
# this library.
# http://configure.readthedocs.io/en/latest/#
from configure import Configuration

# The configure library provides a pretty interface to our
# configuration data. This module doesn't do anything other
# than
config = Configuration.from_file('config/config.yaml').configure()
navBarConfig = Configuration.from_file('config/navBarConfig.yaml').configure()
secret = Configuration.from_file('config/secret.yaml').configure()

# Load the controllers (if needed)
# controllers = Configuration.from_file('controllers.yaml').configure()
# config.controllers = controllers

# This adds the application's base directory to the
# configuration object, so that the rest of the application
# can reference it.
import os
config.sys.base_dir = os.path.abspath(os.path.dirname(__file__))
