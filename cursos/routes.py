from . import cursos
from flask import request, render_template,redirect, url_for
from models import Curso,db, Maestros

import forms

@cursos.route('/cursos/agregar', methods=["GET","POST"])
def agregar():
    create_form = forms.CursoFrom(request.form)
    maestros = Maestros.query.all()

    if request.method == "POST":
        m = Curso(
            nombre = create_form.nombre.data,
			descripcion = create_form.descripcion.data,
			maestro_id = create_form.maestro_id.data
        )

        db.session.add(m)
        db.session.commit()

        return redirect(url_for('cursos.lcursos'))
    return render_template('cursos/agregar.html',form=create_form, maestros = maestros)

@cursos.route('/cursos/modificar', methods=["GET","POST"])
def modificar():
    create_form = forms.CursoFrom(request.form)
    maestros = Maestros.query.all()
    id = request.args.get('id')

    if request.method == "GET":
         m = db.session.query(Curso).filter(Curso.id == id).first()
         create_form.id.data = id
         create_form.nombre.data = m.nombre
         create_form.descripcion.data = m.descripcion
         create_form.maestro_id.data = m.maestro_id

    if request.method == "POST":
        id = create_form.id.data
        m = db.session.query(Curso).filter(Curso.id == id).first()
        m.nombre = create_form.nombre.data
        m.descripcion = create_form.descripcion.data
        m.maestro_id = create_form.maestro_id.data

        db.session.add(m)
        db.session.commit()

        return redirect(url_for('cursos.lcursos'))
    return render_template('cursos/modificar.html',form=create_form, maestros = maestros)

@cursos.route('/cursos/eliminar', methods=["GET","POST"])
def eliminar():
    create_form = forms.CursoFrom(request.form)
    id = request.args.get('id')

    if request.method == "GET":
         m = db.session.query(Curso).filter(Curso.id == id).first()
         create_form.id.data = id
         create_form.nombre.data = m.nombre
         create_form.descripcion.data = m.descripcion
         create_form.maestro_id.data = m.maestro_id

    if request.method == "POST":
        cursos = create_form.id.data
        m = db.session.query(Curso).filter(Curso.id == id).first()
        m.nombre = create_form.nombre.data
        m.descripcion = create_form.descripcion.data
        m.maestro_id = create_form.maestro_id.data

        db.session.delete(m)
        db.session.commit()

        return redirect(url_for('cursos.lcursos'))
    return render_template('cursos/borrar.html',form=create_form)

@cursos.route("/cursos/detalles",methods=["GET","POST"])
def detalles():

	if request.method == "GET":
		id = request.args.get('id')
		m = db.session.query(Curso).filter(Curso.id == id).first()
		nombre = m.nombre
		descripcion = m.descripcion
		maestro = m.maestro.nombre +" " + m.maestro.apellidos

	return render_template("cursos/detalles.html",nombre = nombre, descripcion = descripcion,maestro = maestro)


@cursos.route('/cursos', methods=["GET","POST"])
def lcursos():
    create_form = forms.CursoFrom(request.form)
    curso = Curso.query.all()
    return render_template("cursos/listaC.html",form=create_form,curso=curso)
