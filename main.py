import store
from flask import Flask, render_template, make_response



app = Flask(__name__)
pstore = store.PickleStore()
try:
    pstore.load()
except:
    pstore.make_file()

class Assignment():
    def __init__(self, name, due, length):
        self.name = name
        self.due = due
        self.length = length

    def __str__(self):
        return "[Assignment {} {} {}]".format(self.name, self.due, self.length)

    def html(self):
        return "<p>{}</p>".format(str(self))


@app.route("/")
def home():
    return render_template("main.html")


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
