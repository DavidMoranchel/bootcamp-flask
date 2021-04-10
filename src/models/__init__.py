import datetime
from flask_sqlalchemy import SQLAlchemy

# Init our DB
db = SQLAlchemy()

class BootcampModel(db.Model):

    __tablename__ = 'bootcamp'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)

    # Relations
    generations = db.relationship('GenerationModel', backref='bootcamp', lazy=True)

    def __init__(self, data):
        """Constructor. """
        self.name = data.get("name")
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return BootcampModel.query.all()


    @staticmethod
    def get_by_id(id):
        return BootcampModel.query.get(id)

    def __repr__(self):
        return f'<Bootcamp: {self.name}>'


class GenerationModel(db.Model):

    __tablename__ = 'generation'

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)

    # Relations
    bootcamp_id = db.Column(db.Integer, db.ForeignKey("bootcamp.id"), nullable=False)

    def __init__(self, data):
        """Constructor. """
        self.number = data.get("number")
        self.created_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<Generation: {self.number}>'
