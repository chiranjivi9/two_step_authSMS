from flask import render_template, request, url_for, redirect, session
from flask import abort
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user
from .import app
from .models import LoginForm, SignUpForm
from .confirmation_sender import send_confirmation_code

@app.route('/')
def index():
    return "this is the welcome page"
    return render_template('index.html')

    
