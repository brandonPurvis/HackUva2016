import json
import store
from objects import Assignment
from flask import Flask, render_template, make_response, jsonify
from datetime import datetime


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
    # print(assignment_list(pstore, 700, 700))
    return  make_response("<html><head></head><body>" + page + "</body></html>")

@app.route("/get_rects/<canvas_width>/<canvas_height>/")
def get_rects(canvas_width, canvas_height):
    canvas_width, canvas_height = int(canvas_width), int(canvas_height)
    #Find distance of farthest assignment
    till_due_max = max([(asgn.due - datetime.now()).total_seconds()/3600 for asgn in pstore.store])

    # Creates list of coordinates for creating canvas boxes
    number_of_assignments = len(pstore.store)
    curr_task = 0
    coordinate_list = []
    for asgn in pstore.store:
            till_due = int( (asgn.due - datetime.now()).total_seconds()/3600)
            assign_x = int((till_due/till_due_max)*canvas_width)
            assign_y = int(canvas_height/number_of_assignments)
            curr_task_coor = [0, curr_task*assign_y, assign_x, assign_y]
            coordinate_list.append(curr_task_coor)
            curr_task += 1
    return jsonify({"rects":coordinate_list})

if __name__ == "__main__":
    app.debug = True
    app.run()
