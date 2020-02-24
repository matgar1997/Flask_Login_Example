## Getting Started

check if pipenv is installed "pipenv --version"

if not "pip3 install pipenv"

Typical REST projects have an outer directory, then a "project" directory within that
Inside the outer directory run "pipenv shell"

FROM HERE ON OUT EVERYTHING IS DONE INSIDR THE PIPENV ENVIROMENT
you can leave and re-enter the shell with 
"exit"
"pipenv shell" - wihin the outer directory

"pipenv install -r ./requirements.txt"

"export FLASK_APP=project"
"export FLASK_DEBUG=1"

"flask run" -confirm everything runs up to this point (sanity check)

stop the flask app

open python interpretter
"python"
"from project import db, create_app"
"db.create_all(app=create_app())"

Optional step, if using VS Code
install SQLite by alexcvzz from market place
This will let you have a graphical representation of the database

At this point ./project/db.sqlite3 should exist, right click on it too see
"Open Database" if installed option step

On the bottom left SQLite Explore should have 1 database an 1 user table
Press the arrow/play button next to user to view current users (should be empty since no user was created yet)