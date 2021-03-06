import copy
from operator import attrgetter
import math

class Vertice:
    """
    Constructor de la clase Vertice para crearlo con una clave

    @param clave: un String, Int o Float para identificar al vertice
    """
    def __init__(self, clave, flujo = 0):
        self.id= clave              # Identificador del vertice
        self.grado= 0               # Grado del vertice
        self.lista_entrantes= []    # Lista de los verices a los que esta conectado el vertice
        self.lista_salientes= []
        self.color= -1              # Variable utlizada para el algoritmo de Bipartita: Asiga un color al nodo
        self.bandera= 0             # Indica si el nodo fue visitado o no
        self.padre = None           # Vértice anterior a este
        self.peso_minimo = math.inf # Distancia del padre a este
        self.peso_max = 0
        self.peso_actual = math.inf
        self.flujo = flujo
        

    """
    Destructor de la clase Vertice
    """
    def __del__(self):
        del self

    """
    Sobrecargo de operador para imprimir el objeto de la manera deseada
    """
    def __str__(self):
        return str(self.id) + ' conectado a: E:' + str([id for id in self.lista_entrantes]) + ' S:'+str([id for id in self.lista_salientes])

    def conectarSalientes(self, clave):
        self.lista_salientes.append(clave)

    def conectarEntrantes(self, clave):
        self.lista_entrantes.append(clave)

    """
    Función para agregar que agrega a que vertice esta conectado cada vertice y aumenta el grado de este.

    @param destino: Identificador del vertice que se desea agregar a los que esta conectado
    """
    def conectar(self, destino, dirigida):
        self.grado= self.grado+ 1
        self.conectarSalientes(destino.id)
        destino.conectarEntrantes(self.id)
        if not dirigida:
            destino.grado += 1
            destino.conectarSalientes(self.id)
            self.conectarEntrantes(destino.id)

    """
    Función para revisar si un vertice esta conectado a otro.

    @param clave:   Identificador de vertice que se desea buscar.

    @return:        True o False si se encontro el vertice deseado en la lista_entrantess
    """
    def existeConexion(self, clave, dirigida):
        if clave in self.lista_salientes:
            return True
        else:
            if(not dirigida):
                if clave in self.lista_entrantes:
                    return True
            return False

    def eliminarEntrantes(self, clave):
        self.lista_entrantes.remove(clave)

    def eliminarSalientes(self, clave):
        self.lista_salientes.remove(clave)

    """
    Función para eliminar un vertice de la lista_entrantess.

    @param clave: Identificador de vertice que se desea eliminar.
    """
    def eliminarConexion(self, clave, dirigida):
        self.grado= self.grado- 1
        self.eliminarSalientes(clave.id)
        clave.eliminarEntrantes(self.id)
        if not dirigida:
            clave.eliminarSalientes(self.id)
            self.eliminarEntrantes(clave.id)
            clave.grado -= 1

    """
    Función para revisar el grado de un vertice.

    @return: Un Int que representa el grado del vertice.
    """
    def obtenerGrado(self, dirigida):
        if not dirigida:
            return self.grado
        else:
            return (len(self.lista_entrantes), len(self.lista_salientes))

    """
    Función que restea el grado del vertice y vacia su lista_cinectado.
    """
    def vaciar(self):
        self.grado= 0
        self.lista_entrantes= []
        self.lista_salientes= []


class Arista:
    """
    Constructor de la clase Arista.

    @param clave:   String que sirve como identificador de la arista.
    @param origen:  Identificador del vertice de donde comienza la arista.
    @param destino: Identificador del vertice donde termina la arista.
    @param peso:    Int o Float del peso que tiene la arista.
    """
    def __init__(self, clave, origen, destino, peso= 0, peso_min = 0, costo = 0):
        self.id = clave          #Identificador de la arista
        self.origen = origen     #Identificador del vertice donde empieza la arista
        self.destino = destino   #Identificador del vertice donde termina la arista
        self.peso = peso         #Peso de la arista
        self.peso_actual = 0
        self.peso_min = peso_min
        self.costo = costo
        self.color = -1

    """
    Sobrecargo de operador para imprimir la arista de la forma deseada.
    """
    def __str__(self):
        return str(self.id) + ' Origen: ' + str(self.origen) + ' Destino: ' + str(self.destino) + ' Flujo[' + str(self.peso_min) + ', ' + str(self.peso_actual) + ', ' + str(self.peso)  + ']'

    """
    Destructor de la clase Arista.
    """
    def __del__(self):
        del self

