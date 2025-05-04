from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect 


app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://jd_user:p7I2d6VeADWWtlyUKksf0bwLF6J1gjGj@dpg-d0bbad6uk2gs73cibrug-a/jamdate_huju'
app.config['UPLOAD_FOLDER'] = '/app/uploads'

csrf = CSRFProtect(app) 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Flask-Login login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from app import views
from app import models