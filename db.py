from flask_sqlalchemy import SQLAlchemy
from views import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db represents an interface for interacting with our database
    # Provides:
    # db.Model - Ability to create and manipulate models
    # db.session - Ability to create and manipulate transactions
db = SQLAlchemy(app)

class Title(db.Model):
    __tablename__: 'title'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(), nullable=False, index=True, unique=True)

# Detects models and creates tables for them (if they don't exist)
db.create_all()
