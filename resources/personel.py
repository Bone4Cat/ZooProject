from flask import request
from flask_restful import Resource
from http import HTTPStatus
from utils import hash_password
from models.personel import Personel


class PersonelListResource(Resource):
    def post(self):
        json_data = request.get_json()
        username = json_data.get('username')
        email = json_data.get('email')
        non_hash_password = json_data.get('password')

        if Personel.get_by_username(username):
            return {'message': 'username already used'}, HTTPStatus.BAD_REQUEST
        if Personel.get_by_email(email):
            return {'message': 'email already used'}, HTTPStatus.BAD_REQUEST
        password = hash_password(non_hash_password)
        personel = Personel(
                username=username,
                email=email,
                password=password
        )



        personel.save()
        data = {
                'id': personel.id,
                'username': personel.username,
                'email': personel.email
        }



        return data, HTTPStatus.CREATED





