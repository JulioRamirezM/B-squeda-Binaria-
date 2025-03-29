# -*- coding: utf-8 -*-
"""
Created on Sat Mar 29 16:04:02 2025

@author: julio
"""

import random

def busqueda_binaria(lista, elemento):
    """
    Implementación de búsqueda binaria iterativa.
    Argumentos:
        lista: Lista ordenada de elementos.
        elemento: Elemento a buscar en la lista.
    Returns:
        True si el elemento está en la lista, False si no.
    """
    izquierda = 0
    derecha = len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == elemento:
            return True
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return False

def generar_lista_aleatoria(tamaño, rango_min, rango_max):
    """
    Genera una lista de números aleatorios.
    Argumentos:
        tamaño: Cantidad de elementos en la lista.
        rango_min: Valor mínimo para los números aleatorios.
        rango_max: Valor máximo para los números aleatorios.
    Returns:
        Lista de números aleatorios.
    """
    return [random.randint(rango_min, rango_max) for _ in range(tamaño)]

def main():
    print("PROGRAMA DE BÚSQUEDA BINARIA")
    
    # Entrada de datos
    tamaño = int(input("Ingresa el tamaño de la lista: "))
    rango_min = int(input("Ingresa el valor mínimo para los números aleatorios: "))
    rango_max = int(input("Ingresa el valor máximo para los números aleatorios: "))
    
    # Generar lista aleatoria
    lista_original = generar_lista_aleatoria(tamaño, rango_min, rango_max)
    lista_ordenada = sorted(lista_original)
    
    # Mostrar listas
    print("\nLISTAS GENERADAS")
    print(f"Lista original (desordenada): {lista_original}")
    print(f"Lista ordenada: {lista_ordenada}")
    
    # Bucle para múltiples búsquedas
    while True:
        # Pedir elemento a buscar
        elemento = int(input("\nIngresa el elemento que deseas buscar: "))
        
        # Realizar búsqueda
        encontrado = busqueda_binaria(lista_ordenada, elemento)
        
        # Mostrar resultados
        print("\nRESULTADOS")
        print(f"Elemento buscado: {elemento}")
        if encontrado:
            print(f"El elemento {elemento} SÍ está en la lista.")
        else:
            print(f"El elemento {elemento} NO está en la lista.")
        
        # Preguntar si desea continuar
        continuar = input("\n¿Deseas buscar otro elemento? (s/n): ").lower()
        if continuar != 's':
            print("\n¡Gracias por usar el programa!")
            break

if __name__ == "__main__":
    main()