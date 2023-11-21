"""Our inclass test web application.

Robert Davis 2021/09/13"""
# FLASK_APP=tweeter python3 -m flask run


from flask import Flask
from flask import render_template
from flask import request
from .models import db, User
import os


app_dir = os.path.dirname(os.path.abspath(__file__))
database = "sqlite:///{}".format(os.path.join(app_dir, "hello.sqlite3"))


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = database
    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

    db.init_app(app)

    # Create tables
    with app.app_context():
        db.create_all()

    @app.route("/", methods=["GET", "POST"])
    def home():
        name = request.form.get("name")

        if name:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()

        users = User.query.all()
        return render_template('home.html', users=users)

    @app.route("/about")
    def about():
        return 'This is the best app ever. Literally so much better \
than anything you could ever do in your entire life.'

    return app