# Importa Flask para permitirnos crear nuestra aplicación
#tambien importamos la funcionalidad para renderizar temaplates
#Realizado por Rafael Fernandez
from flask import Flask, render_template  

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def tablero():
    return render_template('tablero_estatico.html') # Devuelve el render del archivo tablero.html

@app.route('/<int:filas>')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def tablero_filas(filas):               
    return render_template("tablero_filas.html",filas=filas) # Devuelve el render del archivo tablero_filas.html pasando un parametro para filas

@app.route('/<int:filas>/<int:columnas>')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def tablero_filas_columnas(filas,columnas):               
    return render_template("tablero_filas_columnas.html",filas=filas,columnas=columnas) # Devuelve el render del archivo tablero_filas.html pasando un parametro para filas y otro para columnas

@app.route('/<int:filas>/<int:columnas>/<string:color1>')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def tablero_filas_columnas_color1(filas,columnas,color1):               
    return render_template("tablero_filas_columnas_color1.html",filas=filas,columnas=columnas,color1=color1) # Devuelve el render del archivo tablero_filas.html pasando un parametro para filas, otro para columnas y otro para color1

@app.route('/<int:filas>/<int:columnas>/<string:color1>/<string:color2>')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def tablero_filas_columnas_color1_color2(filas,columnas,color1,color2):               
    return render_template("tablero_filas_columnas_color1_color2.html",filas=filas,columnas=columnas,color1=color1,color2=color2) # Devuelve el render del archivo tablero_filas.html pasando un parametro para filas, otro para columnas, otro para color1 y otro para color2

if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
