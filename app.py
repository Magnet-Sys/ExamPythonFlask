# Proyecto de Dianna Monsalve
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/ejercicio_1', methods=['GET', 'POST'])
def ejercicio_1():
   nombre = None
   total_sin_descuento = 0
   descuento = 0
   total_a_pagar = 0

   if request.method == 'POST':
       nombre = request.form['nombre']
       edad = int(request.form['edad'])
       cantidad = int(request.form['cantidad'])

       total_sin_descuento = cantidad * 9000

       if 18 <= edad <= 30:
           descuento = total_sin_descuento * 0.15
       elif edad > 30:
           descuento = total_sin_descuento * 0.25

       total_a_pagar = total_sin_descuento - descuento

   return render_template('ejercicio_1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, descuento=descuento, total_a_pagar=total_a_pagar)

if __name__ == '__main__':
   app.run()
