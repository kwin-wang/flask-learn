#!/user/bin/env python
import os

from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand


def init_manage(config_name):
    app = create_app(config_name or 'default')
    manager = Manager(app)
    migrate = Migrate(app, db)

    def make_shell_context():
        return dict(app=app, db=db, User=User, Role=Role)
    manager.add_command('shell', Shell(make_context=make_shell_context))
    manager.add_command('db', MigrateCommand)

    return manager


def main():
    config_name = os.environ.get('FLASK_CONFIG') or 'default'
    manager = init_manage(config_name)
    manager.run()

if __name__ == "__main__":
    main()