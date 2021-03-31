import copy
from operator import attrgetter
import math

class Vertice:
    """
    Constructor de la clase Vertice para crearlo con una clave

    @param clave: un String, Int o Float para identificar al vertice
    """
    def __init__(self, clave):
        self.id= clave              # Identificador del vertice
        self.grado= 0               # Grado del vertice
        self.lista_conectado= []    # Lista de los verices a los que esta conectado el vertice
        self.color= -1              # Variable utlizada para el algoritmo de Bipartita: Asiga un color al nodo
        self.bandera= 0             # Indica si el nodo fue visitado o no
        self.padre = None           # Vértice anterior a este
        self.peso_minimo = math.inf # Distancia del padre a este

    """
    Destructor de la clase Vertice
    """
    def __del__(self):
        del self

    """
    Sobrecargo de operador para imprimir el objeto de la manera deseada
    """
    def __str__(self):
        return str(self.id) + ' conectado a: ' + str([id for id in self.lista_conectado])

    """
    Función para agregar que agrega a que vertice esta conectado cada vertice y aumenta el grado de este.

    @param destino: Identificador del vertice que se desea agregar a los que esta conectado
    """
    def conectar(self, destino):
        self.grado= self.grado+ 1
        self.lista_conectado.append(destino)

    """
    Función para revisar si un vertice esta conectado a otro.

    @param clave:   Identificador de vertice que se desea buscar.

    @return:        True o False si se encontro el vertice deseado en la lista_conectados
    """
    def existeConexion(self, clave):
        if clave in self.lista_conectado:
            return True
        else:
            return False

    """
    Función para eliminar un vertice de la lista_conectados.

    @param clave: Identificador de vertice que se desea eliminar.
    """
    def eliminarConexion(self, clave):
        self.lista_conectado.remove(clave)
        self.grado= self.grado- 1

    """
    Función para revisar el grado de un vertice.

    @return: Un Int que representa el grado del vertice.
    """
    def obtenerGrado(self):
        return self.grado

    """
    Función que restea el grado del vertice y vacia su lista_cinectado.
    """
    def vaciar(self):
        self.grado= 0
        self.lista_conectado= []


class Arista:
    """
    Constructor de la clase Arista.

    @param clave:   String que sirve como identificador de la arista.
    @param origen:  Identificador del vertice de donde comienza la arista.
    @param destino: Identificador del vertice donde termina la arista.
    @param peso:    Int o Float del peso que tiene la arista.
    """
    def __init__(self, clave, origen, destino, peso= 0):
        self.id = clave          #Identificador de la arista
        self.origen = origen     #Identificador del vertice donde empieza la arista
        self.destino = destino   #Identificador del vertice donde termina la arista
        self.peso = peso         #Peso de la arista

    """
    Sobrecargo de operador para imprimir la arista de la forma deseada.
    """
    def __str__(self):
        return str(self.id) + ' Origen: ' + str(self.origen) + ' Destino: ' + str(self.destino)

    """
    Destructor de la clase Arista.
    """
    def __del__(self):
        del self

