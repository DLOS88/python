from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tareas.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class tareas(db.Model):### detro del archivo html show_all en el campo student
    ### html({% for variable in anterior %})
    ### class students(db.Model):
    ### variable = variable22
    ### return render_template('show_all.html', variable22 = students.query.all() )
   id = db.Column('tarea_id', db.Integer, primary_key = True)
   numero = db.Column(db.String(10))
   ### numero nombre de la variable qeu se define en html show_all
   ### html (<td>{{ student.numero }}</td>)
   nombre = db.Column(db.String(50))
   responsable = db.Column(db.String(200))
   pin = db.Column(db.String(10))

   def __init__(self, numero, nombre, responsable,pin):
       self.numero = numero
       self.nombre = nombre
       self.responsable = responsable
       self.pin = pin

@app.route('/')
def show_all():
   return render_template('show_all.html', tarea = tareas.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['nombre'] or not request.form['numero'] or not request.form['responsable']:
         flash('Please enter all the fields', 'error')
      else:
         tar = tareas(request.form['numero'], request.form['nombre'],request.form['responsable'], request.form['pin'])

         db.session.add(tar)
         db.session.commit()
         flash('Record was successfully added')
         return redirect(url_for('show_all'))
   return render_template('new.html')

@app.route("/update", methods=["POST"])
def update():
    numero = request.form.get("oldname")
    tar = tareas.query.filter_by(numero=numero).first()
    return render_template('update.html', result = tar, oldname = numero)

@app.route("/update_record", methods=["POST"])
def update_record():
    name1 = request.form.get("oldname")
    tar = tareas.query.filter_by(numero=name1).first()
    tar.numero = request.form['numero']
    tar.nombre = request.form['nombre']
    tar.responsable = request.form['responsable']
    tar.pin = request.form['pin']
    db.session.commit()
    return redirect('/')

@app.route("/delete", methods=["POST"])
def delete():
    name2 = request.form.get("oldname")
    tar = tareas.query.filter_by(numero=name2).first()
    db.session.delete(tar)
    db.session.commit()
    return redirect("/")

if __name__ == '__main__':
   db.create_all()
   app.run(debug = True)
