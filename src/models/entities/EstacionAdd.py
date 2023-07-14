class EstacionAdd():

    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def to_JSON(self):
        return {
            'name': self.name,
            'latitude': self.latitude,
            'longitude': self.longitude
        }