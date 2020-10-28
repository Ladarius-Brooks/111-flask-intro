#!/usr/bin/env python3
# -*- coding: utf8 -*-
""" Flask init """
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
Bootstrap(app)


app.config["SECRET_KEY"] = "this is a lot of work"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://online_store_db"
db = SQLAlchemy(app)


from app import routes