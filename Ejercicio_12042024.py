class Persona:
    def __init__(self, nombre, edad, genero, direccion, telefono):
        self.nombre = nombre
        self.edad = edad
        self.genero = genero
        self.direccion = direccion
        self.telefono = telefono

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_genero(self):
        return self.genero

    def set_genero(self, genero):
        self.genero = genero

    def get_direccion(self):
        return self.direccion

    def set_direccion(self, direccion):
        self.direccion = direccion

    def get_telefono(self):
        return self.telefono

    def set_telefono(self, telefono):
        self.telefono = telefono
