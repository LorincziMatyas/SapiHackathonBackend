import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, ForeignKey

# Create a SQLAlchemy base
Base = sqlalchemy.orm.declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)


class User():
    username: str
    email: str
    password: str

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


class Teams(Base):
    __tablename__ = "Teams"
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Stocks(Base):
    __tablename__ = "Stocks"
    id = Column(Integer, primary_key=True)
    company_id = Column(Integer)
    stock_number = Column(Integer)
    stock_price = Column(Integer)


class StockLogs(Base):
    __tablename__ = "StockLogs"
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer)
    stock_price = Column(Integer)
    date = Column(Date)


class Companies(Base):
    __tablename__ = "Company"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    budget = Column(Integer)
    factory_id = Column(Integer)


class Factories(Base):
    __tablename__ = "Factory"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    profit = Column(Integer)


class Products(Base):
    __tablename__ = "Product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    unit_price = Column(Integer)
    making_cost = Column(Integer)
    factory_id = Column(Integer)
    quantity = Column(Integer)


class Contracts(Base):
    __tablename__ = "Contract"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    company_id = Column(Integer)
