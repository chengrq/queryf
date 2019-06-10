# -*- encoding=UTF-8 -*-

from query import app, db
from query.models import Component_bug
from flask import render_template, request, redirect

@app.route('/', methods={'post', 'get'})
def index():
    #db.session.add(Component_bug('HTTP'))
    #db.session.commit()
    components = Component_bug.query.all()
    return render_template('index.html', component1 = components)

@app.route('/reg/', methods={'post', 'get'})
def reg():
    component = request.values.get('component').strip()

    
    #if component =='':
    #    return redirect_with_msg('/', u'empty', 'reglogin')

    #com = Component_bug.query.filter_by(component=component).first()
    #if com != None:
    #    return redirect_with_msg('/', u'用户名已经存在', 'reglogin')
    
    db.session.add(Component_bug(component))
    db.session.commit()
    
    return redirect('/')