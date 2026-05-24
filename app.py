# Importamos Flask para crear la aplicación web
from flask import Flask, render_template, request # render_template sirve para mostrar archivos HTML # request sirve para leer datos que envía el usuario desde la página
from clima import historial, favoritos
from clima import (
    consultar_clima,
    agregar_favorito,
    eliminar_favorito,
    eliminar_historial
)

app = Flask(__name__) # Creamos la aplicación Flask

# PÁGINA PRINCIPAL

@app.route("/") # Esta sería la ruta principal
def inicio():

    return render_template("index.html") # Muestra la página HTML inicial (index.html)

# RUTA PARA BUSCAR CLIMA

@app.route("/clima", methods=["GET", "POST"])
def clima():

    ciudad = request.form["ciudad"].strip() # Obtenemos la ciudad que el usuario escribió en el formulario HTML

    if not ciudad:
        return render_template(
            "index.html",
            resultado={
                "error": "Escribe una ciudad válida",
                "tipo_clima": "normal",
                "historial": historial,
                "favoritos": favoritos
            }
        )

    resultado = consultar_clima(ciudad) # Llamamos a la función que consulta el clima en la API

    return render_template("index.html", resultado=resultado) # Enviamos el resultado al HTML para mostrarlo en pantalla

# RUTA PARA AGREGAR FAVORITOS

@app.route("/favorito", methods=["POST"])
def favorito():

    ciudad = request.form["ciudad"].strip()

    if not ciudad:
        return render_template(
            "index.html",
            resultado={
                "error": "Escribe una ciudad válida",
                "tipo_clima": "normal",
                "historial": historial,
                "favoritos": favoritos
            }
        )

    agregar_favorito(ciudad) # La agregamos a la lista de favoritos (en clima.py)

    resultado = consultar_clima(ciudad) # Volvemos a consultar el clima para mostrar datos actualizados

    return render_template("index.html", resultado=resultado) # Mostramos nuevamente la página con datos

@app.route("/eliminar-favorito/<ciudad>")
def borrar_favorito(ciudad):

    eliminar_favorito(ciudad)

    return render_template(
        "index.html",
        resultado={
            "historial": historial,
            "favoritos": favoritos,
            "tipo_clima": "normal"
        }
    )

@app.route("/eliminar-historial/<ciudad>")
def borrar_historial(ciudad):

    eliminar_historial(ciudad)

    return render_template(
        "index.html",
        resultado={
            "historial": historial,
            "favoritos": favoritos,
            "tipo_clima": "normal"
        }
    )

@app.route("/buscar/<ciudad>")
def buscar(ciudad):

    ciudad = ciudad.strip()

    resultado = consultar_clima(ciudad)

    return render_template("index.html", resultado=resultado)

# EJECUTAR EL SERVIDOR WEB

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0") # debug=True permite ver cambios sin reiniciar y muestra errores en pantalla

