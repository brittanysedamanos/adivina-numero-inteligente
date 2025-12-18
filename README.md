# adivina-numero-inteligente
Adivina el Numero - Sistema Inteligente


Estudiante

Nombre: Brittany Jhulisa Sedamanos Leon

Curso: Lógica de programación 1CIB-1A

Fecha: 17 de diciembre de 2025

Universidad: Universidad Internacional del Ecuador

Caracteristicas Principales

-Menú interactivo con navegacion intuitiva
-4 niveles de dificultad configurable (facil, normal, dificil, experto)
-Sistema de estadisticas con calculo de eficiencia
-Reinicio automatico para multiples partidas
-Validacion de entradas del usuario


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


Compatibilidad

Desarrollado en: Python 2.7.16
Razon: Compatibilidad con sistemas educativos legacy



Descripcion
Sistema que utiliza algoritmos de busqueda binaria para adivinar numeros secretos con maxima eficiencia matematica (O(log n)). Desarrollado como proyecto final de lógica de programacion.



INTERFAZ GRÁFICA

¿Por qué Tkinter?
Pensamos mucho en la herramienta para la interfaz gráfica. Elegimos Tkinter por una razón principal: simplicidad con propósito.

Era la opción que venía lista para usar con Python 2.7. Esto nos ahorró dolores de cabeza con instalaciones complicadas en los computadores del laboratorio. Otras herramientas como PyQt eran más poderosas pero también más difíciles de aprender y hacer funcionar.

Tkinter nos dio justo lo que necesitábamos: una forma de crear ventanas, botones y menús para hacer el juego visual sin volvernos locos con la complejidad. Su manera de trabajar con "eventos" (como un clic en un botón) encajaba perfecto con la lógica de nuestro juego donde el usuario siempre está tomando decisiones.



BUCLES

Los bucles son lo que mantiene vivo el programa. Usamos dos tipos principales y cada uno tenía su trabajo.

En el archivo juego.py usamos un bucle while. ¿Por qué? Por que no sabíamos cuántas veces se repetiría. El bucle sigue funcionando mientras el juego esté activo y no se hayan gastado todos los intentos. Es el corazón del algoritmo que sigue preguntando "¿es este tu número?" una y otra vez hasta encontrar la respuesta.

En los archivos de la interfaz gráfica (adivina_gui.py e interfaz_gui.py) usamos muchos bucles for. Su misión era diferente. Aquí sabíamos exactamente qué crear: cinco botones para el menú, diez filas para la tabla de estadísticas. El bucle for recorría una lista de instrucciones y creaba cada elemento uno por uno esto hizo nuestro código más ordenado.

En el main.py original usamos un bucle while para el menú y otro patrón inteligente: un bucle infinito con while True que solo se detenía cuando el usuario daba una respuesta válida. Esto le enseñaba paciencia al programa. Si el usuario escribía una letra donde iba un número el bucle no se rendía. Simplemente mostraba un mensaje amigable y volvía a preguntar. Una lección importante en tratar bien a quien usa tu programa.



DICCIONARIOS, LISTAS Y TUPLAS

Elegir cómo guardar los datos fue clave para un código entendible.

Usamos diccionarios para la configuración. Eran perfectos porque podíamos acceder a los valores con nombres claros como config dificultar o config max_valor. además cuando guardábamos todo en un archivo JSON era como si el diccionario se transformara directamente.

Las listas fueron nuestras aliadas para cosas en secuencia. El historial de intentos de una partida es una lista porque el orden importa: el primer intento,segundo, etc. También usamos una lista para definir todos los botones del menú principal. Esto nos evitó tener un código repetitivo y largo.

Las tuplas las reservamos para lo que no debería cambiar. Definir los niveles de dificultad fue el caso perfecto. Una tupla como ("FÁCIL", 1, 50) es una constante, no se modifica. Nos dio tranquilidad saber que esos valores base estaban protegidos de cambios accidentales.

Pensamos en otras estructuras pero no las usamos. Los conjuntos (sets) no hacían falta porque nunca tuvimos que buscar elementos únicos de forma complicada. Las colas podrían haber sido un poco más eficientes para el historial pero nuestro programa era tan pequeño que la ganancia no valía la pena. Preferimos la claridad a la optimización innecesaria.



ARQUITECTURA

La decisión más inteligente que tomamos fue separar el código en módulos con responsabilidades claras.

Pusimos toda la lógica pura del algoritmo de búsqueda binaria en juego.py. La interfaz de texto fue a interfaz.py y la interfaz gráfica a interfaz_gui.py. Los programas principales main.py y adivina_gui.py se convirtieron en directores de orquesta que unían estas partes.

Esta separación nos dio un superpoder: podíamos cambiar una parte sin romper las otras. ¿Queríamos una nueva pantalla de ayuda gráfica? Solo trabajábamos en interfaz_gui.py. ¿El algoritmo necesitaba un ajuste? Lo hacíamos en juego.py con la seguridad de que ambas versiones del juego (la de consola y la gráfica) se beneficiarían. Hizo el código más fácil de leer, de probar y de explicar.



CONCLUSIONES

Este proyecto fue un ejercicio de elección apropiada. No buscamos usar la herramienta más compleja sino la correcta para cada tarea.
Elegimos Tkinter porque era la opción más práctica y compatible para nuestro entorno. Nos permitió construir una interfaz funcional sin complicaciones técnicas innecesarias.
Los bucles fueron la herramienta fundamental para manejar la interactividad del programa. El bucle while en el núcleo del juego manejó la lógica repetitiva de adivinar, mientras que los bucles for nos ayudaron a construir la interfaz de manera ordenada y eficiente, evitando código repetitivo.
Las estructuras de datos como diccionarios, listas y tuplas nos permitieron organizar la información del juego de forma lógica y accesible. Cada una cumplió un rol específico según cómo necesitábamos acceder y modificar los datos.

Finalmente, la arquitectura fue la decisión de diseño más importante. Separar la lógica del juego, la interfaz y el control nos dio flexibilidad para desarrollar ambas versiones del programa y facilitó el mantenimiento del código. Esta organización hizo que el proyecto fuera comprensible, modificable y escalable.
El resultado no es solo un juego que funciona. Es un sistema bien pensado donde cada parte tiene un propósito claro. Demuestra que en programación a menudo la solución más elegante es la que combina simplicidad y buen diseño de la manera más coherente.


Contacto
GitHub: @brittanysedamanos

Licencia
Este proyecto esta bajo la Licencia MIT. Ver archivo LICENSE para mas detalles.