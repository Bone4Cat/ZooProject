from extensions import db


class Facility(db.Model):
    __tablename__ = 'facility'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    location = db.Column(db.String(200))
    avatar_url = db.Column(db.String(200))

    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now())

    updated_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now(), onupdate = db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("personel.id"))

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'avatar_url': self.avatar_url,
        }

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_location(cls, location):
        return cls.query.filter_by(location=location).first()

    def save(self):
        db.session.add(self)
        db.session.commit()




