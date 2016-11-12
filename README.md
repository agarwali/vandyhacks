# About This Application

You should, at this point, modify this file to include the information we need
about this application. Among other things, it might be good to have
some authorship information, who the client is, contact information...
who knows.

# Relevant Documentation

To work on this application, you'll probably want:

* The Flask Documentation

  http://flask.pocoo.org/

* The Jinja Documentation

  http://jinja.pocoo.org/docs/dev/

* The PeeWee Documentation

  http://docs.peewee-orm.com/en/latest/index.html

* The Configure Documentation

  http://configure.readthedocs.io/en/latest/#

That's most of what comes to mind...

# How To Add Passwordless Login

The passwordless login system is a derivation of the one developed by Matt Jadud

* Matt's Login System 
  https://bitbucket.org/jadudm/berea-handin-0730/src/a5c7ba3b9e58b74f641cde44f9d659a4369ca02c/application/controllers/login/?at=master

## Step One

Create a login directory under controllers

## Step Two 

Copy the two files found in Matt's login folder to your file

## Step Three
You need to add to your setup.sh the mail version, Look at Matt's copy

## Step Four 
mkdir application/templates/views/login

then copy in the the 3 html files from Matt's directory

## Step Five

Add the functions to your validation.py, but make sure to make it equal your database.


