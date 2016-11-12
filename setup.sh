# This sets default values for the versions of the Python
# libraries we are installing. If we wish to override this
# (say, during VM or container setup), we do so by
# exporting these variables into the shell environment before
# sourcing this script. If these variables exist before this
# script is sourced, then the pre-existing values will be used.
FLASK_VERSION="${FLASK_VERSION:-0.11.1}"
WTFORMS_VERSION="${WTFORMS_VERSION:-2.1}"
FLASK_SESSION_VERSION="${FLASK_SESSION_VERSION:-0.2.3}"
FLASK_ADMIN_VERSION="${FLASK_ADMIN_VERSION:-1.4.0}"
PEEWEE_VERSION="${PEEWEE_VERSION:-2.8.1}"
WTF_PEEWEE_VERSION="${WTF_PEEWEE_VERSION:-0.2.6}"
PYYAML_VERSION="${PYYAML_VERSION:-3.11}"
CONFIGURE_VERSION="${CONFIGURE_VERSION:-0.5}"
MAIL_VERSION="${MAIL_VERSION:-0.9.1}"

# Check for virtualenv
command -v virtualenv >/dev/null 2>&1 || { 
  echo >&2 "I require 'virtualenv' but it's not installed.  Aborting."; 
  exit 1;
 }

 # Check for pip
command -v pip >/dev/null 2>&1 || { 
 echo >&2 "I require 'pip' but it's not installed.  Aborting."; 
 exit 1;
}


# If there is a virtual environment, destroy it.
if [ -d venv ]; then
  echo "Deactivating and removing old virtualenv"
  deactivate 2>&1 /dev/null
  rm -rf venv
fi

# Create and activate a clean virtual environment.
virtualenv venv
. venv/bin/activate

# Create a data directory
# We will want this if it is a new project.
mkdir -p data

# Upgrade pip before continuing; avoids warnings.
# This should not affect application behavior.
pip install --upgrade pip

# Install specific versions of libraries to avoid
# different behaviors of applications over time.

pip install -U "flask==$FLASK_VERSION"
# http://flask.pocoo.org/

pip install -U "wtforms==$WTFORMS_VERSION"
# https://wtforms.readthedocs.io/en/latest/

pip install -U "flask-session==$FLASK_SESSION_VERSION"
# http://pythonhosted.org/Flask-Session/

pip install -U "flask-admin==$FLASK_ADMIN_VERSION"
# https://flask-admin.readthedocs.io/en/latest/

pip install -U "peewee==$PEEWEE_VERSION"
# http://docs.peewee-orm.com/en/latest/

pip install -U "wtf-peewee==$WTF_PEEWEE_VERSION"
# https://github.com/coleifer/wtf-peewee

pip install -U "configure==$CONFIGURE_VERSION"
# http://configure.readthedocs.io/en/latest/#

pip install -U "flask-mail==$MAIL_VERSION"
