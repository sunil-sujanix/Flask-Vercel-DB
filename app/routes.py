from flask import render_template,request,url_for,flash,redirect,jsonify
from app import app,db
from app.models import Subscription



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getemails')
def emails():
    res=Subscription.query.all()
    return jsonify({'data':[{"id":j.id,"email":j.email }for j in res]})



@app.route('/subscribe',methods=['POST'])
def subscribe():
    email=request.form['email']
    new_subscription=Subscription(email=email)
    db.session.add(new_subscription)
    db.session.commit()
    flash('Subscription Sucessfull!!','success')
    return redirect(url_for('index'))
