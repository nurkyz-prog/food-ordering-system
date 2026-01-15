from flask import Flask
from models import db
from logging_config import start_logging
from error_handler import register_error_handlers

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///food_ordering.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    start_logging()
    db.init_app(app)
    register_error_handlers(app)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)