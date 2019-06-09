# -*- encoding=UTF-8 -*-

from query import app, db
from query.models import Component_bug
from flask import render_template

@app.route('/')
def index():
    db.session.add(Component_bug('HTTP'))
    db.session.commit()
    components = Component_bug.query.all()
    return render_template('index.html', component1 = components)