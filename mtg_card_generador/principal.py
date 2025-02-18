from generador import cargar_cartas, carta_aleatoria
from formato import mostrar_carta


if __name__ == "__main__":
    cartas = cargar_cartas()
    carta_seleccionada = carta_aleatoria(cartas)
    mostrar_carta(carta_seleccionada)
