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
        animal = Animal(name=data['name'], species=data['species'], gender=data['gender'], birthdate=data['birthdate'],
                        date_aquired=data['date_aquired'], location=data['location'], keeper=data['keeper'])

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
        animal.name = data['name']
        animal.species = data['species']
        animal.gender = data['gender']
        animal.birthdate = data['birthdate']
        animal.date_aquired = data['date_aquired']
        animal.location = data['location']
        animal.keeper = data['keeper']
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


