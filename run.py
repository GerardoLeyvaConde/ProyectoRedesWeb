from flask import Flask, render_template, request, redirect, url_for
from config import DevelopmentConfig
from grafica import Grafica

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
g= Grafica(True)
c= Grafica()
mensaje = "Aqui se muestran los mensajes"
g.mensaje.append(mensaje)
#dirigida= Grafica(True)

g.agregarVertice("a")
g.agregarVertice("b")
g.agregarVertice("c")
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g")
#g.agregarVertice("h")
#g.agregarVertice("i")
#g.agregarVertice("j")
#g.agregarVertice("k")
#g.agregarVertice("l")
#g.agregarVertice("m")
#g.agregarVertice("n")
#g.agregarVertice("o")
#g.agregarVertice("p")
#g.agregarVertice("q")
#g.agregarVertice("r")
#g.agregarVertice("s")
g.agregarArista("e1","a","b", 3)
g.agregarArista("e2","a","c", 1)
g.agregarArista("e3","a","d", 2)
g.agregarArista("e4","b","e", 4)
g.agregarArista("e5","c","a", -1)
g.agregarArista("e6","c","d", 3)
g.agregarArista("e7","c","e", -1)
g.agregarArista("e8","c","f", 5)
g.agregarArista("e9","d","a", -2)
g.agregarArista("e10","e","c", 1)
g.agregarArista("e11","e","g", 3)
g.agregarArista("e12","f","d", -3)
g.agregarArista("e13","f","e", -1)
g.agregarArista("e14","f","g", 2)
g.agregarArista("e15","g","e", -3)
g.agregarArista("e16","g","f", -2)

