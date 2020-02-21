from flask import redirect, render_template,request,url_for
from flask_login import  current_user

from application import app,db,login_required

@app.route("/statistics/<id>", methods=["GET"])
@login_required(role="ADMIN")
def statistics_index(id):
    
   
    return render_template("statistics/allstatisticsbuttons.html")