class Grafica:
    """
    Contructor de la clase Grafica
    """
    def __init__(self, dirigida= False):
        self.lista_vertices= {}     #Diccionario donde estan todos los vertices de la grafica
        self.lista_aristas= {}      #Diccionario donde estan todas las aristas de la grafica
        self.numero_aristas= 0      #Int que representa el número total de vertices en la grafica
        self.numero_vertices= 0     #Int que representa el número total de aristas en la grafica
        self.dirigida = dirigida
        self.peso_grafica= 0
        self.costo = 0
        self.mensaje = []
        self.infinito = math.inf
        self.booleanosalvaje = False

    def __contains__(self, n):
        return n in self.lista_vertices

    """
    Sobrecargo de operador para poder iterar en la lista_vertices
    """
    def __iter__(self):
        return iter(self.lista_vertices.values())

    """
    Destructor de la clase Grafica
    """
    def __del__(self):
        del self
    """
    Función para agregar un vertice a la grafica.

    @param clave: Identificador de vertice que se desea agregar.

    @return:      True o False si se agrego o no el vertice.
    """
    def agregarVertice(self, clave, tipo= None, flujo= 0):
        if clave not in self.lista_vertices:                #Revisa si existe el vertice en la grafica
            self.numero_vertices= self.numero_vertices+ 1   #Sumamos uno al numereot total de vertices
            nuevo_vertice= Vertice(clave)                   #Creamos el vertice
            self.lista_vertices[clave]= nuevo_vertice       #Agrega el vertice al diccionario de vertices
            if tipo:
                self.lista_vertices[clave].color= tipo
            self.lista_vertices[clave].flujo = flujo
            return True                                     #Se agrego el vertice correctamente, regresa True
        else:                                               #Si el vertice existe, regresa False
            return False

    """
    Función para agregar una arista a la grafica

    @param clave:   String que sirve com identificador de la arista.
    @param inicio:  Identificador del vertice donde inicia la arista.
    @param destino: Identificador del vertice donde termina la arista.
    @param peso:    Int o Float que representa el peso de la arsita

    @return:        True o False si se agrego la atista a la grafica.
    """
    def agregarArista(self, clave, inicio, destino, peso= 0, peso_min= 0, costo = 0):
        if (inicio in self.lista_vertices) and (destino in self.lista_vertices):        #Primero revisa que el vertice inicio y destino existan en la grafica
            nueva_arista= Arista(clave, inicio, destino, peso, peso_min, costo)                          #Si existe, entonces crea la arista, la agrega al diccionario de aristas
            self.numero_aristas= self.numero_aristas+ 1                                 #y suma uno al total de aristas
            self.lista_aristas[clave]= nueva_arista

            if inicio == destino:                                                       #Si es un lazo, entonces agrega el identificador del vertice
                self.lista_vertices[inicio].conectar(self.lista_vertices[destino], True)                           #a la lista_entrantess del vertice y suma un uno extra al grado del vertice
                self.lista_vertices[inicio].grado= self.lista_vertices[inicio].grado+ 1
            else:                                                                       #Si no es un lazo, entonces agrega el identificador del vertice destino a la
                self.lista_vertices[inicio].conectar(self.lista_vertices[destino], self.dirigida)                           #lista_entrantes del vetice inicio y viceversa
            return True
        else:                                                                           #En caso de que no existe vertice inicio o destino, regresa False
            return False

    """
    Función para buscar un vertice en la grafica.

    @param clave: Identificador del vetice que se desea buscar.

    @return:      El vertice buscado o None.
    """
    def buscarVertice(self, clave):
        if clave in self.lista_vertices:        #Si encuentra el vertice, regresa el vertice
            return self.lista_vertices[clave]
        else:                                   #En el caso de de que no encontro el vertice, regresa None
            return None

    """
    Función para buscar arista en la grafica.

    @param inicio:  Identificador del vertice donde inicia la arista.
    @param destino: Identificador del vertice donde termina la arista.

    @return:        La arista buscada o None.
    """
    def buscarArista(self, inicio, destino, clave = None):
        if clave != None:
            if clave in self.lista_aristas:
                return self.lista_aristas[clave]
            else:
                return False
        if (inicio in self.lista_vertices) and (destino in self.lista_vertices):    #Revisa si existen los vertices inicio y destino.Como las aristas aun no tienen
            for arista in self.lista_aristas:                                       #dirección, busca en ambas dirreciones. Si el inicio es destino o origen y viceversa.
                if (self.lista_aristas[arista].origen == inicio) and (self.lista_aristas[arista].destino == destino):
                    return self.lista_aristas[arista]

                if not self.dirigida:
                    if (self.lista_aristas[arista].origen == destino) and (self.lista_aristas[arista].destino == inicio):
                        return self.lista_aristas[arista]

            return None                                                             #Si no encontro la arista, regresa None
        else:                                                                       #Si no existe alguno de los vertices, regresa None
            return None


    """
    Función que copia la grafica.

    @return: La copia de la grafica.
    """
    def copiar(self, grafica=None):
        if grafica:
            self.vaciarGrafica()
            self.lista_vertices = copy.deepcopy(grafica.lista_vertices)
            self.lista_aristas = copy.deepcopy(grafica.lista_aristas)
            self.dirigida = copy.deepcopy(grafica.dirigida)
            self.costo = copy.deepcopy(grafica.costo)
            self.numero_aristas= copy.deepcopy(grafica.numero_aristas)
            self.numero_vertices= copy.deepcopy(grafica.numero_vertices)
            self.peso_grafica= copy.deepcopy(grafica.peso_grafica)
            for v in self.lista_vertices:
                print(self.lista_vertices[v])
            return
        else:
            return copy.deepcopy(self)

    """
    Función para eliminar un vertice de la grafica.

    @param clave:   Identificador del vertice.

    @return:        True o False si se elimina el vertice o no.
    """
    def eliminarVertice(self, clave):
        if clave in self.lista_vertices:                                #Revisa que el vertice exista en la grafica
            self.vaciarVertice(clave)
            self.numero_vertices= self.numero_vertices- 1               #Se resta uno al número total de vertices, se elimina el vertice y regresa True.
            del self.lista_vertices[clave]
            return True
        else:                                                           #En caso de que no exista el vertice, regresa False
            return False

    """
    Función para eliminar arista de la grafica.

    @param inicio:  Identificador del vertice donde inica la arista.
    @param destino: Identificador del vertice donde termina la arista.

    @return:        True o False si se elimina la arista de la grafica o no.
    """
    def eliminarArista(self, inicio, destino, clave = None):
        if clave != None:
            if clave  in self.lista_aristas:
                inicio = self.lista_aristas[clave].origen
                destino = self.lista_aristas[clave].destino
            else:
                return False
        if (inicio in self.lista_vertices) and (destino in self.lista_vertices):            #Revisa si existen el vertice inicio y destino
            if self.lista_vertices[inicio].existeConexion(destino, self.dirigida):                         #Si destino esta en lista_entrantess de inicio
                if inicio == destino:                                                       #Entonces checa si es un lazo, si lo es, lo borra de lista_entrantess
                    self.lista_vertices[inicio].eliminarConexion(self.lista_vertices[destino], True)                   #y resta menos 1 al grado
                    self.lista_vertices[inicio].grado= self.lista_vertices[inicio].grado- 1
                else:                                                                       #Si no es un lazo, borra destino de lista_entrantess de inicio u¿y viceversa
                    self.lista_vertices[inicio].eliminarConexion(self.lista_vertices[destino], self.dirigida)
                arista= self.buscarArista(inicio, destino)                                  #Buscamos la arista en el diccionario de aristas para borrarla
                del self.lista_aristas[arista.id]
                self.numero_aristas= self.numero_aristas - 1                                #Restamos uno al total de aristas en la grafica y regreasmos True
                return True
        else:                                                                               #Si no existe inicio o destino, regresamos False
            return False


    """
    Función auxiliar para verificar si existe alguna arista que este vinculado con un vertice dado.

    @param clave:   Identificador del vertice.

    @return:        True o False si existe una arista que este vinculada al vertice.
    """
    def existeArista(self, clave):
        for arista in self.lista_aristas:
            if (self.lista_aristas[arista].origen== clave) or (self.lista_aristas[arista].destino== clave):
                return True
        return False


    """
    Función para obtener el grado de un vertice,

    @param clave:   Identificador del vertice.

    @return:        Un Int que representa el grado del vertice.
    """
    def gradoVertice(self, clave):
        if clave in self.lista_vertices:                        #Busca si el vertice existe en la grafica
            return self.lista_vertices[clave].obtenerGrado(self.dirigida)    #Obtiene el grado del vertice y lo regresa
        else:                                                 #En caso de que el vertice no exista, regresa -1
            return -1

    """
    Función que regresa la cantidad total de vertices en la grafica

    @return:    Un Int que representa el núemero total de vertices en la grafica.
    """
    def numeroVertices(self):
        return self.numero_vertices

    """
    Función que regresa el número total de atistas.

    @return:    Un Int que representa el número total de aristas.
    """
    def numeroAristas(self):
        return self.numero_aristas

    """
    Función que reinicia los valores de un vertice.

    @param calve:   Identificador del vertice.

    @return:    True o False si se vacio correctamente el vertice o no.
    """
    def vaciarVertice(self, clave):
        if clave in self.lista_vertices:                                            #Revisa si el vertice existe en la grafica.
            vertices= list()
            for vertice in self.lista_vertices[clave].lista_salientes:                                 #Buscamos en los vertices de la grafica
                vertices.append(vertice)
            for v in vertices:
                self.eliminarArista(clave, v)

            vertices.clear()
            for vertice in self.lista_vertices[clave].lista_entrantes:
               vertices.append(vertice)
            for v in vertices:
                self.eliminarArista(v, clave)
            self.lista_vertices[clave].vaciar()                          #Se vacia el vertice
            return True                                                  #Regresa True al concluir
        else:                                                            #Regresa False al no existir el vertice en la grafica
            return False

    """
    Función para vaciar la grafica
    """
    def vaciarGrafica(self):
        self.lista_aristas.clear()          #Elimina todas las aristas del diccionario lista_aristas
        self.lista_vertices.clear()         #Elimina todos los vertices del diccionario lista_vertices
        self.numero_aristas= 0              #Regresa a 0 al número total de aristas
        self.numero_vertices= 0             #Regresa a 0 al número total de vertices
    """
    Función auxiliar pare regresar las variables color y bandera de un vertice a sus valores originales.
    """
    def restablecerVertices(self):
        for vertice in self.lista_vertices:         #Para todos lo vertices
            self.lista_vertices[vertice].color= -1  #Regresamos a su valor predeterminado la variable color
            self.lista_vertices[vertice].bandera= 0 #Y a la variable bandera
            self.lista_vertices[vertice].padre= None  #Regresamos a su valor predeterminado la variable color
            self.lista_vertices[vertice].peso_minimo= math.inf

    def restablecerColores(self):
        self.peso_grafica = 0
        self.costo = 0
        controlandoSalvaje = 0
        for vertice in self.lista_vertices:
            if (self.lista_vertices[vertice].peso_minimo == math.inf and self.lista_vertices[vertice].peso_max == 0) and self.booleanosalvaje:
                controlandoSalvaje += 1
            self.lista_vertices[vertice].peso_actual = math.inf
            if self.lista_vertices[vertice].color == '+' or self.lista_vertices[vertice].color == '-':
                continue
            if self.lista_vertices[vertice].color == 10:
                self.lista_vertices[vertice].color = '+'
            elif self.lista_vertices[vertice].color == 20:
                self.lista_vertices[vertice].color = '-'
            else:
                self.lista_vertices[vertice].color = -1
        if controlandoSalvaje == self.numero_vertices:
            self.booleanosalvaje = False
        for arista in self.lista_aristas:
            self.lista_aristas[arista].peso_actual = 0
            self.lista_aristas[arista].color = -1
    """
    Función auxiliar que ayuda a determinar si la grafica es bipartita,

    @param clave:   Identificador del vertice.

    @return:        True o False, si es bipartita o no.
    """
    def bipartita(self, clave):
        cola= []            #Creamos una cola
        cola.append(clave)  #Agregamos el vertice a la cola

        while cola:
            u= cola.pop()                               #Sacamos el vertice "u" de la cola
            if self.lista_vertices[u].existeConexion(u, self.dirigida):#Si hay un lazo, entonces regresa False
                return False

            for vertice in self.lista_vertices[u].lista_salientes:                        #Buscamos en los vertices a los que esta coenctado "u"
                if self.lista_vertices[vertice].color== -1:                               #Si el vertice vecino no tiene color
                    self.lista_vertices[vertice].color= 1- self.lista_vertices[u].color   #Entonces le asignamos el color contrario de "u"
                    cola.append(vertice)                                                  #Lo agregamos a cola
                    self.lista_vertices[vertice].bandera= 1                               #Y lo marcamos como visitado, ya que ya tiene color
                elif self.lista_vertices[vertice].color== self.lista_vertices[u].color:   #Si el vertice vecino tiene el mismo color que de donde viene
                    return False                                                          #Entonces no se cumple el algoritmo y regresa False
        return True

    """
    Función que determina si la grafica es bipartita.

    @return: True si es bipartita, False en caso contrario.
    """
    def esBipartita(self):
        lista_v= []                                             #Creamos una lista v para agregar a los vertices de color 1
        lista_u= []                                             #Creamos una lista u para agregar a los vertices de color 0
        for vertice in self.lista_vertices:                     #Para todos los vertices de la grafica
            if self.lista_vertices[vertice].bandera== 0:        #Si el vertice no a sido visitado
                self.lista_vertices[vertice].color= 1           #Se le asigna el color 1
                if not self.bipartita(vertice):                 #Se llama a nuestra función auxliar que marcar a sus vertices vecinos. Si la funcion auxiliar regresa True el algoritmo prosigue
                    self.restablecerVertices()                  #En caso contrario establecemos las variables color y bandera a su valor original
                    return (lista_u, lista_v, False)                                #Regresa False y el algorimo concluye
            if self.lista_vertices[vertice].color== 1:          #Si el vertice es de color 1 lo agrega a lista_v
                lista_v.append(self.lista_vertices[vertice])
            elif self.lista_vertices[vertice].color== 0:        #Si el vertice es de color 0 lo agrega a lista_ui
                lista_u.append(self.lista_vertices[vertice])
            self.lista_vertices[vertice].bandera= 1             #Asigna bandera a 1 lo que significa que el vertice ya fue visitado

        self.restablecerVertices()
        return (lista_u, lista_v, True)

    """
    Función que determina si la grafica es conexa.

    @return: True si es conexa, False en caso contrario.
    """
    def conexa(self):
        cola= []                                                           #Creamos una cola
        cola.append(list(self.lista_vertices.keys())[0])                   #Agregamos el primer vertice de la grafica
        self.lista_vertices[list(self.lista_vertices.keys())[0]].bandera= 1#Marcamos el promer vertice como visitado
        num_banderas= 1                                                    #Número de vertices visitados

        while cola:
            u= cola.pop(0)
            for vertice in self.lista_vertices[u].lista_salientes:
                if self.lista_vertices[vertice].bandera== 0:
                    cola.append(vertice)
                    self.lista_vertices[vertice].bandera= 1
                    num_banderas+= 1
        self.restablecerVertices()
        if num_banderas == self.numero_vertices:
            return True
        else:
            return False
    """
    Función que emplea el algoritmo de Fleury.

    @return:    True si se completo el algorimo e imprime el camino de Euler, False si no se cumple el algorirmo.
    """
    def Fleury(self):
        impares= 0          #Número de vertices con grados impares
        pila= []
        cola= []
        copia= self.copiar()#Copia de la grafica para trabajar con ella.

        for vertice in copia.lista_vertices:
            if (copia.lista_vertices[vertice].grado % 2) != 0:      #Buscamos la cantidad de vertices impares.
                impares= impares + 1
                if impares== 1:
                    cola.append(copia.lista_vertices[vertice].id)   #Si hay un vertice con grado impar, asignamos nuesto vc(vertice cola) y lo guardamos en la cola
                    vc= copia.lista_vertices[vertice]
                if impares== 2:
                    pila.append(copia.lista_vertices[vertice].id)   #Si hay 2 vertices con grado impar, asignamos nuesto vp(vertice pila) y lo guardamos en la pila
                    vp= copia.lista_vertices[vertice]

        if impares != 0 and impares != 2:   #Si en la grafica no hay 0 o 2 vertices con grado impar, entonces no se cumple el algoritmo.
            print("\nError: La cantidad de nodos de grado impar no cumple.")
            txt = "Error: La cantidad de nodos de grado impar no cumple."
            return (cola, impares, txt)

        if not copia.conexa():              #Si la grafica no es conexa, no se cumple el algoritmo
            print("\nError: La grafica no es conexa.")
            txt = "Error: La grafica no es conexa."
            return (cola, impares, txt)


        if impares== 0:                                                                 #Si no hay ningun vertice de grado impar, vc y vp se asignan a cualquier vertice
            cola.append(copia.lista_vertices[list(copia.lista_vertices.keys())[0]].id)  #En este caso al primero de la grafica
            pila.append(copia.lista_vertices[list(copia.lista_vertices.keys())[0]].id)  #Se agregan a la pila y cola
            vc= copia.lista_vertices[list(copia.lista_vertices.keys())[0]]
            vp= vc

        while vc.grado != 0 and vp.grado != 0:
            for vertice in copia.lista_vertices[vc.id].lista_salientes:
                if copia.lista_vertices[vertice].grado != 1:
                    cola.append(copia.lista_vertices[vertice].id)
                    copia.eliminarArista(vc.id, vertice)
                    vc= copia.lista_vertices[vertice]
                    break
            if vp.grado == 1:
                vecino= copia.lista_vertices[vp.id].lista_salientes[0]
                copia.eliminarArista(vp.id, vecino)
                aux= copia.buscarVertice(vecino)
                pila.append(copia.lista_vertices[aux.id].id)
                vp= copia.lista_vertices[aux.id]
        pila= pila[:-1]

        del copia
        while pila:
            cola.append(pila[-1])
            pila= pila[:-1]
        return (cola, impares, True)


    """
    Función que busca un árbol de expasión o un bosque, mediante el metodo de busqueda a lo profundo o a lo ancho.

    @param tipo: Int (1 o 0) que representa que tipo de busque va a realizar.
    """
    def busquedas(self, tipo):
        grafiquita = Grafica()                                                     #Copia de la grafica original con la que trabaja el algoritmo
        frontera = []                                                              #Cola o pila segun el tipo de busqueda
        frontera.append(self.lista_vertices[list(self.lista_vertices.keys())[0]]) #Agregamos el primer vertice de la grafica
        v = frontera[0]
        num_explorados = 1                                                         #Int que representa el número de vertices explorados en la grafica
        bosque = False                                                             #Variable que estable y es un bosque o no
        i = 0                                                                      #Variable auxiliar para los Id de las aristas

        while True:
            if num_explorados == self.numero_vertices:   #Revisar ya se exploraron todos los vertices
                break                                   #Si el numero de vertices explorados es igual al número de vertices totales en la grafica. Se rompe el ciclo
            elif len(frontera) == 0:                     #Si la frontera que es nuestra pila/cola esta vacia y no estan todos los nodos explorados. Entoncecs es un bosque
                bosque = True
                for vertice in self.lista_vertices:                     #Revisa los vertices de la grafica para encontrar uno que no hay sido visitado.
                    if self.lista_vertices[vertice].bandera == 0:        #Agregamos el primero que encuentra a frontera
                        frontera.append(self.lista_vertices[vertice])
                        num_explorados += 1
                        break
            print(v)
            if tipo == 0: #Busqueda a lo profundo (0)
                cont = 0
                for vertice in self.lista_vertices[v.id].lista_salientes:
                    if (self.lista_vertices[vertice].bandera == 0):
                        break
                    cont += 1
                if cont == len(self.lista_vertices[v.id].lista_salientes):
                    v.bandera = 1
                    v = frontera[-1]
                    frontera = frontera[:-1]

            elif tipo== 1: #Busqueda a los ancho (1)
                v = frontera[0]
                frontera= frontera[1:]

            v.bandera = 1
            grafiquita.agregarVertice(v.id)

            for vertice in self.lista_vertices[v.id].lista_salientes:
                if (self.lista_vertices[vertice] not in frontera) and (self.lista_vertices[vertice].bandera == 0):
                    grafiquita.agregarVertice(vertice)
                    grafiquita.agregarArista('e'+str(i),v.id, vertice)
                    i += 1
                    num_explorados += 1

                    if tipo == 0:
                        frontera.append(v)
                        v = self.lista_vertices[vertice]
                        break
                    elif tipo == 1:
                        frontera.append(self.lista_vertices[vertice])

        self.restablecerVertices()
        return (grafiquita, bosque)
    """
    Algoritmo que busca el árbol de minima expansion en una grafica conexa.
    """
    def kruskal(self):
        grafiquita = Grafica()                                      #El arbol de minima expansion o bosque
        aristas_ordenadas= []                                       #Lista de aristas ordenada por pesos de menor a mayor
        total_vertices = self.numero_vertices
        lista_padres = list(range(total_vertices))                  #Lista de padres de los vértices
        self.peso_grafica= 0                                   #Peso total del árbol o bosque
        bosque = False

        for vertice in self.lista_vertices:                     #Copiamos los vertices de la grafica original en lo que sera nuestro
            grafiquita.agregarVertice(vertice)                  #árbol de minima expansion o bosque.

        for arista in self.lista_aristas:                          #Guardamos todas las aristas en nuestra lista
            aristas_ordenadas.append(self.lista_aristas[arista])


        aristas_ordenadas.sort(key=attrgetter('peso'))               #Ordenamos la lista en base el peso
        vertices = list(self.lista_vertices.values())                #Lista de vertices

        for arista in aristas_ordenadas:
            if busqueda(lista_padres, vertices.index(self.lista_vertices[arista.origen])) is not busqueda(lista_padres, vertices.index(self.lista_vertices[arista.destino])): #Si los vertices no tienen la misma raíz
                grafiquita.agregarArista(arista.id, arista.origen, arista.destino, arista.peso)     #Agregamos la arista
                lista_padres= union(lista_padres, vertices.index(self.lista_vertices[arista.origen]), vertices.index(self.lista_vertices[arista.destino])) #Reacomodamos las raices
                self.peso_grafica += arista.peso                                                           #Sumamos el peso de la arista al peso total del árbol
            if  grafiquita.numero_aristas == total_vertices - 1:            #Si el número total de aristas es igual al el numero de vertices menos uno, entonces ya tenemos el arbol de expansion
                break


        if grafiquita.numero_aristas is not total_vertices - 1:            #Si la cantidad de aristas no cumple con ser #vertices-1, entonces debe ser un bosque.
            bosque = True

        return (grafiquita, self.peso_grafica, bosque)

    def prim(self):
        grafiquita = Grafica()
        lista_actuales = []
        lista_actuales.append(self.lista_vertices[list(self.lista_vertices.keys())[0]])
        lista_actuales[0].bandera = 1
        visitados = 1
        bosque = False
        self.peso_grafica = 0

        for vertice in self.lista_vertices:                     # Copiamos los vertices de la grafica original en lo que sera nuestro
            grafiquita.agregarVertice(vertice)                  # árbol de minima expansion o bosque.

        while(visitados < grafiquita.numero_vertices):
            lista_vecinos = []

            for vertice in lista_actuales:
                for vecino in self.lista_vertices[vertice.id].lista_salientes:

                    if self.lista_vertices[vecino].bandera == 0:
                        if self.buscarArista(vertice.id, vecino):
                            lista_vecinos.append(self.buscarArista(vertice.id, vecino))

            # Segmento para bosques
            if len(lista_vecinos) == 0:
                bosque = True
                lista_actuales = []

                for vertice in self.lista_vertices:                     #Revisa los vertices de la grafica para encontrar uno que no hay sido visitado.
                    if self.lista_vertices[vertice].bandera == 0:        #Agregamos el primero que encuentra a frontera
                        self.lista_vertices[vertice].bandera = 1
                        lista_actuales.append(self.lista_vertices[vertice])
                        visitados += 1
                        break

                continue

            minimo = pesoMinimo(lista_vecinos)

            grafiquita.agregarArista(minimo.id, minimo.origen, minimo.destino, minimo.peso)
            self.peso_grafica += minimo.peso

            # Solo uno tiene bandera = 0
            if self.lista_vertices[minimo.origen].bandera == 0:
                self.lista_vertices[minimo.origen].bandera = 1
                lista_actuales.append(self.lista_vertices[minimo.origen])

            elif self.lista_vertices[minimo.destino].bandera == 0:
                self.lista_vertices[minimo.destino].bandera = 1
                lista_actuales.append(self.lista_vertices[minimo.destino])

            visitados += 1

        self.restablecerVertices()
        return (grafiquita, self.peso_grafica, bosque)


    def dijkstra(self, inicio):
        assert inicio in self.lista_vertices
        grafiquita = Grafica(self.dirigida)
        cola = []

        # Copiamos los vertices de la grafica original
        for vertice in self.lista_vertices:
            grafiquita.agregarVertice(vertice)

        # Primer paso del algoritmo de Dijkstra
        cola.append(inicio)                                   # Guardamos etiquetas de vértices
        grafiquita.lista_vertices[inicio].bandera = 1         # 1 es marca temporal, 2 marca definitiva
        grafiquita.lista_vertices[inicio].peso_minimo = 0
        while cola:
            actual = cola[0]                                  # Obtenemos el primer elemento de la cola
            cola = cola[1:]                                   # y lo borramos de la cola y le ponemos
            grafiquita.lista_vertices[actual].bandera = 2     # la marca definitiva

            for vertice in self.lista_vertices[actual].lista_salientes:
                 arista = self.buscarArista(actual, vertice)
                 v = grafiquita.lista_vertices[vertice]

                 if v.bandera == 0:
                     grafiquita.agregarArista(arista.id, actual, vertice, arista.peso)
                     v.bandera = 1
                     v.peso_minimo = grafiquita.lista_vertices[actual].peso_minimo + arista.peso
                     cola.append(vertice)

                 elif v.bandera == 1:
                     if v.peso_minimo > grafiquita.lista_vertices[actual].peso_minimo + arista.peso:
                         grafiquita.eliminarArista(v.lista_entrantes[0], vertice)
                         v.peso_minimo = grafiquita.lista_vertices[actual].peso_minimo + arista.peso
                         grafiquita.agregarArista(arista.id, actual, vertice, arista.peso)

            cola = sortear(grafiquita.lista_vertices, cola)

        return grafiquita

    def dijkstraGeneral(self, inicio):
        aristas = []
        ciclo = []
        self.restablecerVertices()
        grafiquita = self.dijkstra(inicio)

        for arista in self.lista_aristas:
            if arista not in grafiquita.lista_aristas:
                aristas.append(self.lista_aristas[arista])

        aristas.sort(key=attrgetter('peso'))
        while True:
            fin = True
            for a in aristas:
                if grafiquita.lista_vertices[a.origen].peso_minimo + a.peso < grafiquita.lista_vertices[a.destino].peso_minimo:
                    # Identificación de ciclos
                    ciclo.append(a.origen)
                    if not grafiquita.lista_vertices[a.origen].lista_entrantes:
                        ancestro= None
                    else:
                        ancestro = grafiquita.lista_vertices[a.origen].lista_entrantes[0]
                    while True:
                        ciclo.append(ancestro)
                        if ancestro == a.destino:
                            # Ciclo positivo
                            if grafiquita.lista_vertices[a.origen].peso_minimo - grafiquita.lista_vertices[ancestro].peso_minimo + a.peso >= 0:
                                ciclo.clear()
                                break

                            # Ciclo negativo
                            else:
                                ciclo.reverse()
                                ciclo.append(ancestro)
                                return (self, ciclo, grafiquita.lista_vertices[a.origen].peso_minimo - grafiquita.lista_vertices[ancestro].peso_minimo + a.peso )

                        elif ancestro == None:
                            ciclo.clear()
                            break

                        if not grafiquita.lista_vertices[ancestro].lista_entrantes:
                            ancestro= None
                        else:
                            ancestro = grafiquita.lista_vertices[ancestro].lista_entrantes[0]
                        #ancestro = grafiquita.lista_vertices[ancestro].lista_entrantes[0]

                    fin = False
                    auxrista = grafiquita.buscarArista(grafiquita.lista_vertices[a.destino].lista_entrantes[0], a.destino)
                    grafiquita.eliminarArista(grafiquita.lista_vertices[a.destino].lista_entrantes[0], a.destino)
                    grafiquita.agregarArista(a.id, a.origen, a.destino, a.peso)

                    delta = grafiquita.lista_vertices[a.destino].peso_minimo - (grafiquita.lista_vertices[a.origen].peso_minimo + a.peso)

                    frontera = []
                    frontera.append(grafiquita.lista_vertices[a.destino])
                    aristas.remove(a)

                    while frontera:
                        v = frontera[0]
                        frontera = frontera[1:]
                        v.bandera = 1
                        grafiquita.lista_vertices[v.id].peso_minimo -= delta

                        for vertice in grafiquita.lista_vertices[v.id].lista_salientes:
                            if (grafiquita.lista_vertices[vertice] not in frontera) and (grafiquita.lista_vertices[vertice].bandera == 2):
                                frontera.append(grafiquita.lista_vertices[vertice])

                    for v in grafiquita.lista_vertices:
                        grafiquita.lista_vertices[v].bandera= 2
                    break
            if fin: break

            if auxrista is not None:
                aristas.append(auxrista)
            aristas.sort(key=attrgetter('peso'))

        return (grafiquita, 0, 1)

    def floyd(self):
        total_vertices= self.numero_vertices
        distancias= [None] * total_vertices * total_vertices
        rutas= [None] * total_vertices * total_vertices
        nombres= [v for v in self.lista_vertices]
        free4all = [None] * total_vertices * total_vertices

        for i in range(total_vertices):
            for j in range(total_vertices):
                arista = self.buscarArista(nombres[i], nombres[j])
                if(i == j):
                    distancias[i + i * total_vertices] =  0
                    rutas[i + i * total_vertices] =  nombres[i]
                elif(arista):
                    distancias[j + i * total_vertices] =  arista.peso
                    rutas[j + i * total_vertices] =  nombres[i]
                else:
                    distancias[j + i * total_vertices] =  math.inf
                    rutas[j + i * total_vertices] =  None

        for c in range(total_vertices):
            for i in range(total_vertices):
                for j in range(total_vertices):
                    if(distancias[c + i * total_vertices] + distancias[j + c * total_vertices] < distancias[j + i * total_vertices]):
                        distancias[j + i * total_vertices] =  distancias[c + i * total_vertices] + distancias[j + c * total_vertices]
                        rutas[j + i * total_vertices] =  rutas[j + c * total_vertices]

                if(distancias[i + i * total_vertices] < 0):
                    aux = i
                    ruta_aux= list()
                    distancia_aux= distancias[i + i * total_vertices]
                    ruta_aux.append(nombres[aux])
                    aux = nombres.index(rutas[aux + i * total_vertices])
                    while(aux != i):
                        ruta_aux.append(nombres[aux])
                        aux = nombres.index(rutas[aux + i * total_vertices])
                        if (aux == i):
                            ruta_aux.append(nombres[aux])

                    ruta_aux.reverse()
                    return (ruta_aux, distancia_aux, True)

        for i in range(total_vertices):
            for j in range(total_vertices):
                aux = j
                ruta_aux= list()

                if (aux == i):
                    ruta_aux.append(nombres[aux])

                while(aux != i):
                    if(rutas[j + i * total_vertices] is None):
                        break

                    ruta_aux.append(nombres[aux])
                    aux = nombres.index(rutas[aux + i * total_vertices])

                    if (aux == i):
                        ruta_aux.append(nombres[aux])


                ruta_aux.reverse()
                free4all[j + i * total_vertices] = (ruta_aux, distancias[j + i * total_vertices])

        return (free4all, nombres, False)

    def AlgoritmoFordFulkerson(self, maximo = math.inf):
        grafiquita = self.copiar()
        aristas_peso_min = list()
        vertices_min = list()
        nombres_aristas = list()
        multiples_cosas = False
        i = 0

        for v in grafiquita:
            if v.peso_minimo != math.inf and v.peso_minimo != 0:
                vertices_min.append(v)
            if v.color == '+' or v.color == '-':
                i += 1
            if i > 2:
                multiples_cosas = True
                break

        if multiples_cosas:
            grafiquita = agregarFuentesYsumideros(grafiquita)

        if vertices_min:
            for v in vertices_min:
                f = 0
                grafiquita.agregarVertice(v.id + "aux")
                for b in v.lista_salientes:
                    auxrista = grafiquita.buscarArista(v.id, b)
                    nombres_aristas.append(auxrista.id)
                    grafiquita.agregarArista(auxrista.id + "aux", v.id + "aux", b , auxrista.peso, auxrista.peso_min, auxrista.costo)
                    grafiquita.eliminarArista(auxrista.origen, auxrista.destino)

                grafiquita.agregarArista("auxrista" + str(i),v.id, v.id + "aux", v.peso_max, v.peso_minimo)
                f += 1

        for a in grafiquita.lista_aristas:
            if grafiquita.lista_aristas[a].peso_min != 0:
                aristas_peso_min.append(grafiquita.lista_aristas[a])


        if aristas_peso_min:
            for v in grafiquita.lista_vertices:
                if grafiquita.lista_vertices[v].color == '+':
                    fuente_viejo = grafiquita.lista_vertices[v]
                    fuente_viejo.color = 'c'
                elif grafiquita.lista_vertices[v].color == '-':
                    sumidero_viejo = grafiquita.lista_vertices[v]
                    fuente_viejo.color = 'd'

            grafiquita.agregarArista("auxS" , fuente_viejo.id, sumidero_viejo.id, math.inf)
            grafiquita.agregarArista("auxE" , sumidero_viejo.id, fuente_viejo.id, math.inf)

            grafiquita.agregarVertice("FN", "+")
            grafiquita.agregarVertice("SN", "-")
            e = 0

            for a in aristas_peso_min:
                arista = grafiquita.buscarArista(a.origen, "SN")
                if arista:
                    arista.peso += a.peso_min
                else:
                    grafiquita.agregarArista("auxiliar" + str(e), a.origen, "SN", a.peso_min)

                arista2 = grafiquita.buscarArista("FN", a.destino)
                if arista2:
                    arista2.peso += a.peso_min
                else:
                    grafiquita.agregarArista("auxiliar2" + str(e), "FN", a.destino, a.peso_min)

                a.peso_actual += a.peso_min
                e += 1

            grafiquita = fordFulkerson(grafiquita, maximo)

            aux = grafiquita.buscarArista(sumidero_viejo.id, fuente_viejo.id)
            grafiquita.peso_grafica = aux.peso_actual

            grafiquita.eliminarVertice("SN")
            grafiquita.eliminarVertice("FN")

            grafiquita.eliminarArista(fuente_viejo.id, sumidero_viejo.id)
            grafiquita.eliminarArista(sumidero_viejo.id, fuente_viejo.id)

            fuente_viejo.color = '+'
            sumidero_viejo.color = '-'

        grafiquita = fordFulkerson(grafiquita, maximo)


        if vertices_min:
            for v in vertices_min:
                vertaux = grafiquita.buscarVertice(v.id+"aux")
                for b in vertaux.lista_salientes:
                    auxrista = grafiquita.buscarArista(vertaux.id, b)
                    grafiquita.agregarArista(nombres_aristas[0], v.id, b , auxrista.peso, auxrista.peso_min, auxrista.costo)
                    grafiquita.lista_aristas[nombres_aristas[0]].peso_actual = auxrista.peso_actual
                    nombres_aristas = nombres_aristas[1:]

                grafiquita.eliminarVertice(vertaux.id)

        if multiples_cosas:
            grafiquita = eliminarFuentesYsumideros(grafiquita)

        return grafiquita

    def flujoCosteMinimoPrimal(self, flujo_elegido = math.inf):
        grafiquita = self.copiar()
        copia = Grafica()
        grafiquita = grafiquita.AlgoritmoFordFulkerson(flujo_elegido)
        marginal = grafiquita.copiar()
        inicio = None
        cola = list()

        for v in grafiquita:
            if v.color == '+':
                inicio = v
                break

        for a in grafiquita.lista_aristas:
            marginal.agregarArista(grafiquita.lista_aristas[a].id + "aux", grafiquita.lista_aristas[a].destino, grafiquita.lista_aristas[a].origen, grafiquita.lista_aristas[a].peso_actual, 0, grafiquita.lista_aristas[a].costo * -1)
            marginal.lista_aristas[a].peso -= grafiquita.lista_aristas[a].peso_actual
   
        copia, ciclo, d = dijkstraGeneralPeso(marginal,inicio.id)

        for a in grafiquita.lista_aristas:
            grafiquita.costo += (grafiquita.lista_aristas[a].costo * grafiquita.lista_aristas[a].peso_actual)

        while d < 0:
            cola = []
            minimo = math.inf
            for i in range(len(ciclo)):
                if i+1 < len(ciclo):
                    o = ciclo[i]
                    f = ciclo[i+1]
                    auxrista = marginal.buscarArista(o, f)
                    if auxrista.peso < minimo:
                        minimo = auxrista.peso
                    cola.append(auxrista)

            for c in cola:
                c.peso -= minimo
                arista = marginal.buscarArista(c.destino, c.origen)
                arista.peso += minimo

                if 'aux' in c.id:
                    arista = grafiquita.buscarArista(c.destino, c.origen)
                    arista.peso_actual -= minimo
                else:
                    arista = grafiquita.buscarArista(c.origen, c.destino)
                    arista.peso_actual += minimo

            grafiquita.costo += minimo * d

            
            copia, ciclo, d = dijkstraGeneralPeso(marginal, inicio.id)

        return grafiquita

    def flujoConsumoMinimoDual(self, flujo_elegido):
        copia = Grafica()
        self.costo = 0
        grafiquita = self.copiar()
        marginal = self.copiar()
        aristas_peso_min = list()
        vertices_min = list()
        nombres_aristas = list()
        multiples_cosas = False
        inicio = None
        final = None
        cola = list()
        i = 0

        for v in grafiquita:
            if v.peso_minimo != math.inf and v.peso_min != 0:
                vertices_min.append(v)
            if v.color == '+' or v.color == '-':
                i += 1
            if i > 2:
                multiples_cosas = True
                break

        if multiples_cosas:
            grafiquita = agregarFuentesYsumideros(grafiquita)

        if vertices_min:
            for v in vertices_min:
                f = 0
                grafiquita.agregarVertice(v.id + "aux")
                for b in v.lista_salientes:
                    auxrista = grafiquita.buscarArista(v.id, b)
                    nombres_aristas.append(auxrista.id)
                    grafiquita.agregarArista(auxrista.id + "aux", v.id + "aux", b , auxrista.peso, auxrista.peso_min)
                    grafiquita.eliminarArista(auxrista.origen, auxrista.destino)

                grafiquita.agregarArista("auxrista" + str(i),v.id, v.id + "aux", v.peso_max, v.peso_minimo)
                f += 1

        for a in grafiquita.lista_aristas:
            if grafiquita.lista_aristas[a].peso_min != 0:
                aristas_peso_min.append(grafiquita.lista_aristas[a])
                

        if aristas_peso_min:
            for v in grafiquita.lista_vertices:
                if grafiquita.lista_vertices[v].color == '+':
                    fuente_viejo = grafiquita.lista_vertices[v]
                    fuente_viejo.color = 'c'
                elif grafiquita.lista_vertices[v].color == '-':
                    sumidero_viejo = grafiquita.lista_vertices[v]
                    fuente_viejo.color = 'd'

            grafiquita.agregarArista("auxS" , fuente_viejo.id, sumidero_viejo.id, math.inf)
            grafiquita.agregarArista("auxE" , sumidero_viejo.id, fuente_viejo.id, math.inf)

            grafiquita.agregarVertice("FN", "+")
            grafiquita.agregarVertice("SN", "-")
            e = 0

            for a in aristas_peso_min:
                arista = grafiquita.buscarArista(a.origen, "SN")
                if arista:
                    arista.peso += a.peso_min
                else:
                    grafiquita.agregarArista("auxiliar" + str(e), a.origen, "SN", a.peso_min)

                arista2 = grafiquita.buscarArista("FN", a.destino)
                if arista2:
                    arista2.peso += a.peso_min
                else:
                    grafiquita.agregarArista("auxiliar2" + str(e), "FN", a.destino, a.peso_min)
                
                a.peso_actual += a.peso_min
                e += 1

            grafiquita = fordFulkerson(grafiquita, flujo_elegido)

            aux = grafiquita.buscarArista(sumidero_viejo.id, fuente_viejo.id)
            grafiquita.peso_grafica = aux.peso_actual

            grafiquita.eliminarVertice("SN")
            grafiquita.eliminarVertice("FN")

            grafiquita.eliminarArista(fuente_viejo.id, sumidero_viejo.id)
            grafiquita.eliminarArista(sumidero_viejo.id, fuente_viejo.id)

            fuente_viejo.color = '+'
            sumidero_viejo.color = '-'

            for a in aristas_peso_min:
                a.peso -= a.peso_min
                grafiquita.costo += a.peso_min * a.costo

        
        #
        if grafiquita.peso_grafica > flujo_elegido:
            return False

        for a in grafiquita.lista_aristas:
            grafiquita.costo += grafiquita.lista_aristas[a].peso_actual * grafiquita.lista_aristas[a].costo

        ya = 0
        for v in grafiquita:
            if v.color == '+':
                inicio = v
                ya += 1
            if v.color == '-':
                final = v
                ya += 1
            if ya == 2:
                break

        
        marginal.copiar(grafiquita)
        for a in grafiquita.lista_aristas:
            marginal.agregarArista(grafiquita.lista_aristas[a].id + "aux", grafiquita.lista_aristas[a].destino, grafiquita.lista_aristas[a].origen, grafiquita.lista_aristas[a].peso_actual, 0, grafiquita.lista_aristas[a].costo * -1)
            marginal.lista_aristas[a].peso -= grafiquita.lista_aristas[a].peso_actual

        copia, ciclo, d = dijkstraGeneralPeso(marginal,inicio.id)

        while d < 0:
            cola = []
            minimo = math.inf
            for i in range(len(ciclo)):
                if i+1 < len(ciclo):
                    o = ciclo[i]
                    f = ciclo[i+1]
                    auxrista = marginal.buscarArista(o, f)
                    if auxrista.peso < minimo:
                        minimo = auxrista.peso
                    cola.append(auxrista)

            for c in cola:
                c.peso -= minimo
                arista = marginal.buscarArista(c.destino, c.origen)
                arista.peso += minimo

                if 'aux' in c.id:
                    arista = grafiquita.buscarArista(c.destino, c.origen)
                    arista.peso_actual -= minimo
                else:
                    arista = grafiquita.buscarArista(c.origen, c.destino)
                    arista.peso_actual += minimo

            grafiquita.costo += minimo * d
                
            copia, ciclo, d = dijkstraGeneralPeso(marginal, inicio.id)


        if grafiquita.peso_grafica == flujo_elegido:
            return grafiquita
            
        else:
            while grafiquita.peso_grafica < flujo_elegido:
                cola = []
                actual = copia.lista_vertices[final.id]
                flujo_minimo = math.inf
                costo_camino = copia.lista_vertices[actual.id].peso_minimo

                while True:
                    if actual.id == inicio.id:
                        break
                    arista = copia.buscarArista(actual.lista_entrantes[0], actual.id)
                    if arista:
                        if arista.peso < flujo_minimo:
                            flujo_minimo = arista.peso
                    cola.append(arista)
                    actual = copia.buscarVertice(actual.lista_entrantes[0])
                    
                if grafiquita.peso_grafica + flujo_minimo >= flujo_elegido:
                    flujo_minimo = flujo_elegido - grafiquita.peso_grafica

                grafiquita.costo += flujo_minimo * costo_camino
                grafiquita.peso_grafica += flujo_minimo

                for c in cola:
                    arista = marginal.buscarArista(c.origen, c.destino)
                    arista.peso -= flujo_minimo

                    arista = marginal.buscarArista(c.destino, c.origen)
                    arista.peso += flujo_minimo

                    if 'aux' in arista.id:
                        auxrista = grafiquita.buscarArista(arista.destino, arista.origen)
                        auxrista.peso_actual += flujo_minimo
                    else:
                        auxrista = grafiquita.buscarArista(arista.origen, arista.destino)
                        auxrista.peso_actual -= flujo_minimo
                    
                copia, ciclo, d = dijkstraGeneralPeso(marginal, inicio.id)             
        #

        for a in aristas_peso_min:
            a.peso += a.peso_min
            a.peso_actual += a.peso_min

        if vertices_min:
            for v in vertices_min:
                vertaux = grafiquita.buscarVertice(v.id+"aux")
                for b in vertaux.lista_salientes:
                    auxrista = grafiquita.buscarArista(vertaux.id, b)
                    grafiquita.agregarArista(nombres_aristas[0], v.id, b , auxrista.peso, auxrista.peso_min)
                    nombres_aristas = nombres_aristas[1:]
                    
                grafiquita.eliminarVertice(vertaux.id)

        if multiples_cosas:
            grafiquita = eliminarFuentesYsumideros(grafiquita)

        return grafiquita
    
    def simplex(self):
        copia = Grafica()
        copia.copiar(self)
        total = 0
        i = 0
        oferta = list()
        demanda = list()
        aristas_peso_minimo = list()
        aristas_aux = list()
        flujo = 0
        coste = 0

        for v in self.lista_vertices:
            if self.lista_vertices[v].flujo < 0:
                demanda.append(self.lista_vertices[v])
            elif self.lista_vertices[v].flujo > 0:
                oferta.append(self.lista_vertices[v])
            total += self.lista_vertices[v].flujo

        if total < 0:
            copia.agregarVertice("aux", None, -1 * total)
            for v in demanda:
                copia.agregarArista("e" + str(copia.numero_aristas + 1), "aux",  v.id)
        elif total > 0:
            copia.agregarVertice("aux", None, -1 * total)
            for v in oferta:
                copia.agregarArista("e" + str(copia.numero_aristas + 1), v.id,  "aux")

        for a in copia.lista_aristas:
            copia.lista_aristas[a].costo = 0
            if  copia.lista_aristas[a].peso_min > 0:
                aristas_peso_minimo.append(copia.lista_aristas[a])

        if aristas_peso_minimo:
            for a in aristas_peso_minimo:
                a.peso_actual = a.peso_min

        copia.agregarVertice("aux2")

        for v in copia.lista_vertices:
            if v != "aux2":
                delta = copia.lista_vertices[v].flujo

                for a in aristas_peso_minimo:
                    if v == a.origen:
                        delta -= a.peso_actual
                    elif v == a.destino:
                        delta += a.peso_actual
                        
                if delta < 0:
                    copia.agregarArista("aux" + str(i), "aux2", v, math.inf, 0, 1)
                    copia.lista_aristas["aux" + str(i)].peso_actual = delta * -1
                    aristas_aux.append(copia.lista_aristas["aux" + str(i)])
                    i += 1
                elif delta > 0:
                    copia.agregarArista("aux" + str(i), v, "aux2", math.inf, 0, 1)
                    copia.lista_aristas["aux" + str(i)].peso_actual = delta
                    aristas_aux.append(copia.lista_aristas["aux" + str(i)])
                    i += 1
        
        while True:
            (copia, flujo, coste) = metodoSimplex(copia)

            eliminar = []

            for arista in aristas_aux:
                if copia.lista_aristas[arista.id].peso_actual == 0:
                    copia.eliminarArista(arista.origen, arista.destino, arista.id)
                    eliminar.append(arista)

            for e in eliminar:
                aristas_aux.remove(e)

            if (len(copia.lista_vertices["aux2"].lista_entrantes) + len(copia.lista_vertices["aux2"].lista_salientes)) == 0:
                copia.eliminarVertice("aux2")
                break

        for a in self.lista_aristas:
            copia.lista_aristas[a].costo = self.lista_aristas[a].costo
            copia.costo += copia.lista_aristas[a].costo * copia.lista_aristas[a].peso_actual

        (copia, flujo, coste) = metodoSimplex(copia)

        while(coste > 0):
            copia.costo -= (flujo * coste)
            (copia, flujo, coste) = metodoSimplex(copia)

        for ver in copia.lista_vertices:
            delta = copia.lista_vertices[ver].flujo
            for a in aristas_peso_minimo:
                if ver == a.origen:
                    delta += a.peso_actual
                elif ver == a.destino:
                    delta -= a.peso_actual

        vertgroup = list()
        flujos_flojos = list()
        for verx in copia.lista_vertices:
            f = 0
            for aris in copia.lista_aristas:
                if copia.lista_aristas[aris].origen == verx:
                    f -= copia.lista_aristas[aris].peso_actual
                elif copia.lista_aristas[aris].destino == verx:
                    f += copia.lista_aristas[aris].peso_actual
            
            if f != 0:
                vertgroup.append(verx)
                flujos_flojos.append(f)


        for arista in copia.lista_aristas:
            if (copia.lista_aristas[arista].origen in vertgroup) and (copia.lista_aristas[arista].destino in vertgroup):
                indiceO = vertgroup.index(copia.lista_aristas[arista].origen)
                indiceD = vertgroup.index(copia.lista_aristas[arista].destino)
                flujo_disponible = copia.lista_aristas[arista].peso_actual - copia.lista_aristas[arista].peso_min

                if flujos_flojos[indiceO] < 0 and flujos_flojos[indiceD] > 0:
                    flujo_disponible = min(flujo_disponible, flujos_flojos[indiceO] * -1)
                    flujo_disponible = min(flujo_disponible, flujos_flojos[indiceD])
                    copia.lista_aristas[arista].peso_actual -= flujo_disponible
                    copia.costo -= flujo_disponible * copia.lista_aristas[arista].costo
        return copia
        
