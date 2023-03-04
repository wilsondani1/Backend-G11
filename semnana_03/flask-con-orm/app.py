from flask import Flask
from base_de_datos import conexion
from dotenv import load_dotenv
from os import environ
from flask_migrate import Migrate
from flask_restful import Api
from models.nivel_model import Nivel
from models.maestro_model import Maestro 
from models.seccion_model import Seccion
from controllers.nivel_controller import NivelController

load_dotenv() # es ele ncargado de leer el archivo .env si es que existe 

app=Flask(__name__)
#print(app.config)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

Flask_api = Api(app=app)
#siq ueiro crear mi conexion en otro oro archivo e inicializar la configuracion de mi conexion tengo que utilizar el entorno int_app 
conexion.init_app(app)
# ahora inicio la  inicializacion de mi clase migrate 
#se le pasa la aplicacion como primer parametro y la conexion (instancia SQLMigrate)
Migrate(app=app,db=conexion)

#defino las rutas de mi bd
Flask_api.add_resource(NivelController,'/nivel')
Flask_api.add_resource(NivelController,'/nivel/<id>')


if __name__ == '__main__':
    app.run(debug=True)
