from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    escuela = "UTL"
    alumnos = ["MArio","Luis","Pedro","Dario"]
    return render_template("index.html",escuela =  escuela, alumnos = alumnos)

@app.route("/alumnos")
def alumno():
    return render_template("alumnos.html")

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
    


if __name__ =="__main__":
    app.run(debug = True)   #se utiliza debug = True para ctivar "actualizaciones en caliente" similar liveServer
#   para tumbar el servidor es con el comando ctrl + c
#   para activarlo se ejecuta el archivo, escribir en la terminal "py nombre.py"