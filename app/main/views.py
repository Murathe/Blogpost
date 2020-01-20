from flask import render_template, request, redirect, url_for, abort
from ..requests import get_quote
from flask_login import login_required
from . import main
from ..models import Comment, User, Post
from .forms import CommentForm, UpdateProfile, PostForm
from flask_login import login_required, current_user
from ..import db, photos

@main.route('/', methods=['GET','POST'])
def index():
   random_quote = get_quote()
   categories = ['ART', 'FINANCE', 'GAMING', 'MUSIC']
   
   return render_template('index.html', categories=categories, quotes=random_quote)

