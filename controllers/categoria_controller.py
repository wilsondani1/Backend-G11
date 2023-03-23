from flask_restful import Resource, request
from flask import send_file
from werkzeug.utils import secure_filename
from os import path
 # universal unique identifier
from uuid import uuid4
from dtos.categoria_dto import CategoriaDto
from models.categoria_model import Categoria
from db import conexion
from sqlalchemy.orm import Query

class ImagenesController(Resource):
    def post(self):
        # Si nosotros queremos enviar informacion por el form-data ahora utilizaremos la propiedad 'form'
        print(request.form)
        # Para obtener las llaves que contengan archivos 'files'
        print(request.files)
        
        imagen = request.files.get('imagen')

        print(imagen.filename)
        # save sirve para guardar la imagen, pero utilizamos el secure_filename para que sea un nombre valido
        
        nombre_seguro = secure_filename(uuid4().hex + '-' + imagen.filename)
        #imagen.save (secure_filename(imagen.filename))
        imagen.save(path.join('imagenes',nombre_seguro))

        return {
            'message': 'Categoria creada exitosamente'
        }

    def get(self, nombre):
   
        try:
            return send_file(path.join('imagenes',nombre))
        except FileNotFoundError:
            return send_file(path.join('imagenes','not_found.png'))
        
class CategoriasController(Resource):
    def post(self):
        #mimetype_validos = []
        mimetype_validos = 'image/'

        data = request.form.to_dict()
        try:
                # vamos a recibir  la imagen mediante la llave llamda imagen
            imagen = request.files.get('imagen')
            print(imagen.filename)
            if mimetype_validos not in imagen.mimetype:
                raise Exception ('el archivo no es un archivo valido')
            
            dto = CategoriaDto()

            nombre = secure_filename(uuid4().hex+'_'+imagen.filename)
            #agrega ami formulario el nombre de mi imagen que me envia el cliente
            #agregamos la carpeta donde se alamcenara la imagen y con el nuevo nombre 

            data['imagen'] = 'imagenes/' +nombre
            data_serializada = dto.load(data)

            nueva_categoria= Categoria(**data_serializada)
            conexion.session.add(nueva_categoria)

            #guarda la imagen en nuestro servidor
            imagen.save(path.join('imagenes',nombre))

            conexion.session.commit()
            
            return{
                'message': 'categoria creada exitosamente'
                }
        
        except Exception as error:
            conexion.session.rollback()
            return{
                'message': 'error al crear la categoria',
                'content': error.args
            }
               
    def get(self):
        query: Query = conexion.session.query(Categoria)
        resultado = query.all()
        dto = CategoriaDto()
        data = dto.dump(resultado,many=True)

        return{
            'content': data
        }
