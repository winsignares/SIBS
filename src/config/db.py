from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

<<<<<<< HEAD
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:secret@adso_mysql/adso'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

=======
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/dbcitas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
>>>>>>> a3087c4ca59074afcc144fbb8a1a6805efbcae79

app.secret_key = "dbcitas"

db = SQLAlchemy(app)

ma = Marshmallow(app)