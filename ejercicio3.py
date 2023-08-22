class Animal:
    def comer():
        print("Estoy comiendo")

class Mamifero(Animal):
    def amamantar():
        print("Estoy amamantando")

class Ave(Animal):
    def volar():
        print("Estoy volando")

class Murcielago(Mamifero,Ave):
    pass

murcielago = Murcielago

murcielago.comer()
murcielago.amamantar()
murcielago.volar()

print(murcielago.mro())