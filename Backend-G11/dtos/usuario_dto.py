from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema,fields
from models.usuario_model import Usuario


class UsuarioDto(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario

class loginDto(Schema):
        correo = fields.Email(requierd=True,error_messages={'required':'el correo debe ser requerido'})
        password = fields.Str(requierd=True,error_messages={'required':'el password debe ser requerido'})
