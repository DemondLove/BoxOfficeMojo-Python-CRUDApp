from flask_sqlalchemy import SQLAlchemy
from views import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db represents an interface for interacting with our database
    # Provides:
    # db.Model - Ability to create and manipulate models
    # db.session - Ability to create and manipulate transactions
db = SQLAlchemy(app)
