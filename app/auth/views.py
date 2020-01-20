from . import auth
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from ..models import User
from forms import SignupForm, LoginForm
from .. import db
from ..email import mail_message
import markdown2