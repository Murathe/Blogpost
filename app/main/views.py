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

@main.route('/blog/<string:category>')
def posts(category):
   posts = list(Post.query.filter_by(category=category))
   return render_template('/blog.html', posts=posts)

@main.route('/post', methods=['GET', 'POST'])
@login_required
def add():
    post_form=PostForm()
    if post_form.validate_on_submit():
        post=post(title=post_form.title.data, text=post_form.data, category=post_form.category.data, user_id=current_user.id, username=current_user.username)

        post.save_post()
        return redirect(url_for('main.index'))

    return render_template('./post.html', post_form=post_form)

@main.route('/delete/<int:id>', methods['GET', 'POST'])
@login_required
def delete(id):
    deleted = Post.query.filter_by(id=id).first()
    db.session.delete(deleted)
    db.session.commit()

    return redirect(url_for('main.index.html'))



@main.route('/comment/new/<int:post_id>', methods=['GET','POST'])
@login_required