from flask import Flask, render_template, request
import forms
from config import DevelopmentConfig
from grafica import Grafica

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
g= Grafica()

@app.route('/', methods= ['GET', 'POST'])
def index():
    añadir_vertice= forms.AñadirVertice(request.form)
    if(request.method == 'POST'):
        g.agregarVertice(añadir_vertice.id_vertice.data)
        print(añadir_vertice.id_vertice.data)
    title= "Prueba de Interfaz"
    vertices = []
    for key, data in g.lista_vertices.items():
        vertices.append(key)

    return render_template('index.html', title= title, form= añadir_vertice, grafica= g, vertices=vertices)

if __name__ == '__main__':
    app.run()
