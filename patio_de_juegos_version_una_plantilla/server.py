# Importa Flask para permitirnos crear nuestra aplicación
#tambien importamos la funcionalidad para renderizar temaplates
from cmath import phase
from flask import Flask, render_template  

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def indice():
    return render_template('index.html') # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/play')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def play():               #devuelve hola dojo
    return render_template("play.html")

@app.route('/play/<int:num>')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def play_num(num):               #devuelve hola dojo
    return render_template("play_num.html",num=num)

@app.route('/play/<int:num>/<string:color>')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def play_num_color(num,color):               #devuelve hola dojo
    return render_template("play_num_color.html", num=num, color=color)


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración


