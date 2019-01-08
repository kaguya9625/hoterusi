from flask import Blueprint, render_template,request, redirect, url_for

search = Blueprint('search', __name__,template_folder='templates',static_folder='./static')

@search.route('/searchtop',methods=['GET','POST'])
def searchtop():
    return render_template('searchTop.html')

@search.route('/searchresult',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        locate = request.form['locate']
        checkin = request.form['checkIn']
        checkout = request.form['checkOut']
        roomnumber = request.form['roomnumber']
        adult = request.form['adult']
        child = request.form['child']
        money = request.form['range']
        return render_template('SearchResult.html',locate=locate,checkIn=checkin,checkOut=checkout,roomnumber=roomnumber,adult=adult,child=child,range=money)