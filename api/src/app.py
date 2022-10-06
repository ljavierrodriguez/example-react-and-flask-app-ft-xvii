from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
import os

# Importando Rutas
from routes.main import bpMain
from routes.user import bpUser
from routes.agenda import bpAgenda

load_dotenv()

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"{os.getenv('DIALECT')}+{os.getenv('DRIVER')}://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

db.init_app(app)
Migrate(app, db)
CORS(app)

app.register_blueprint(bpMain)
app.register_blueprint(bpUser, url_prefix='/api')
app.register_blueprint(bpAgenda, url_prefix='/api')

if __name__ == '__main__':
    app.run()