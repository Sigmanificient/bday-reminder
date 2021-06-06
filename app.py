import sqlite3
from flask import Flask
from flask import g

DATABASE = r'db/db.sqlite'
app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


@app.teardown_appcontext
def close_connection(_):
    db = getattr(g, '_database', None)

    if db is not None:
        db.close()


@app.route('/')
def hello_world():
    cur = get_db().cursor()

    result = cur.execute("select * from sqlite_master").fetchall()
    cur.close()
    return repr(result)


if __name__ == '__main__':
    app.run()
