def saludar(nombre):
    saludo = 'hola   {}'.format(nombre)
    print(saludo)
saludar('wilson')

def saludar_varios(*args):

    print(args)
    for nombre in args:
        saludo = 'hola{}'.format(nombre)
        print(saludo)

saludar_varios('roxana','juana','martin','roberto')
saludar_varios('pedro','luis')
saludar_varios()
saludar_varios('eduardo',20,True,10.5)

def informacion_usuario(**kwargs):
    #sssss
    print(kwargs)
    # devolver  el valor si es que exite la llave si no existe devolvera vacio
    print(kwargs.get('estatura','no hayy'))
try:
    print(kwargs['estatura'])
except:
    print('no exite la llave estatura')

informacion_usuario(nombre='eduardo',edad =30,esta_civil='soltero',estatura=1.88)
informacion_usuario(nombre='Pamela',apellido='Juarez',nacionalidad='colonbiana',fecha_de_nacimiento='31/06/2023')

#recibir dos valores y hacer la divicion dividendo/divisor y retornar un RESULTADO
def dividir (dividendo,divisor):
    #si la divicion da un error entonces  retornar un mensane que diga 'divicion incorrecta'
    try: 
        resultado = dividendo/divisor
        return resultado
    except ZeroDivisionError:
        #aqui cuando la dicion sea entre 0
        return'no puede haber divicon entre 0'
    
    except TypeError:
        #ingresar si la divicion tiene algun caracter
        return 'la divicon solo es entre numeros'
    except:
        #ingresara si no es ninguno d elos dos eroores anteriores
        return'error desconocido'


valor = dividir(10,5)
print (valor)
valor = dividir(10,0)
print (valor)
valor = dividir('a','h')
print (valor)
try:
    valor = dividir(5,)
    print(valor)
except TypeError:
    print('estubo mal llamar asi a la funcion')