def metodoSimplex(grafica):
    copia = Grafica()
    copia.copiar(grafica)
    aristas = list()
    no_basicos = list()
    flujo = math.inf
    coste = 0

    for a in grafica.lista_aristas:
        if grafica.lista_aristas[a].peso == grafica.lista_aristas[a].peso_actual:
            copia.eliminarArista(grafica.lista_aristas[a].origen, grafica.lista_aristas[a].destino, grafica.lista_aristas[a].id)
        elif (grafica.lista_aristas[a].peso_actual - grafica.lista_aristas[a].peso_min) == 0:
            no_basicos.append(grafica.lista_aristas[a])
            copia.eliminarArista(grafica.lista_aristas[a].origen, grafica.lista_aristas[a].destino, grafica.lista_aristas[a].id)

    for a in no_basicos:
        flujo = math.inf
        frontera = []
        aristas = []
        v = copia.lista_vertices[a.destino]
        v.bandera = 1
        while True:
            cont = 0
            for vertice in copia.lista_vertices[v.id].lista_salientes:
                if (copia.lista_vertices[vertice] in frontera):
                    cont += 1
                    continue
                if (copia.lista_vertices[vertice].bandera == 0):
                    break
                cont += 1
        
            for vertice in copia.lista_vertices[v.id].lista_entrantes:
                if copia.lista_vertices[vertice] in frontera:
                    cont += 1
                    continue
                if (copia.lista_vertices[vertice].bandera == 0):
                    break
                cont += 1

            if cont == (len(copia.lista_vertices[v.id].lista_salientes) + len(copia.lista_vertices[v.id].lista_entrantes)):
                if cont != 0 and (len(copia.lista_vertices[v.id].lista_salientes) + len(copia.lista_vertices[v.id].lista_entrantes)) != 0:
                    v.bandera = 1
                    v = frontera[-1]
                    frontera = frontera[:-1]
                    aristas = aristas[:-1]

            termino = False
            for vertices in copia.lista_vertices[v.id].lista_salientes:
                if (copia.lista_vertices[vertices] not in frontera) and (copia.lista_vertices[vertices].bandera == 0):
                    auxrista = copia.buscarArista(v.id, vertices)
                    auxrista = grafica.buscarArista(v.id, vertices, auxrista.id)
                    aristas.append(auxrista)
                    frontera.append(v)
                    v = copia.lista_vertices[vertices]
                    termino = True
                    break
            
            if termino == False:
                for vertices in copia.lista_vertices[v.id].lista_entrantes:
                    if (copia.lista_vertices[vertices] not in frontera) and (copia.lista_vertices[vertices].bandera == 0):
                        auxrista = copia.buscarArista(vertices, v.id)
                        auxrista = grafica.buscarArista(vertices, v.id, auxrista.id)
                        aristas.append(auxrista)
                        frontera.append(v)
                        v = copia.lista_vertices[vertices]
                        break
            if v.id == a.origen:
                frontera.append(v)
                break
            if len(frontera) == 0:
                break

        copia.restablecerVertices()
        coste = 0

        for i in range(len(frontera)-1):
            v1 = frontera[i]
            v2 = frontera[i + 1]
            aurista = copia.buscarArista(v1.id, v2.id)
            aux = aristas[i]
            if aurista != None:
                aurista = grafica.buscarArista(v1.id, v2.id, aurista.id)
                if aurista.id == aux.id:
                    flujo = min(flujo, aux.peso - aux.peso_actual)
                    coste -= aux.costo
                else:
                    flujo = min(flujo, aux.peso_actual - aux.peso_min)
                    coste += aux.costo
            else:
                flujo = min(flujo, aux.peso_actual - aux.peso_min)
                coste += aux.costo

        coste -= a.costo
        flujo = min(flujo, a.peso - a.peso_actual)
        
        if coste > 0:
            aristas.append(a)
            for i in range(len(frontera)-1):
                v1 = frontera[i]
                v2 = frontera[i + 1]
                aurista = copia.buscarArista(v1.id, v2.id)
                aux = aristas[i]
                if aurista != None:
                    aurista = grafica.buscarArista(v1.id, v2.id, aurista.id)
                    if aurista.id == aux.id:
                        grafica.lista_aristas[aux.id].peso_actual += flujo
                    else:
                        grafica.lista_aristas[aux.id].peso_actual -= flujo
                else:
                    grafica.lista_aristas[aux.id].peso_actual -= flujo
            a.peso_actual += flujo
            break
    return (grafica, flujo, coste)

