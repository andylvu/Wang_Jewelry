from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

# Load environment variables
db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')

# Construct the SQLAlchemy database URI
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{db_username}:{db_password}@{db_host}:3306/{db_name}"

db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text)
    price = db.Column(db.Float)

@app.route('/')
def home():
    return 'Hello, this is the home page!'

@app.route('/items/add', methods = ['POST'])
def add_item():
    
    return 'Item added sucessfully'

@app.route('/items/<item_id>')
def get_item(item_id):
    item = Item.query.get(item_id)
    return render_template('item_details.html', item = item)


if __name__ == '__main__':
    app.run(debug=True)