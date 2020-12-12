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

        firstname = json_data.get('firstname')
        lastname = json_data.get('lastname')
        phone_number = json_data.get('phone_number')
        role = json_data.get('role')
        avatar_url = json_data.get('avatar_url')

        personel = Personel(
                username=username,
                email=email,
                password=password,
                firstname=firstname,
                lastname=lastname,
                phone_number=phone_number,
                role=role,
                avatar_url=avatar_url
        )

        personel.save()

        return personel.data, HTTPStatus.CREATED
