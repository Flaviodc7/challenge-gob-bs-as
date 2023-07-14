class Estacion():

    def __init__(self, id, name, location):
        self.id = id
        self.name = name
        self.location = location

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location
        }