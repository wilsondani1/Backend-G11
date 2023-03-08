from flask_restful  import Resource ,request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto

class NivelController(Resource):

    #GET POST,PUT
    def get(self):
        query: Query = conexion.session.query(Nivel)
        #selc *from niveles ;
        resultado = query.all() 
        dto = NivelDto()
        #drump > es un metodo en la cual le paso la instancia que quiero convertir  a tipo de datos genericos. si se le pasa mas de un a instancia osea una lista de instancias se le tine que adicinar el paramatro many = tru para indicar que lo entra que interar
        niveles = dto.dump(resultado, many=True)

        # al escribir esta  linea ya no se hace los de abajo 

        # print(resultado[0].numero)
        # print(resultado[0].descripcion) 
        # niveles = []
        # for nivel in resultado:
        #     niveles.append({
        #         'id':nivel.id,
        #         'numero':nivel.numero,
        #         'descripcion':nivel.descripcion
        #     })

        return{
             'contect': niveles
            
        }

    def post(self):
        data = request.json
        dto = NivelDto()
        # load > aca le pasamos un diccionario y lo convertira y validara si toda la informacion es correcta, si no lo es, emitira un error y si la informacion esta bien, entonces devolvera un diccionario con la data correcta
        try:
            data_validada =dto.load(data)
            print(data_validada)

            nuevo_nivel = Nivel(numero=data_validada.get('numero'), descripcion=data_validada.get('descripcion'))

            # con el metodo add indicamos que queremos guardar ese nuevo registro
            conexion.session.add(nuevo_nivel)
            # con el metodo commit queremos guardar de manera permantente esa informacion en la base de datos
            conexion.session.commit()

            return {
                'message': 'Nivel creado exitosamente'
            }, 201
        except Exception as error:
            return {
                'message': 'Error al crear el nivel',
                'content': error.args
            }
        
class UnNivelController(Resource):
    def get(self, id):
        query: Query = conexion.session.query(Nivel)
        nivel_encontrado = query.filter_by(id= id).first()
        # TODO: Implementar si no existe ese nivel, retornar un message diciendo que el nivel no existe
        dto = NivelDto()
        resultado = dto.dump(nivel_encontrado)

        return {
            'content': resultado
        }
