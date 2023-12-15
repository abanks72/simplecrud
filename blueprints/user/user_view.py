from flask import Blueprint, render_template, request, redirect, url_for
from models import db, User

user_view = Blueprint('user', __name__, template_folder='templates')

@user_view.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('home.home'))

    return render_template('add_user.html')

@user_view.route('/delete_user/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    
    return redirect(url_for('home.home'))

@user_view.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']

        db.session.commit()
        return redirect(url_for('home.home'))

    return render_template('update_user.html', user=user)
