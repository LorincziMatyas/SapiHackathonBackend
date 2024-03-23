
import time
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from threading import Thread
from database_manager import DatabaseManager
from models import Products

app = Flask(__name__)
CORS(app)

db_manager = DatabaseManager()
db_manager.clear_database()
db_manager.topup_database()


def stock_change():
    time.sleep(3)
    while True:
        stocks = db_manager.get_all_stocks()
        for stock in stocks:
            print(f"Old stock price {stock.stock_price} for stock {stock.id}")
            price_change = random.randint(-2, 2)
            new_price = stock.stock_price + price_change
            new_price = max(0, new_price)
            db_manager.update_stock_price(stock.id, new_price)
            print(f"Stock price for stock {stock.id} changed to {new_price}")
            print()
        time.sleep(5)


@app.route('/api/users')
def get_users():
    users = db_manager.get_all_users()
    user_data = []
    for user in users:
        user_data.append({
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password,
            'teamid': user.team_id,
        })
    return jsonify(user_data)

@app.route('/api/products/<int:id>')
def get_product_by_id(id):
    product = db_manager.get_product_by_id(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'unit_price': product.unit_price,
        'making_cost': product.making_cost,
        'factory_id': product.factory_id,
        'quantity':product.quantity
    })

@app.route('/api/products')
def get_products():
    products = db_manager.get_all_products()
    return jsonify(products)

@app.route('/api/newproduct',methods=['POST'])
def add_product():
   try:
        # Extract data from request.json
        data = request.get_json()
      
        name = data['name']
        description = data['description']
        unit_price = data['unit_price']
        making_cost = data['making_cost']
        factory_id = data['factory_id']
        quantity = data['quantity']

        # Create a new Product object
        new_product = Products(name=name, description=description,
                              unit_price=unit_price, making_cost=making_cost,
                              factory_id=factory_id,quantity=quantity)

        # Add the product to the database session
        db_manager.session.add(new_product)
        db_manager.session.commit()

        # Return a success response
        return jsonify({'message': 'Product added successfully!'}), 201

   except Exception as e:
        # Handle any errors
        db_manager.session.rollback()  # Rollback on errors
        return jsonify({'message': f'Error adding product: {str(e)}'})


@app.route('/api/teams')
def get_teams():
    teams = db_manager.get_all_teams()
    team_data = []
    for team in teams:
        team_data.append({
            'id': team.id,
            'name': team.name,
        })
    return jsonify(team_data)


@app.route('/api/stocks')
def get_stocks():
    stocks = db_manager.get_all_stocks()
    stock_data = []
    for stock in stocks:
        stock_data.append({
            'id': stock.id,
            'company_id': stock.company_id,
            'stocknumber': stock.stock_number,
            'stockprice': stock.stock_price,
        })
    return jsonify(stock_data)


@app.route('/api/companies')
def get_companies():
    companies = db_manager.get_all_companies()
    company_data = []
    for company in companies:
        company_data.append({
            'id': company.id,
            'name': company.name,
            'description': company.description,
            'budget': company.budget,
        })
    return jsonify(company_data)


@app.route('/api/login', methods=['POST'])
def login():
    # Assuming the client sends the username and password in the request body
    data = request.json
    if 'username' not in data or 'password' not in data:
        return jsonify({'error': 'Username and password are required'}), 400

    # Retrieve the username and password from the request data
    username = data['username']
    password = data['password']

    # Check if the user exists in the database
    user = db_manager.get_user_by_name(username)
    if user is None:
        return jsonify({'error': 'User not found'}), 404

    # Check if the password matches
    if user.password != password:
        return jsonify({'error': 'Incorrect password'}), 401

    # Login successful, return user data
    return jsonify({'message': 'Login successful', 'user': {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'teamid': user.team_id
    }}), 200


if __name__ == '__main__':
    # thread_stock = Thread(target=stock_change, args=[]).start()
    app.run(debug=True)
