from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
url_con = 'mysql+pymysql://root@localhost/adso'
app.config['SQLALCHEMY_DATABASE_URI'] = url_con
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "adso3"

db = SQLAlchemy(app)

ma = Marshmallow(app)