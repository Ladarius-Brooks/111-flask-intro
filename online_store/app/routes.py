#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Route files """
from app import app
from flask import g, request, render_template, flash, redirect, session, url_for
from app.forms.name import ProductForm
from app.forms.user import NameForm
from app.forms.admin import AdminForm
from app.db import get_db, get_all_users, create_user


def get_all_products(): 
    cursor = get_db().execute("SELECT * FROM product", ())
    results = cursor.fetchall()  
    cursor.close()
    return results


def create_product(product):
    sql = """INSERT INTO product (
                    id, 
                    item_title,
                    item_brand, 
                    item_type, 
                    item_price, 
                    ship_price, 
                    sku
                    )
            VALUES (?, ?, ?, ?, ?, ?, ?)"""
    cursor = get_db()
    cursor.execute(sql, product)
    cursor.commit()
    return True


def delete_product(product_id):

    sql = "DELETE from product where id=" + product_id
    cursor = get_db()
    cursor.execute(sql)
    cursor.commit()  
    cursor.close()
    return True


@app.route("/items")
def scan_products():
    items = get_all_items()
    return render_template("items.html", products=items)


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route('/')
def index(): 
    return "Hello world"


@app.route('/login', methods=["GET", "POST"])
def login():

    if "POST" in request.method:
        password = request.form.get("password")
        if password == "111":
            flash("Successful login")
            return redirect(url_for("get_products"))
        else:
            flash("Invalid Admin Password")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route('/info/items', methods=["GET", "POST"])
def get_products():
    
    if "GET" in request.method:

        return render_template('info.html', products=get_all_products(), form=ProductForm())

    if "POST" in request.method:
        id = request.form.get("id")
        product_title = request.form.get("product_title")
        brand_name = request.form.get("brand_name")
        product_descrip = request.form.get("product_descrip")
        product_price = request.form.get("product_price")
        ship_price = request.form.get("ship_price")
        sku = request.form.get("sku")

        create_product((id, product_title, brand_name,
                        product_descrip, product_price, ship_price, sku))
        return redirect(url_for("get_products"))


@app.route('/product/delete', methods=["POST"])
def product_delete():
    if "POST" in request.method:
        id = request.form.get("id")
        delete_product(id)
        return redirect(url_for("scan_products"))


@app.route('/users', methods=["GET", "POST"])
def get_users():
    out = {"ok": True, "body": ""}
    body_list = []
    if "GET" in request.method:
        form = NameForm()
        raw_data = get_all_users()
        for item in raw_data:
            temp_dict = {
                "id": item[0],
                "first_name": item[1],
                "last_name": item[2],
                "address": item[3],
                "billing_card": item[4],
                "phone_number": item[5],
            }
            body_list.append(temp_dict)
        if not body_list:
            body_list.append({})
        out["body"] = body_list
        return render_template(
            "user_signin.html",
            first_name=out["body"][0].get("first_name"),
            last_name=out["body"][0].get("last_name"),
            address=out["body"][0].get("address"),
            billing_card=out["body"][0].get("billing_card"),
            phone_number=out["body"][0].get("phone_number"),
            form=form)
    if "POST" in request.method:
        flash("Created new user!")
        return redirect(url_for("get_users"))


@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p> your user agent is %s</p>" % user_agent


@app.errorhandler(404)
def page_not_found(exception):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(exception):
    return render_template("500.html"), 500
