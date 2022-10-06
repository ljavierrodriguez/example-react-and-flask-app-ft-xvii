from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    active = db.Column(db.Boolean(), default=True)
    agendas = db.relationship('Agenda', cascade="all, delete", backref="user")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.active
        }

    def serialize_with_agendas(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.active,
            "agendas": [agenda.serialize() for agenda in self.agendas]
        }

    def serialize_with_agendas_with_contacts(self):
        return {
            "id": self.id,
            "username": self.username,
            "active": self.active,
            "agendas": [agenda.serialize_with_contacts() for agenda in self.agendas]
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
class Agenda(db.Model):
    __tablename__ = 'agendas'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    contacts = db.relationship('Contact', cascade="all, delete", backref="agenda")

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "users_id": self.users_id,
            "owner": self.user.username
        }

    def serialize_with_contacts(self):
        return {
            "id": self.id,
            "title": self.title,
            "users_id": self.users_id,
            "owner": self.user.username,
            "contacts": [contact.serialize() for contact in self.contacts]
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit() 


class Contact(db.Model):
    __tablename__ = 'contacts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100))
    phone = db.Column(db.String(120), nullable=False)
    agendas_id = db.Column(db.Integer, db.ForeignKey('agendas.id', ondelete='CASCADE'), nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()




'''

serialize:

{
    "id": 1,
    "username": "lrodriguez@4geeks.co",
    "active": true
}

serialize_with_agendas:

{
    "id": 1,
    "username": "lrodriguez@4geeks.co",
    "active": true,
    "agendas": [ // serialize
        {
            "id": 1,
            "title": "4Geeks",
            "users_id": 1,
            "owner": "lrodriguez@4geeks.co"
        }
    ]
}

serialize_with_agendas_with_contacts:

{
    "id": 1,
    "username": "lrodriguez@4geeks.co",
    "active": true,
    "agendas": [ // serialize_with_contacts
        {
            "id": 1,
            "title": "4Geeks",
            "users_id": 1,
            "owner": "lrodriguez@4geeks.co",
            "contacts": [
                {
                    "id": 1,
                    "name": "John Doe",
                    "email": "john.doe@gmail.com,
                    "phone": "+1 111 111 11"
                }
            ]
        }
    ]
}




'''