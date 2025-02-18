import json
import random

def cargar_cartas(nombre_archivo="data/cards.json"):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def carta_aleatoria(cartas):
    return random.choice(cartas)
