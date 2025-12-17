# -*- coding: utf-8 -*-
"""
Utilidades del sistema
"""

import os
import platform

def limpiar_pantalla():
    """Limpia la pantalla segun el sistema operativo."""
    if platform.system() == "Darwin" or platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    else:
        print("\n" * 50)

def pausar():
    """Pausa la ejecucion."""
    raw_input("\nPresiona ENTER para continuar...")