def dijkstraPeso(grafica, inicio):
    assert inicio in grafica.lista_vertices
    grafiquita = Grafica(grafica.dirigida)
    cola = []

    # Copiamos los vertices de la grafica original
    for vertice in grafica.lista_vertices:
        grafiquita.agregarVertice(vertice)

    # Primer paso del algoritmo de Dijkstra
    cola.append(inicio)                                   # Guardamos etiquetas de vértices
    grafiquita.lista_vertices[inicio].bandera = 1         # 1 es marca temporal, 2 marca definitiva
    grafiquita.lista_vertices[inicio].peso_minimo = 0
    while cola:
        actual = cola[0]                                  # Obtenemos el primer elemento de la cola
        cola = cola[1:]                                   # y lo borramos de la cola y le ponemos
        grafiquita.lista_vertices[actual].bandera = 2     # la marca definitiva

        for vertice in grafica.lista_vertices[actual].lista_salientes:
                arista = grafica.buscarArista(actual, vertice)
                v = grafiquita.lista_vertices[vertice]

                if v.bandera == 0:
                    if arista.peso > 0:
                        grafiquita.agregarArista(arista.id, actual, vertice, arista.peso, arista.peso_min, arista.costo)
                        v.bandera = 1
                        v.peso_minimo = grafiquita.lista_vertices[actual].peso_minimo + arista.costo
                        cola.append(vertice)

                elif v.bandera == 1:
                    if v.peso_minimo > grafiquita.lista_vertices[actual].peso_minimo + arista.costo:
                        if arista.peso > 0:
                            grafiquita.eliminarArista(v.lista_entrantes[0], vertice)
                            v.peso_minimo = grafiquita.lista_vertices[actual].peso_minimo + arista.costo
                            grafiquita.agregarArista(arista.id, actual, vertice, arista.peso, arista.peso_min, arista.costo)

        cola = sortear(grafiquita.lista_vertices, cola)

    return grafiquita

