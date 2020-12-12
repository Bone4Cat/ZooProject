from extensions import db


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
    avatar_url = db.Column(db.String(300))

    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())

    updated_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("personel.id"))

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'gender': self.gender,
            'birthdate': str(self.birthdate),
            'date_aquired': str(self.date_aquired),
            'location': self.location,
            'keeper': self.keeper,
            'avatar_url': self.avatar_url
        }

    @classmethod
    def get_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    def save(self):
        db.session.add(self)
        db.session.commit()