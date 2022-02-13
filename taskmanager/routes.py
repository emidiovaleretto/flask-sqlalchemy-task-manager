from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/new-task")
def new_task():
    return render_template("tasks.html", page_title="new_task")