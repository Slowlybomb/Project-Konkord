from flask import Flask, render_template, session, redirect, url_for, g, request, flash 
from database import get_db, close_db
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash
from forms import
from functools import wraps
from werkzeug.utils import secure_filename
import os
from random import randint

app = Flask(__name__)
app.teardown_appcontext(close_db)
app.config["SECRET_KEY"] = "XYU"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

