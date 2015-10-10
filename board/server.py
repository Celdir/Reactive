from flask import Flask
from database import db_add_user, db_get_user, db_get_all_users
from json import dumps

# Because we need an app.
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

QUERY_USER = """
SELECT * FROM reactive.users WHERE name = '%s';
"""

@app.route("/add_user/<username>")
def add_user(username):
    results = db_add_user(username)
    processed = []
    for result in results:
        n = (result.name, str(result.id), result.score)
        processed.append(n)
    return dumps(processed)

@app.route("/get_user/<username>")
def get_user(username):
    results = db_get_user(username)
    processed = []
    for result in results:
        n = (result.name, str(result.id), result.score)
        processed.append(n)
    return dumps(processed)

@app.route("/get_all_users/")
def get_all_users():
    results = db_get_all_users()
    processed = []
    for result in results:
        n = (result.name, str(result.id), result.score)
        processed.append(n)
    return dumps(processed)

if __name__ == "__main__":
    app.run(debug=True)

