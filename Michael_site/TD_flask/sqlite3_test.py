import sqlite3
import json

from flask import g
from flask import Flask, render_template, url_for
from markupsafe import escape
app = Flask(__name__)

DATABASE = '/home/michael/SQL/sql-mysteries-master/sql-murder-mystery.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext   #teardown permet de le faire à chaque fois à la fin
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/') 
def index():
    return '<a href="/interview">Interview</a>'


@app.route('/interview2')
def all_lists_t():
    c = get_db().cursor()
    c.execute("select * from interview")

    return render_template('interview.html', title="mon titre", results=c.fetchall())


@app.route('/interview')
def all_lists():
    c = get_db().cursor()
    c.execute("select * from interview")
    content = '<b>Mother of all interviews<b>'
    content += '<ul>'
    for tpl in c.fetchall():
        content += f'<li><a href="/interview/{tpl[0]}">Interview {tpl[1]}</a><li>'
    content += '</ul>'
    return content

@app.route('/intervieww/<int:list_id>')
def one_list(list_id):
    return f'interview whose identifier = {list_id}'


@app.route('/interview/<int:person_id>')
def select_interview(person_id):
    c = get_db().cursor()
    c.execute(f"select * from interview where person_id ={person_id}")
    content = '<b>Selected interview<b>'
    content += '<ul>'
    for tpl in c.fetchall():
        content += f'<li>{tpl[1]}<li>'
    content += '</ul>'
    return content

if __name__ == "__main__":
    app.run()

