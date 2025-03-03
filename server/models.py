from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)

    animals = db.relationship('Animal', back_populates='zookeeper')

    def __repr__(self):
        return f'''
        <h1>ID: {self.id}</h1>
        <h1>Name: {self.name}</h1>
        <h1>Birthday: {self.birthday}</h1>
        '''

class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

    animals = db.relationship('Animal', back_populates='enclosure')

    def __repr__(self):
        return f'''
        <h1>ID: {self.id}</h1>
        <h1>Environment: {self.environment}</h1>
        <h1>Open to Visitors: {self.open_to_visitors}</h1>
        '''


class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    species = db.Column(db.String)

    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))

    zookeeper = db.relationship('Zookeeper', back_populates='animals')
    enclosure = db.relationship('Enclosure', back_populates='animals')



    def __repr__(self):
        return f'''
        <h1>Name: {self.name}</h1>
        <h1>Species: {self.species}</h1>
        '''
