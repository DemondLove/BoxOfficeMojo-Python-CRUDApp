from bom import db

class Title(db.Model):
    __tablename__: 'title'
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String(), nullable=False, index=True, unique=True)

    # def getTitleByID(id):
    #     response = self.query.filter_by(id=id).first()
    #     return response.title

    @classmethod
    def getTitleByID(cls, id):
        response = Title.query.filter_by(id=id).first()
        return response.title