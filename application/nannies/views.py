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
    nannies=Nanny.query.filter_by(name=request.form.get("name"),age=request.form.get("age"),phonenumber=request.form.get("phonenumber"))
    if nannies:   
            return 'hello world!'#redirect(url_for("nanny_alreadyonagency"))
    
    else:
        db.session().add(nannynew)
        db.session.flush()
        nannyagencynanny=NannyAgencyNanny(current_user.id, nannynew.id)
        db.session().add(nannyagencynanny)
        db.session().commit()

    return redirect(url_for("nannies_index", id=current_user.id))


#@app.route("/nannies/alreadyonanotheragency/") 
#@login_required(role="ADMIN")
  #  return render_template("nannies/alreadyonagency.html")


#@app.route("/nannies/addnannywhoisalreadyonanotheragency/") 
#@login_required(role="ADMIN")
#tälle voisi antaa edellisessä luodun nannyn niin ei tulisi päällekkäisyyksiä




