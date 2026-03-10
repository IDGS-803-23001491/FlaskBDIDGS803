from . import maestros
from flask import request, render_template,redirect, url_for
from models import Maestros,db

import forms

@maestros.route('/maestros/agregar', methods=["GET","POST"])
def agregar():
    create_form = forms.MaestroFrom(request.form)

    if request.method == "POST":
        m = Maestros(
            nombre = create_form.nombre.data,
			apellidos = create_form.apellidos.data,
			especialidad = create_form.especialidad.data,
			email = create_form.email.data
        )

        db.session.add(m)
        db.session.commit()

        return redirect(url_for('maestros.lmaestros'))
    return render_template('maestros/agregar.html',form=create_form)

@maestros.route('/maestros/modificar', methods=["GET","POST"])
def modificar():
    create_form = forms.MaestroFrom(request.form)
    matricula = request.args.get('id')

    if request.method == "GET":
         m = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
         create_form.matricula.data = matricula
         create_form.nombre.data = m.nombre
         create_form.apellidos.data = m.apellidos
         create_form.especialidad.data = m.especialidad
         create_form.email.data = m.email

    if request.method == "POST":
        matricula = create_form.matricula.data
        m = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        m.nombre = create_form.nombre.data
        m.apellidos = create_form.apellidos.data
        m.especialidad = create_form.especialidad.data
        m.email = create_form.email.data

        db.session.add(m)
        db.session.commit()

        return redirect(url_for('maestros.lmaestros'))
    return render_template('maestros/modificar.html',form=create_form)

@maestros.route('/maestros/eliminar', methods=["GET","POST"])
def eliminar():
    create_form = forms.MaestroFrom(request.form)
    id = request.args.get('id')

    if request.method == "GET":
         m = db.session.query(Maestros).filter(Maestros.matricula == id).first()
         create_form.matricula.data = id
         create_form.nombre.data = m.nombre
         create_form.apellidos.data = m.apellidos
         create_form.especialidad.data = m.especialidad
         create_form.email.data = m.email

    if request.method == "POST":
        maestros = create_form.matricula.data
        m = db.session.query(Maestros).filter(Maestros.matricula == id).first()
        m.nombre = create_form.nombre.data
        m.apellidos = create_form.apellidos.data
        m.especialidad = create_form.especialidad.data
        m.email = create_form.email.data

        db.session.delete(m)
        db.session.commit()

        return redirect(url_for('maestros.lmaestros'))
    return render_template('maestros/borrar.html',form=create_form)

@maestros.route("/maestros/detalles",methods=["GET","POST"])
def detalles():

	if request.method == "GET":
		matricula = request.args.get('id')
		m = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
		nombre = m.nombre
		apellidos = m.apellidos
		especialidad = m.especialidad
		email = m.email

	return render_template("maestros/detalles.html",nombre = nombre, apellidos = apellidos,especialidad = especialidad, email = email)


@maestros.route('/maestros', methods=["GET","POST"])
def lmaestros():
    create_form = forms.MaestroFrom(request.form)
    maestro = Maestros.query.all()
    return render_template("maestros/listaM.html",form=create_form,maestro=maestro)


@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"