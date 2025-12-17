# -*- coding: utf-8 -*-
"""
MODULO: Interfaz de usuario
"""

def mostrar_bienvenida():
    print("=" * 50)
    print("        ADIVINA EL NUMERO - JUEGO INTELIGENTE")
    print("=" * 50)
    print("\nBIENVENIDO AL SISTEMA DE ADIVINANZAS MATEMATICAS")
    print("La computadora usara busqueda binaria para ganar.")
    
    nombre = ""
    while not nombre:
        nombre = input("\nIngresa tu nombre: ").strip()
        if not nombre:
            print("El nombre no puede estar vacio.")
    
    return nombre

def mostrar_despedida(nombre, intentos):
    print("\n" + "=" * 50)
    print("            FIN DEL JUEGO")
    print("=" * 50)
    print("\nGracias por jugar, " + nombre + "!")
    print("Total de intentos: " + str(intentos))
    
    if intentos <= 7:
        print("Eficiencia: ALTA (algoritmo funciono bien)")
    else:
        print("Eficiencia: MEDIA (¿hubo cambios de numero?)")
    
    print("\n" + "=" * 50)