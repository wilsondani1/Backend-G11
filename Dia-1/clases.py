class Persona:
    estatura = 1.80
    peso = 80
    signo_sodiacal = 'wilson'

    def sumar (self,*args):
        #self es como el this en el caso de js,c#,c++
         #cuando una funcion se declara o define dentro de una clase pasa a llamarse METODO
         #recibbir un numero ilimitado de numeros para realizar su sumatoria
        total = 0
        #arg (10,5,41,526,489,63)
        for numero in args:
            total = total + numero
        return total
    
    def saludar (self,nombre):
        return 'hola {}'.format(nombre)
    
#cuando sacamos una copia de una de la cclase  para utilizarla estamos creando una instancia
Persona1 = Persona()
Persona2 = Persona()

#modifico los atributos de la persona en partiular 
Persona1.peso = 70
Persona2.peso = 50

#todas la modficaciones que hacenos es independiente de la instancia

print(Persona1.peso)
print(Persona2.peso)
#todas las modificaciones que hacenos es independiente de la instancia
resultado1 = Persona1.sumar(10,5,41,526,489,63)
resultado2 = Persona2.sumar(5,8,65,985,492,520,700)
print(resultado1)
print(resultado2)