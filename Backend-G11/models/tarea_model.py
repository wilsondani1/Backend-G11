from sqlalchemy import Column,types
from enum import Enum
from sqlalchemy import ForeignKey
from bd import conexion


class EstadoTareaEnum(Enum):
    #https://docs.python.org/3/library/enum.html
    PENDIENTE = 'PENDIENTE'
    RELIZANDOSE = 'RELIZANDOSE'
    REALIZADA = 'REALIZADA'
    CANCELADA = 'CANCELADA'


class tarea (conexion.Model):
    id = Column(type_=types.Integer,primary_key=True,autoincrement=True)
    nombre = Column(type_=types.Text,nullable= False )
    descripcion = Column(type_=types.Text, default= 'no tiene descripcion')
    fechaVencimiento = Column(type_=types.DateTime, name='fecha_de_vencimiento')
    estado = Column (type_=types.Enum(EstadoTareaEnum),default=EstadoTareaEnum.PENDIENTE)
    
    usuarioId = Column(ForeignKey(column='usuarios.id'),type_=types.Integer,nullable=False,name='usuario_id')

    __tablename__ = 'tareas'
