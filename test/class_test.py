class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    owner_of_item = relationship("User", uselist=False, backref="owner")

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)

    owner_id = Column(Integer, ForeignKey('items.id'), nullable=False