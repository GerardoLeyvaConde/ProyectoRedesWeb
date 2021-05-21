from flask import Flask, render_template, request, redirect, url_for
from config import DevelopmentConfig
from grafica import Grafica

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
g= Grafica(True)
c= Grafica()
mensaje = "Aquí se muestran los mensajes de control"
g.mensaje.append(mensaje)
#Aqui puedes añardir graficas para probar
##########################################################
#g.dirigida = False
"""
#Bipartita
g.agregarVertice("a")
g.agregarVertice("b")
g.agregarVertice("c")
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g")

g.agregarArista("e1","a","c")
g.agregarArista("e2","a","d")
g.agregarArista("e3","a","g")
g.agregarArista("e4","b","f")
g.agregarArista("e5","c","e")
g.agregarArista("e6","d","e")
g.agregarArista("e7","f","g")
#g.agregarArista("e8","c","d")
"""
################################################
g.dirigida = False

#Euler

g.agregarVertice("a")
g.agregarVertice("b")
g.agregarVertice("c")
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g")
g.agregarVertice("h")

g.agregarVertice("i")


g.agregarArista("e1","a","b")
g.agregarArista("e2","a","c")
g.agregarArista("e3","a","d")
g.agregarArista("e4","b","c")
g.agregarArista("e5","b","e")
g.agregarArista("e6","b","g")
g.agregarArista("e7","c","d")
g.agregarArista("e8","c","f")
g.agregarArista("e9","c","f")
g.agregarArista("e10","d","e")
g.agregarArista("e11","d","g")
g.agregarArista("e12","e","f")
g.agregarArista("e13","e","h")
g.agregarArista("e14","f","g")
g.agregarArista("e15","g","h")
#g.agregarArista("e16","c","a")

g.agregarArista("e16","h","i")

