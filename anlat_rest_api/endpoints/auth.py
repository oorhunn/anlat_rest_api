from flask_restful import Resource
from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
import db_inserts
from model.users import Users
from datetime import datetime


class Auth(Resource):
    def get(self):
        return render_template('auth/register.html')

    def post(self):
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        date = datetime.utcnow()
        body = {'username': username,
                'email': email,
                'password': generate_password_hash(password),
                'proved': True,
                'register_date': date}
        error = None
        # TODO  regex shit from these lines
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required'
        ses = db_inserts.dbsession()
        data = ses.query(Users).all()
        for us in data:
            if f'{us.username}' == username:
                error = 'this user already registered'
        if error is None:
            db_inserts.userinserter(body)
            return redirect(url_for('auth.login'))
        flash(error)
        pass
