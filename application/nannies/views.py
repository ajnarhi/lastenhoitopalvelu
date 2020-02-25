from flask import redirect, render_template,request,url_for
from flask_login import  current_user

from application import app,db,login_required
from application.nannies.models import Nanny
from application.nannies.forms import NannyForm
from application.auth.models import NannyAgencyNanny

@app.route("/nannies/<id>", methods=["GET"])
@login_required(role="ADMIN")
def nannies_index(id):
    nannies = Nanny.query.join(Nanny.nannyagency).filter_by(nannyagency_id=id)
    print (nannies)
    return render_template("nannies/list.html",nannies=nannies)

@app.route("/nannies/new/")
@login_required(role="ADMIN")
def nannies_form():
    return render_template("nannies/new.html", form=NannyForm())

@app.route("/nannies/addtoagency/<id>", methods=["POST"]) 
@login_required(role="ADMIN")
def nannies_create(id):
    form = NannyForm(request.form)

    if not form.validate():
        return render_template("nannies/new.html", form = form)

    nannynew = Nanny(request.form.get("name"),request.form.get("age"),request.form.get("phonenumber"))
    nannies=Nanny.query.filter_by(name=request.form.get("name"),age=request.form.get("age"),phonenumber=request.form.get("phonenumber")).count()
    print (nannies)
    if nannies > 0:   
            return render_template("nannies/alreadyonagency.html", nanny=nannynew, id=current_user.id)
    
    else:
        db.session().add(nannynew)
        db.session.flush()
        nannyagencynanny=NannyAgencyNanny(current_user.id, nannynew.id)
        db.session().add(nannyagencynanny)
        db.session().commit()

    return redirect(url_for("nannies_index", id=current_user.id))


@app.route("/nannies/addnannywithagency/<id>", methods=["POST"]) 
@login_required(role="ADMIN")
def nannies_createagain(id):
    nannynew = Nanny(request.form.get("name"),request.form.get("age"),request.form.get("phonenumber"))

    db.session().add(nannynew)
    db.session.flush()
    nannyagencynanny=NannyAgencyNanny(current_user.id, nannynew.id)
    db.session().add(nannyagencynanny)
    db.session().commit()

    return redirect(url_for("nannies_index", id=current_user.id))


@app.route("/nannies/delete/<id>", methods=["GET"])
@login_required
def nannies_deletefromagency(id):
    
    nanny = Nanny.query.get(id)
    NannyAgencyNanny.query.filter_by(nannyagency_id=current_user.id, nanny_id=nanny.id).delete()
    db.session().commit()

    return redirect(url_for("nannies_index", id=current_user.id))

@app.route("/nannies/update/<id>")
@login_required(role="ADMIN")
def nannies_update_form(id):
    nanny=Nanny.query.get(id)
    return render_template("nannies/update.html", form=NannyForm(), id=nanny.id)

@app.route("/nannies/updatenanny/<id>", methods=["POST"]) 
@login_required(role="ADMIN")
def nannies_update(id):
    form = NannyForm(request.form)

    nanny=Nanny.query.get(id)
    nanny.name = request.form.get("name")
    nanny.age= request.form.get("age")
    nanny.phonenumber=request.form.get("phonenumber")
    
    db.session().commit()

    return redirect(url_for("nannies_index", id=current_user.id))





