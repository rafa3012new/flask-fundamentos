# Importa Flask para permitirnos crear nuestra aplicación
#tambien importamos la funcionalidad para renderizar temaplates
from flask import Flask, render_template  

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def indice():
    return render_template('index.html') # Devuelve el render el archivo index.html

@app.route('/play')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def play():             
    return render_template("play.html") # Devuelve el render el archivo play.html

@app.route('/play/<int:num>')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def play_num(num):             
    return render_template("play_num.html",num=num) # Devuelve el render el archivo play.html pasando 1 parametro

@app.route('/play/<int:num>/<string:color>')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def play_num_color(num,color):        
    return render_template("play_num_color.html", num=num, color=color) # Devuelve el render el archivo play.html pasando 2 parametros


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración


