from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/ejercicio1', methods=['GET', 'POST'])
def calculo():
    promedio = ""
    aprobado = ""

    if request.method == 'POST':
            nota1 = int(request.form['nota1'])
            nota2 = int(request.form['nota2'])
            nota3 = int(request.form['nota3'])
            asistencia = int(request.form['asistencia'])

            if 10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70 and 0 <= asistencia <= 100:
                promedio = (nota1 + nota2 + nota3) / 3

                if promedio >= 40 and asistencia >= 75:
                    aprobado = "Aprobado"
                else:
                    aprobado = "Reprobado"

    return render_template('ejercicio1.html', promedio=promedio, aprobado=aprobado)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def respuestas():
        nombre_mayor = ""
        cantidad_caracteres = ""

        if request.method == 'POST':
            nombre1 = request.form['nombre1']
            nombre2 = request.form['nombre2']
            nombre3 = request.form['nombre3']


            longitudes = {
                nombre1: len(nombre1),
                nombre2: len(nombre2),
                nombre3: len(nombre3)
            }
            nombre_mayor = max(longitudes, key=longitudes.get)
            cantidad_caracteres = longitudes[nombre_mayor]

        return render_template('ejercicio2.html',nombre_mayor=nombre_mayor, cantidad_caracteres=cantidad_caracteres)

if __name__ == '__main__':
    app.run()