from flask import redirect, render_template,request,url_for
from flask_login import  current_user

from application import app,db,login_required
from application.nannies.models import Nanny

@app.route("/statistics/<id>", methods=["GET"])
@login_required(role="ADMIN")
def statistics_index(id):
    
   
    return render_template("statistics/allstatistics.html",has_workingtimes=Nanny.find_nannies_with_workingtimes())


