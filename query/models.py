# -*- encoding=UTF-8 -*-
from query import db

class Component_bug(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    component = db.Column(db.String(1024))
    
    def __init__(self, component):
        self.component = component

    def __repr__(self):
        return '<Component %d %s>' % (self.id, self.component)


class Assignee_bug(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    assignee = db.Column(db.String(1024))

    def __init__(self, assignee):
        self.assignee = assignee

    def __repr__(self):
        return '<Assignee %d %s>' % (self.id, self.assignee)

class Target_Milestone_bug(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    target = db.Column(db.String(1024))
 
    def __init__(self, target):
        self.target = target

    def __repr__(self):
        return '<Target %d %s>' % (self.id, self.target)

class Status_bug(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(1024))
    
    def __init__(self, status):
        self.status = status

    def __repr__(self):
        return '<Status %d %s>' % (self.id, self.status)