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

g.agregarVertice("a", '+')
#g.lista_vertices['a'].flujo = 5
g.agregarVertice("b")
#g.lista_vertices['b'].flujo = 0
g.agregarVertice("c")
#g.lista_vertices['c'].flujo = 3
g.agregarVertice("d")
#g.lista_vertices['d'].flujo = -8
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g", '-')
#g.agregarVertice("h")
#g.agregarVertice("i")
#g.agregarVertice("j")
#g.agregarVertice("k", '-')
#g.agregarVertice("l")
#g.agregarVertice("m", '-')
#g.agregarVertice("n", '-')
#g.agregarVertice("o")
#g.agregarVertice("p")
#g.agregarVertice("q")
#g.agregarVertice("r")
#g.agregarVertice("s")
#g.lista_vertices['h'].peso_minimo = 7
#g.lista_vertices['h'].peso_max = 20
#g.lista_vertices['i'].peso_minimo = 9
#g.lista_vertices['i'].peso_minimo = 21
"""
g.agregarArista("e1","a","b", 6)
g.lista_aristas['e1'].costo = 1
g.agregarArista("e2","a","c", 3)
g.lista_aristas['e2'].costo = 4
g.agregarArista("e3","b","d", 4)
g.lista_aristas['e3'].costo = 2
g.agregarArista("e4","c","b", 8)
g.lista_aristas['e4'].peso_min = 1
g.lista_aristas['e4'].costo = -1
g.agregarArista("e5","c","d", 5)
g.lista_aristas['e5'].peso_min = 1
g.lista_aristas['e5'].costo = 6
"""
g.agregarArista("e1","a","b", 33, 0, 15)
#g.lista_aristas['e1'].peso_actual = 10
g.agregarArista("e2","a","c", 72, 0, 9)
#g.lista_aristas['e2'].peso_actual = 5
g.agregarArista("e3","a","d", 41, 0, 7)
#g.lista_aristas['e3'].peso_actual = 0
g.agregarArista("e4","b","e", 10, 0, 7)
#g.lista_aristas['e4'].peso_actual = 10
g.agregarArista("e5","c","b", 19, 0, 3)
#g.lista_aristas['e5'].peso_actual = 0
g.agregarArista("e6","c","d", 10, 0, 8)
#g.lista_aristas['e6'].peso_actual = 0
g.agregarArista("e7","c","f", 25, 0, 20)
#g.lista_aristas['e7'].peso_actual = 5
g.agregarArista("e8","d","f", 12, 0, 3)
#g.lista_aristas['e8'].peso_actual = 0
g.agregarArista("e9","e","c", 18, 0, 2)
#g.lista_aristas['e9'].peso_actual = 0
g.agregarArista("e10","e","g", 23, 0, 20)
#g.lista_aristas['e10'].peso_actual = 10
g.agregarArista("e11","f","e", 20, 0, 7)
#g.lista_aristas['e11'].peso_actual = 0
g.agregarArista("e14","f","g", 40, 0, 13)
#g.lista_aristas['e12'].peso_actual = 5
#g.peso_grafica = 15
#############################################
"""
g.agregarArista("e1","a","b", 75)
g.lista_aristas['e1'].peso_min = 2
g.agregarArista("e2","a","d", 30)
g.agregarArista("e3","a","e", 33)
g.lista_aristas['e3'].peso_min = 1
g.agregarArista("e4","b","c", 46)
g.agregarArista("e5","b","e", 42)
g.agregarArista("e6","c","e", 29)
g.agregarArista("e7","c","f", 21)
g.lista_aristas['e7'].peso_min = 3
g.agregarArista("e8","d","e", 25)
g.agregarArista("e9","d","h", 9)
g.agregarArista("e10","d","j", 15)
g.agregarArista("e11","e","h", 12)
g.agregarArista("e12","f","e", 18)
g.agregarArista("e13","f","g", 8)
g.agregarArista("e14","f","i", 12)
g.agregarArista("e15","g","c", 40)
g.lista_aristas['e15'].peso_min = 1
g.agregarArista("e16","g","i", 40)
g.agregarArista("e17","h","f", 17)
g.agregarArista("e18","h","i", 10)
g.agregarArista("e19","h","k", 14)
g.lista_aristas['e19'].peso_min = 2
g.agregarArista("e20","i","k", 19)
g.agregarArista("e21","i","l", 25)
g.agregarArista("e22","j","h", 6)
g.agregarArista("e23","j","m", 45)
g.agregarArista("e24","k","j", 19)
g.lista_aristas['e24'].peso_min = 1
g.agregarArista("e25","k","l", 18)
g.agregarArista("e26","k","n", 50)
g.lista_aristas['e26'].peso_min = 3
g.agregarArista("e27","l","g", 70)
g.lista_aristas['e27'].peso_min = 3
g.agregarArista("e28","l","n", 62)
g.agregarArista("e29","m","k", 29)
g.agregarArista("e30","n","m", 54)

####################################################
g.agregarArista("e1","a","b", -8)
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
    g.mensaje = []
    mensaje = "La grafica se camio a"

    if g.dirigida:
        g.dirigida = False
        mensaje += " no dirigida"
    else:
        g.dirigida = True
        mensaje += " dirigida"
    g.mensaje.append(mensaje)

    return redirect(url_for('index'))

@app.route('/vertices', methods= ['POST'])
def agregarVertice():
    g.mensaje = []
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice')
        if(g.dirigida == True):
            dir = request.form.get('fuentesumid')
            flux = request.form.get('flujo')
            if(dir == 'None'):
                if(flux):
                    g.agregarVertice(vertice, flujo=int(flux))
                else:
                    g.agregarVertice(vertice)
            else:
                if(flux):
                    g.agregarVertice(vertice, dir, int(flux))
                else:
                    g.agregarVertice(vertice, dir)
        else:
            g.agregarVertice(vertice)


        mensaje = "Se agrego el vertice exitosamente!"
        g.mensaje.append(mensaje)
        print(vertice)
    return redirect(url_for('index'))

@app.route('/aristas', methods= ['POST'])
def agregarArista():
    g.mensaje = []
    if(request.method == 'POST'):
        a1 = request.form.get('id_a1')
        a2 = request.form.get('id_a2')
        peso = request.form.get('peso')
        fMin = request.form.get('flujomin')
        cost = request.form.get('costo')

        #Cambiar clave
        i = g.numero_aristas
        mensaje = ""
        
        if (g.dirigida == True):
            if(g.agregarArista("e"+str(i+1), a1, a2, int(peso), int(fMin), int(cost))):
                mensaje += "Se agrego la arista exitosamente!"
            else:
                mensaje += "Error al agregar arista"
        else:
            if(g.agregarArista("e"+str(i+1), a1, a2)):
                mensaje += "Se agrego la arista exitosamente!"
            else:
                mensaje += "Error al agregar arista"
        g.mensaje.append(mensaje)

    return redirect(url_for('index'))

@app.route('/buscarVertice', methods= ['POST'])
def buscarVertice():
    g.restablecerColores()
    g.mensaje = []
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice_buscar')
        v = g.buscarVertice(vertice)
        mensaje = ""
        if v:
            mensaje += "Se encontro el vertice exitosamente!"
            v.color= 1
        else:
            mensaje += "No se encontro el vertice"
        g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/buscarArista', methods= ['POST'])
def buscarArista():
    g.restablecerColores()
    g.mensaje = []
    if(request.method == 'POST'):
        a1 = request.form.get('id_a1_b')
        a2 = request.form.get('id_a2_b')
        a = g.buscarArista(a1, a2)
        a.color= 1
    return redirect(url_for('index'))

@app.route('/eliminarVertice', methods= ['POST'])
def eliminarVertice():
    g.mensaje = []
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice')
        g.eliminarVertice(vertice)
        print("Borrado:", vertice)
    return redirect(url_for('index'))

@app.route('/eliminarArista', methods= ['POST'])
def eliminarArista():
    g.mensaje = []
    if(request.method == 'POST'):
        a1 = request.form.get('id_a1')
        a2 = request.form.get('id_a2')
        #Cambiar clave
        g.eliminarArista(a1, a2)
    return redirect(url_for('index'))

@app.route('/vaciarVertice', methods= ['POST'])
def vaciarVertice():
    g.mensaje = []
    if(request.method == 'POST'):
        vertice = request.form.get('id_vertice_vaciar')
        g.vaciarVertice(vertice)
    return redirect(url_for('index'))

@app.route('/vaciarGrafica')
def vaciarGrafica():
    g.mensaje = []
    g.vaciarGrafica()
    return redirect(url_for('index'))

@app.route('/copiarGrafica')
def copiarGrafica():
    c.copiar(g)
    g.mensaje = []
    mensaje = "Se copio la grafica exitosamente"
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/cargarCopia')
def cargarCopia():
    g.copiar(c, True)
    g.mensaje = []
    mensaje = "Se cargo la copia de la grafica exitosamente!"
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/bipartita')
def esBipartita():
    g.restablecerColores()
    (u, v, t) = g.esBipartita()
    g.mensaje = []
    mensaje = ""

    if t:
        for vertice in u:
            vertice.color = 1
        for vertice in v:
            vertice.color = 0
        mensaje += "La grafica es bipartita"
    else:
        mensaje += "La grafica no es bipartita"
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/fleury')
def fleury():
    g.restablecerColores()
    g.mensaje = []
    mensaje = ""

    (ruta, cerrado, paseo) = g.Fleury()
    print(ruta)

    if paseo == True:
        mensaje += "El paseo de Euler es "
        if cerrado == 0:
            mensaje += "cerrado"
        else:
            mensaje += "abierto"
        mensaje += " y la ruta es: ["
        for i in range(len(ruta) - 1):
            origen = ruta[0]
            destino = ruta[1]
            ruta = ruta[1:]
            arista = g.buscarArista(origen, destino)
            arista.color = 1
            mensaje += str(origen) + ", "
        mensaje += str(destino) + "]"
    else:
        mensaje = paseo
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/busquedaAncho')
def busquedaAncho():
    (grafica_ancho, bosque) = g.busquedas(1)
    g.mensaje = []

    g.copiar(grafica_ancho)
    mensaje = "Se realizo la busqueda a lo ancho exitosamente!"
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/busquedaProfundo')
def busquedaProfundo():
    (grafica_profundo, bosque) = g.busquedas(0)
    g.mensaje = []
    g.copiar(grafica_profundo)
    mensaje = "Se realizo la busqueda a lo profundo exitosamente!"
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/kruskal')
def kruskal():
    (grafica_kruskal, peso_grafica_kruskal, bosque_kruskal) = g.kruskal()
    g.mensaje = []
    mensaje = ""
    print(peso_grafica)
    if bosque_kruskal:
        mensaje = "El peso del bosque es: " + str(peso_grafica_kruskal)
    else:
        mensaje = "El peso de la grafica es: " + str(peso_grafica_kruskal)
    g.copiar(grafica_kruskal)
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/prim')
def prim():
    (grafica_prim, peso_grafica_prim, bosque_prim) = g.prim()
    g.mensaje = []
    mensaje = ""
    if bosque_prim:
        mensaje = "El peso del bosque es: " + str(peso_grafica_prim)
    else:
        mensaje = "El peso de la grafica es: " + str(peso_grafica_prim)
    g.copiar(grafica_prim)
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/dijkstra', methods= ['POST'])
def dijkstra():
    g.restablecerColores()
    if request.method == 'POST':
        vertice = request.form.get('id_vertice_dijkstra')
        (grafica_dijkstra, ciclo_negativo_dijkstra, peso_ciclo_dijkstra) = g.dijkstraGeneral(vertice)
        g.mensaje = []
        mensaje = ""
        if peso_ciclo_dijkstra < 0:
            print(ciclo_negativo_dijkstra)
            mensaje += "Se encontro un ciclo negativo con ruta: ["
            for i in range(len(ciclo_negativo_dijkstra) - 1):
                    origen = ciclo_negativo_dijkstra[0]
                    destino = ciclo_negativo_dijkstra[1]
                    ciclo_negativo_dijkstra = ciclo_negativo_dijkstra[1:]
                    arista = g.buscarArista(origen, destino)
                    arista.color = 1
                    mensaje += str(origen) + ", "
            mensaje += str(destino) + "]"
        else:
            g.copiar(grafica_dijkstra)
            mensaje += "Se realizo el algortimo de Dijkstra exitosamente!"
        g.mensaje.append(mensaje)
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
    g.restablecerColores()
    grafica_fulkerson = g.AlgoritmoFordFulkerson()
    g.mensaje = []
    mensaje = "Se realizo Ford Fulkerson exitosamente"
    g.copiar(grafica_fulkerson)
    g.mensaje.append(mensaje)
    for a in g.lista_aristas:
        if g.lista_aristas[a].peso_actual > 0:
            g.lista_aristas[a].color = 1
        print(g.lista_aristas[a])
    mensaje = "El flujo de la grafica es: " + str(g.peso_grafica)
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/flujoCosteMinimoPrimal', methods= ['POST'])
def flujoCosteMinimoPrimal():
    g.restablecerColores()
    if(request.method == 'POST'):
        flujo = request.form.get('flujo_primal')
        flujo = int(flujo)
        grafica_primal = g.flujoCosteMinimoPrimal(flujo)
        g.mensaje = []
        mensaje = "Se realizo correctamente el calculo de la cantidad de flujo primal"
        g.copiar(grafica_primal)
        g.mensaje.append(mensaje)
        for a in g.lista_aristas:
            if g.lista_aristas[a].peso_actual > 0:
                g.lista_aristas[a].color = 1
            print(g.lista_aristas[a])
        mensaje = "El costo de la grafica es: " + str(g.costo)
        g.mensaje.append(mensaje)

    return redirect(url_for('index'))

@app.route('/flujoConsumoMinimoDual', methods= ['POST'])
def flujoConsumoMinimoDual():
    g.restablecerColores()
    g.mensaje = []
    if(request.method == 'POST'):
        flujo = request.form.get('flujo_dual')
        flujo = int(flujo)
        grafica_dual = g.flujoConsumoMinimoDual(flujo)
        if grafica_dual == False:
            mensaje = "No se cumplio el flujo"
            g.mensaje.append(mensaje)
        else:
            mensaje = "Se realizo correctamente el calculo de la cantidad de flujo dual"
            g.copiar(grafica_dual)
            g.mensaje.append(mensaje)
            for a in g.lista_aristas:
                if g.lista_aristas[a].peso_actual > 0:
                    g.lista_aristas[a].color = 1
                print(g.lista_aristas[a])
            mensaje = "El costo de la grafica es: " + str(g.costo)
            g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/simplex')
def simplex():
    g.restablecerColores()
    g.mensaje = []

    grafica_simplex = g.simplex()
    mensaje = "Se realizo correctamente el calculo de la cantidad de flujo simplex"
    g.copiar(grafica_simplex)
    g.mensaje.append(mensaje)

    for a in g.lista_aristas:
        if g.lista_aristas[a].peso_actual > 0:
            g.lista_aristas[a].color = 1
    mensaje = "El costo de la grafica es: " + str(g.costo)
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run()
