from flask_restful  import Resource ,request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.nivel_model import Nivel
from dtos.nivel_dto import NivelDto

class NivelController(Resource):

    #GET POST,PUT
    def get(self):
        query: Query = conexion.session.query(Nivel)
        #select *from niveles :
        resultado = query.all()

        dto = NivelDto()
        dto .dump(resultado,many=True)


#        print (resultado[0].numero)
#        print (resultado[0].descripcion)
#        niveles =[]
#        for nivel in resultado:
#            niveles.append({
#                'id':nivel.id,
#                'numero':nivel.numero,
#                'descripcion':nivel.descripcion
#            })
            
        return{
            'content':niveles

        }
    def post(self):
        data = request.json
        dto = NivelDto()

        try:
            data_validada=dto.load(data)

            nuevo_nivel = Nivel(numero=data.get('numero'),descripcion=data.get('descripcion'))

            conexion.session.add(nuevo_nivel)

            conexion.session.commit()
            return{
                'message':'nivelcreado exitosamente'
            },201
        except Exception as error:
             return{
            'message':'error al crear el nivel',
            'content': error.args
            }

class UnNivelController(Resource):
    def get(self.id):
        query:Query = conexion.session.query(Nivel)
        nivel_encontrado = query.filter_by(id=id).first()
        dto =NivelDto()
        resultado =dto.drump(nivel_encontrado)

        return {
            'content': resultado
        }