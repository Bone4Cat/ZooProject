from extensions import db

facility_list = []


def get_last_id():
    if facility_list:
        last_facility = facility_list[-1]


    else:
        return 1
    return last_facility.id + 1

class Facility(db.Model):
    __tablename__ = 'facility'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    location = db.Column(db.String(200))

    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now())

    updated_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now(), onupdate = db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("personel.id"))




