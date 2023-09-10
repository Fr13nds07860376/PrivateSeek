# How to Perform a Google Search using python code By FR13NDS 

from googlesearch import search
import requests

# Banner de la herramienta
banner = """
*******************************
*                             *
*   PrivateSeek               *
*                             *
*******************************
"""

# Imprimir el banner
print(banner)



# Lista de palabras clave para filtrar los resultados
palabras_clave = ["top secret", "classified", "desclasificados", "confidential", "UAP", "OVNIS", "extraterrestrial", "pdf", "doc", "photos", "videos", "leaked", "technology"]

google_query = str(input("Please, enter your Google search term: "))

for i in search(google_query, start=0, pause=2):
    print(i)

search_query = "UAP OVNIS"
url = f"https://www.google.com/search?q={search_query}"
response = requests.get(url)

def realizar_busqueda_filtrada(palabras_clave, max_resultados):
    # Implementa la lógica de búsqueda y filtrado aquí
    pass

resultados = realizar_busqueda_filtrada(palabras_clave, 5)  # Obtener 5 resultados filtrados

for resultado in resultados:
    title = resultado.find("h3").get_text()  # Obtener el título del resultado
    description = resultado.find("span", class_="aCOpRe").get_text()  # Obtener la descripción del resultado

    if "UAP" in title.lower() or "UAP" in description.lower():
        # El resultado contiene la palabra clave "OVNIS" "UFO" "UAP" "Ultra secreto" "Secreto" "Confidencial" "desclasificados"
        print(title)
        print(description)
        print()

