class Producto:
    def __init__(self ,nombre,precio,cantidad,fecha_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_vencimiento = fecha_vencimiento
        #__atributo privad ose puede acceder ala informacion desde fuera de la clase
        self.__ganancia = 0.3

    def prueba(self):
        self.__ganancia
        print(self.__ganancia)

pitajaya = Producto('pitajaya',4.50,100,'2023-02-22')
print(pitajaya.nombre)
#print(pitajaya.__ganancia)
pitajaya.prueba()