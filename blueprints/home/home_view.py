from flask import Blueprint, render_template
from models import User

home_view = Blueprint('home', __name__, template_folder='templates')

@home_view.route('/')
def home():
    users = User.query.all()
    return render_template('home.html', users=users)
