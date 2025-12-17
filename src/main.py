# -*- coding: utf-8 -*-
"""
PROYECTO: ADIVINA EL NUMERO - SISTEMA INTELIGENTE
AUTOR: [Tu Nombre]
FECHA: [Fecha]
DESCRIPCION: Sistema que usa busqueda binaria para adivinar numeros
"""

# Importar modulos
import juego
import interfaz

def main():
    """Funcion principal del programa."""
    
    # Mostrar bienvenida y obtener nombre
    nombre_jugador = interfaz.mostrar_bienvenida()
    
    # Crear instancia del juego
    juego_actual = juego.JuegoAdivinanza(nombre_jugador)
    
    # Iniciar el juego
    juego_actual.iniciar()
    
    # Mostrar despedida
    interfaz.mostrar_despedida(nombre_jugador, juego_actual.intentos)
    
    # Pausa final
    input("\nPresiona ENTER para salir del juego...")

# Punto de entrada del programa
if __name__ == "__main__":
    main()
