# Importa Flask para permitirnos crear nuestra aplicación
#tambien importamos la funcionalidad para renderizar temaplates
#Realizado por Rafael Fernandez
from flask import Flask, render_template  

app = Flask(__name__)    # Crea una nueva instancia de la clase Flask llamada "app"

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def render_tabla(): 
  #Lista de estudiantes
  users = [
   {'first_name' : 'Michael', 'last_name' : 'Choi'},
   {'first_name' : 'John', 'last_name' : 'Supsupin'},
   {'first_name' : 'Mark', 'last_name' : 'Guillen'},
   {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ]
  
  return render_template('tabla_html.html', students = users) # Devuelve el render del archivo tabla_html.html


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración
