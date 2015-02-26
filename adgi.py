import flask, flask.views
from flask import url_for, request, session, redirect
from jinja2 import environment, FileSystemLoader
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext import admin
from flask.ext.admin.contrib import sqla
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin, BaseView, expose
from flask import render_template, request
from flask import session, redirect
from flask_oauth import OAuth
from functools import wraps
import time
import os

app = flask.Flask(__name__)
db = SQLAlchemy(app)
app.secret_key = '234234rfascasascqweqscasefsdvqwefe2323234dvsv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
# os.environ['DATABASE_URL']

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    image = db.Column(db.String(320))
    join_date = db.Column(db.String(64))

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    author = db.Column(db.String(64))
    genre = db.Column(db.String(64))
    image = db.Column(db.String(320))
    created_at = db.Column(db.String(64))

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    author = db.Column(db.String(64))
    genre = db.Column(db.String(64))
    image = db.Column(db.String(320))
    created_at = db.Column(db.String(64))


@app.route('/', methods=['GET', 'POST'])
def index():
    # if not session:
    #     return redirect('signup')
    return flask.render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()

    # port=int(os.environ['PORT']), host='0.0.0.0'