from flask import url_for, flash, render_template, send_from_directory
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.utils import redirect

from models import User 
from main import app, db 
from webpanel.forms import LoginForm, NewUserForm, ChangePasswordForm


@app.login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for("root"))


@app.route("/webpanel")
@app.route("/webpanel/")
def root():
    return redirect(url_for("login"))


@app.route("/webpanel/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("admin"))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
        else:
            login_user(user, remember=False)
            return redirect(url_for("admin"))

    return render_template("login.html", form=form)


@app.route("/webpanel/create", methods=["GET", "POST"])
@login_required
def new_user():
    form = NewUserForm()
    if form.validate_on_submit():
        u = User(username=form.username.data)
        u.set_password(form.password.data)
        db.session.add(u)
        db.session.commit()
    return render_template("new_user.html", form=form)


@app.route("/webpanel/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        print(type(current_user))
        u = User.query.filter_by(username=current_user.username).first()
        u.set_password(form.new_password.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for("admin"))

    return render_template("changepw.html", form=form, username=current_user.username)


@app.route("/webpanel/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/webpanel/common.css")
def common_css():
    return send_from_directory("templates", "common.css")


@app.route("/webpanel/admin")
@login_required
def admin():
    return render_template("webpanel.html")