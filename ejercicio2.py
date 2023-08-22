class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def nombre (self):
        print(self.nombre)

    def edad(self):
        print(self.edad)

class Estudiante(Persona):
    def __init__(self,nombre,edad,grado):
        super().__init__(nombre,edad)
        self.grado = grado

    def grado(self):
        print(self.grado)

estudiante = Estudiante("juan", 13, 2)
print(f"El estudiante {estudiante.nombre} tiene {estudiante.edad} años y va a {estudiante.grado} grado.")
    
