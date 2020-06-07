from src.logging import logger
from flask import Blueprint, request
from flask_restful import Resource, Api
from flask_mail import Message, Mail

api_blueprint = Blueprint('api_blueprint', __name__)
api = Api(api_blueprint)
mail = Mail()


class DevInquery(Resource):
	def post(self):
		data = request.json
		logger.info(f'request data [{type(data)}]: {data}')
		email_body = f"FREELANCE SITE INQUERY:\n" \
		             f"name: {data['name']}\n" \
		             f"email: {data['email']}\n" + \
		             f"_"*12 + \
		             f"\n{data['message']}"
		msg = Message(
			subject="Freelance Site Inquery",
		    body=email_body,
		    sender=data['email'],
		    recipients=["jacobbrookswork@gmail.com"]
		)
		mail.send(msg)
		response = {
			'status': 200,
			'body': 'Success',
		}
		logger.info(f'response: {response}')
		return response


api.add_resource(DevInquery, '/dev-inquery')
