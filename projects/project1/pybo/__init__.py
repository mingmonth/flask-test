from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from . import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    # migrate 객체가 models.py 파일을 참조하게 함
    from . import models

    # Blueprint
    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app
