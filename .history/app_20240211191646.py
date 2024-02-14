from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}:3306/{os.environ.get('DB_NAME')}"

db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)