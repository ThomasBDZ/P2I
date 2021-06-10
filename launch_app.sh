#!/usr/bin/python3

FILE="./application/env"

echo "creating env directory"
python3 -m venv $FILE
source $FILE/bin/activate
pip3 install Flask
export FLASK_APP="./application/app.py"
export FLASK_DEBUG=1
flask run