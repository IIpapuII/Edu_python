# objeto libro
class Libro():
    tamano = "17x24"
    peso = '200gr'
    paginas = "150"
    registro = False
    coleccion = "NoAun"
    precio = 40000

    def Resistrar(self):
        self.registro = True
        return "Registrado"
    def Coleccion(self):
        self.coleccion = "programacion"
        return self.coleccion 

programa = Libro()
print("Grandesa= ",programa.tamano)
print("registro ", programa.Resistrar())
print("tipo colecion ", programa.Coleccion()
)