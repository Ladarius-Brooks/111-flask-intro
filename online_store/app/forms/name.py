#!/usr/bin/env python3
#-*- coding: utf8 -*-

from flask_wtf import Flaskform
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ProductForm(FlaskForm):
    id = StringField("ID:", validators=[DataRequired()])
    item_name = StringField("Item Name:", validators=[DataRequired()])
    item_brand = StringField("Item Brand:", validators=[DataRequired()])
    item_type = StringField("Item Type:", validators=[DataRequired()])
    item_price = StringField("Item Price:", validators=[DataRequired()])
    ship_price = StringField("Ship Price:", validators=[DataRequired()])
    sku = StringField("SKU Number:", validators=[DataRequired()])
    submit = SubmitField("Submit")
