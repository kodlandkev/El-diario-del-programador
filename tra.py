import csv

def crear_diccionario(archivo):
    """Crea un diccionario a partir de un archivo CSV."""
    diccionario = {}
    with open(archivo, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        for row in reader:
            espanol, ingles = row
            diccionario[espanol] = ingles
    return diccionario

def traducir(palabra, diccionario):
    """Traduce una palabra."""
    return diccionario.get(palabra, "Palabra no encontrada")


if __name__ == "__main__":
    mi_diccionario = crear_diccionario("en-es.csv")

    while True:
        opcion = input("1. Traducir\n2. Agregar palabra\n3. Salir\n")
        if opcion == "1":
            palabra = input("Ingrese la palabra a traducir: ")
            traduccion = traducir(palabra, mi_diccionario)
            print(traduccion)
        else:
            print("Opción inválida")