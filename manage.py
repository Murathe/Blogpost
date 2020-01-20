from app import create_app,db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.model import User, Comment, POst, Quote

#Create app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manger.command
def test():
    '''
    Run unittests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')

if __name__ == '__main__':
    manager.run()
