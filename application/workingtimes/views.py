from flask import render_template, request, redirect, url_for
from datetime import datetime

from application import app, db,login_required
from application.workingtimes.models import Workingtimes
from application.workingtimes.forms import WorkingtimesForm
from flask_login import current_user

@app.route("/workingtimes/<id>/")
@login_required(role="ADMIN")
def workingtimes_list(id):
    workingtimes=Workingtimes.query.filter_by(nanny_id=id)
    return render_template("workingtimes/listofworkingtimes.html", workingtimes=workingtimes)


@app.route("/workingtimes/new/<id>")
@login_required(role="ADMIN")
def workingtimes_form(id):
    return render_template("workingtimes/new.html", form = WorkingtimesForm(), nanny_id=id)

@app.route("/workingtimes/create/<id>", methods=["POST"])
@login_required(role="ADMIN")
def workingtimes_create(id):
    w = Workingtimes(datetime.strptime(request.form.get("time"), '%Y-%m-%d').date(), False,id)

    db.session().add(w)
    db.session().commit()
  
    return redirect(url_for("nannies_index", id=current_user.id))

@app.route("/workingtimes/reserve/<id>/", methods=["POST"])
@login_required(role="ADMIN")
def workingtimes_set_reserved(id):

    w = Workingtimes.query.get(id)
    w.reserved = True
    db.session().commit()
  
    return redirect(url_for("workingtimes_list", id=w.nanny_id)) #kun klikataan aika w varatuksi, palataan ajan w omaavan nannyn vapaana oleviin aikoihin

@app.route("/workingtimes/delete/<id>", methods=["GET"])
@login_required(role="ADMIN")
def workingtimes_delete(id):

    workingtime = Workingtimes.query.get(id)
    
    db.session().delete(workingtime)
    db.session().commit()

    return redirect(url_for("workingtimes_list", id=workingtime.nanny_id))


@app.route("/workingtimes/cancelreservevation/<id>/", methods=["POST"])
@login_required(role="ADMIN")
def workingtimes_cancel_reservation(id):

    w = Workingtimes.query.get(id)
    w.reserved = False
    db.session().commit()
  
    return redirect(url_for("workingtimes_list", id=w.nanny_id))