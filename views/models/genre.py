from ._helper import db

class Genre(db.Model):
    __tablename__: 'genre'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    genre = db.Column(db.String(), nullable=False, index=True, unique=True)

    def __repr__(self):
        return 'Genre ID: {id} is {genre}'.format(id=self.id, genre=self.genre)