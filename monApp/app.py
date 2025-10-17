from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap5 import Bootstrap
from flask_login import LoginManager

app = Flask(__name__)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']
# Create database connection object
db = SQLAlchemy(app)
#db.init_app(app)
Bootstrap(app)
login_manager = LoginManager(app)
