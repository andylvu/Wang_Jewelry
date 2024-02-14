from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'wangjewelry.c1askaoscuvm.us-east-1.rds.amazonaws.com'
db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)