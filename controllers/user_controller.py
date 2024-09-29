from flask import render_template, request, redirect, url_for
from models.user_model import UserModel

def index():
    users = UserModel.get_all_users()
    return render_template('index.html', users=users)

def create():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        UserModel.create_user(name, email)
        return redirect(url_for('index'))
    return render_template('create.html')

def update(user_id):
    user = UserModel.get_user_by_id(user_id)
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        UserModel.update_user(user_id, name, email)
        return redirect(url_for('index'))
    return render_template('update.html', user=user)

def list():
    return render_template('users.html')

def delete(user_id):
    UserModel.delete_user(user_id)
    return redirect(url_for('index'))