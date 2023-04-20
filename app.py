# Importar la libreria
from flask import Flask, request, render_template, redirect, jsonify

# Objeto de tipo Flask
app = Flask(__name__)

Personas = []

# Raiz del sitio
@app.route('/')
def inicio():
    # return (f"Hola mundo...")
    # mensaje = "Bienvenido al desarrollo de aplicaciones web"
    # return render_template("bienvenido.html", texto=mensaje)
    return redirect("calculadora")
# El código contiene una función llamada hola mundo que contiene un decorador @app.route('/') para
# mapear la ruta de la URL de la función. Adicionalmente la ruta apunta a la raíz del proyecto.

@app.route("/saludo/<nombre>")
def saludo(nombre):
    return (f"Hola {nombre}")

@app.route("/numero/<n>")
def parImpar(n):
    if (int(n)%2 == 0):
        return (f"El número {n} es par")
    else:
        return (f"El número {n} es impar")
    
@app.route("/saludar/<nombre>")
def saludar(nombre):
    titulo = request.args.get('titulo')
    edad = request.args.get('edad')
    genero = request.args.get('genero')
    return (f"Hola {titulo} {nombre} Edad: {edad} Genero: {genero}")

@app.route("/tablas")
def tablas():
    Personas.clear()
    persona1 = ["Juan Sebastián","Laguna Yara","juansebt.0610@gmail.com"]
    persona2 = ["Javier Alexis","Rojas","jalexis87@gmail.com"]
    persona3 = ["Maira Fernanda","Osorio Flores","mafalda266@gmail.com"]
    persona4 = ["Fransua","Gomez","franco0001@gmail.com"]
    Personas.append(persona1)
    Personas.append(persona2)
    Personas.append(persona3)
    Personas.append(persona4)
    
    return render_template('tabla.html', personas=Personas)

@app.route("/calculadora")
def calculadora():
    return render_template('calculadora.html')

@app.route("/operaciones", methods=["POST"])
def operaciones():
    if request.method == "POST":
        mensaje = ""
        d = (None,None,None)
        accion = request.form["btnAction"]
        if (accion == "Sumar"):
            n1 = float(request.form["txtNumero1"])
            n2 = float(request.form["txtNumero2"])
            # if (n1 and n2):
            resultado = n1 + n2
            d = (n1,n2,resultado)
        elif (accion == "Restar"):
            n1 = float(request.form["txtNumero1"])
            n2 = float(request.form["txtNumero2"])
            # if (n1 and n2):
            resultado = n1 - n2
            d = (n1,n2,resultado)
        elif (accion == "Multiplicar"):
            n1 = float(request.form["txtNumero1"])
            n2 = float(request.form["txtNumero2"])
            # if (n1 and n2):
            resultado = n1 * n2
            d = (n1,n2,resultado)
        elif (accion == "Dividir"):
            n1 = float(request.form["txtNumero1"])
            n2 = float(request.form["txtNumero2"])
            # if (n1 and n2):
            if (n2 == 0.0):
                mensaje = "ERROR - ¡No se puede dividir por cero!"
                print(mensaje)
            else:
                resultado = n1 / n2
                d = (n1,n2,resultado)
        print(mensaje)
        return render_template("calculadora.html",datos=d,mensaje=mensaje)
    
@app.route("/sumar",methods=["POST"])
def sumar():
    n1 = float(request.form["txtNumero1"])
    n2 = float(request.form["txtNumero2"])
    resultado = n1 + n2
    return jsonify({"resultado":resultado, "estado":True})

@app.route("/restar",methods=["POST"])
def restar():
    n1 = float(request.form["txtNumero1"])
    n2 = float(request.form["txtNumero2"])
    resultado = n1 - n2
    return jsonify({"resultado":resultado, "estado":True})

@app.route("/multiplicar",methods=["POST"])
def multiplicar():
    n1 = float(request.form["txtNumero1"])
    n2 = float(request.form["txtNumero2"])
    resultado = n1 * n2
    return jsonify({"resultado":resultado, "estado":True})

@app.route("/dividir",methods=["POST"])
def dividir():
    n1 = float(request.form["txtNumero1"])
    n2 = float(request.form["txtNumero2"])
    if (n2 == 0):
        return jsonify({"resultado":"ERROR - ¡No se puede dividir por cero!", "estado":True})
    else:
        resultado = n1 / n2
        return jsonify({"resultado":resultado, "estado":True})

# Iniciar la aplicación    
if (__name__ == "__main__"):
    app.run(host="0.0.0.0", port=3000, debug=True)
# En el código anterior se crea una instancia de Flask y se inicia la aplicación por el puerto 3000 y en
# modo debug para que se recargue automaticamente si hay actualizaciones en el código y muestre
# errores.