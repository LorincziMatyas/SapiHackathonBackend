import time
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
from threading import Thread
from database_manager import DatabaseManager

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
        time.sleep(10)


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
            'stock_number': stock.stock_number,
            'stock_price': stock.stock_price,
        })
    return jsonify(stock_data)


@app.route('/api/stocklogs')
def get_stock_logs():
    stock_logs = db_manager.get_stock_history()
    stock_log_data = []
    for stock_log in stock_logs:
        stock_log_data.append({
            'id': stock_log.id,
            'stock_id': stock_log.stock_id,
            'stock_price': stock_log.stock_price,
            'date': stock_log.date,
        })
    return jsonify(stock_log_data)


@app.route('/api/stocks/<int:id>')
def get_stock_by_id(id):
    stock_prices = db_manager.get_stock_history_by_id(id)
    if not stock_prices:
        return jsonify({'error': 'Stock not found'}), 404

    return jsonify(stock_prices)


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


@app.route('/api/companies/<int:id>')
def getCompanyById(id):
    company = getCompanyById(id)
    if not company:
        return jsonify({'error': 'Company not found'}), 404
    return jsonify(company)


if __name__ == '__main__':
    thread_stock = Thread(target=stock_change, args=[]).start()
    app.run(debug=True)