################################################
#g.dirigida = False
"""
#Expansion 1
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
g.agregarVertice("l")
 
g.agregarArista("e1", "a", "b")
g.agregarArista("e2", "a", "h")
g.agregarArista("e3", "b", "c")
g.agregarArista("e4", "b", "d")
g.agregarArista("e5", "b", "h")
g.agregarArista("e6", "b", "j")
g.agregarArista("e7", "c", "d")
g.agregarArista("e8", "d", "e")
g.agregarArista("e9", "d", "f")
g.agregarArista("e10", "d", "k")
g.agregarArista("e11", "e", "f")
g.agregarArista("e12", "f", "g")
g.agregarArista("e13", "f", "l")
g.agregarArista("e14", "g", "h")
g.agregarArista("e15", "h", "i")
g.agregarArista("e16", "i", "j")
g.agregarArista("e17", "i", "k")
g.agregarArista("e18", "i", "l")
g.agregarArista("e19", "j", "k")
g.agregarArista("e20", "j", "l")
g.agregarArista("e21", "k", "l")
"""
################################################
#g.dirigida = False
"""
#Expansio 2
g.agregarVertice("a")
g.agregarVertice("b")
g.agregarVertice("c")
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g")
g.agregarVertice("h")
g.agregarVertice("i")
 
g.agregarArista("e1", "a", "b")
g.agregarArista("e2", "a", "c")
g.agregarArista("e3", "a", "d")
g.agregarArista("e4", "b", "c")
g.agregarArista("e5", "b", "d")
g.agregarArista("e6", "e", "f")
g.agregarArista("e7", "e", "h")
g.agregarArista("e8", "f", "g")
g.agregarArista("e9", "f", "h")
g.agregarArista("e10", "f", "i")
g.agregarArista("e11", "g", "h")
g.agregarArista("e12", "g", "i")
"""
#g.dirigida = False
"""
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

g.agregarArista("e1", "a", "b", 3)
g.agregarArista("e2", "a", "c", 1)
g.agregarArista("e3", "a", "d", 2)
g.agregarArista("e4", "a", "f", 1)
g.agregarArista("e5", "b", "c", 2)
g.agregarArista("e6", "b", "d", 3)
g.agregarArista("e7", "b", "e", 10)
g.agregarArista("e8", "c", "e", 1)
g.agregarArista("e9", "c", "h", 1)
g.agregarArista("e10", "d", "e", 2)
g.agregarArista("e11", "d", "f", 4)
g.agregarArista("e12", "e", "f", 2)
g.agregarArista("e13", "e", "g", 1)
g.agregarArista("e14", "e", "h", 2)
g.agregarArista("e15", "f", "g", 2)
g.agregarArista("e16", "f", "i", 3)
g.agregarArista("e17", "g", "h", 1)
g.agregarArista("e18", "g", "i", 2)
g.agregarArista("e19", "g", "j", 3)
g.agregarArista("e20", "h", "j", 5)
g.agregarArista("e21", "i", "j", 2)
g.agregarArista("e22", "i", "k", 7)
g.agregarArista("e23", "j", "k", 1)
"""
#g.dirigida = False
"""
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
g.agregarVertice("l")
g.agregarVertice("m")

g.agregarArista("e1", "a", "b", 1)
g.agregarArista("e2", "a", "d", 3)
g.agregarArista("e3", "a", "e", 2)
g.agregarArista("e4", "b", "c", 5)
g.agregarArista("e5", "b", "e", 3)
g.agregarArista("e6", "b", "f", 4)
g.agregarArista("e7", "c", "d", 2)
g.agregarArista("e8", "c", "f", 2)
g.agregarArista("e9", "c", "g", 1)
g.agregarArista("e10", "d", "g", 1)
g.agregarArista("e11", "e", "f", 5)
g.agregarArista("e12", "e", "g", 1)
g.agregarArista("e13", "f", "g", 2)
g.agregarArista("e14", "h", "i", 2)
g.agregarArista("e15", "h", "l", 1)
g.agregarArista("e16", "i", "j", 3)
g.agregarArista("e17", "i", "l", 2)
g.agregarArista("e18", "j", "k", 5)
g.agregarArista("e19", "j", "l", 4)
g.agregarArista("e20", "j", "m", 1)
g.agregarArista("e21", "k", "m", 2)
g.agregarArista("e22", "l", "m", 2)
"""
################################################
################################################
################################################
#g.dirigida = True
"""
#Dikjstra
g.agregarVertice("a")
g.agregarVertice("b")
g.agregarVertice("c")
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
 
g.agregarArista("e1","a","b", 7)
g.agregarArista("e2","a","c", 9)
g.agregarArista("e3","a","d", 14)
g.agregarArista("e4","b","e", 15)
g.agregarArista("e5","c","e", 11)
g.agregarArista("e6","c","d", 2)
g.agregarArista("e7","d","f", 9)
g.agregarArista("e8","e","f", 6)
"""
#g.dirigida = True
"""
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

g.agregarVertice("l")

g.agregarVertice("m")

g.agregarVertice("n")

g.agregarVertice("o")

g.agregarVertice("p")

g.agregarVertice("q")

g.agregarVertice("r")

g.agregarVertice("s")

g.agregarArista("e1", "a", "b", 8)

g.agregarArista("e2", "a", "e", 10)

g.agregarArista("e3", "b", "c", 14)

g.agregarArista("e4", "b", "f", 2)

g.agregarArista("e5", "c", "a", 2)

g.agregarArista("e6", "c", "d", 3)

g.agregarArista("e7", "c", "g", -10)

g.agregarArista("e8", "d", "b", 9)

g.agregarArista("e9", "d", "g", 8)

g.agregarArista("e10", "d", "h", -5)

g.agregarArista("e11", "e", "a", 1)

g.agregarArista("e12", "e", "f", 4)

g.agregarArista("e13", "e", "i", 4)

g.agregarArista("e14", "e", "j", -1)

g.agregarArista("e15", "f", "a", 2)

g.agregarArista("e16", "f", "g", 3)

g.agregarArista("e17", "g", "b", 5)

g.agregarArista("e18", "g", "h", 1)

g.agregarArista("e19", "g", "k", 8)

g.agregarArista("e20", "h", "c", 12)

g.agregarArista("e21", "h", "l", 2)

g.agregarArista("e22", "i", "f", 3)

g.agregarArista("e23", "i", "m", 3)

g.agregarArista("e24", "i", "q", 7)

g.agregarArista("e25", "j", "i", -2)

g.agregarArista("e26", "j", "m", 5)

g.agregarArista("e27", "j", "n", 7)

g.agregarArista("e28", "k", "f", -1)

g.agregarArista("e29", "k", "j", 3)

g.agregarArista("e30", "k", "o", -4)

g.agregarArista("e31", "l", "d", 3)

g.agregarArista("e32", "l", "k", 5)

g.agregarArista("e33", "m", "p", 3)

g.agregarArista("e34", "m", "n", 9)

g.agregarArista("e35", "n", "k", -4)

g.agregarArista("e36", "n", "o", 3)

g.agregarArista("e37", "n", "p", -2)

g.agregarArista("e38", "o", "l", 2)

g.agregarArista("e39", "o", "s", -7)

g.agregarArista("e40", "p", "o", 5)

g.agregarArista("e41", "p", "r", 4)

g.agregarArista("e42", "p", "s", 6)

g.agregarArista("e43", "q", "m", 4)

g.agregarArista("e44", "q", "p", -1)

g.agregarArista("e45", "q", "s", -2)

g.agregarArista("e46", "r", "q", 2)

g.agregarArista("e47", "s", "r", 3)
"""

