from marshmallow_sqlalchemy import SQLAlchemyAutoSchema,auto_field
from marshmallow import fields
from models.producto_model import Producto
from dtos.categoria_dto import CategoriaDto

class ProductoDto(SQLAlchemyAutoSchema):
    class Meta:
        include_fk =True
        model = Producto

# class MOstrarProductosDto(SQLAlchemyAutoSchema):
#     categoriaId = fields.Nested(nested=CategoriaDto)
#     class Meta:
#         include_fk = True
#         model = Producto

