from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sayhello import config
from flask_moment import Moment
from faker import Faker


app = Flask("sayhello")
app.config.from_object(config)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


db = SQLAlchemy(app)
moment = Moment(app)
fake = Faker("zh_CN")




from sayhello import views, errors, commands
from sayhello.models import *

with app.app_context():
    db.create_all()