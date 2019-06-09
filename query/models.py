# -*- encoding=UTF-8 -*-
from query import db

class Component_bug(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    component = db.Column(db.String(1024))
    
    def __init__(self, component):
        self.component = component

    def __repr__(self):
        return '<Component %d %s>' % (self.id, self.component)