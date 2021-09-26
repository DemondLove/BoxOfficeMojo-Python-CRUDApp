from ._helper import db

class MPAARating(db.Model):
    __tablename__: 'mpaarating'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rating = db.Column(db.String(), nullable=False, index=True, unique=True)

    def __repr__(self):
        return 'MPAARating ID: {id} is {rating}'.format(id=self.id, rating=self.rating)