from wtforms import Form
from wtforms import StringField,IntegerField,PasswordField
from wtforms import EmailField
from wtforms import validators

class UserFrom(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre',[
        validators.DataRequired(message='El campo es requerido'),
        validators.Length(min=4,max=20,message='Ingrese nombre entre 4 y 20')
    ])
    apaterno = StringField('A. Paterno',[
        validators.DataRequired(message='El campo es requerido')
    ])
    email = EmailField('Correo',[
        validators.DataRequired(message='El campo es requerido'),
        validators.Email(message='Ingrese un correo válido')
    ])
