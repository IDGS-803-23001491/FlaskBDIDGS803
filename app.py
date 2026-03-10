from flask import Flask, render_template, request, redirect, url_for, flash, g
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from models import db,Alumnos
from maestros.routes import maestros

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
csrf = CSRFProtect()
db.init_app(app)
migrate = Migrate(app,db)

import forms

@app.route("/",methods=["GET","POST"])
@app.route("/index")
def index():
	create_form = forms.UserFrom(request.form)
	alumno = Alumnos.query.all()
	return render_template("index.html",form=create_form,alumno=alumno)

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
	create_form = forms.UserFrom(request.form)

	if request.method == "POST":
		alum = Alumnos(
			nombre = create_form.nombre.data,
			apellidos = create_form.apellidos.data,
			telefono = create_form.telefono.data,
			email = create_form.email.data
				 )
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("Alumnos.html",form=create_form)
	

@app.route("/detalles",methods=["GET","POST"])
def detalles():

	if request.method == "GET":
		id = request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		nombre = alum1.nombre
		apellidos = alum1.apellidos
		telefono = alum1.telefono
		email = alum1.email

	return render_template("detalles.html",nombre = nombre, apellidos = apellidos,telefono = telefono, email = email)

@app.route("/modificar",methods=["GET","POST"])
def modificar():
	create_form = forms.UserFrom(request.form)
	id = request.args.get('id')
	if request.method == "GET":
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		create_form.id.data = id
		create_form.nombre.data = alum1.nombre
		create_form.apellidos.data = alum1.apellidos
		create_form.telefono.data = alum1.telefono
		create_form.email.data = alum1.email

	if request.method == "POST":
		id = create_form.id.data
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		alum1.nombre = create_form.nombre.data
		alum1.apellidos = create_form.apellidos.data
		alum1.telefono = create_form.telefono.data
		alum1.email = create_form.email.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template("modificar.html",form=create_form)

@app.route("/eliminar",methods=["GET","POST"])
def eliminar():
	create_form = forms.UserFrom(request.form)
	id = request.args.get('id')
	if request.method == "GET":
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		create_form.id.data = id
		create_form.nombre.data = alum1.nombre
		create_form.apellidos.data = alum1.apellidos
		create_form.telefono.data = alum1.telefono
		create_form.email.data = alum1.email

	if request.method == "POST":
		id = create_form.id.data
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		alum1.nombre = create_form.nombre.data
		alum1.apellidos = create_form.apellidos.data
		alum1.telefono = create_form.telefono.data
		alum1.email = create_form.email.data
		db.session.delete(alum1)
		db.session.commit()
		return redirect(url_for('index'))

	return render_template("eliminar.html",form=create_form)

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True)
