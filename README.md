# adivina-numero-inteligente
Adivina el Numero - Sistema Inteligente
Descripcion
Sistema que utiliza algoritmos de busqueda binaria para adivinar numeros secretos con maxima eficiencia matematica (O(log n)). Desarrollado como proyecto final de lógica de programacion.


Caracteristicas Principales

-Menú interactivo con navegacion intuitiva
-4 niveles de dificultad configurable (facil, normal, dificil, experto)
-Sistema de estadisticas con calculo de eficiencia
-Reinicio automatico para multiples partidas
-Validacion de entradas del usuario


Arquitectura del Sistema

SISTEMA ADIVINA EL NUMERO
- Interfaz de Usuario (interfaz.py)
- Logica del Juego (juego.py) - Algoritmo de busqueda binaria
- Configuracion (config.py) - Gestion de dificultad y estadisticas
- Utilidades (utils.py) - Funciones auxiliares
- Control Principal (main.py) - Coordinacion del sistema


Estructura del Proyecto

adivina-numero-inteligente/
- src/                 # Codigo fuente
- main.py              # Punto de entrada principal
- juego.py             # Implementacion del algoritmo
- interfaz.py          # Interaccion con el usuario
- config.py            # Configuracion y estadisticas
- utils.py             # Utilidades del sistema
- docs/diagramas/      # Documentacion visual (10 diagramas)
- requirements.txt     # Dependencias (Python 2.7)
- LICENSE              # Licencia MIT
- README.md            # Este archivo


Instalacion y Ejecucion

Requisitos
Python 2.7.16 o superior (desarrollado y probado en 2.7.16)

Git (para clonar el repositorio)

Pasos para Ejecutar

1-Clonar el repositorio
git clone https://github.com/brittanysedamanos/adivina-numero-inteligente.git

2-Navegar al directorio
cd adivina-numero-inteligente/src

3-Ejecutar (Python 2.7)
python main.py
Algoritmo Implementado
Busqueda Binaria:

Complejidad: O(log n)

-Para 100 numeros: maximo 7 intentos
-Estrategia: "divide y venceras"
-Siempre elige el punto medio del rango actual


Unidades de Programacion Implementadas
-Variables y operadores - Gestion de rangos y calculos
-Estructuras condicionales - Menus y validaciones
-Estructuras repetitivas - Ciclo principal del juego
-Funciones y modulos - Arquitectura modular profesional


Documentacion Visual
-El proyecto incluye 10 diagramas en la carpeta docs/diagramas/:
-4 diagramas de flujo del sistema
-6 capturas del sistema funcionando
-Vista completa del algoritmo y flujo del juego


Compatibilidad

Desarrollado en: Python 2.7.16
Razon: Compatibilidad con sistemas educativos legacy
Adaptaciones: raw_input(), math.log()/math.log(2), sin f-strings


Estudiante
Nombre: Brittany Jhulisa Sedamanos Leon
Curso: Lógica de programación 1CIB-1A
Fecha: 17 de diciembre de 2025
Universidad: Universidad Internacional del Ecuador

Contacto
GitHub: @brittanysedamanos

Licencia
Este proyecto esta bajo la Licencia MIT. Ver archivo LICENSE para mas detalles.