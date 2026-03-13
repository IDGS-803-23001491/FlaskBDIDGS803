from . import inscripciones
from flask import request, render_template,redirect, url_for
from models import Curso,db,Alumnos

import forms

@inscripciones.route('/inscripciones', methods=["GET","POST"])
def linscripciones():
    create_form = forms.CursoFrom(request.form)
    curso = Curso.query.all()
    return render_template("inscripciones/lista.html",form=create_form,curso=curso)

@inscripciones.route('/inscripciones/agregar', methods=["GET","POST"])
def agregar():
    create_form = forms.CursoFrom(request.form)
    alumnos = Alumnos.query.all()
    id = request.args.get('id')

    if request.method == "GET":
         m = db.session.query(Curso).filter(Curso.id == id).first()
         create_form.id.data = id
         create_form.nombre.data = m.nombre

    if request.method == "POST":
        print(int(request.form.get("alumno_id")))
        m = db.session.query(Curso).filter(Curso.id == id).first()
        alumno = db.session.query(Alumnos).filter(Alumnos.id == int(request.form.get("alumno_id"))).first()

        if alumno not in m.alumnos:
            m.alumnos.append(alumno)
            db.session.commit()

        return redirect(url_for('inscripciones.linscripciones'))
    return render_template('inscripciones/agregar.html',form=create_form, alumnos = alumnos)

@inscripciones.route('/inscripciones/eliminar', methods=["GET","POST"])
def eliminar():
    create_form = forms.CursoFrom(request.form)
    
    id = request.args.get('id')

    if request.method == "GET":
         m = db.session.query(Curso).filter(Curso.id == id).first()
         alumnos = m.alumnos
         create_form.id.data = id
         create_form.nombre.data = m.nombre

    if request.method == "POST":
        print(int(request.form.get("alumno_id")))
        m = db.session.query(Curso).filter(Curso.id == id).first()
        alumno = db.session.query(Alumnos).filter(Alumnos.id == int(request.form.get("alumno_id"))).first()

        m.alumnos.remove(alumno)
        db.session.commit()

        return redirect(url_for('inscripciones.linscripciones'))
    return render_template('inscripciones/borrar.html',form=create_form, alumnos = alumnos)
