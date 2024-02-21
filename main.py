from flask import Flask, render_template, request, flash, Response, redirect
from flask_wtf.csrf import CSRFProtect
import form
from flask import g

app = Flask(__name__)
app.secret_key = 'clave_secreta'


@app.route("/index")
def index():
    escuela = "UTL"
    alumnos = ["MArio","Luis","Pedro","Dario"]
    return render_template("index.html",escuela =  escuela, alumnos = alumnos)

@app.route("/alumnos", methods=["GET","POST"])
def alumno():
    g.nombre = 'Daniel'
    print('dentro alumnos')
    nom = ''
    apa = ''
    ama = ''
    correo = ''
    alum_form = form.UserForm(request.form)
    if request.method == 'POST' and alum_form.validate():
        print(f'hola: {g.nombre}')
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data
        correo = alum_form.correo.data
        mensaje = f'Bienvenido {nom}'
        flash(mensaje)
        print("nombre: {x}, apaterno: {y}, amaterno: {t}, correo: {w}".format(x = nom, y = apa, t = ama, w = correo))
        
    
    return render_template("alumnos.html", form = alum_form )

@app.route("/maestros")
def maestro():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return "<p><h1>Sei hey!!</h1></p>"
    
@app.route("/user/<string:name>")
def user(name):
    return "<p>hola estimado: "+ name + "</p>"

@app.route("/numero/<int:n>")
def numero(n):
    return "el numero es: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id, name):
    return "Id: {} Nombre {}".format(id, name)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "el valor de {} + {} = {}".format(n1, n2, n1 + n2)

@app.route("/default")
@app.route("/default/<string:ab>")
def func2(ab = "UTL"):
    return "el valor es: "+ ab
    
@app.route("/multiplicar", methods=["GET","POST"])
def multi():
    if request.method == "POST":
        num1= request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1>La multiplicacion es:  {}</h1>".format(str(int(num1)*int(num2)))
    else:
        return '''
        <form action"/multiplicar method="POST">
            <label>N1:</label>
            <input type="text" name="n1" />
            <br>
            <label>N2:</label>
            <input type="text" name="n2" />
            <input type="submit" />
        </form>
        '''

@app.route("/formulario1")
def formulario1():
    return render_template("formulario.html")

@app.route("/formulario2")
def formulario2():
    return render_template("formulario2.html")

@app.route("/resultado", methods=["GET","POST"])
def resultado():
    if request.method == "POST":
        num1= request.form.get("n1")
        num2 = request.form.get("n2")
        return "<h1>La multiplicacion es:  {}</h1>".format(str(int(num1)*int(num2)))



# realizado 20/02/2024 

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.nombre = 'Daniel'
    print('before_request')
    
    
@app.after_request
def after_request(response):
    print('ultimo')
    if 'Daniel' not in g.nombre and request.endpoint not in['/index']:
        return redirect('index.html')
    return response
    
# ------------------------------------------------------------
if __name__ =="__main__":
    app.run(debug = True)   #se utiliza debug = True para ctivar "actualizaciones en caliente" similar liveServer
#   para tumbar el servidor es con el comando ctrl + c
#   para activarlo se ejecuta el archivo, escribir en la terminal "py nombre.py"