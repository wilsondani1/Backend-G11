from sqlalchemy import Column ,types
from sqlalchemy.sql.schema import ForeignKey
from datetime import datetime
from db import conexion

class Producto(conexion.Model):
    id = Column(type_=types.Integer ,autoincrement=True,primary_key=True)
    nombre = Column(type_=types.Text, nullable=False)
    precio = Column(type_=types.Float)
    imagen = Column(type_=types.Text)
    categoriaId = Column(ForeignKey(column='categoria.id'),type_=types.Integer,nullable=False,name='categoria_id')

    created_at = Column(type_=types.DateTime, default=datetime.utcnow,name='createdAt')

    __tablename__ = 'productos'