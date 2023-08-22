class Estudiante:
    def __init__(self,nombre,edad,grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} esta estudiando")

nombre = input("Introduzca su nombre: ")
edad = input("Introduzca su edad: ")
grado = input("Introduzca su grado: ")

lucas = Estudiante(nombre, edad, grado)
print(lucas.nombre)
print(lucas.edad)
print(lucas.grado)

algo = input("Que estas haciendo? ")
if(algo.lower() == "estudiar"):
    lucas.estudiar()
else:
    print(f"{lucas.nombre} no esta estudiando")
