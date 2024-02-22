from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DB connection
DB_URI = #postgreSQL credentials
engine = create_engine(DB_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Prop(Base):
    __tablename__ = 'props'

    name = Column("name", String, primary_key=True)
    points = Column("points", Integer)
    prop = Column("prop", String)

    def __init__(self, name, points, prop):
        self.name = name
        self.points = points
        self.prop = prop

    def __repr__(self):
        return f"({self.name} {self.points} {self.prop})"
    

#Insert data into database
def insert_props_into_database():
    for prop_title, prop_description in scrape_draftkings_by_category():
        prop = Prop(prop_title, prop_description)
        session.add(prop)
    session.commit()

#Create DB tables
Base.metadata.create_all(engine)

#Insert scraped data into database
insert_props_into_database()




person = Person(1231, "Mike", "Smith", "m", 25)