def dijkstraGeneralPeso(grafica, inicio):
    aristas = []
    ciclo = []
    grafica.restablecerVertices()
    grafiquita = dijkstraPeso(grafica, inicio)

    for arista in grafica.lista_aristas:
        if arista not in grafiquita.lista_aristas and grafica.lista_aristas[arista].peso > 0:
            aristas.append(grafica.lista_aristas[arista])

    aristas.sort(key=attrgetter('costo'))
    while True:
        fin = True
        for a in aristas:
            if grafiquita.lista_vertices[a.origen].peso_minimo + a.costo < grafiquita.lista_vertices[a.destino].peso_minimo:
                # Identificación de ciclos
                ciclo.append(a.origen)
                if not grafiquita.lista_vertices[a.origen].lista_entrantes:
                    ancestro= None
                else:
                    ancestro = grafiquita.lista_vertices[a.origen].lista_entrantes[0]
                while True:
                    ciclo.append(ancestro)
                    if ancestro == a.destino:
                        # Ciclo positivo
                        if grafiquita.lista_vertices[a.origen].peso_minimo - grafiquita.lista_vertices[ancestro].peso_minimo + a.costo >= 0:
                            ciclo.clear()
                            break

                        # Ciclo negativo
                        else:
                            ciclo.reverse()
                            ciclo.append(ancestro)
                            return (grafica, ciclo, grafiquita.lista_vertices[a.origen].peso_minimo - grafiquita.lista_vertices[ancestro].peso_minimo + a.costo )

                    elif ancestro == None:
                        ciclo.clear()
                        break

                    if not grafiquita.lista_vertices[ancestro].lista_entrantes:
                        ancestro= None
                    else:
                        ancestro = grafiquita.lista_vertices[ancestro].lista_entrantes[0]
                    #ancestro = grafiquita.lista_vertices[ancestro].lista_entrantes[0]

                fin = False
                auxrista = grafiquita.buscarArista(grafiquita.lista_vertices[a.destino].lista_entrantes[0], a.destino)
                grafiquita.eliminarArista(grafiquita.lista_vertices[a.destino].lista_entrantes[0], a.destino)
                grafiquita.agregarArista(a.id, a.origen, a.destino, a.peso, a.peso_min, a.costo)

                delta = grafiquita.lista_vertices[a.destino].peso_minimo - (grafiquita.lista_vertices[a.origen].peso_minimo + a.costo)

                frontera = []
                frontera.append(grafiquita.lista_vertices[a.destino])
                aristas.remove(a)

                while frontera:
                    v = frontera[0]
                    frontera = frontera[1:]
                    v.bandera = 1
                    grafiquita.lista_vertices[v.id].peso_minimo -= delta

                    for vertice in grafiquita.lista_vertices[v.id].lista_salientes:
                        if (grafiquita.lista_vertices[vertice] not in frontera) and (grafiquita.lista_vertices[vertice].bandera == 2):
                            frontera.append(grafiquita.lista_vertices[vertice])

                for v in grafiquita.lista_vertices:
                    grafiquita.lista_vertices[v].bandera= 2
                break
        if fin: break

        if auxrista is not None:
            aristas.append(auxrista)
        aristas.sort(key=attrgetter('costo'))

    for v in grafiquita:
        print(v)

    return (grafiquita, 0, 1)

