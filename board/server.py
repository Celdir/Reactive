from flask import Flask
import database
from json import dumps

# Because we need an app.
app = Flask(__name__)

@app.route("/add_user/<username>")
def add_user(username):
    results = database.add_user(username)
    processed = []
    for result in results:
        n = (result.name, str(result.id), result.score)
        processed.append(n)
    return dumps(processed)

@app.route("/get_all_users/")
def get_all_users():
    results = database.get_all_users()
    processed = []
    for result in results:
        n = (result.name, str(result.id), result.score)
        processed.append(n)
    return dumps(processed)

@app.route("/get_user/<username>")
def get_user(username):
    results = database.get_user(username)
    processed = []
    for result in results:
        n = (result.name, str(result.id), result.score)
        processed.append(n)
    return dumps(processed)

@app.route("/clear_all_records/")
def clear_all_records():
    results = database.clear_all_records()
    return "[]"

if __name__ == "__main__":
    app.run(debug=True)

