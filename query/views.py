# -*- encoding=UTF-8 -*-

from query import app, db
from query.models import Component_bug, Assignee_bug, Target_Milestone_bug
from flask import render_template, session, request, redirect, flash, get_flashed_messages
import json
app.config["SECRET_KEY"] = "hskghsaklg"

@app.route('/', methods={'post', 'get'})
def index():
    #db.session.add(Component_bug('HTTP'))
    #db.session.commit()
    components = Component_bug.query.order_by(Component_bug.component.asc()).all()
    assignees = Assignee_bug.query.order_by(Assignee_bug.assignee.asc()).all()
    targets = Target_Milestone_bug.query.all()
    return render_template('search.html', component1 = components, assignee1 = assignees, target1 = targets)



@app.route('/addcomp/', methods={'post', 'get'})
def addcomp():
    comp = request.values.get('addcom').strip()
    if comp =='':
        flash('component can not be empty')
        return redirect('/')    


    compon = Component_bug.query.filter_by(component=comp).first()
    if compon != None:
        flash('component already exists')
        return redirect('/')

    Comp = Component_bug(comp)

    db.session.add(Comp)
    db.session.commit()
    next = request.values.get('next')
    if next != None and next.startswith('/'):
        return redirect(next)
    
    return redirect('/')

@app.route('/addassi/', methods={'post', 'get'})
def addassi():
    assi = request.values.get('addass').strip()
    if assi =='':
        flash('assignee can not be empty')
        return redirect('/')    


    assign = Assignee_bug.query.filter_by(assignee=assi).first()
    if assign != None:
        flash('assignee already exists')
        return redirect('/')

    Assi = Assignee_bug(assi)

    db.session.add(Assi)
    db.session.commit()
    next = request.values.get('next')
    if next != None and next.startswith('/'):
        return redirect(next)
    
    return redirect('/')


@app.route('/addtarg/', methods={'post', 'get'})
def addtarg():
    targ = request.values.get('addtar').strip()
    if targ =='':
        flash('target milestone can not be empty')
        return redirect('/')    


    targe = Target_Milestone_bug.query.filter_by(target=targ).first()
    if targe != None:
        flash('target milestone already exists')
        return redirect('/')

    Targ = Target_Milestone_bug(targ)

    db.session.add(Targ)
    db.session.commit()
    next = request.values.get('next')
    if next != None and next.startswith('/'):
        return redirect(next)
    
    return redirect('/')

@app.route('/delcomp/', methods={'post', 'get'})
def delcomp():
    comp = request.values.get('addcom').strip()
    Comp = Component_bug.query.filter_by(component=comp).first()
    if Comp == None:
        flash('component does not exist')
        return redirect('/')

    db.session.delete(Comp)
    db.session.commit()
    next = request.values.get('next')
    if next != None and next.startswith('/'):
        return redirect(next)
    
    return redirect('/')

@app.route('/delassi/', methods={'post', 'get'})
def delassi():
    assi = request.values.get('addass').strip()
    Assi = Assignee_bug.query.filter_by(assignee=assi).first()
    if Assi == None:
        flash('assignee does not exist')
        return redirect('/')

    db.session.delete(Assi)
    db.session.commit()
    next = request.values.get('next')
    if next != None and next.startswith('/'):
        return redirect(next)
    
    return redirect('/')

@app.route('/deltarg/', methods={'post', 'get'})
def deltarg():
    targ = request.values.get('addtar').strip()
    Targ = Target_Milestone_bug.query.filter_by(target=targ).first()
    if Targ == None:
        flash('target milestone does not exist')
        return redirect('/')

    db.session.delete(Targ)
    db.session.commit()
    next = request.values.get('next')
    if next != None and next.startswith('/'):
        return redirect(next)
    
    return redirect('/')