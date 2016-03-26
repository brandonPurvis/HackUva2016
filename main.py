
import store
from objects import Assignment
from flask import Flask, render_template, make_response



app = Flask(__name__)
pstore = store.PickleStore()
try:
    pstore.load()
except:
    pstore.make_file()

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/create_assignment")
def create_assignment():
    return render_template("create_assignment.html")


@app.route("/add_assignment/<name>/<due>/<length>")
def add_assignment(name, due, length):
    global pstore
    newAssignment = Assignment(name, due, length)
    pstore.add_item(newAssignment)
    print("added " + str(newAssignment)) 
    return render_template("assignment_added.html")

@app.route("/show")
def show():
    page = "TEST"
    pstore.get()
    for asgn in pstore.store:
        page += asgn.html()
    print(page)
    return  make_response("<html><head></head><body>" + page + "</body></html>")

if __name__ == "__main__":
    app.debug = True
    app.run()
