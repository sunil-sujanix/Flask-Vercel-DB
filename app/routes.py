from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Subscription

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form["email"]
    new_subscription = Subscription(email=email)
    db.session.add(new_subscription)
    db.session.commit()
    flash("Subscription Successful!", "success")
    return redirect(url_for("main.index"))

@main_bp.route("/getemails")
def get_emails():
    res = Subscription.query.all()
    return jsonify({"data": [{"id": j.id, "email": j.email} for j in res]})
