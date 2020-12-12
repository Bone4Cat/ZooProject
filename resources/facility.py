from flask import request
from flask_restful import Resource
from http import HTTPStatus
from models.facility import Facility

class FacilityListResource(Resource):
    def get(self):
        facilities = Facility.get_all_published()
        data = []
        for facility in facilities:
            data.append(facility.data)
        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()
        facility = Facility(name=data['name'], description=data['description'], location=data['location'])
        facility.save()
        return facility.data, HTTPStatus.CREATED

class FacilityResource(Resource):
    def get(self, facility_id):
        facility = Facility.get_by_id(facility_id)

        if facility is None:
            return {'message': 'facility not found'}, HTTPStatus.NOT_FOUND
        return facility.data, HTTPStatus.OK

    def put(self, facility_id):
        data = request.get_json()
        facility = Facility.get_by_id(facility_id)

        if facility is None:
            return {'message': 'facility not found'}, HTTPStatus.NOT_FOUND
        facility.name = data['name']
        facility.description = data['description']
        facility.location = data['location']
        facility.save()
        return facility.data, HTTPStatus.OK


class FacilityPublishResource(Resource):
    def put(self, facility_id):
        facility = Facility.get_by_id(facility_id)

        if facility is None:
            return {'message': 'facility not found'}, HTTPStatus.NOT_FOUND
        facility.is_publish = True
        facility.save()
        return {}, HTTPStatus.NO_CONTENT

    def delete(self, facility_id):
        facility = Facility.get_by_id(facility_id)

        if facility is None:
            return {'message': 'facility not found'}, HTTPStatus.NOT_FOUND
        facility.is_publish = False
        facility.save()
        return {}, HTTPStatus.NO_CONTENT


