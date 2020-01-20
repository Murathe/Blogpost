from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), index = True)
    email = db.Column(db.String(20), unique = True, index = True)
    bio = db.column(db.String(100))
    profile_pic_path = db.Column(db.String(2000))
    password_hash = db.Column(db.String(200))
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError('No reading password')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_passowrd(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.username}'

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))

class POst(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(30))
    text = db.Column(db.String)
    title = db.Column(db.String)
    username = db.Column(db.String(30), index = True)
    post_id = db.Column(db.Integer)
    Category = db.Column(db.String(50))
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    comments = db.relationship('Comment', backref = 'posts', lazy = 'dynamic')

    def save_post(self):
        db.session.add(self)
        db.session.commit()

    def get_posts(self):
        posts = Post.query.all()
        return posts

    def get_post(self):
        post = Post.query.filter_by(post_id)
        return post

    def __repr__(self):
        return f'User {self.name}'


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    comment_id = db.Column(db.Integer,)
    title = db.Column(db.String)
    username = db.Column(db.String(40), index = True)
    text = db.Column(db.String)
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def get_comments(self):
        comment = Comment.query.filter_by(comment_id)
        return comment

    def get_comment(self):
        comment = Comment.query.filter_by(comment_id)
        return comment

class Quote:
    def __init__(self,id,quote,author):
        self.id = id
        self.quote = quote
        self.author = author
    


    

