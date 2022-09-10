from flask import Flask  # Importa Flask para permitirnos crear nuestra aplicación
app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def hola_mundo():
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/dojo')          # El decorador "@" asocia esta ruta dojo con la función inmediatamente siguiente
def hola_dojo():               #devuelve hola dojo
    return 'Hola Dojo!'


@app.route('/say/<myvariable>')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def say(myvariable):
    return f'Hola {myvariable}'


@app.route('/repeat/<int:numero>/<string:myvariable>')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def repeat(numero, myvariable):
    return f'Hola {myvariable * numero}'




if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración



