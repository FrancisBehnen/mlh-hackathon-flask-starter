# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, flash

from app.models.signee import Signee

import sys

blueprint = Blueprint('home', __name__)

@blueprint.route('/')
def index():
    email = request.args.get('email', '')

    if email:
        e = Signee.signUp(email)
        print("Someone signed up!", file=sys.stderr)
        flash('Thank you for signing up with: ' + e.email, 'info')

    return render_template('home/index.html')
