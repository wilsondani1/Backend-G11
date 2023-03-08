from  base_de_datos import conexion
from sqlalchemy import Column,types
from sqlalchemy.sql.schema import ForeignKey

class Seccion(conexion.Model):
    id = Column(type_=types.Integer ,primary_key=True,autoincrement=True)
    nombre = Column(type_=types.Text ,nullable = False)
    alumnos = Column(type_=types.Integer, default=10)
    
    # si una columna sera utilizada como llave forania entonces tendremos que utilizar la clase foreinnkey , el ella usaremos el parametro 'column' el cual indicaremos LA TABLA
    nivelId = Column(ForeignKey(column='niveles.id'),type_=types.Integer,nullable=False,name='nivel_id')

    maestroId = Column(ForeignKey(column='maestros.id'),type_=types.Integer,nullable=False,name='maestro_id')

#como se llama la tabla de la base de datos
    __tablename__ = 'secciones'
