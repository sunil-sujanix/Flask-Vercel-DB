from flask import render_template, request, redirect, url_for, flash, jsonify
from app.models import Subscription
from app import db

def register_routes(app):
    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/subscribe", methods=["POST"])
    def subscribe():
        email = request.form["email"]
        new_subscription = Subscription(email=email)
        db.session.add(new_subscription)
        db.session.commit()
        flash("Subscription Successful!", "success")
        return redirect(url_for("index"))

    @app.route("/getemails")
    def get_emails():
        res = Subscription.query.all()
        return jsonify({"data": [{"id": j.id, "email": j.email} for j in res]})
