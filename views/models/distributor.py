from ._helper import db

class Distributor(db.Model):
    __tablename__: 'distributor'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    distributor = db.Column(db.String(), nullable=False, index=True, unique=True)
    
    def __repr__(self):
        return 'Distributor ID: {id} is {distributor}'.format(id=self.id, distributor=self.distributor)