from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://ubuntu:thinkful@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default = datetime.utcnow)

    seller_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    bids = relationship("Bid", backref="items")

    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    #not sure below is required
    auction_items = relationship("Item", backref = "seller")
    
    bids = relationship("Bid", backref = "user")

    
class Bid(Base):
    __tablename__= "bids"
    id = Column(Integer, primary_key=True)
    bid_price = Column(Integer, nullable=False)
    item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
#Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

###############################################

#Add three users to the database
u1 = User()
u2 = User()
u3 = User()
u1.username = 'Bob'
u2.username = 'Dick'
u3.username = 'Harry'
u1.password = 'password123'
u2.password = 'biscuit123'
u3.password = 'sheep123'

#Make one user auction a baseball

b = Item(name='Baseball', description='bally thing', seller_id=u3)
#b.name = 'Baseball'
#b.description = 'A round medium sized baseball. For ball type activities'
#b.seller_id = u1

#Have each user bid

session.add_all([u1,u2,u3,b])
session.commit()
