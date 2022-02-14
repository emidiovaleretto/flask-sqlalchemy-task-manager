from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/new-task")
def new_task():
    return render_template("tasks.html", page_title="new_task")

@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", page_title="categories", categories=categories)

@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))

    return render_template("add_category.html", page_title="add_category")