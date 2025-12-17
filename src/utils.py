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
        print("\n" * 50)  # 50 lineas nuevas si no se detecta

def pausar():
    """Pausa la ejecucion hasta que el usuario presione ENTER."""
    raw_input("\nPresiona ENTER para continuar...")
    