class Producto:
    def __init__(self ,nombre,precio,cantidad,fecha_vencimiento):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.fecha_vencimiento = fecha_vencimiento
        #__atributo privado se puede acceder a la informacion desde fuera de la clase
        self.__ganancia = 0.3
        #_atributo > protegido en python se suele utilizar la configuracion de atributos y metodos protegidos para cuestiones de herencias  peroc uanod se esta heredando la la clase no se puede acceder a este elemento

    def prueba(self):
        self.__ganancia
        print(self.__ganancia)

    def mostrar_valor_venta(self):
        return{
            'valor de venta': (self.precio * self.__ganancia) + self.precio
        }

pitajaya = Producto('pitajaya',4.50,100,'2023-02-22')
print(pitajaya.nombre)
#print(pitajaya.__ganancia)
#pitajaya.prueba()
print(pitajaya.mostrar_valor_venta())