class Grafica:
    """
    Contructor de la clase Grafica
    """
    def __init__(self):
        self.lista_vertices= {}     #Diccionario donde estan todos los vertices de la grafica
        self.lista_aristas= {}      #Diccionario donde estan todas las aristas de la grafica
        self.numero_aristas= 0      #Int que representa el número total de vertices en la grafica
        self.numero_vertices= 0     #Int que representa el número total de aristas en la grafica

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
    def agregarVertice(self, clave):
        if clave not in self.lista_vertices:                #Revisa si existe el vertice en la grafica
            self.numero_vertices= self.numero_vertices+ 1   #Sumamos uno al numereot total de vertices
            nuevo_vertice= Vertice(clave)                   #Creamos el vertice
            self.lista_vertices[clave]= nuevo_vertice       #Agrega el vertice al diccionario de vertices
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
    def agregarArista(self, clave, inicio, destino, peso= 0, dirigida=False):
        if (inicio in self.lista_vertices) and (destino in self.lista_vertices):        #Primero revisa que el vertice inicio y destino existan en la grafica
            nueva_arista= Arista(clave, inicio, destino, peso)                          #Si existe, entonces crea la arista, la agrega al diccionario de aristas
            self.numero_aristas= self.numero_aristas+ 1                                 #y suma uno al total de aristas
            self.lista_aristas[clave]= nueva_arista

            if inicio == destino:                                                       #Si es un lazo, entonces agrega el identificador del vertice
                self.lista_vertices[inicio].conectar(destino)                           #a la lista_conectados del vertice y suma un uno extra al grado del vertice
                self.lista_vertices[inicio].grado= self.lista_vertices[inicio].grado+ 1
            else:                                                                       #Si no es un lazo, entonces agrega el identificador del vertice destino a la
                self.lista_vertices[inicio].conectar(destino)                           #lista_conectado del vetice inicio y viceversa
                if not dirigida: self.lista_vertices[destino].conectar(inicio)

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
    def buscarArista(self, inicio, destino, dirigida=False):
        if (inicio in self.lista_vertices) and (destino in self.lista_vertices):    #Revisa si existen los vertices inicio y destino.Como las aristas aun no tienen
            for arista in self.lista_aristas:                                       #dirección, busca en ambas dirreciones. Si el inicio es destino o origen y viceversa.
                if (self.lista_aristas[arista].origen == inicio) and (self.lista_aristas[arista].destino == destino):
                    return self.lista_aristas[arista]

                if not dirigida:
                    if (self.lista_aristas[arista].origen == destino) and (self.lista_aristas[arista].destino == inicio):
                        return self.lista_aristas[arista]

            return None                                                             #Si no encontro la arista, regresa None
        else:                                                                       #Si no existe alguno de los vertices, regresa None
            return None


    """
    Función que copia la grafica.

    @return: La copia de la grafica.
    """
    def copiar(self):
        return copy.deepcopy(self)

    """
    Función para eliminar un vertice de la grafica.

    @param clave:   Identificador del vertice.

    @return:        True o False si se elimina el vertice o no.
    """
    def eliminarVertice(self, clave):
        if clave in self.lista_vertices:                                #Revisa que el vertice exista en la grafica
            for vertice in self.lista_vertices:
                if self.lista_vertices[vertice].existeConexion(clave):  #Primero busca en en el resto de los vertices si estan conectados al vertice que se quiere eliminar.
                    self.eliminarArista(vertice, clave)                 #Si lo esta, elimina ese vertice de su lista_conectado y la aristas.
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
    def eliminarArista(self, inicio, destino, dirigida=False):
        if (inicio in self.lista_vertices) and (destino in self.lista_vertices):            #Revisa si existen el vertice inicio y destino
            if self.lista_vertices[inicio].existeConexion(destino):                         #Si destino esta en lista_conectados de inicio
                if inicio == destino:                                                       #Entonces checa si es un lazo, si lo es, lo borra de lista_conectados
                    self.lista_vertices[inicio].eliminarConexion(destino)                   #y resta menos 1 al grado
                    self.lista_vertices[inicio].grado= self.lista_vertices[inicio].grado- 1
                else:                                                                       #Si no es un lazo, borra destino de lista_conectados de inicio u¿y viceversa
                    self.lista_vertices[inicio].eliminarConexion(destino)
                    if not dirigida: self.lista_vertices[destino].eliminarConexion(inicio)
                arista= self.buscarArista(inicio, destino, dirigida)                                  #Buscamos la arista en el diccionario de aristas para borrarla
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
            return self.lista_vertices[clave].obtenerGrado()    #Obtiene el grado del vertice y lo regresa
        else:                                                   #En caso de que el vertice no exista, regresa -1
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
            existe_arista= True
            while existe_arista:                                                    #Ciclo para eliminar todas las aristas relacionadas con el vertice
                for arista in self.lista_aristas:
                    if (self.lista_aristas[arista].origen == clave) or (self.lista_aristas[arista].destino == clave):#Buscamos la primera arista que este relacionado con el vertic
                        del self.lista_aristas[arista]                                                               #La eliminamos y restamos uno al total de aristas.
                    self.numero_aristas= self.numero_aristas- 1
                    break                                               #Se sale del ciclo for debido al cambio de tamaño del diccionario lista_aristas de la grafica
                if not self.existeArista(clave):                        #Si siguene existiendo aristas relacionados con el vertice. el ciclo continua
                    existe_arista= False                                #En caso contrario el ciclo termina

            for vertice in self.lista_vertices:                                 #Buscamos en los vertices de la grafica
                if self.lista_vertices[vertice].existeConexion(clave):          #Si el vertice a vaciar esta en lista_conectados de algun vertice
                    while clave in self.lista_vertices[vertice].lista_conectado:#Se elimina las veces que este el vertice
                        self.lista_vertices[vertice].eliminarConexion(clave)

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
            self.lista_vertices[vertice].peso_minimo= 0 #Y a la variable bandera

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
            if self.lista_vertices[u].existeConexion(u):#Si hay un lazo, entonces regresa False
                return False

            for vertice in self.lista_vertices[u].lista_conectado:                        #Buscamos en los vertices a los que esta coenctado "u"
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
                    return (lista_u, lista_u, False)                                #Regresa False y el algorimo concluye
            if self.lista_vertices[vertice].color== 1:          #Si el vertice es de color 1 lo agrega a lista_v
                lista_v.append(self.lista_vertices[vertice].id)
            elif self.lista_vertices[vertice].color== 0:        #Si el vertice es de color 0 lo agrega a lista_ui
                lista_u.append(self.lista_vertices[vertice].id)
            self.lista_vertices[vertice].bandera= 1             #Asigna bandera a 1 lo que significa que el vertice ya fue visitado

        '''
        print("\nEs bipartita")                                   #Si el algorimo llego hasta aqui, significa que la grafica es bipartita
        print("V: %s"%(lista_v))                                #Imprime las listas u y v. Restablece los vertices y regresa True
        print("U: %s"%(lista_u))
        '''
        self.restablecerVertices()
        return (lista_u, lista_u, True)

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
            for vertice in self.lista_vertices[u].lista_conectado:
                if self.lista_vertices[vertice].bandera== 0:
                    cola.append(vertice)
                    self.lista_vertices[vertice].bandera= 1
                    num_banderas+= 1

        if num_banderas == self.numero_vertices:
            self.restablecerVertices()
            return True
        else:
            self.restablecerVertices()
            return False
    """
    Función que emplea el algoritmo de Fleury
    """
    def algoritmoFleury(self):
        impares = 0
        inicio = self.lista_vertices[list(self.lista_vertices.keys())[0]]
        copia = self.copiar()
        cola = []
        cola_vertices = []

        for vertice in self.lista_vertices:
            if (self.lista_vertices[vertice].grado % 2) != 0:
                impares = impares + 1
                inicio = self.lista_vertices[vertice]

        if impares != 0 and impares != 2:
            print("Error: La cantidad de nodos de grado impar no cumple.")
            return False

        if not self.conexa():
            print("Error: La grafica no es conexa.")
            return False

        while copia.numero_aristas != 0:
            for vecino in copia.lista_vertices[inicio.id].lista_conectado:
                destino = vecino
                arista = copia.buscarArista(inicio.id, vecino)
                cola.append(arista)
                cola_vertices.append(inicio)
                aux = copia.copiar()
                aux.eliminarArista(inicio.id, vecino)
                if len(copia.lista_vertices[inicio.id].lista_conectado) == 1:
                    copia.eliminarArista(inicio.id, vecino)
                    copia.eliminarVertice(inicio.id)
                    inicio = copia.buscarVertice(destino)
                    break
                elif aux.conexa():
                    copia.eliminarArista(inicio.id, vecino)
                    inicio = copia.buscarVertice(destino)
                    break
                else:
                    cola.pop(-1)
                    cola_vertices.pop(-1)

        if impares == 0:
            print("El paseo de Euler es cerrado.")
        else:
            print("El paseo de Euler es abierto.")

        cola_vertices.append(inicio)
        camino = []
        while cola_vertices:
            v = cola_vertices.pop()
            camino.append(v.id)
            if cola:
                a = cola.pop()
                camino.append(a.id)
        print(camino)
        del copia
        del aux
        return True

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
            if (copia.lista_vertices[vertice].grado % 2) != 0:      #Buscamos la cantidad de verices impares.
                impares= impares + 1
                if impares== 1:
                    cola.append(copia.lista_vertices[vertice].id)   #Si hay un vertice con grado impar, asignamos nuesto vc(vertice cola) y lo guardamos en la cola
                    vc= copia.lista_vertices[vertice]
                if impares== 2:
                    pila.append(copia.lista_vertices[vertice].id)   #Si hay 2 vertices con grado impar, asignamos nuesto vp(vertice pila) y lo guardamos en la pila
                    vp= copia.lista_vertices[vertice]

        if impares != 0 and impares != 2:   #Si en la grafica no hay 0 o 2 vertices con grado impar, entonces no se cumple el algoritmo.
            print("\nError: La cantidad de nodos de grado impar no cumple.")
            return (cola, impares, False)

        if not copia.conexa():              #Si la grafica no es conexa, no se cumple el algoritmo
            print("\nError: La grafica no es conexa.")
            return (cola, impares, False)


        if impares== 0:                                                                 #Si no hay ningun vertice de grado impar, vc y vp se asignan a cualquier vertice
            cola.append(copia.lista_vertices[list(copia.lista_vertices.keys())[0]].id)  #En este caso al primero de la grafica
            pila.append(copia.lista_vertices[list(copia.lista_vertices.keys())[0]].id)  #Se agregan a la pila y cola
            vc= copia.lista_vertices[list(copia.lista_vertices.keys())[0]]
            vp= vc

        while vc.grado != 0 and vp.grado != 0:
            for vertice in copia.lista_vertices[vc.id].lista_conectado:
                if copia.lista_vertices[vertice].grado != 1:
                    cola.append(copia.lista_vertices[vertice].id)
                    copia.eliminarArista(vc.id, vertice)
                    vc= copia.lista_vertices[vertice]
                    break
            if vp.grado == 1:
                vecino= copia.lista_vertices[vp.id].lista_conectado[0]
                copia.eliminarArista(vp.id, vecino)
                aux= copia.buscarVertice(vecino)
                pila.append(copia.lista_vertices[aux.id].id)
                vp= copia.lista_vertices[aux.id]
        pila= pila[:-1]

        del copia
        while pila:
            cola.append(pila[-1])
            pila= pila[:-1]
        '''
        if impares == 0:
            print("\nEl paseo de Euler es cerrado.")

        else:
            print("\nEl paseo de Euler es abierto.")
        print(cola)
        '''
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

            if tipo == 0: #Busqueda a lo profundo (0)
                cont = 0
                for vertice in self.lista_vertices[v.id].lista_conectado:
                    if (self.lista_vertices[vertice].bandera == 0):
                        break
                    cont += 1
                if cont == len(self.lista_vertices[v.id].lista_conectado):
                    v.bandera = 1
                    v = frontera[-1]
                    frontera = frontera[:-1]

            elif tipo== 1: #Busqueda a los ancho (1)
                v = frontera[0]
                frontera= frontera[1:]

            v.bandera = 1
            grafiquita.agregarVertice(v.id)

            for vertice in self.lista_vertices[v.id].lista_conectado:
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

        '''
        if bosque:
            print("\nEl bosque es:")
        else:
            print("\nEl árbol de expansión es:")

        for v in grafiquita:
            print(v)
        '''
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
        peso_total= 0                                               #Peso total del árbol o bosque
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
                peso_total += arista.peso                                                           #Sumamos el peso de la arista al peso total del árbol
            if  grafiquita.numero_aristas == total_vertices - 1:            #Si el número total de aristas es igual al el numero de vertices menos uno, entonces ya tenemos el arbol de expansion
                break


        if grafiquita.numero_aristas is not total_vertices - 1:            #Si la cantidad de aristas no cumple con ser #vertices-1, entonces debe ser un bosque.
            bosque = True
        '''

        if bosque:                                          #Imprimimos el arbol o bosque
            print("\nEl bosque es: ")
        else:
            print("\nEl árbol de mínima expansión es: ")
        for v in grafiquita:
            print(v)

        if bosque:                                      #Imprimimos el peso total del arbol o bosque
            print("\nPeso del bosque: ", peso_total)
        else:
            print("\nPeso del árbol: ", peso_total)
        '''

        return (grafiquita, peso_total, bosque)

    def prim(self):
        grafiquita = Grafica()
        lista_actuales = []
        lista_actuales.append(self.lista_vertices[list(self.lista_vertices.keys())[0]])
        lista_actuales[0].bandera = 1
        visitados = 1
        bosque = False
        peso_total = 0

        for vertice in self.lista_vertices:                     # Copiamos los vertices de la grafica original en lo que sera nuestro
            grafiquita.agregarVertice(vertice)                  # árbol de minima expansion o bosque.

        while(visitados < grafiquita.numero_vertices):
            lista_vecinos = []

            for vertice in lista_actuales:
                for vecino in self.lista_vertices[vertice.id].lista_conectado:

                    if self.lista_vertices[vecino].bandera == 0:
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

            min = pesoMinimo(lista_vecinos)

            grafiquita.agregarArista(min.id, min.origen, min.destino, min.peso)
            peso_total += min.peso

            # Solo uno tiene bandera = 0
            if self.lista_vertices[min.origen].bandera == 0:
                self.lista_vertices[min.origen].bandera = 1
                lista_actuales.append(self.lista_vertices[min.origen])

            elif self.lista_vertices[min.destino].bandera == 0:
                self.lista_vertices[min.destino].bandera = 1
                lista_actuales.append(self.lista_vertices[min.destino])

            visitados += 1

        #Imprimimos el árbol o bosque
        '''
        if bosque:
            print("\nEl bosque es: ")
        else:
            print("\nEl árbol de mínima expansión es: ")

        for v in grafiquita:
            print(v)

        # Imprimimos el peso total del arbol o bosque
        if bosque:
            print("\nPeso del bosque: ", peso_total)
        else:
            print("\nPeso del árbol: ", peso_total)

        del grafiquita
        '''

        self.restablecerVertices()
        return (grafiquita, peso_total, bosque)


    def dijkstra(self, inicio):
        assert inicio in self.lista_vertices
        grafiquita = Grafica()
        cola = []

        # Copiamos los vertices de la grafica original
        for vertice in self.lista_vertices:
            grafiquita.agregarVertice(vertice)

        # Primer paso del algoritmo de Dijkstra
        cola.append(inicio)                                   # Guardamos etiquetas de vértices
        grafiquita.lista_vertices[inicio].bandera = 1         # 1 es marca temporal, 2 marca definitiva
        grafiquita.lista_vertices[inicio].padre = None        # Padre es None
        grafiquita.lista_vertices[inicio].peso_minimo = 0
        while cola:
            actual = cola[0]                                  # Obtenemos el primer elemento de la cola
            cola = cola[1:]                                   # y lo borramos de la cola y le ponemos
            grafiquita.lista_vertices[actual].bandera = 2     # la marca definitiva

            for vertice in self.lista_vertices[actual].lista_conectado:
                 arista = self.buscarArista(actual, vertice, True)
                 v = grafiquita.lista_vertices[vertice]

                 if v.bandera == 0:
                     grafiquita.agregarArista(arista.id, actual, vertice, arista.peso, True)
                     v.bandera = 1
                     v.padre = actual
                     v.peso_minimo = grafiquita.lista_vertices[actual].peso_minimo + arista.peso
                     cola.append(vertice)

                 elif v.bandera == 1:
                     if v.peso_minimo > grafiquita.lista_vertices[actual].peso_minimo + arista.peso:

                         grafiquita.eliminarArista(v.padre, vertice, True)
                         v.peso_minimo = grafiquita.lista_vertices[actual].peso_minimo + arista.peso
                         v.padre = actual
                         grafiquita.agregarArista(arista.id, actual, vertice, arista.peso, True)

            cola = sortear(grafiquita.lista_vertices, cola)

        return grafiquita

    def dijkstraGeneral(self, inicio):
        aristas = []
        ciclo = []
        grafiquita = self.dijkstra(inicio)

        for arista in self.lista_aristas:
            if arista not in grafiquita.lista_aristas:
                aristas.append(self.lista_aristas[arista])

        aristas.sort(key=attrgetter('peso'))
        while True:
            fin = True
            for a in aristas:
                if grafiquita.lista_vertices[a.origen].peso_minimo + a.peso < grafiquita.lista_vertices[a.destino].peso_minimo:
                    if grafiquita.lista_vertices[a.destino].padre is None:
                        grafiquita.lista_vertices[a.origen].padre = None
                    # Identificación de ciclos
                    ciclo.append(a.origen)
                    ancestro = grafiquita.lista_vertices[a.origen].padre
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

                        ancestro = grafiquita.lista_vertices[ancestro].padre

                    fin = False

                    auxrista = self.buscarArista(grafiquita.lista_vertices[a.destino].padre, a.destino, True)

                    grafiquita.eliminarArista(grafiquita.lista_vertices[a.destino].padre, a.destino, True)
                    grafiquita.agregarArista(a.id, a.origen, a.destino, a.peso, True)

                    delta = grafiquita.lista_vertices[a.destino].peso_minimo - (grafiquita.lista_vertices[a.origen].peso_minimo + a.peso)
                    grafiquita.lista_vertices[a.destino].peso_minimo = grafiquita.lista_vertices[a.origen].peso_minimo + a.peso
                    grafiquita.lista_vertices[a.destino].padre = a.origen

                    frontera = []
                    frontera.append(grafiquita.lista_vertices[a.destino])
                    aristas.remove(a)

                    v = frontera[0]
                    frontera = frontera[1:]

                    v.bandera = 1

                    for vertice in grafiquita.lista_vertices[v.id].lista_conectado:
                        if (grafiquita.lista_vertices[vertice] not in frontera) and (grafiquita.lista_vertices[vertice].bandera == 2):

                            frontera.append(grafiquita.lista_vertices[vertice])

                    while frontera:
                        v = frontera[0]
                        frontera = frontera[1:]
                        v.bandera = 1
                        grafiquita.lista_vertices[v.id].peso_minimo -= delta

                        for vertice in grafiquita.lista_vertices[v.id].lista_conectado:
                            if (grafiquita.lista_vertices[vertice] not in frontera) and (grafiquita.lista_vertices[vertice].bandera == 2):

                                frontera.append(grafiquita.lista_vertices[vertice])

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
                arista = self.buscarArista(nombres[i], nombres[j], True)
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
                    #if(c == i or c == j):
                        #continue
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
                distancia_aux= 0
                if (aux == i):
                    ruta_aux.append(nombres[aux])
                    distancia_aux += distancias[aux + i*total_vertices]
                while(aux != i):
                    if(rutas[j + i * total_vertices] is None):
                        break
                    ruta_aux.append(nombres[aux])
                    distancia_aux += distancias[aux + i*total_vertices]
                    aux = nombres.index(rutas[aux + i * total_vertices])
                    if (aux == i):
                        ruta_aux.append(nombres[aux])
                        distancia_aux += distancias[aux + i*total_vertices]

                ruta_aux.reverse()
                free4all[j + i * total_vertices] = (ruta_aux, distancia_aux)
                        
        return (free4all, nombres, False)
        

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
