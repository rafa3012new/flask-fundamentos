from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)  
app.secret_key = 'session_counter_rafael'

#ruta principal
@app.route('/')          
def contador_visitas():    

  session['contador'] = session['contador']+1 if 'contador' in session else 1

  if 'incrementoboton' not in session:
    session['incrementoboton'] = 2

  
  return render_template('contador_visitas.html')

#ruta llimpiar session
@app.route('/destroysession', methods=['GET','POST'])          
def limpiar_contador():
  session.clear()
  return redirect('/')

#ruta para actualizar el incremento del boton
@app.route('/menuincrementoboton')          
def menu_actualizar_boton():    

  return render_template('configurar_incremento.html')



#ruta para actualizar el incremento del boton
@app.route('/actualizarincrementoboton', methods=['POST'])          
def actualizar_boton():    

  session['incrementoboton'] = int(request.form['select_incremento'])

  #para que cuando se redirija le sume esta resta
  session['contador']-=1

  return redirect('/')

#ruta para actualizar el incremento del boton
@app.route('/incrementoboton')          
def contador_boton():    

  session['contador'] = session['contador']+session['incrementoboton'] if 'contador' in session else session['incrementoboton']

  #para que cuando se redirija le sume esta resta
  session['contador']-=1

  return redirect('/')




if __name__=="__main__":  
    app.run(debug=True)    
