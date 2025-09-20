from flask import Flask,jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config



app=Flask(__name__)

app.config.from_object(Config)

db=SQLAlchemy(app)

migrate=Migrate(app,db)




from app import routes,models
from app.models import Subscription



@app.route('/getemails')
def emails():
    res=Subscription.query.all()
    return jsonify({'data':[{"id":j.id,"email":j.email }for j in res]})