################################################
#g.dirigida = True
"""
#kruskal
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

 
g.agregarArista("e1","a","b", 7)
g.agregarArista("e2","a","c", 9)
g.agregarArista("e3","a","d", 14)
g.agregarArista("e4","b","e", 15)
g.agregarArista("e5","c","e", 11)
g.agregarArista("e6","c","d", 2)
g.agregarArista("e7","d","f", 9)
g.agregarArista("e8","e","f", 6)
"""
################################################
#g.dirigida = True
"""
#Floyd
g.agregarVertice("a")
g.agregarVertice("b")
g.agregarVertice("c")
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g")
 
g.agregarArista("e1", "a", "b", 3)
g.agregarArista("e2", "a", "c", 1)
g.agregarArista("e3", "a", "d", 2)
g.agregarArista("e4", "b", "e", 3)
g.agregarArista("e5", "c", "a", 1)
g.agregarArista("e6", "c", "b", 2)
g.agregarArista("e7", "c", "d", 3)
g.agregarArista("e8", "c", "e", 1)
g.agregarArista("e9", "c", "f", 5)
g.agregarArista("e10", "d", "a", 2)
g.agregarArista("e11", "e", "c", 1)
g.agregarArista("e12", "e", "g", 3)
g.agregarArista("e13", "f", "e", 1)
g.agregarArista("e14", "f", "d", 3)
g.agregarArista("e15", "f", "g", 2)
g.agregarArista("e16", "g", "e", 3)
g.agregarArista("e17", "g", "f", 2)
"""


