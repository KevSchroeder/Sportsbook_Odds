from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Person(Base):
    __tablename__ = 'odds'

    name = Column("name", String, primary_key=True)
    points = Column("points", Integer)
    prop = Column("prop", String)

    def __init__(self, name, points, prop):
        self.name = name
        self.points = points
        self.prop = prop

    def __repr__(self):
        return f"({self.name} {self.points} {self.prop})"
    

engine = create_engine("sqlite:///mydb.db", echo=True)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

person = Person(1231, "Mike", "Smith", "m", 25)
