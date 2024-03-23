from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from models import StockLogs, Users, Teams, Companies, Stocks, Factories, Products, Contracts, Base
import datetime


class DatabaseManager:
    def __init__(self, db_url="sqlite:///business.db"):
        self.engine = create_engine(db_url, echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    """TEAM FUNCTIONS"""

    def add_team(self, team: Teams):
        session = self.Session()
        session.add(team)
        session.commit()
        session.close()

    def get_all_teams(self) -> list:
        session = self.Session()
        teams = session.query(Teams).all()
        session.close()
        return teams

    def get_team_by_id(self, team_id: int) -> Teams:
        session = self.Session()
        team = session.query(Teams).filter(Teams.id == team_id).first()
        session.close()
        return team

    def get_team_by_name(self, team_name: str) -> Teams:
        session = self.Session()
        team = session.query(Teams).filter(Teams.name == team_name).first()
        session.close()
        return team

    def delete_team_by_id(self, team_id: int) -> None:
        session = self.Session()
        session.query(Teams).filter(Teams.id == team_id).delete()
        session.query(Users).filter(Users.team_id == team_id).delete()
        session.commit()
        session.close()

    def delete_team_by_name(self, team_name: str) -> None:
        session = self.Session()
        id = session.query(Teams).filter(Teams.name == team_name).first().id
        session.query(Teams).filter(Teams.id == id).delete()
        session.query(Users).filter(Users.team_id == id).delete()
        session.commit()
        session.close()

    """USER FUNCTIONS"""

    def add_user(self, user: Users):
        session = self.Session()
        session.add(user)
        session.commit()
        session.close()

    def get_all_users(self) -> list:
        session = self.Session()
        users = session.query(Users).all()
        session.close()
        return users

    def get_user_by_id(self, user_id: int) -> Users:
        session = self.Session()
        user = session.query(Users).filter(Users.id == user_id).first()
        session.close()
        return user

    def get_user_by_name(self, user_name: str) -> Users:
        session = self.Session()
        user = session.query(Users).filter(Users.name == user_name).first()
        session.close()
        return user

    def delete_user_by_id(self, user_id: int) -> None:
        session = self.Session()
        session.query(Users).filter(Users.id == user_id).delete()
        session.commit()
        session.close()

    def delete_user_by_name(self, user_name: str) -> None:
        session = self.Session()
        session.query(Users).filter(Users.name == user_name).delete()
        session.commit()
        session.close()

    """COMPANY FUNCTIONS"""

    def add_company(self, company: Companies):
        session = self.Session()
        session.add(company)
        session.commit()
        session.close()

    def get_all_companies(self) -> list:
        session = self.Session()
        companies = session.query(Companies).all()
        session.close()
        return companies

    def get_company_by_id(self, company_id: int) -> Companies:
        session = self.Session()
        company = session.query(Companies).filter(Companies.id == company_id).first()
        session.close()
        return company

    def get_company_by_name(self, company_name: str) -> Companies:
        session = self.Session()
        company = session.query(Companies).filter(Companies.name == company_name).first()
        session.close()
        return company

    def delete_company_by_id(self, company_id: int) -> None:
        session = self.Session()
        session.query(Companies).filter(Companies.id == company_id).delete()
        session.commit()
        session.close()

    def delete_company_by_name(self, company_name: str) -> None:
        session = self.Session()
        session.query(Companies).filter(Companies.name == company_name).delete()
        session.commit()
        session.close()

    """STOCK FUNCTIONS"""

    def add_stock(self, stock: Stocks):
        session = self.Session()
        session.add(stock)
        session.commit()
        session.close()

    def get_all_stocks(self) -> list:
        session = self.Session()
        stocks = session.query(Stocks).all()
        session.close()
        return stocks

    def get_stock_by_id(self, stock_id: int) -> Stocks:
        session = self.Session()
        stock = session.query(Stocks).filter(Stocks.id == stock_id).first()
        session.close()
        return stock
    
    def get_stock_history_by_id(self, stock_id: int) -> list:
        session = self.Session()
        stock_price_objects = session.query(StockLogs).filter(StockLogs.stock_id == stock_id).all()
        stock_prices = []
        for stock_price_object in stock_price_objects:
            stock_prices.append(stock_price_object.stock_price)
        return stock_prices

    def get_stock_history(self) -> list:
        session = self.Session()
        stock_prices = session.query(StockLogs).all()
        return stock_prices

    def get_stock_by_name(self, stock_name: str) -> Stocks:
        session = self.Session()
        stock = session.query(Stocks).filter(Stocks.company_name == stock_name).first()
        session.close()
        return stock

    def update_stock_price(self, stock_id: int, new_price: int) -> None:
        session = self.Session()
        stock = session.query(Stocks).filter(Stocks.id == stock_id).first()
        stock.stock_price = new_price
        stock_log = StockLogs(stock_id=stock_id, stock_price=new_price, date=datetime.datetime.now())
        session.add(stock_log)
        session.commit()
        session.close()

    def delete_stock_by_id(self, stock_id: int) -> None:
        session = self.Session()
        session.query(Stocks).filter(Stocks.id == stock_id).delete()
        session.commit()
        session.close()

    def delete_stock_by_name(self, stock_name: str) -> None:
        session = self.Session()
        session.query(Stocks).filter(Stocks.company_name == stock_name).delete()
        session.commit()
        session.close()

    """FACTORY FUNCTIONS"""

    def add_factory(self, factory: Factories):
        session = self.Session()
        session.add(factory)
        session.commit()
        session.close()

    def get_all_factories(self) -> list:
        session = self.Session()
        factories = session.query(Factories).all()
        session.close()
        return factories

    def get_factory_by_id(self, factory_id: int) -> Factories:
        session = self.Session()
        factory = session.query(Factories).filter(Factories.id == factory_id).first()
        session.close()
        return factory

    def get_factory_by_name(self, factory_name: str) -> Factories:
        session = self.Session()
        factory = session.query(Factories).filter(Factories.name == factory_name).first()
        session.close()
        return factory

    def delete_factory_by_id(self, factory_id: int) -> None:
        session = self.Session()
        session.query(Factories).filter(Factories.id == factory_id).delete()
        session.commit()
        session.close()

    def delete_factory_by_name(self, factory_name: str) -> None:
        session = self.Session()
        session.query(Factories).filter(Factories.name == factory_name).delete()
        session.commit()
        session.close()

    """PRODUCT FUNCTIONS"""

    def add_product(self, product: Products):
        session = self.Session()
        session.add(product)
        session.commit()
        session.close()

    def get_all_products(self) -> list:
        session = self.Session()
        products = session.query(Products).all()
        session.close()
        return products

    def get_product_by_id(self, product_id: int) -> Products:
        session = self.Session()
        product = session.query(Products).filter(Products.id == product_id).first()
        session.close()
        return product

    def get_product_by_name(self, product_name: str) -> Products:
        session = self.Session()
        product = session.query(Products).filter(Products.name == product_name).first()
        session.close()
        return product

    def delete_product_by_id(self, product_id: int) -> None:
        session = self.Session()
        session.query(Products).filter(Products.id == product_id).delete()
        session.commit()
        session.close()

    def delete_product_by_name(self, product_name: str) -> None:
        session = self.Session()
        session.query(Products).filter(Products.name == product_name).delete()
        session.commit()
        session.close()

    """CONTRACT FUNCTIONS"""

    def add_contract(self, contract: Contracts):
        session = self.Session()
        session.add(contract)
        session.commit()
        session.close()

    def get_all_contracts(self) -> list:
        session = self.Session()
        contracts = session.query(Contracts).all()
        session.close()
        return contracts

    def get_contract_by_id(self, contract_id: int) -> Contracts:
        session = self.Session()
        contract = session.query(Contracts).filter(Contracts.id == contract_id).first()
        session.close()
        return contract

    def get_contract_by_name(self, contract_name: str) -> Contracts:
        session = self.Session()
        contract = session.query(Contracts).filter(Contracts.name == contract_name).first()
        session.close()
        return contract

    def delete_contract_by_id(self, contract_id: int) -> None:
        session = self.Session()
        session.query(Contracts).filter(Contracts.id == contract_id).delete()
        session.commit()
        session.close()

    def delete_contract_by_name(self, contract_name: str) -> None:
        session = self.Session()
        session.query(Contracts).filter(Contracts.name == contract_name).delete()
        session.commit()
        session.close()

    """DATABASE FUNCTIONS"""

    def clear_database(self) -> None:
        session = self.Session()
        session.query(Users).delete()
        session.query(Teams).delete()
        session.commit()
        session.close()

    def topup_database(self) -> None:
        session = self.Session()

        if session.query(Users).count() == 0:
            users = [
                Users(
                    name="John",
                    email="Doe",
                    password="1234",
                    team_id="1"
                ),
                Users(
                    name="Johssssn",
                    email="Dossse",
                    password="22221234",
                    team_id="2"
                ),
            ]

            for user in users:
                session.add(user)

        if session.query(Teams).count() == 0:
            teams = [
                Teams(name="Team1"),
                Teams(name="Team2"),
                Teams(name="Team3"),
                Teams(name="Team4"),
            ]

            for team in teams:
                session.add(team)

        if session.query(Stocks).count() == 0:
            stocks = [
                Stocks(company_id=1, stock_number=100, stock_price=50),
                Stocks(company_id=2, stock_number=200, stock_price=60),
                Stocks(company_id=3, stock_number=150, stock_price=70),
                Stocks(company_id=4, stock_number=120, stock_price=80),
                Stocks(company_id=5, stock_number=180, stock_price=90),
                Stocks(company_id=6, stock_number=220, stock_price=100),
                Stocks(company_id=7, stock_number=130, stock_price=110),
                Stocks(company_id=8, stock_number=170, stock_price=120),
                Stocks(company_id=9, stock_number=190, stock_price=130),
                Stocks(company_id=10, stock_number=160, stock_price=140),
            ]

            for stock in stocks:
                session.add(stock)

        if session.query(Companies).count() == 0:
            companies = [
                Companies(name="Company1", description="Description1", budget=100000),
                Companies(name="Company2", description="Description2", budget=200000),
                Companies(name="Company3", description="Description3", budget=300000),
                Companies(name="Company4", description="Description4", budget=400000),
                Companies(name="Company5", description="Description5", budget=500000),
                Companies(name="Company6", description="Description6", budget=600000),
                Companies(name="Company7", description="Description7", budget=700000),
                Companies(name="Company8", description="Description8", budget=800000),
                Companies(name="Company9", description="Description9", budget=900000),
                Companies(name="Company10", description="Description10", budget=1000000),
            ]

            for company in companies:
                session.add(company)

        session.commit()
        session.close()
