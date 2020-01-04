from flask_restful import Resource, marshal

from app.models import User
from app import request, db
from app.schemas import user_field
from flask import current_app

import jwt
import datetime


class Login(Resource):
    def post(self):
        payload = request.only(['username', 'password'])

        username = payload['username']
        password = payload['password']

        user = User.query.filter_by(username=username).first()

        if not user or not user.compare_password(password):
            return {"action": False, "message": "Registro não encontrado!"}, 404

        data = {
            "id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=10)
        }

        token = jwt.encode(data, current_app.config['SECRET_KEY'], algorithm='HS256')

        return {"token": token.decode('utf-8')}


class Register(Resource):
    def post(self):
        payload = request.only(['username', 'password'])

        username = payload['username']
        password = payload['password']

        user = User(username, password)

        db.session.add(user)
        db.session.commit()

        return marshal(user, user_field, "user")