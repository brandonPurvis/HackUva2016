from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/add_assignment")
def add_assignment():
    return render_template("add_assignment.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
