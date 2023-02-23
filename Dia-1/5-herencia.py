class persona:
    def __init__(self,nombre,apellido) :
        self.nombre = nombre
        self.apellido = apellido

    def saludar (self):
        return ('buenos dias')
    

class beneficios :
    def __init__(self,detalle):
        self.detalle =detalle
    def mostrar_detalle(self):
        return{
            'detalle' :self.detalle
        }

class alumnno(persona):
    def __init__(self,nombre,apellido,grado):
        self.grado = grado
        #llamando al contrutor de la clase que estoy heredando
        super().__init__(nombre,apellido)

    def saludar(self):
        #en paython esto es polimorfismos  se escribe lo del ptin pese a que ya esta declarado arriba se imprime por jerarquia
        #en este caso estamos modificando el comportamiento de la clase padre llamada saludar
        saludo_padre = super().saludar()
        print (saludo_padre +'hola soy un alumno ')

    def dar_vueltas (self):
        print('dando vueltas')
    

class docente (persona):
    def __init__(self,nombre,apellido,seguro_social):
        self.seguro_social = seguro_social
        super().__init__(nombre,apellido)
    

    def evaluar (self):
        print('evaluando.........')

eduardo =alumnno ('eduardo','de rivera','quinta')
paolo = docente ('paola','socco','1596485')

eduardo.saludar()
print(paolo.saludar())
print (eduardo.nombre)