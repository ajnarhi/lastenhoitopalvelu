from flask import redirect, render_template,request,url_for
from application import app,db
from application.nannies.models import Nanny
from application.nannies.forms import NannyForm

@app.route("/nannies", methods=["GET"])
def nannies_index():
    return render_template("nannies/list.html", nannies = Nanny.query.all())

@app.route("/nannies/new/")
def nannies_form():
    return render_template("nannies/new.html", form=NannyForm())

@app.route("/nannies/", methods=["POST"])
def nannies_create():
    form = NannyForm(request.form)

    if not form.validate():
        return render_template("nannies/new.html", form = form)

    t = Nanny(request.form.get("name"),request.form.get("age"),request.form.get("phonenumber"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("nannies_index"))
