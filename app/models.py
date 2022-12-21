from app import db
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(),nullable=False)
    user_name = db.Column(db.String(),nullable=False,unique=True)
    email= db.Column(db.String(),nullable=False,unique=True)
    is_active = db.Column(db.Boolean,default=True)
    user_type = db.Column(db.String(),default='Student',nullable=False)
    phone_number = db.Column(db.String(),nullable=False,unique=True)

    def __init__(self, name, user_name, email,is_active,user_type):
        self.name = name
        self.user_name = user_name
        self.email = email
        self.is_active = is_active
        self.user_type = user_type

    def __repr__(self):
        return f'<id {self.id}>'

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = db.column(UUID(as_uuid=True), db.ForeignKey('user.id'),nullable=False)
    address = db.column(db.String(),nullable=True)
    present_class= db.column(db.Integer(),default=1)

    def __repr__(self):
        return f'<id {self.id}>'

class Teacher(db.Model):

     __tablename__ = 'teacher'

     employee_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
     user_id = db.column(UUID(as_uuid=True), db.ForeignKey('user.id'),nullable=False)
     address = db.column(db.String(),nullable=True)
     account_number = db.column(db.String(),default='')

     def __repr__(self):
        return f'<id {self.id}>'

class Session(db.Model):

     __tablename__ = 'sessions'

     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
     teacher_id = db.column(UUID(as_uuid=True), db.ForeignKey('teacher.id'),nullable=False)
     start_time = db.Column(db.DateTime,nullable=False)
     end_time = db.Column(db.DateTime,nullable=False)
     lessons  = db.column(db.String(),nullable=False,default='')

     def __repr__(self):
        return f'<id {self.id}>'

class SessionRoom(db.Model):

     __tablename__ = 'session_room'

     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
     session_id = db.column(UUID(as_uuid=True), db.ForeignKey('session.id'),nullable=False)
     user_id =  db.column(UUID(as_uuid=True), db.ForeignKey('user.id'),nullable=False)
     status = db.Column(db.String(),default='Accepted',nullable=False)

     def __repr__(self):
        return f'<id {self.id}>'

