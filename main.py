from bom import app, db
from bom.models import Title
# from models._helper import db
# from models import distributor, genre, mpaarating, title
# from flask_sqlalchemy import SQLAlchemy
# from flask import Flask

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sql.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Title(db.Model):
#     __tablename__: 'title'
    
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     title = db.Column(db.String(), nullable=False, index=True, unique=True)

#     def __repr__(self):
#         return 'Title ID: {id} is {title}'.format(id=self.id, title=self.title)

# class Genre(db.Model):
#     __tablename__: 'genre'
    
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     genre = db.Column(db.String(), nullable=False, index=True, unique=True)

#     def __repr__(self):
#         return 'Genre ID: {id} is {genre}'.format(id=self.id, genre=self.genre)

# class Distributor(db.Model):
#     __tablename__: 'distributor'
    
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     distributor = db.Column(db.String(), nullable=False, index=True, unique=True)
    
#     def __repr__(self):
#         return 'Distributor ID: {id} is {distributor}'.format(id=self.id, distributor=self.distributor)

# class MPAARating(db.Model):
#     __tablename__: 'mpaarating'
    
#     id = db.Column(db.Integer, autoincrement=True, primary_key=True)
#     rating = db.Column(db.String(), nullable=False, index=True, unique=True)

#     def __repr__(self):
#         return 'MPAARating ID: {id} is {rating}'.format(id=self.id, rating=self.rating)

# # Detects models and creates tables for them (if they don't exist)
# db.create_all()
# title = Title(title='Dunkirk')
# db.session.add(title)
# db.session.commit()
# db.create_all()

# print(Title.query.first())

if __name__ == '__main__':
    app.run()