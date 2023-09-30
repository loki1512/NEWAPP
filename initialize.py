from models import *
import pandas as pd
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
#app.register_blueprint(admin_app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartphones.sqlite3'
db.init_app(app)
app.secret_key='secret'
app.app_context().push()
db.create_all()
data=pd.read_csv('flipkart_smartphones.csv')
for i in range(len(data)):
    ph=Phones(brand=data.loc[i,'brand'],model=data.loc[i,'model'],price=data.loc[i,'price'],color=data.loc[i,'color'],rating=data.loc[i,'rating'])
    db.session.add(ph)
    db.session.commit()