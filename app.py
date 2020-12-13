from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from Config import Config
from extensions import db, jwt

from resources.facility import FacilityListResource, FacilityResource, FacilityPublishResource
from resources.animal import AnimalListResource, AnimalResource, AnimalPublishResource
from resources.personel import PersonelListResource
from resources.token import TokenResource, RefreshResource, RevokeResource, black_list


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.app_context().push()
    register_extensions(app)
    register_resources(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

    @jwt.token_in_blacklist_loader
    def chek_if_token_in_blacklist(decrypted_token):
        jti = decrypted_token['jti']
        return jti in black_list


def register_resources(app):

    api = Api(app)

    api.add_resource(PersonelListResource, '/personels')

    api.add_resource(FacilityListResource, '/facilities')
    api.add_resource(FacilityResource, '/facilities/<int:facility_id>')
    api.add_resource(FacilityPublishResource, '/facilities/<int:facility_id>/publish')

    api.add_resource(AnimalListResource, '/animals')
    api.add_resource(AnimalResource, '/animals/<int:animal_id>')
    api.add_resource(AnimalPublishResource, '/animals/<int:animal_id>/publish')

    api.add_resource(TokenResource, '/token')
    api.add_resource(RefreshResource, '/refresh')
    api.add_resource(RevokeResource, '/revoke')


if __name__ == '__main__':
    app = create_app()
    app.run()
