from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


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


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)

    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
        
    return render_template("edit_category.html", category=category)


@app.route("/remove_category/<int:category_id>")
def delete_category(category_id):

    category_to_delete = Category.query.get_or_404(category_id)
    db.session.delete(category_to_delete)
    db.session.commit()
    
    return redirect(url_for("categories"))


@app.route("/add_task", methods=["GET","POST"])
def add_task():

    # Retrieve all categories from DB and display them in the select input
    categories = list(Category.query.order_by(Category.category_name).all())

    if request.method == "POST":
        task_name = request.form.get("task_name")
        task_description = request.form.get("task_description")
        is_urgent = True if request.form.get("is_urgent") else False
        due_date = request.form.get("due_date")
        id = request.form.get("category_id")
        
        task_to_save = Task(
            task_name=task_name,
            task_description=task_description,
            is_urgent=is_urgent,
            due_date=due_date,
            category_id=id
        )

        db.session.add(task_to_save)
        db.session.commit()

        return redirect(url_for('home'))

    return render_template("add_task.html", page_title="add_task", categories=categories)


@app.route("/edit_task/<int:task_id>", methods=["GET", "POST"])
def edit_task(task_id):
    categories = list(Category.query.order_by(Category.category_name).all())
    task = Task.query.get_or_404(task_id)

    if request.method == "POST":
        task.task_name = request.form.get("task_name")
        task.task_description = request.form.get("task_description")
        task.due_date = request.form.get("due_date")
        task.is_urgent = True if request.form.get("is_urgent") else False
        task.category_id = request.form.get("category_id")
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit_task.html", task=task, categories=categories)


@app.route("/delete_task/<int:task_id>")
def delete_task(task_id):

    task_to_delete = Task.query.get_or_404(task_id)
    db.session.delete(task_to_delete)
    db.session.commit()
    return redirect(url_for("home"))

    