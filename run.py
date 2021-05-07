from flask import Flask, render_template, request, redirect, url_for
from config import DevelopmentConfig
from grafica import Grafica

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
g= Grafica()
c= Grafica()
#dirigida= Grafica(True)

g.agregarVertice("a")
g.agregarVertice("b")
g.agregarVertice("c")
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g")
g.agregarVertice("h")
g.agregarVertice("i")
g.agregarVertice("j")
g.agregarVertice("k")
#g.agregarVertice("l")
#g.agregarVertice("m")
#g.agregarVertice("n")
#g.agregarVertice("o")
#g.agregarVertice("p")
g.agregarArista("e1","a","b", 3)
g.agregarArista("e2","a","c", 1)
g.agregarArista("e3","a","d", 2)
g.agregarArista("e4","a","f", 1)
g.agregarArista("e5","b","c", 2)
g.agregarArista("e6","b","d", 3)
g.agregarArista("e7","b","e", 10)
g.agregarArista("e8","c","e", 1)
g.agregarArista("e9","c","h", 1)
g.agregarArista("e10","d","e", 2)
g.agregarArista("e11","d","f", 10)
g.agregarArista("e12","e","f", 2)
g.agregarArista("e13","e","g", 1)
g.agregarArista("e14","e","h", 2)
g.agregarArista("e15","f","g", 2)
g.agregarArista("e16","f","i", 3)
g.agregarArista("e17","g","h", 1)
g.agregarArista("e18","g","i", 2)
g.agregarArista("e19","g","j", 3)
g.agregarArista("e20","h","j", 5)
g.agregarArista("e21","i","j", 2)
g.agregarArista("e22","i","k", 7)
g.agregarArista("e23","j","k", 1)

"""
g.agregarArista("e1","a","b")
g.agregarArista("e2","a","e")
g.agregarArista("e3","a","f")
g.agregarArista("e4","b","c")
g.agregarArista("e5","b","e")
g.agregarArista("e6","b","g")
g.agregarArista("e7","c","d")
g.agregarArista("e8","c","g")
g.agregarArista("e9","c","h")
g.agregarArista("e10","d","h")
g.agregarArista("e11","e","f")
g.agregarArista("e12","e","i")
g.agregarArista("e13","f","g")
g.agregarArista("e14","f","j")
g.agregarArista("e15","f","o")
g.agregarArista("e16","g","h")
g.agregarArista("e17","g","k")
g.agregarArista("e18","h","l")
g.agregarArista("e19","i","j")
g.agregarArista("e20","i","m")
g.agregarArista("e21","j","m")
g.agregarArista("e22","j","n")
g.agregarArista("e23","k","l")
g.agregarArista("e24","k","n")
g.agregarArista("e25","k","o")
g.agregarArista("e26","l","p")
g.agregarArista("e27","n","o")
g.agregarArista("e29","o","p")

g.agregarArista("e1","a","b")
g.agregarArista("e2","a","h")
g.agregarArista("e3","b","c")
g.agregarArista("e4","b","d")
g.agregarArista("e5","b","h")
g.agregarArista("e6","b","j")
g.agregarArista("e7","c","d")
g.agregarArista("e8","d","e")
g.agregarArista("e9","d","f")
g.agregarArista("e10","d","k")
g.agregarArista("e11","e","f")
g.agregarArista("e12","f","g")
g.agregarArista("e13","f","h")
g.agregarArista("e14","f","l")
g.agregarArista("e15","g","h")
g.agregarArista("e16","h","i")
g.agregarArista("e17","i","j")
g.agregarArista("e18","i","k")
g.agregarArista("e19","i","l")
g.agregarArista("e20","j","k")
g.agregarArista("e21","j","l")
g.agregarArista("e22","k","l")
"""
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

@app.route('/direccion')
def direccionGrafica():
    g.vaciarGrafica()

    if g.dirigida:
        g.dirigida = False
    else:
        g.dirigida = True

    return redirect(url_for('index'))

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
        peso = request.form.get('peso')
        fMin = request.form.get('flujomin')
        fMax = request.form.get('flujomax')
        dir = request.form.get('dirigida')

        #Cambiar clave
        i = g.numero_aristas
        g.agregarArista("e"+str(i+1), a1, a2, peso, fMin, fMax)
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

@app.route('/vaciarVertice', methods= ['POST'])
def vaciarVertice():
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice_vaciar')
        g.vaciarVertice(vertice)
    return redirect(url_for('index'))

@app.route('/vaciarGrafica')
def vaciarGrafica():
    g.vaciarGrafica()
    return redirect(url_for('index'))

@app.route('/copiarGrafica')
def copiarGrafica():
    c.copiar(g, True)
    return redirect(url_for('index'))

@app.route('/cargarCopia')
def cargarCopia():
    g.copiar(c, True)
    return redirect(url_for('index'))

@app.route('/bipartita')
def esBipartita():
    g.restablecerColores()
    (u, v, t) = g.esBipartita()

    if t:
        for vertice in u:
            vertice.color = 1
        for vertice in v:
            vertice.color = 0
    return redirect(url_for('index'))

@app.route('/fleury')
def fleury():
    g.restablecerColores()

    (ruta, cerrado, paseo) = g.Fleury()
    print(ruta)
    if paseo:
        for i in range(len(ruta) - 1):
            origen = ruta[0]
            destino = ruta[1]
            ruta = ruta[1:]
            arista = g.buscarArista(origen, destino)
            arista.color = 1
    return redirect(url_for('index'))

@app.route('/busquedaAncho')
def busquedaAncho():
    (grafica_ancho, bosque) = g.busquedas(1)

    g.copiar(grafica_ancho)
    return redirect(url_for('index'))

@app.route('/busquedaProfundo')
def busquedaProfundo():
    (grafica_profundo, bosque) = g.busquedas(0)

    g.copiar(grafica_profundo)
    return redirect(url_for('index'))

@app.route('/kruskal')
def kruskal():
    (grafica_kruskal, peso_grafica_kruskal, bosque_kruskal) = g.kruskal()
    print(peso_grafica)
    g.copiar(grafica_kruskal)
    return redirect(url_for('index'))

@app.route('/prim')
def prim():
    (grafica_prim, peso_grafica_prim, bosque_prim) = g.prim()
    g.copiar(grafica_prim)
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