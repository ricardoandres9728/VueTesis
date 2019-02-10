from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()


def registrar_blueprints(app):
    from usuario.views import usuario_app
    app.register_blueprint(usuario_app)

def create_app(**config_overrides):
    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    app.config.update(config_overrides)
    db.init_app(app)
    migrate.init_app(app=app, db=db)
    csrf.init_app(app)
    login_manager.init_app(app)
    registrar_blueprints(app)
    return app
