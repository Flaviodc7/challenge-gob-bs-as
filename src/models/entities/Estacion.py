class Estacion():

    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud

    def to_JSON(self):
        return {
            'nombre': self.nombre,
            'latitud': self.latitud,
            'longitud': self.longitud
        }