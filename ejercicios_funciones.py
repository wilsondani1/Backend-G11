#crear una funcion que reciba las lista de ciudades y ordenarlos
#por la cantidad de habitantes de mayor a menor

from pprint import pprint

ciudades = [
    {
        'nombre':'Tumbes',
        'habitantes': 500000
    },
    {
        'nombre':'Arequipa',
        'habitantes': 800000
    },

    {
        'nombre':'Loreto',
        'habitantes': 10000
    },

]

#def ordenarciudades(lista_ciudades):
#    habitates_ultima_ciudad = 0
#    for ciudad in lista_ciudades:
#        if ciudad['habitantes'] < habitates_ultima_ciudad :
#            continue
#        else:    
#           print(ciudad['habitantes'])
#            habitates_ultima_ciudad = ciudad['habitantes']

#ordenarciudades(ciudades)
    
#metodo 2

def mifuncion(ciudad):
    return ciudad['habitantes']

ciudades.sort( key=mifuncion,reverse=True)
#pprint(ciudades)
ciudades.append({'nombre':'cusco','habitantes':20000})
#ciudades.pop(0)       //para eliminar
#ciudades.remove({ 'nombre':'cusco','habitantes':20000 })     //para eliminar

#eliminar un campo 
index = 0
for ciudad in ciudades:
    if ciudad['nombre']== 'cusco' :
        ciudades.remove(ciudades[index])
    index = index + 1
pprint(ciudades)

#ef ordenarciudades(lista_ciudades):

#ejemplo 3 para lo de arriba
#lista = ['Arequipa','Cusco','tumbes']
#lista.remove("Arequipa")
#print(lista)