from application import app, db
from flask import render_template, request
from application.nannies.models import Nanny

@app.route("/nannies/new/")
def nannies_form():
    return render_template("nannies/new.html")

@app.route("/nannies/", methods=["POST"])
def nannies_create():
    t=Nanny(request.form.get("name"))

    db.session().add(t)
    db.session().commit()


    return "hello world!"
