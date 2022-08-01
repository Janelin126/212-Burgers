# This command will cd into the correct folder, activate your virtual environment,
# set the correct commands for Flask and run it. 
# So once it's set up, you will only have to double click it to start Flask.
# No more terminal tomfoolery!

# However, to first use it, you MUST give the computer permission to run this file!
# Open terminal, cd to the correct folder (remember you can drag the folder in)
# and use the command:
# chmod u+x flask.command

# You’ll still have to find the full file path to your Github folder. Right click the folder, hold down OPTION.
# Copy as Pathname will appear and you can paste this into the following command in place of [FILEPATH].

#! /bin/sh
cd /Users/20019567/Desktop/github/212-Burgers
source env/bin/activate
export FLASK_APP=run.py
export FLASK_DEBUG=1
flask run