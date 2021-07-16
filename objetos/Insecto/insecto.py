class insecto():
    tipo = ""
    color = ""
    grande = ""
    habita = ""

    def registrar(self):
        self.tipo = input("Ingrese el tipo de insecto : ")
        self.grande = input("Ingrese el tamaño: ")
        return "Registro Exitoso"

    def registrocolor(self):
        colora = ["blanco", "rojo","azul"]
        print("Seleccion el tipo de color")
        for i in range(len(colora)):
            print(i,". ",colora[i])
        try:
            numero = 0
            print("Ingrese el numero de acuerdo al color")
            numero = int(input("Ingrese: "))
            self.color = colora[numero]
        except:
            print("el valor no corresponde a un numero o se sale del rango")
             
    
