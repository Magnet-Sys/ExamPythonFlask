# Proyecto de Dianna Monsalve

# Se importan las clases Flask, render_template y request desde el módulo flask
from flask import Flask, render_template, request

# Se crea una instancia de la clase Flask
app = Flask(__name__)

# Se define la ruta para la página de inicio-->
@app.route('/')
def index():
    # Se renderiza la plantilla index.html
   return render_template('index.html')

# Se define la ruta para el ejercicio 1 -->
@app.route('/ejercicio_1', methods=['GET', 'POST'])
def ejercicio_1():
    # Se inicializan las variables
   nombre = None
   total_sin_descuento = 0
   descuento = 0
   total_a_pagar = 0
    # Se verifica metodo de la solicitud
   if request.method == 'POST':
       # Se obtienen los valores del formulario
       nombre = request.form['nombre']
       edad = int(request.form['edad'])
       cantidad = int(request.form['cantidad'])
        # Se calcula el total sin descuento
       total_sin_descuento = cantidad * 9000
        # Se calcula el descuento según la edad
       if 18 <= edad <= 30:
           descuento = total_sin_descuento * 0.15
       elif edad > 30:
           descuento = total_sin_descuento * 0.25
        # Se calcula total a pagar
       total_a_pagar = total_sin_descuento - descuento
    # Se renderiza la plantilla 'ejercicio_1' con los valores calculados
   return render_template('ejercicio_1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, total_a_pagar=total_a_pagar)

# Se define la ruta para el ejercicio 2 -->
@app.route('/ejercicio_2', methods=['GET', 'POST'])
def ejercicio_2():
    # Se inicailiza la variable mensaje
   mensaje = None
    # Se verifica metodo de la solicitud
   if request.method == 'POST':
       # Se obtienen los valores del formulario
       nombre = request.form['nombre']
       contrasena = request.form['contraseña']
        # Se verifica el nombre de usuario y la contraseña
        # Se refactoriza la condicion del if utilizando operador 'in' para mejorar el codigo
       if nombre in ('juan', 'Juan') and contrasena == 'admin':
           mensaje = 'Bienvenido Administrador Juan'
       elif nombre in ('pepe', 'Pepe') and contrasena == 'user':
           mensaje = 'Bienvenido Usuario Pepe'
       else:
           mensaje = 'Usuario o contraseña incorrectos'
    # Se renderizaa la plantilla 'ejercicio_2' con el mensaje segun la condicion
   return render_template('ejercicio_2.html', mensaje=mensaje)

# Se ejecuta la aplicación
if __name__ == '__main__':
   app.run()
