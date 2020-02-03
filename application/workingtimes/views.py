from flask import render_template, request, redirect, url_for
from datetime import datetime

from application import app, db
from application.workingtimes.models import Workingtimes
from application.workingtimes.forms import WorkingtimesForm

@app.route("/workingtimes/new/")
def workingtimes_form():
    return render_template("workingtimes/new.html", form = WorkingtimesForm())

@app.route("/workingtimes/", methods=["POST"])
def workingtimes_create():
    w = Workingtimes(datetime.strptime(request.form.get("time"), '%Y-%m-%d').date(), False,1)

    db.session().add(w)
    db.session().commit()
  
    return "hello world!"