def fordFulkerson(grafiquita, maximo):
    cola = list()
    fuente = None
    sumidero = None

    for v in grafiquita.lista_vertices:
        if grafiquita.lista_vertices[v].color == '+':
            fuente = grafiquita.lista_vertices[v]
        elif grafiquita.lista_vertices[v].color == '-':
            sumidero = grafiquita.lista_vertices[v]

    while(True):
        if grafiquita.peso_grafica >= maximo:
            break
        cola = []
        fuente.bandera = 1
        cola.append(fuente)

        while cola:
            c = cola[0]
            cola = cola[1:]

            if c.bandera == 1:
                c.bandera = 3
            elif c.bandera == 2:
                c.bandera = 4

            for v in c.lista_salientes:
                if grafiquita.lista_vertices[v].bandera != 0:
                    continue
                a = grafiquita.buscarArista(c.id, v)
                chorrito = min(a.peso - a.peso_actual, c.peso_actual)
                chorrito = min(chorrito, maximo - grafiquita.peso_grafica)

                if chorrito == 0:
                    continue

                grafiquita.lista_vertices[v].bandera = 1
                grafiquita.lista_vertices[v].padre = c
                grafiquita.lista_vertices[v].peso_actual = chorrito
                cola.append(grafiquita.lista_vertices[v])

            for v in c.lista_entrantes:
                if grafiquita.lista_vertices[v].bandera != 0:
                    continue
                a = grafiquita.buscarArista(v, c.id)
                chorrito = min(a.peso_actual - a.peso_min, c.peso_actual)
                chorrito = min(chorrito, maximo - grafiquita.peso_grafica)

                if chorrito == 0:
                    continue

                grafiquita.lista_vertices[v].bandera = 2
                grafiquita.lista_vertices[v].padre = c
                grafiquita.lista_vertices[v].peso_actual = chorrito
                cola.append(grafiquita.lista_vertices[v])

            if sumidero in cola:
                grafiquita.peso_grafica += sumidero.peso_actual
                break

        if not cola:
            break

        actual= sumidero
        chorrito = sumidero.peso_actual

        while(actual != fuente):
            if actual.bandera == 1 or actual.bandera == 3:
                a = grafiquita.buscarArista(actual.padre.id, actual.id)
                a.peso_actual += chorrito

            if actual.bandera == 2 or actual.bandera == 4:
                a = grafiquita.buscarArista(actual.id, actual.padre.id)
                a.peso_actual -= chorrito
            if actual.padre == fuente:
                break

            actual = actual.padre

        for v in grafiquita:
            v.bandera = 0
            v.peso_actual = math.inf
            v.padre = None

        if grafiquita.peso_grafica >= maximo:
            break

    return grafiquita

