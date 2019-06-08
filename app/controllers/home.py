# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash

from app.models.signee import Signee

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
    return render_template('home/index.html')

@blueprint.route('/home')
def home():
    email = request.args.get('email', '')

    if email:
        e = Signee.signUp(email)
        flash('Thank you for signing up with: ' + e.email, 'info')

    return render_template('home/home.html')