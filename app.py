from flask import Flask
from models import db
from blueprints.home.home_view import home_view
from blueprints.user.user_view import user_view

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db.init_app(app)

# Register Blueprints
app.register_blueprint(home_view)
app.register_blueprint(user_view)

if __name__ == '__main__':
    app.run(debug=True)
