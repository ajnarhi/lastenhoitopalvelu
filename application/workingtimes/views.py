from flask import render_template, request, redirect, url_for
from datetime import datetime

from application import app, db
from application.workingtimes.models import Workingtimes
from application.workingtimes.forms import WorkingtimesForm

@app.route("/workingtimes/<id>/")
def workingtimes_list(id):
    workingtimes=Workingtimes.query.filter_by(nanny_id=id)
    return render_template("workingtimes/listofworkingtimes.html", workingtimes=workingtimes)


@app.route("/workingtimes/new/")
def workingtimes_form():
    return render_template("workingtimes/new.html", form = WorkingtimesForm())

@app.route("/workingtimes/", methods=["POST"])
def workingtimes_create():
    w = Workingtimes(datetime.strptime(request.form.get("time"), '%Y-%m-%d').date(), False,1)

    db.session().add(w)
    db.session().commit()
  
    return "hello world!"

@app.route("/workingtimes/reserve/<id>/", methods=["POST"])
def workingtimes_set_reserved(id):

    w = Workingtimes.query.get(id)
    w.reserved = True
    db.session().commit()
  
    return redirect(url_for("workingtimes_list", id=w.nanny_id)) #kun klikataan aika w varatuksi, palataan ajan w omaavan nannyn vapaana oleviin aikoihin

