import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

# Create a SQLAlchemy base
Base = sqlalchemy.orm.declarative_base()


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)



class  User():
    username:str
    email:str
    password:str

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


class Factories(Base):
    __tablename__ = "factories"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    profit = Column(Integer)
    company_id = Column(Integer, ForeignKey('companies.id'))
    company = relationship("Companies", back_populates="factories")
    product = relationship("Products", uselist=False, back_populates="factory") 
    
    def serialize(self):
        serialized_products = []
        if self.product is not None:
            serialized_products.append({
                'id': self.product.id,
                'name': self.product.name,
                'description': self.product.description,
                'unit_price': self.product.unit_price,
                'making_cost': self.product.making_cost,
                'quantity': self.product.quantity
            })
        
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'profit': self.profit,
            'company_id': self.company_id,
            'products': serialized_products
        }

# Then define the Companies class
class Companies(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    budget = Column(Integer)
    factories = relationship("Factories", back_populates="company")
    budget = Column(Integer)
    factories = relationship("Factories", back_populates="company")

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    unit_price = Column(Integer)
    making_cost = Column(Integer)
    factory_id = Column(Integer, ForeignKey('factories.id'), unique=True)  # Foreign key to link to factories
    quantity = Column(Integer)
    
    # Define the back reference to the factory
    factory = relationship("Factories", back_populates="product")  # 1-to-1 relationship with factory


class Contracts(Base):
    __tablename__ = "Contract"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    company_id = Column(Integer)
