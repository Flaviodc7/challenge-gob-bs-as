class EstacionEdit():

    def __init__(self, id, name, latitude, longitude):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def to_JSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude
        }