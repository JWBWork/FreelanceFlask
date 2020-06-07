import json
from flask import Flask
from flask_cors import CORS
from flask_talisman import Talisman
from src import api_blueprint, mail

config = json.load(open('./config.json', 'r'))

application = app = Flask(__name__)
app.config['SECRET_KEY'] = config['SECRET_KEY']
app.register_blueprint(api_blueprint)

mail_settings = config['MAIL']
app.config.update(mail_settings)
mail.init_app(app)
# Talisman(app)
CORS(app)


@app.route("/")
def hello():
	return "Hello World!"


if __name__ == '__main__':
	app.run()
