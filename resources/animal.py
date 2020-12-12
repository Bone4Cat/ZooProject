from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.animal import Animal


class AnimalListResource(Resource):
    def get(self):
        data = []
        animals = Animal.get_all_published()
        for animal in animals:
            data.append(animal.data)
        return {'data': data}, HTTPStatus.OK

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

    def put(self, animal_id):
        data = request.get_json()
        animal = Animal.get_by_id(animal_id)

        if animal is None:
            return {'message': 'animal not found'}, HTTPStatus.NOT_FOUND

        animal.name = data.get('name') if data.get('name') else animal.name
        animal.species = data.get('species') if data.get('species') else animal.species
        animal.gender = data.get('gender') if data.get('gender') else animal.gender
        animal.birthdate = data.get('birthdate') if data.get('birthdate') else animal.birthdate
        animal.date_aquired = data.get('date_aquired') if data.get('date_aquired') else animal.date_aquired
        animal.location = data.get('location') if data.get('location') else animal.location
        animal.keeper = data.get('keeper') if data.get('keeper') else animal.keeper
        animal.avatar_url = data.get('avatar_url') if data.get('avatar_url') else animal.avatar_url

        animal.save()

        return animal.data, HTTPStatus.OK


class AnimalPublishResource(Resource):
    def put(self, animal_id):
        animal = Animal.get_by_id(animal_id)

        if animal is None:
            return {'message': 'animal not found'}, HTTPStatus.NOT_FOUND
        animal.is_publish = True
        animal.save()
        return {}, HTTPStatus.NO_CONTENT

    def delete(self, animal_id):
        animal = Animal.get_by_id(animal_id)

        if animal is None:
            return {'message': 'animal not found'}, HTTPStatus.NOT_FOUND
        animal.is_publish = False
        animal.save()
        return {}, HTTPStatus.NO_CONTENT


