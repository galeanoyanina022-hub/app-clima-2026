# leHacer un programaque le pida una ciudad al usuario, busque el clima en internet y muestre: temperatura, humedad, clima

import requests # Importamos requests para conectarnos a la API

historial = [] # Historial de búsquedas (se guarda mientras el programa está abierto)

favoritos = [] # Lista de favoritos

def consultar_clima(ciudad): # Función que consulta el clima

    ciudad = ciudad.title()

    if ciudad not in historial:

        historial.append(ciudad) # Agregamos la ciudad al historial

    api_key = "f29f1337d56a610d0fc5198e8ba14903" # Mi API key

    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es" # URL de la API

    respuesta = requests.get(url) # Hacemos la petición a internet

    if respuesta.status_code == 200: # Verificamos si salió bien

        datos = respuesta.json()

        # Extraemos datos principales
        temperatura = datos["main"]["temp"]
        humedad = datos["main"]["humidity"]
        clima = datos["weather"][0]["description"]
        # ICONO SEGÚN CLIMA
        # FONDO SEGÚN EL CLIMA

        # 🌧️ LLUVIA
        # con esto la app reconoce tormenta, nieve, niebla, nubes, sol

        if "lluv" in clima or "rain" in clima:

            tipo_clima = "lluvia"
            icono = "🌧️"

        # ☀️ SOLEADO
        elif "despejado" in clima or "clear" in clima:

            icono_api = datos["weather"][0]["icon"]

            # 🌙 si es de noche
            if "n" in icono_api:

                tipo_clima = "noche"
                icono = "🌙"

            else:

                tipo_clima = "soleado"
                icono = "☀️"

        # ⛈️ TORMENTA
        elif "torment" in clima or "storm" in clima:

            tipo_clima = "lluvia"
            icono = "⛈️"

        # 🌫️ NIEBLA
        elif "niebla" in clima or "mist" in clima or "fog" in clima:

            tipo_clima = "nublado"
            icono = "🌫️"

        # ❄️ NIEVE
        elif "snow" in clima or "nieve" in clima:

            tipo_clima = "nieve"
            icono = "❄️"

        # ☁️ NUBLADO
        elif "nube" in clima or "cloud" in clima:

            tipo_clima = "nublado"
            icono = "☁️"

        # 🌡️ DEFAULT
        else:

            tipo_clima = "normal"
            icono = "🌡️"

        # Devolvemos todo a Flask

        return {
            "ciudad": ciudad,
            "temperatura": temperatura,
            "humedad": humedad,
            "clima": clima,
            "icono": icono,
            "tipo_clima": tipo_clima,
            "historial": historial,
            "favoritos": favoritos
        }

    else: # Si falla la API entonces retorna:

        return {
            "error": "⚠️ No se encontró la ciudad o hubo un problema con la conexión",
            "tipo_clima": "normal",
            "historial": historial,
            "favoritos": favoritos,
        }

# Agregar a Favoritos

def agregar_favorito(ciudad): # Función para agregar favoritos
    if ciudad not in favoritos: # Evita duplicados
        favoritos.append(ciudad)
# ❌ Eliminar favorito

def eliminar_favorito(ciudad):

    if ciudad in favoritos:
        favoritos.remove(ciudad)

# ❌ Eliminar historial

def eliminar_historial(ciudad):

    if ciudad in historial:
        historial.remove(ciudad)
