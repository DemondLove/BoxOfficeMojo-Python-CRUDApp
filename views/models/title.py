from ._helper import db

class Title(db.Model):
    __tablename__: 'title'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(), nullable=False, index=True, unique=True)
