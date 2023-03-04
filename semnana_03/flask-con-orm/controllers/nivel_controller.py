from flask_restful  import Resource ,request
from sqlalchemy.orm import Query
from base_de_datos import conexion
from models.nivel_model import Nivel

class NivelController(Resource):
    #GET POST,PUT
    def get(self):
        query: Query = conexion.session.query(Nivel)
        #select *from niveles :
        resultado = query.all()
        print (resultado[0].numero)
        print (resultado[0].descripcion)
        nivels =[]
        for nivel in resultado:
            nivels.append({
                'id':nivel.id,
                'numero':nivel.numero,
                'descripcion':nivel.descripcion
            })
            
        return{
            'message':'hola desde el GET del nivel'

        }