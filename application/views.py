from flask import render_template
from application import app
from application.nannies.models import Nanny

@app.route("/")
def index():
    return render_template("index.html", has_workingtimes=Nanny.find_nannies_with_workingtimes())
