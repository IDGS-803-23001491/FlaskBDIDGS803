from . import alumnos
from flask import request, render_template,redirect, url_for
from models import Alumnos,db

import forms

@alumnos.route("/alumnos/agregar",methods=["GET","POST"])
def agregar():
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
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/agregar.html",form=create_form)
	
@alumnos.route("/alumnos/modificar",methods=["GET","POST"])
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
		return redirect(url_for('alumnos.index'))

	return render_template("alumnos/modificar.html",form=create_form)

@alumnos.route("/alumnos/eliminar",methods=["GET","POST"])
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
		return redirect(url_for('alumnos.index'))

	return render_template("alumnos/borrar.html",form=create_form)

@alumnos.route("/alumnos/detalles",methods=["GET","POST"])
def detalles():

	if request.method == "GET":
		id = request.args.get('id')
		alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		nombre = alum1.nombre
		apellidos = alum1.apellidos
		telefono = alum1.telefono
		email = alum1.email
		cursos = alum1.cursos

	return render_template("alumnos/detalles.html",nombre = nombre, apellidos = apellidos,
						telefono = telefono, email = email, cursos = cursos)

@alumnos.route("/alumnos",methods=["GET","POST"])
def index():
	create_form = forms.UserFrom(request.form)
	alumno = Alumnos.query.all()
	return render_template("alumnos/listaA.html",form=create_form,alumno=alumno)