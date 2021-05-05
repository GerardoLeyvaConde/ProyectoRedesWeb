from flask import Flask, render_template, request, redirect, url_for
from config import DevelopmentConfig
from grafica import Grafica

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
g= Grafica()
dirigida= Grafica(True)

@app.route('/')
def index():
    title = "Prueba de Interfaz"
    vertices = []
    for key, data in g.lista_vertices.items():
        vertices.append(key)

    aristas = []
    for key, data in g.lista_aristas.items():
        aristas.append([data.origen, data.destino])

    num_v = g.numero_vertices
    num_a = g.numero_aristas

    return render_template('index.html', num_v = num_v, num_a = num_a, title=title, grafica=g, vertices=vertices, aristas=aristas)

@app.route('/vertices', methods= ['POST'])
def agregarVertice():
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice')
        g.agregarVertice(vertice)
        print(vertice)
    return redirect(url_for('index'))

@app.route('/aristas', methods= ['POST'])
def agregarArista():
    if(request.method == 'POST'):
        a1 = request.form.get('id_a1')
        a2 = request.form.get('id_a2')
        #Cambiar clave
        i = g.numero_aristas
        g.agregarArista("e"+str(i+1), a1, a2)
        i+=1
    return redirect(url_for('index'))

@app.route('/buscarVertice', methods= ['POST'])
def buscarVertice():
    g.restablecerColores()
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice_buscar')
        v = g.buscarVertice(vertice)
        v.color= 1
    return redirect(url_for('index'))

@app.route('/buscarArista', methods= ['POST'])
def buscarArista():
    g.restablecerColores()
    if(request.method == 'POST'):
        a1 = request.form.get('id_a1_b')
        a2 = request.form.get('id_a2_b')
        a = g.buscarArista(a1, a2)
        a.color= 1
    return redirect(url_for('index'))

@app.route('/eliminarVertice', methods= ['POST'])
def eliminarVertice():
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice')
        g.eliminarVertice(vertice)
        print("Borrado:", vertice)
    return redirect(url_for('index'))

@app.route('/eliminarArista', methods= ['POST'])
def eliminarArista():
    if(request.method == 'POST'):
        a1 = request.form.get('id_a1')
        a2 = request.form.get('id_a2')
        #Cambiar clave
        g.eliminarArista(a1, a2)
    return redirect(url_for('index'))

@app.route('/obtenerGrado', methods= ['POST'])
def obtenerGrado():
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice_grado')
        v = g.gradoVertice(vertice)
        print(v)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