##########################################################
#g.dirigida = True
"""
#FordFulkerson
g.agregarVertice("a", '+')
g.agregarVertice("b", '+')
g.agregarVertice("c", '+')
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g")
g.agregarVertice("h")
g.agregarVertice("i")
g.agregarVertice("j")
g.agregarVertice("k", '-')
g.agregarVertice("l")
g.agregarVertice("m", '-')
g.agregarVertice("n", '-')

g.booleanosalvaje = True
g.lista_vertices['h'].peso_max = 20
g.lista_vertices['i'].peso_minimo = 9


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
"""
################################################
#g.dirigida = True
"""
#Primal con flujo 30

g.agregarVertice("a", '+')
g.agregarVertice("b")
g.agregarVertice("c")
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g")
g.agregarVertice("h")
g.agregarVertice("i")
g.agregarVertice("j", '-')
g.agregarVertice("k")

g.booleanosalvaje = True
g.lista_vertices['f'].peso_minimo = 3
g.lista_vertices['f'].peso_max = 25

g.agregarArista("e1","a","b", 15, 3, 2)
g.agregarArista("e2","a","c", 26, 6, 10)
g.agregarArista("e3","b","e", 17, 0, 7)
g.agregarArista("e4","c","b", 14, 0, -3)
g.agregarArista("e5","c","d", 18, 0 , 1)
g.agregarArista("e6","c","e", 10, 0 , 5)
g.agregarArista("e7","d","a", 13, 0, 3)
g.agregarArista("e8","d", "f", 4, 1 ,3)
g.agregarArista("e9","e","f", 13,0,2)
g.agregarArista("e10","e","g", 20,0,-5)
g.agregarArista("e11","e","h", 38,1,4)
g.agregarArista("e12","f","i", 13,0,-6)
g.agregarArista("e13","g","j", 19,0,6)
g.agregarArista("e14","h","f", 10, 0 , -1)
g.agregarArista("e15","h","g", 14,0,5)
g.agregarArista("e16","h","i", 10,0,2)
g.agregarArista("e17","h","j", 31,0,-2)
g.agregarArista("e18","i","k", 25,0,3)
g.agregarArista("e19","k","j", 70,0,6)
"""
################################################
#g.dirigida = True
"""
#Dual con flujo 22

g.agregarVertice("a", '+')
g.agregarVertice("b")
g.agregarVertice("c")
g.agregarVertice("d")
g.agregarVertice("e")
g.agregarVertice("f")
g.agregarVertice("g", '-')

g.agregarArista("e1","a","b", 12, 0, 7)
g.agregarArista("e2","a","c", 26, 0, 1)
g.agregarArista("e3","a","d", 13, 0, 10)
g.agregarArista("e4","b","e", 26, 0, 3)
g.agregarArista("e5","c","b", 4, 0 ,5)
g.agregarArista("e6","c","d", 40, 0, 2)
g.agregarArista("e7","c", "e", 13, 0 ,7)
g.agregarArista("e8","c","f", 19,0,6)
g.agregarArista("e9","d","b", 10,0,2)
g.agregarArista("e10","d","f", 26,0,3)
g.agregarArista("e11","e","f", 30,0,10)
g.agregarArista("e12","e","g", 50,0,3)
g.agregarArista("e13","f","g", 41,0,2)
"""
################################################
#g.dirigida = True
"""
#Simplex
g.agregarVertice("1")
g.lista_vertices["1"].flujo = 1
g.agregarVertice("2")
g.lista_vertices["2"].flujo = 0
g.agregarVertice("3")
g.lista_vertices["3"].flujo = 2
g.agregarVertice("4")
g.lista_vertices["4"].flujo = -3
 
g.agregarArista("e1", "1", "2", 5, 2, 1)
g.agregarArista("e2", "1", "4", 3, 1, -2)
g.agregarArista("e3", "2", "4", 2, 0, -1)
g.agregarArista("e4", "3", "1", 5, 0, 5)
g.agregarArista("e5", "3", "2", 2, 0, 1)
g.agregarArista("e6", "4", "3", 5, 0, 3)
"""
##################################################
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
                g.booleanosalvaje = True
                g.lista_vertices[vertice].peso_minimo = int(rmin)
            if rmax:
                g.booleanosalvaje = True
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
    g.restablecerColores()
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

    ruta2 = list()
    aristas_ruta = list()
    ruta2 = ruta.copy()

    for i in range(len(ruta2) - 1):
        origen2 = ruta2[0]
        destino2 = ruta2[1]
        ruta2 = ruta2[1:]
        for ar in g.lista_aristas:
            if (g.lista_vertices[origen2].existeConexion(destino2, False)):
                if ar in aristas_ruta:
                    continue
                else:
                    aristas_ruta.append(ar)
                    g.lista_aristas[ar].color = 1
                    break   


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
            g.mensaje.append(mensaje)
            mensaje = "El peso es: " + str(peso_ciclo_dijkstra)
            g.mensaje.append(mensaje)
        else:
            g.copiar(grafica_dijkstra)
            mensaje += "Se realizó el algortimo de Dijkstra correctamente!"
            g.mensaje.append(mensaje)
            for vert in g.lista_vertices:
                if vert != vertice:
                    mensaje = "El peso de la ruta de " + vertice + " -> " + vert + " es: " + str(g.lista_vertices[vert].peso_minimo)
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
                mensaje += str(origen) + ", "
            mensaje += str(destino) + "]"
            g.mensaje.append(mensaje)
            mensaje = "El peso es: " + str(nombres)
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
