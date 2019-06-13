# -*- encoding=UTF-8 -*-

from query import app, db
from query.models import Component_bug, Assignee_bug, Target_Milestone_bug
from flask_script import Manager

manager = Manager(app)

@manager.command
def init_database():
    db.drop_all()
    db.create_all()
    db.session.add(Component_bug('NFS'))
    db.session.commit()

if __name__ == 'main':
    manager.run()
