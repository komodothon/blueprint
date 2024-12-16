"""app/main/routes.py"""

from flask import render_template, redirect, url_for, flash, session
from flask_login import login_required, current_user
from datetime import datetime


from . import main
from app import db
from app.forms import CreatePostForm
from app.models import Post


@main.route("/")
def home():
    return render_template("home.html")

@main.route("/about")
@login_required
def about():
    return render_template("about.html")

@main.route("/create_post", methods=["GET", "POST"])
@login_required
def create_post():
    create_post_form = CreatePostForm()

    if create_post_form.validate_on_submit():
        title = create_post_form.title.data
        content = create_post_form.content.data
        date = datetime.now()
        user_id = current_user.id

        post = Post(title=title, content=content, date=date, user_id=user_id)

        try:
            db.session.add(post)
            db.session.commit()
            flash("Post created successfully")
        except Exception as e:
            db.session.rollback()
            flash("An error occured while creating a post", "danger")
            return redirect("main.create_post")

        return redirect(url_for("main.home"))
    return render_template("create_post.html", form=create_post_form)