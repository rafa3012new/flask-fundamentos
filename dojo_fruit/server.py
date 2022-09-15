from dataclasses import replace
from flask import Flask, render_template, request, redirect, session
from datetime import date
import os

app = Flask(__name__)
app.secret_key = 'secretninja'

#!/usr/bin/env python3



#Ruta Raiz carga una lista de diccionarios via GET render
@app.route('/')        
def main_page(): 

  ruta = request.base_url

  lista_frutas = [
  {'nombre' : 'Frutilla Blanca', 'precio' : 0.50, 'ruta': ruta+'static/img/Frutilla Blanca.jpg' },
  {'nombre' : 'Chirimoya',       'precio' : 3.00, 'ruta': ruta+'static/img/Chirimoya.jpg' },
  {'nombre' : 'Banana',          'precio' : 0.75, 'ruta': ruta+'static/img/Banana.webp' },
  {'nombre' : 'Naranja',         'precio' : 3.00, 'ruta': ruta+'static/img/Naranja.jpg' },
  {'nombre' : 'Limon',           'precio' : 3.00, 'ruta': ruta+'static/img/Limon.jpg' },
  {'nombre' : 'Sandia',          'precio' : 3.00, 'ruta': ruta+'static/img/Sandia.jpg' },
  {'nombre' : 'Maqui',           'precio' : 0.60, 'ruta': ruta+'static/img/Maqui.png' },
  {'nombre' : 'Papaya',          'precio' : 0.50, 'ruta': ruta+'static/img/Papaya.jpg' },
  {'nombre' : 'Manzana',         'precio' : 1.00, 'ruta': ruta+'static/img/Manzana.jpg' },
  {'nombre' : 'Melon',           'precio' : 0.75, 'ruta': ruta+'static/img/Melon.jpg' },
  {'nombre' : 'Mango',           'precio' : 0.50, 'ruta': ruta+'static/img/Mango.webp' },
  {'nombre' : 'Piña',            'precio' : 3.00, 'ruta': ruta+'static/img/Piña.jpg' },
  {'nombre' : 'kiwi',            'precio' : 3.00, 'ruta': ruta+'static/img/Kiwi.webp' },
  {'nombre' : 'Rosa Mosqueta',   'precio' : 1.00, 'ruta': ruta+'static/img/Rosa Mosqueta.jpg' },
  {'nombre' : 'Frutilla',        'precio' : 0.75, 'ruta': ruta+'static/img/Frutilla.jpg' },
  {'nombre' : 'Agua y Manto',    'precio' : 0.25, 'ruta': ruta+'static/img/Agua y Manto.jpg' },
  {'nombre' : 'Uvas',            'precio' : 0.25, 'ruta': ruta+'static/img/Uva.jpg' },
  {'nombre' : 'Duraznos',        'precio' : 0.25, 'ruta': ruta+'static/img/Durazno.jpg' },
  {'nombre' : 'Peras',           'precio' : 0.25, 'ruta': ruta+'static/img/Pera.webp' },
  {'nombre' : 'Guayabas',        'precio' : 0.25, 'ruta': ruta+'static/img/Guayaba.jpg' }
  ]


  # la variable de lista de diccionarios lista_fruta se guarda en una variable de sesion
  session['lista_frutas'] = lista_frutas

  #tambien se devuelve la lista de diccionarios como una variable renderizada GET como practica
  return render_template('main.html', frutas = lista_frutas) 
  
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
@app.route('/procesar', methods=['POST'])
def procesar_usuario():

  #se obtinenen la columna cantidad de la tabla como un arreglo de inputs del form
  #colocando como el nombre del campo mas corchetes
  #se obtiene el arreglo con el metodo getlist()
  lista_cantidad = request.form.getlist('cantidad[]')

  #se agrega a la variable de sesion lista_frutas las siguientes columnas
  #cantidad obtenida del array de inputs con getlist
  #subtotal obtenido del calculo del campo precio * cantidad
  x = 0
  total_articulos = 0
  monto_total = 0
  nueva_lista = []


  for i in session['lista_frutas']:
    i['cantidad']= lista_cantidad[x]
    i['subtotal']= i['precio']*float(lista_cantidad[x])
    total_articulos+= int(lista_cantidad[x])
    monto_total+=  i['subtotal']
    if float(lista_cantidad[x]) > 0:
      nueva_lista.append(i)
    x+= 1
  

  
  if len(nueva_lista) > 0:
    session['lista_frutas'] = nueva_lista
  else:
    session['lista_frutas'] = [{'nombre' : 'No selecciono Fruta', 'precio' : 0.00, 'cantidad':0,'subtotal':0 }]

  
  #se obtienen los otros inputs de texto plano del form
  #y se almacenan en variables de sesion
  session['nombre_estudiante'] = request.form['nombre_estudiante']
  session['id_estudiante'] = request.form['id_estudiante']
  session['total_articulos'] = total_articulos
  session['monto_total'] = monto_total
  

  #se redirige el POST hacia la pagina de checkout
  return redirect('/checkout')



#Ruta para el checkout
@app.route('/checkout')
def checkout():
  #se rederiza la pagina checkout
  diasemana = ['Domingo','Lunes','Martes','Miercoles','Jueves','Viernes','Sabado','Domingo']
  meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
    
  today = diasemana[date.today().weekday()] + ', ' + str(date.today().day) + ' de ' + meses[date.today().month] + ' de ' + str(date.today().year)
  return render_template('checkout.html',hoy = today)



#Ruta para el checkout
@app.route('/catalogo')
def catalog_page(): 
  return render_template('catalog.html') 


if __name__=="__main__":   # Asegúrate de que este archivo se esté ejecutando directamente y no desde un módulo diferente    
    app.run(debug=True)    # Ejecuta la aplicación en modo de depuración