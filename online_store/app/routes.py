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

def create_user(): 
    cursor = get_db().execute("insert into user values", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def update_user(): 
    cursor = get_db().execute("update user set", ())
    results = cursor.fetchall()
    cursor.close()
    return results

def get_user():
    cursor = get_db().execute("SELECT * FROM user where last_name=", ()) 
    if user is None:
        print ('User not found')
    results = cursor.fetchall() 
    cursor.close()
    return results

def delete_user(): 
    cursor = get_db().execute("delete from user where last_name=", ())
    if user is None:
        print ('User not found')
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

@app.route('/users', methods = ["GET", "POST","PUT", "DELETE"])
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
        raw_data = create_user()
        for item in raw_data: 
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict)
        out["body"] = body_list 
        return out

    if "PUT" in request.method:
        raw_data = update_user() 
        for item in raw_data:
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict) 
        out["body"] = body_list
        return out
    
    if "DELETE" in request.method:
        raw_data = delete_user() 
        for item in raw_data:
            temp_dict = {
                "first_name": item[0],
                "last_name": item[1],
                "hobbies": item[2]
            }
            body_list.append(temp_dict)
        out["body"] = body_list 
        return out
        


