from flask import redirect, render_template,request,url_for
from flask_login import  current_user

from application import app,db,login_required
from application.nannies.models import Nanny
from application.workingtimes.models import Workingtimes

@app.route("/statistics/<id>", methods=["GET"])
@login_required(role="ADMIN")
def statistics_index(id):
    
   
    return render_template("statistics/allstatistics.html", 
     mostfree_workingtimes_agency=Nanny.find_nanny_with_most_workingtimes_in_current_agency(), mostreserved_nanny_agency=Nanny.find_nanny_with_most_reservations_in_agency(),
     has_workingtimes_agency=Nanny.find_nannies_with_workingtimes_in_current_agency(), sum_all_freetimes_agency=Workingtimes.find_all_freetimes_agency(), sum_all_reservedtimes_agency=Workingtimes.find_all_reserved_agency())


