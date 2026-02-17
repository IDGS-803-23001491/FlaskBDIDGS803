from wtforms import Form
from wtforms import StringField,IntegerField,PasswordField
from wtforms import EmailField
from wtforms import validators

class UserFrom(Form):
    id = IntegerField('id')
    nombre = StringField('nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4,max=20,message='Ingrese nombre entre 4 y 20')
    ])
    apaterno = StringField('apaterno',[
        validators.DataRequired(message='El campo es requerido')
    ])
    email = EmailField('correo',[
        validators.DataRequired(message='El campo es requerido'),
        validators.Email(message='Ingrese un correo válido')
    ])
