from flask import Flask

from src.models import db
from src.views import bootcamp_api

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:123456@localhost:5432/bootcamp" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(bootcamp_api, url_prefix='/api/bootcamps/')

from src.models import *
db.init_app(app)
db.app = app

@app.route("/")
def hola_mundo():
    return "Hola mundo"

if __name__ == '__main__':
    app.run(debug=True)