from flask import Flask, render_template, request, redirect, url_for
from config import DevelopmentConfig
from grafica import Grafica

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
g= Grafica(True)
c= Grafica()
mensaje = "Aquí se muestran los mensajes"
g.mensaje.append(mensaje)
#Aqui puedes añardir graficas para probar

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
    g.mensaje = []
    mensaje = "La gráfica se cambio a"

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
            fs = request.form.get('fuentesumid')
            flux = request.form.get('flujo')
            rmin = request.form.get('restmin')
            rmax = request.form.get('restmax')
            if not flux:
                flux = 0
            if(fs == 'None'):
                g.agregarVertice(vertice, flujo= int(flux))
            else:
                g.agregarVertice(vertice, fs, int(flux))
            if rmin:
                g.lista_vertices[vertice].peso_minimo = int(rmin)
            if rmax:
                g.lista_vertices[vertice].peso_max = int(rmax)
        else:
            g.agregarVertice(vertice)

        mensaje = "Se agregó el vértice "+vertice+" correctamente!"
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
            if not peso:
                peso = 0
            if not fMin:
                fMin = 0
            if not cost:
                cost = 0
            if(g.agregarArista("e"+str(i+1), a1, a2, int(peso), int(fMin), int(cost))):
                mensaje += "Se agregó la arista correctamente!"
            else:
                mensaje += "Error al agregar la arista, revise que los vértices existan"
        else:
            if not peso:
                peso = 0
            if(g.agregarArista("e"+str(i+1), a1, a2, int(peso))):
                mensaje += "Se agregó la arista correctamente!"
            else:
                mensaje += "Error al agregar la arista, revise que los vértices existan"
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
            mensaje += "Se encontró el vértice: " + v.id +"!"
            if v.color == '+':
                v.color = 10
            elif v.color == '-':
                v.color = 20
            else:
                v.color = 1
        else:
            mensaje += "No existe el vértice " + vertice
        g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/buscarArista', methods= ['POST'])
def buscarArista():
    g.restablecerColores()
    g.mensaje = []
    mensaje= ""
    if(request.method == 'POST'):
        a1 = request.form.get('id_a1_b')
        a2 = request.form.get('id_a2_b')
        a = g.buscarArista(a1, a2)
        if a:
            a.color= 1
            mensaje = "La arista esta marcada con rojo"
        else:
            if g.dirigida:
                mensaje = "No se encontró la arista " + a1 + " -> " + a2
            else:
                mensaje = "No se encontró la arista " + a1 + " <-> " + a2
    g.mensaje.append(mensaje)
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
    mensaje = "Se copió la grafica correctamente"
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/cargarCopia')
def cargarCopia():
    g.copiar(c)
    g.mensaje = []
    mensaje = "Se cargó la copia de la grafica correctamente!"
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
        mensaje += "La gráfica es bipartita, se muestran de diferentes colores los dos grupos"
    else:
        mensaje += "La gráfica no es bipartita"
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
    g.restablecerColores()
    (grafica_ancho, bosque) = g.busquedas(1)
    g.mensaje = []

    g.copiar(grafica_ancho)
    mensaje = "Se realizó la busqueda a lo ancho correctamente!"
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/busquedaProfundo')
def busquedaProfundo():
    g.restablecerColores()
    (grafica_profundo, bosque) = g.busquedas(0)
    g.mensaje = []
    g.copiar(grafica_profundo)
    mensaje = "Se realizó la busqueda a lo profundo correctamente!"
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/kruskal')
def kruskal():
    g.restablecerColores()
    (grafica_kruskal, peso_grafica_kruskal, bosque_kruskal) = g.kruskal()
    g.mensaje = []
    mensaje = ""
    if bosque_kruskal:
        mensaje = "El peso del bosque es: " + str(peso_grafica_kruskal)
    else:
        mensaje = "El peso del árbol es: " + str(peso_grafica_kruskal)
    g.copiar(grafica_kruskal)
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/prim')
def prim():
    g.restablecerColores()
    (grafica_prim, peso_grafica_prim, bosque_prim) = g.prim()
    g.mensaje = []
    mensaje = ""
    if bosque_prim:
        mensaje = "El peso del bosque es: " + str(peso_grafica_prim)
    else:
        mensaje = "El peso del árbol es: " + str(peso_grafica_prim)
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
            mensaje += "Se encontró un ciclo negativo con ruta: ["
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
            mensaje += "Se realizó el algortimo de Dijkstra correctamente!"
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
            mensaje = "Se encontró un ciclo negativo con ruta: ["
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
    mensaje = "Se realizó Ford Fulkerson correctamente!"
    g.copiar(grafica_fulkerson)
    g.mensaje.append(mensaje)
    for a in g.lista_aristas:
        if g.lista_aristas[a].peso_actual > 0:
            g.lista_aristas[a].color = 1
        print(g.lista_aristas[a])
    mensaje = "El flujo de la gráfica es: " + str(g.peso_grafica)
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
        mensaje = "Se realizó correctamente el cálculo del costo de flujo Primal"
        g.copiar(grafica_primal)
        g.mensaje.append(mensaje)
        for a in g.lista_aristas:
            if g.lista_aristas[a].peso_actual > 0:
                g.lista_aristas[a].color = 1
            print(g.lista_aristas[a])
        mensaje = "El costo de la gráfica es: " + str(g.costo)
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
            mensaje = "No se cumplió el flujo"
            g.mensaje.append(mensaje)
        else:
            mensaje = "Se realizó correctamente el cálculo del costo de flujo Dual"
            g.copiar(grafica_dual)
            g.mensaje.append(mensaje)
            for a in g.lista_aristas:
                if g.lista_aristas[a].peso_actual > 0:
                    g.lista_aristas[a].color = 1
                print(g.lista_aristas[a])
            mensaje = "El costo de la gráfica es: " + str(g.costo)
            g.mensaje.append(mensaje)
    return redirect(url_for('index'))

@app.route('/simplex')
def simplex():
    g.restablecerColores()
    g.mensaje = []

    grafica_simplex = g.simplex()
    mensaje = "Se realizó correctamente el cálculo del costo de flujo Simplex"
    g.copiar(grafica_simplex)
    g.mensaje.append(mensaje)

    for a in g.lista_aristas:
        if g.lista_aristas[a].peso_actual > 0:
            g.lista_aristas[a].color = 1
    mensaje = "El costo de la gráfica es: " + str(g.costo)
    g.mensaje.append(mensaje)
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run()
