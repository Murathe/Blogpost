from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import MIgrate, MigrateCommand
from app.model import User, Comment, POst, Quote