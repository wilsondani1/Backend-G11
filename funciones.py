#def suma (a,b):
#    print(b)
#
#suma(2,3)

def suma (numero_1,numero_2):
    return numero_1+numero_2
    #resultado = numero_1 + numero_2
    #return resultado
#resultado_suma = suma (4,3)
#print (resultado_suma)
def resta (a,b):
    return a - b

def multiplicacion (a,b):
    return a * b

def divicion (a,b):
    return a / b

#print(divicion (2,4))

#print ('que operacion decea realizar')
#opcion  = input ('indicar operacion matematica:')
#print('la operacion que solicito es ' + opcion)

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def divicion(a,b):
    return a / b



def clacularResultadoporoperacion(operacion,valor_1,valor_2): 
    if operacion == 'suma' :
        return f'el resultado de la {operacion} es: {suma(valor_1,valor_2)}'
    
    elif operacion == 'resta' :
        return f'el resultado de la {operacion } es : {resta(valor_1,valor_2)}'
    else:
        return ' la operacion no existe'
    
operacion = input ('ingrese el tipo de operacion:  ') 
valor_1 = int(input ('ingrese el primer numero: '))
valor_2 = int (input ('ingrese el segundo numero: '))   

resultado = clacularResultadoporoperacion (operacion,valor_1,valor_2)
print (resultado)

#nombre = input ('ingrese su nombre: ')
#edad = input ('ingrese su edad: ')
# print ('hola'+ nombre+'que tal') clasico
#print(f'hola {nombre}, tu tienes {edad} años')    manera 1
#print('hola {}, tu tienes {} años'.format(nombre,edad))       manera 2