def agregarFuentesYsumideros(grafica):
    grafica.agregarVertice("inicio")
    grafica.agregarVertice("fin")
    i = 0

    for v in grafica:
        if v.color == '+':
            v.color = 'a'
            grafica.agregarArista(str(i) + "aux","inicio", v.id, math.inf)
            i += 1
        if v.color == '-':
            v.color = 'b'
            grafica.agregarArista(str(i) + "fin",v.id, "fin", math.inf)
            i += 1
    v = grafica.buscarVertice("inicio")
    v.color = '+'

    v = grafica.buscarVertice("fin")
    v.color = '-'

    return grafica

def eliminarFuentesYsumideros(grafica):
    grafica.eliminarVertice("inicio")
    grafica.eliminarVertice("fin")

    for v in grafica:
        if v.color == 'a':
            v.color = '+'

        if v.color == 'b':
            v.color = '-'
    return grafica

'''
Funciones auxiliares para algoritmo de Kruskal
'''
def busqueda(lista, indice):
    if(lista[indice] == indice): return indice
    return busqueda(lista, lista[indice])

def union(lista, u, v):
    lista[busqueda(lista, u)] = busqueda(lista, v)
    return lista

'''
Función auxiliar para algoritmo de Prim
'''
def pesoMinimo(lista_aristas):
    menor = lista_aristas[0]
    lista_aristas = lista_aristas[1:]

    for a in lista_aristas:
        if a.peso < menor.peso: menor = a

    return menor

'''
Función auxiliar para algoritmo de Dijkstra
'''
def sortear(lista_vertices, cola):
    lista_ordenada = []
    for vertice in cola:
        lista_ordenada.append(lista_vertices[vertice])

    lista_ordenada.sort(key=attrgetter('peso_minimo'))

    for i in range(len(cola)):
        cola[i] = lista_ordenada[i].id

    return cola
