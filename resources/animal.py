from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from http import HTTPStatus
from models.animal import Animal


class AnimalListResource(Resource):

    def get(self):
        data = []
        animals = Animal.get_all()
        for animal in animals:
            data.append(animal.data)
        return {'data': data}, HTTPStatus.OK

    @jwt_required
    def post(self):
        data = request.get_json()
        animal = Animal(name=data.get('name'),
                        species=data.get('species'),
                        gender=data.get('gender'),
                        birthdate=data.get('birthdate'),
                        date_aquired=data.get('date_aquired'),
                        location=data.get('location'),
                        keeper=data.get('keeper'),
                        avatar_url=data.get('avatar_url')
                        )

        animal.save()
        return animal.data, HTTPStatus.CREATED


class AnimalResource(Resource):
    def get(self, animal_id):
        animal = Animal.get_by_id(animal_id)

        if animal is None:
            return {'message': 'animal not found'}, HTTPStatus.NOT_FOUND
        return animal.data, HTTPStatus.OK

    def delete(self, animal_id):
        animal = Animal.get_by_id(animal_id)

        if animal is None:
            return {'message': 'animal not found'}, HTTPStatus.NOT_FOUND
        animal.delete()
        return {}, HTTPStatus.NO_CONTENT

    def put(self, animal_id):
        data = request.get_json()
        animal = Animal.get_by_id(animal_id)

        if animal is None:
            return {'message': 'animal not found'}, HTTPStatus.NOT_FOUND

        animal.name = data.get('name') if 'name' in data.keys() else animal.name
        animal.species = data.get('species') if 'species' in data.keys() else animal.species
        animal.gender = data.get('gender') if 'gender' in data.keys() else animal.gender
        animal.birthdate = data.get('birthdate') if 'birthdate' in data.keys() else animal.birthdate
        animal.date_aquired = data.get('date_aquired') if 'date_aquired' in data.keys() else animal.date_aquired
        animal.location = data.get('location') if 'location' in data.keys() else animal.location
        animal.keeper = data.get('keeper') if 'keeper' in data.keys() else animal.keeper
        animal.avatar_url = data.get('avatar_url') if 'avatar_url' in data.keys() else animal.avatar_url

        animal.save()

        return animal.data, HTTPStatus.OK