"""
g.agregarArista("e1","a","b", -8)##################33333
g.agregarArista("e2","a","e", 10)
g.agregarArista("e3","b","c", 14)
#g.agregarArista("e4","a","f", 1)
g.agregarArista("e5","b","f", 2)
g.agregarArista("e6","c","a", 2)
g.agregarArista("e7","c","d", 3)
g.agregarArista("e8","c","g", -10)
g.agregarArista("e9","d","b", 9)
g.agregarArista("e10","d","g", 8)
g.agregarArista("e11","d","h", -5)
g.agregarArista("e12","e","a", 1)
g.agregarArista("e13","e","f", 4)
g.agregarArista("e14","e","i", 4)
g.agregarArista("e15","e","j", -1)
g.agregarArista("e16","f","a", 2)
g.agregarArista("e17","f","g", 3)
g.agregarArista("e18","g","b", 5)
g.agregarArista("e19","g","h", 1)
g.agregarArista("e20","g","k", 8)
g.agregarArista("e21","h","c", 12)
g.agregarArista("e22","h","l", 2)
g.agregarArista("e23","i","f", 3)
g.agregarArista("e24","i","m", 3)
g.agregarArista("e25","i","q", 7)
g.agregarArista("e26","j","i", -2)
g.agregarArista("e27","j","m", 5)
g.agregarArista("e28","j","n", 7)
g.agregarArista("e29","k","f", -1)
g.agregarArista("e30","k","j", 3)
g.agregarArista("e31","k","o", -4)
g.agregarArista("e32","l","d", 3)
g.agregarArista("e33","l","g", -2)
g.agregarArista("e34","l","k", 5)
g.agregarArista("e35","m","n", 9)
g.agregarArista("e36","m","p", 3)
g.agregarArista("e37","n","k", -4)
g.agregarArista("e38","n","o", 3)
g.agregarArista("e39","n","p", -2)
g.agregarArista("e40","o","l", 2)
g.agregarArista("e41","o","s", -7)
g.agregarArista("e42","p","o", 5)
g.agregarArista("e43","p","r", 4)
g.agregarArista("e44","p","s", 6)
g.agregarArista("e45","q","p", -1)
g.agregarArista("e46","q","s", -2)
g.agregarArista("e47","r","q", 2)
g.agregarArista("e48","s","r", 3)
####################################################333
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

    mensaje = request.args.get('mensaje' , 'Aqui se muestran los mensajes"')

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
        g.mensaje = "Se agrego el vertice exitosamente!"
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
        if(g.agregarArista("e"+str(i+1), a1, a2, peso, fMin, fMax)):
            g.mensaje = "Se agrego la arista exitosamente!"
        else:
            g.mensaje = "Error al agregar arista"

    return redirect(url_for('index'))

@app.route('/buscarVertice', methods= ['POST'])
def buscarVertice():
    g.restablecerColores()
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice_buscar')
        v = g.buscarVertice(vertice)
        if v:
            g.mensaje = "Se encontro el vertice exitosamente!"
            v.color= 1
        else:
            g.mensaje = "No se encontro el vertice"
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
    c.copiar(g)
    g.mensaje = "Se copio la grafica exitosamente"
    return redirect(url_for('index'))

@app.route('/cargarCopia')
def cargarCopia():
    g.copiar(c, True)
    g.mensaje = "Se cargo la copia de la grafica exitosamente!"
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
        g.mensaje = "La grafica es bipartita"
    else:
        g.mensaje = "La grafica no es bipartita"
    return redirect(url_for('index'))

@app.route('/fleury')
def fleury():
    g.restablecerColores()

    (ruta, cerrado, paseo) = g.Fleury()
    print(ruta)

    if paseo == True:
        g.mensaje = "El paseo de Euler es "
        if cerrado == 0:
            g.mensaje += "cerrado"
        else:
            g.mensaje += "abierto"
        g.mensaje += " y la ruta es: ["
        for i in range(len(ruta) - 1):
            origen = ruta[0]
            destino = ruta[1]
            ruta = ruta[1:]
            arista = g.buscarArista(origen, destino)
            arista.color = 1
            g.mensaje += str(origen) + ", "
        g.mensaje += str(destino) + "]"
    else:
        g.mensaje = paseo
    return redirect(url_for('index'))

@app.route('/busquedaAncho')
def busquedaAncho():
    (grafica_ancho, bosque) = g.busquedas(1)

    g.copiar(grafica_ancho)
    g.mensaje = "Se realizo la busqueda a lo ancho exitosamente!"
    return redirect(url_for('index'))

@app.route('/busquedaProfundo')
def busquedaProfundo():
    (grafica_profundo, bosque) = g.busquedas(0)

    g.copiar(grafica_profundo)
    g.mensaje = "Se realizo la busqueda a lo profundo exitosamente!"
    return redirect(url_for('index'))

@app.route('/kruskal')
def kruskal():
    (grafica_kruskal, peso_grafica_kruskal, bosque_kruskal) = g.kruskal()
    print(peso_grafica)
    if bosque_kruskal:
        g.mensaje = "El peso del bosque es: " + str(peso_grafica_kruskal)
    else:
        g.mensaje = "El peso de la grafica es: " + str(peso_grafica_kruskal)
    g.copiar(grafica_kruskal)
    return redirect(url_for('index'))

@app.route('/prim')
def prim():
    (grafica_prim, peso_grafica_prim, bosque_prim) = g.prim()
    if bosque_prim:
        g.mensaje = "El peso del bosque es: " + str(peso_grafica_prim)
    else:
        g.mensaje = "El peso de la grafica es: " + str(peso_grafica_prim)
    g.copiar(grafica_prim)
    return redirect(url_for('index'))

@app.route('/dijkstra')
def dijkstra():
    g.restablecerColores()
    (grafica_dijkstra, ciclo_negativo_dijkstra, peso_ciclo_dijkstra) = g.dijkstraGeneral("a")

    if peso_ciclo_dijkstra < 0:
        print(ciclo_negativo_dijkstra)
        g.mensaje = "Se encontro un ciclo negativo con ruta: ["
        for i in range(len(ciclo_negativo_dijkstra) - 1):
                origen = ciclo_negativo_dijkstra[0]
                destino = ciclo_negativo_dijkstra[1]
                ciclo_negativo_dijkstra = ciclo_negativo_dijkstra[1:]
                arista = g.buscarArista(origen, destino)
                arista.color = 1
                g.mensaje += str(origen) + ", "
        g.mensaje += str(destino) + "]"
    else:
        g.copiar(grafica_dijkstra)
        g.mensaje = "Se realizo el algortimo de Dijkstra exitosamente!"
    return redirect(url_for('index'))

@app.route('/floyd', methods= ['POST'])
def floyd():
    g.restablecerColores()
    g.mensaje = []
    mensaje = ""
    if request.method == 'POST':
        (grafica_floyd, nombres, booleano) = g.floyd()

        if booleano == True:
            print(grafica_floyd)
            mensaje = "Se encontro un ciclo negativo con ruta: ["
            for i in range(len(grafica_floyd) - 1):
                origen = grafica_floyd[0]
                destino = grafica_floyd[1]
                grafica_floyd = grafica_floyd[1:]
                arista = g.buscarArista(origen, destino)
                arista.color = 1
                g.mensaje += str(origen) + ", "
            mensaje += str(destino) + "]"
            g.mensaje.append(mensaje)
        else:
            vertice = request.form.get('id_vertice_floyd')
            index_vertice = nombres.index(vertice)
            for i in range(len(nombres)):
                if i == index_vertice:
                    continue
                mensaje = "Ruta de " + vertice + " -> " + nombres[i] + " es ["
                ruta = grafica_floyd[i + index_vertice * len(nombres)][0]
                for j in range(len(ruta) - 1):
                    origen2 = ruta[0]
                    destino2 = ruta[1]
                    ruta = ruta[1:]
                    arista = g.buscarArista(origen2, destino2)
                    arista.color = 1
                    mensaje += str(origen2) + ", "
                mensaje += str(destino2) + "] con peso: " + str(grafica_floyd[i + index_vertice * len(nombres)][1])
                g.mensaje.append(mensaje)
        return redirect(url_for('index'))

@app.route('/obtenerGrado', methods= ['POST'])
def obtenerGrado():
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice_grado')
        v = g.gradoVertice(vertice)
        print(v)
    return redirect(url_for('index'))

@app.route('/fordFulkerson')
def fordFulkerson():
    return redirect(url_for('index'))

@app.route('/flujoCosteMinimoPrimal')
def flujoCosteMinimoPrimal():
    return redirect(url_for('index'))

@app.route('/flujoConsumoMinimoDual')
def flujoConsumoMinimoDual():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
