#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Route files """
from app import app
from flask import g, request
import sqlite3

DATABASE ="online_store_db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def get_all_users():
        cursor = get_db().execute("select * from user", ())
        results = cursor.fetchall()
        cursor.close()
        return results


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return "Hello, World"

@app.route('/aboutme')
def aboutme():
    return {
        "first_name": "Ladarius",
        "last_name": "Brooks",
        "hobby": "sports and video games"

    }

@app.route('/users', methods = ["GET", "POST"])
def get_users():
    # creating an output dictionary

    out = {"ok": True, "body": ""}
    body_list = [] 
    if "GET" in request.method:
        # get_all_users() returns all records from the user table
        raw_data = get_all_users()
        for item in raw_data:
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict)
        out["body"] = body_list
        return out
    if "POST" in request.method:
        # create a new user
        pass


