from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

# creation instance of the database base class
db_class = declarative_base()


class User(db_class):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(100))
    password = Column(String(100))
    user_type = Column(String(50))

    def __repr__(self):
        return f"user({self.id},{self.name},{self.email},{self.user_type})"

    @property
    def json(self):
        return {'id':self.id,
                'name':self.name,
                'email':self.email,
                'password':self.password,
                'user_type':self.user_type}


class Department(db_class):
    __tablename__ = 'department'
    id = Column(Integer, Sequence('Dep_id_seq'), primary_key=True)
    name = Column(String(50))
    tseats = Column(Integer)
    aseats = Column(Integer)
    cofmarks = Column(Integer)

    def __repr__(self):
        return f"Dep({self.id},{self.name}," \
               f"total_seats={self.tseats}," \
               f"Avaliable_seats={self.aseats}," \
               f"cut_of_marks={self.cofmarks})"


class Enrolls(db_class):
    __tablename__ = 'enrolls'
    id = Column(Integer, Sequence('enrol_id_seq'), primary_key=True)
    name = Column(String(50))
    Age = Column(Integer)
    cofmarks = Column(Integer)
    department = Column(String(50))

    def __repr__(self):
        return f"Enroll({self.id},{self.name},{self.Age}," \
               f"{self.cofmarks},{self.department})"

    @property
    def json(self):
        return {'name':self.name,
                'Age':self.Age,
                'cofmarks':self.cofmarks,
                'department':self.department}
