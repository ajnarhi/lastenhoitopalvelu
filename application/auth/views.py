from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, AgencyUpdateForm


from flask_login import  current_user

from application.auth.models import NannyAgencyNanny

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
	
	NannyAgencyNanny.query.filter_by(nannyagency_id=current_user.id).delete()
	agency=User.query.get(id)
	db.session().delete(agency)
	db.session().commit()

    
	return redirect(url_for("index"))	



@app.route("/auth/update/<id>")
@login_required(role="ADMIN")
def agency_update_form(id):
    agency=User.query.get(id)
    return render_template("auth/agencyupdate.html", form=AgencyUpdateForm(), agency=agency)

@app.route("/auth/update_agency/<id>", methods = ["GET", "POST"])
def update_agency(id):
	form = AgencyUpdateForm(request.form)
	agency=User.query.get(id)
	if not form.validate():
		return render_template("auth/agencyupdate.html", form = form, agency=agency)

	
	agency.password = request.form.get("password")
	db.session().commit()
	
	#return redirect (url_for("index"))
	return redirect(url_for("update_success"))

@app.route("/auth/update_successful")
def update_success():	
	return render_template("auth/passwordchanged.html")