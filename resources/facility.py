from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.facility import Facility, facility_list

class FacilityListResource(Resource):
    def get(self):
        data = []
        for facility in facility_list:
            if facility.is_publish is True:
                data.append(facility.data)
        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        facility = Facility(name=data['name'], description=data['description'], location=data['location'])


        facility_list.append(facility)
        return facility.data, HTTPStatus.CREATED

class FacilityResource(Resource):
    def get(self, facility_id):
        facility = next((facility for facility in facility_list if facility.id == facility_id and facility.is_publish == True), None)

        if facility is None:
            return {'message': 'facility not found'}, HTTPStatus.NOT_FOUND
        return facility.data, HTTPStatus.OK

    def put(self, facility_id):
        data = request.get_json()
        facility = next((facility for facility in facility_list if facility.id ==  facility_id), None)

        if facility is None:
            return {'message': 'facility not found'}, HTTPStatus.NOT_FOUND
        facility.name = data['name']
        facility.description = data['description']
        facility.location = data['location']

        return facility.data, HTTPStatus.OK

class FacilityPublishResource(Resource):
    def put(self, facility_id):
        facility = next((facility for facility in facility_list if facility.id == facility_id), None)

        if facility is None:
            return {'message': 'facility not found'}, HTTPStatus.NOT_FOUND
        facility.is_publish = True
        return {}, HTTPStatus.NO_CONTENT

    def delete(self, facility_id):
        facility = next((facility for facility in facility_list if facility.id == facility_id), None)

        if facility is None:
            return {'message': 'facility not found'}, HTTPStatus.NOT_FOUND
        facility.is_publish = False
        return {}, HTTPStatus.NO_CONTENT


