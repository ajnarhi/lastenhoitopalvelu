from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm

from application.auth.models import User

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
	if request.method == "GET":
		return render_template("auth/loginform.html", form = LoginForm())
	
	form = LoginForm(request.form)
	if not form.validate():
			return render_template("auth/loginform.html", form = form)

	if request.form.get('login'):
		
		user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
		if not user:
			return render_template("auth/loginform.html", form = form,
                               error = "No such username or password. Register a new user or check spelling.")
	else:
        	user=User(request.form.get("username"),request.form.get("username"),request.form.get("password"))
        	db.session().add(user)
        	db.session().commit()

	login_user(user)
	return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/delete_agency/<id>", methods = ["GET", "POST"])
def auth_delete_agency(id):


	agency=User.query.get(id)
	db.session().delete(agency)
	db.session().commit()

    
	return redirect(url_for("index"))	
