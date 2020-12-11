from extensions import db

animal_list = []


def get_last_id():
    if animal_list:
        last_animal = animal_list[-1]


    else:
        return 1
    return last_animal.id + 1

class Animal(db.Model):
    __tablename__ = 'animal'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    birthdate = db.Column(db.DateTime())
    date_aquired = db.Column(db.DateTime())
    location = db.Column(db.String(200))
    keeper = db.Column(db.String(200))

    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now())

    updated_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now(), onupdate = db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("personel.id"))