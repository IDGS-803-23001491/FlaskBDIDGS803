from flask import Flask, render_template, request, redirect, url_for, flash, g
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db,Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

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
			aPaterno = create_form.apaterno.data,
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
		aPaterno = alum1.aPaterno
		email = alum1.email

	return render_template("detalles.html",nombre = nombre, aPaterno = aPaterno, email = email)

if __name__ == '__main__':
	csrf.init_app(app)
	db.init_app(app)
	with app.app_context():
		db.create_all()
	app.run(debug=True)
