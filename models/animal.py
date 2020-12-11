animal_list = []


def get_last_id():
    if animal_list:
        last_animal = animal_list[-1]
    else:
        return 1
    return last_animal.id + 1


class Animal:

    def __init__(self, name, species, gender, birthdate, date_acquired, location, keeper):
        self.id = get_last_id()
        self.name = name
        self.species = species
        self.gender = gender
        self.birthdate = birthdate
        self.date_acquired = date_acquired
        self.location = location
        self.keeper = keeper
        self.is_publish = False

    @property
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'species': self.species,
            'gender': self.gender,
            'birthdate': self.birthdate,
            'date_acquired': self.date_acquired,
            'location': self.location,
            'keeper': self.keeper
        }