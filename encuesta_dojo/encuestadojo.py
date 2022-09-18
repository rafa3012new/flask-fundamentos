from flask import Flask, render_template, request, redirect, session
from datetime import date
import os

app = Flask(__name__)
app.secret_key = 'secretninja'

#!/usr/bin/env python3

#Ruta Raiz carga una lista de diccionarios via GET render
@app.route('/')
def main_page():
  #tambien se devuelve la lista de diccionarios como una variable renderizada GET como practica
  return render_template('main.html')

#Ruta para Limpiar
@app.route('/limpiar')
def limpiar():
  session.clear()
  return redirect('/')


#Ruta por si el susuario volvio atras por un boton y no por el explorador
@app.route('/regreso')
def redirigir():
  print("ESTAMOS REDIRIGIENDO A INDEX!!!!")
  return redirect('/')


#Ruta para procesar ejecutando un metodo POST
@app.route('/grabar', methods=['POST'])
def procesar_usuario():

  #se obtienen los otros inputs de texto plano del form
  #y se almacenan en variables de sesion del form post
  session['nombre_estudiante'] = request.form['nombre_estudiante']
  session['ubicacion_dojo'] = request.form['ubicacion_dojo']
  session['idioma_favorito'] = request.form['idioma_favorito']
  session['comentarios'] = request.form['comentarios']
  #se alamacena la variable de tipo array_input con el metodo getlist
  session['lenguaje'] = request.form.getlist('lenguaje[]')
  session['edad'] = request.form['edad']

  #se redirige el POST hacia la pagina de checkout
  return redirect('/result')


#Ruta para el checkout
@app.route('/result')
def checkout():
  #se rederiza la pagina checkout
  diasemana = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
  meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

  today = diasemana[date.today().weekday()] + ', ' + str(date.today().day) + ' de ' + meses[date.today().month] + ' de ' + str(date.today().year)
  return render_template('enviado.html',hoy = today)


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración