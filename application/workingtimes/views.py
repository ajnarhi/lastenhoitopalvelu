from flask import render_template, request, redirect, url_for
from datetime import datetime

from application import app, db
from application.workingtimes.models import Workingtimes
from application.workingtimes.forms import WorkingtimesForm

@app.route("/workingtimes/<id>/")
def workingtimes_list(id):
    workingtimes=Workingtimes.query.filter_by(nanny_id=id)
    return render_template("workingtimes/listofworkingtimes.html", workingtimes=workingtimes)


@app.route("/workingtimes/new/<id>")
def workingtimes_form(id):
    return render_template("workingtimes/new.html", form = WorkingtimesForm(), nanny_id=id)

@app.route("/workingtimes/create/<id>", methods=["POST"])
def workingtimes_create(id):
    w = Workingtimes(datetime.strptime(request.form.get("time"), '%Y-%m-%d').date(), False,id)

    db.session().add(w)
    db.session().commit()
  
    return "hello world!"

@app.route("/workingtimes/reserve/<id>/", methods=["POST"])
def workingtimes_set_reserved(id):

    w = Workingtimes.query.get(id)
    w.reserved = True
    db.session().commit()
  
    return redirect(url_for("workingtimes_list", id=w.nanny_id)) #kun klikataan aika w varatuksi, palataan ajan w omaavan nannyn vapaana oleviin aikoihin

