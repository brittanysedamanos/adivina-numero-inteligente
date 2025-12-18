# -*- coding: utf-8 -*-
"""
MODULO: Interfaz gráfica de usuario para Python 2.7
"""

import Tkinter as tk
import ttk
import config
import json
import os
import tkMessageBox

def mostrar_configuracion(root, app):
    """Muestra la ventana de configuración de dificultad."""
    config_window = tk.Toplevel(root)
    config_window.title("Configuracion de Dificultad")
    config_window.geometry("500x450")
    config_window.configure(bg='#f0f0f0')
    config_window.transient(root)
    config_window.grab_set()
    
    # Título
    tk.Label(config_window,
            text="CONFIGURACION DE DIFICULTAD",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50').pack(pady=20)
    
    # Frame principal
    main_frame = tk.Frame(config_window, bg='#f0f0f0')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    # Dificultades predefinidas
    dificultades = [
        ("FACIL", "Numeros del 1 al 50", 10),
        ("NORMAL", "Numeros del 1 al 100", 15),
        ("DIFICIL", "Numeros del 1 al 200", 20),
        ("EXPERTO", "Numeros del 1 al 500", 25)
    ]
    
    # Variable para selección
    seleccion = tk.StringVar(value="normal")
    
    for i, (nombre, desc, intentos) in enumerate(dificultades):
        frame = tk.Frame(main_frame, bg='#ecf0f1', relief=tk.GROOVE)
        frame.pack(fill=tk.X, pady=5, padx=20)
        
        rb = tk.Radiobutton(frame,
                           text=nombre,
                           variable=seleccion,
                           value=nombre.lower(),
                           font=("Arial", 11, "bold"),
                           bg='#ecf0f1')
        rb.pack(anchor=tk.W, padx=10, pady=5)
        
        tk.Label(frame,
                text=desc + " | Max intentos: " + str(intentos),
                font=("Arial", 9),
                bg='#ecf0f1').pack(anchor=tk.W, padx=30, pady=(0,5))
    
    # Personalizado
    frame_personal = tk.Frame(main_frame, bg='#ecf0f1', relief=tk.GROOVE)
    frame_personal.pack(fill=tk.X, pady=5, padx=20)
    
    rb_personal = tk.Radiobutton(frame_personal,
                                text="PERSONALIZADO",
                                variable=seleccion,
                                value="personalizado",
                                font=("Arial", 11, "bold"),
                                bg='#ecf0f1')
    rb_personal.pack(anchor=tk.W, padx=10, pady=5)
    
    # Entradas para personalizado
    personal_frame = tk.Frame(frame_personal, bg='#ecf0f1')
    personal_frame.pack(anchor=tk.W, padx=30, pady=(0,10))
    
    tk.Label(personal_frame, text="Minimo:", bg='#ecf0f1').grid(row=0, column=0, padx=2)
    entry_min = tk.Entry(personal_frame, width=10)
    entry_min.grid(row=0, column=1, padx=5)
    entry_min.insert(0, "1")
    
    tk.Label(personal_frame, text="Maximo:", bg='#ecf0f1').grid(row=0, column=2, padx=2)
    entry_max = tk.Entry(personal_frame, width=10)
    entry_max.grid(row=0, column=3, padx=5)
    entry_max.insert(0, "100")
    
    tk.Label(personal_frame, text="Intentos:", bg='#ecf0f1').grid(row=0, column=4, padx=2)
    entry_intentos = tk.Entry(personal_frame, width=10)
    entry_intentos.grid(row=0, column=5, padx=5)
    entry_intentos.insert(0, "30")
    
    def aplicar_configuracion():
        """Aplica la configuración seleccionada."""
        dificultad = seleccion.get()
        
        if dificultad == "facil":
            nueva_config = {
                "dificultad": "facil",
                "min_valor": 1,
                "max_valor": 50,
                "max_intentos": 10
            }
        elif dificultad == "normal":
            nueva_config = {
                "dificultad": "normal",
                "min_valor": 1,
                "max_valor": 100,
                "max_intentos": 15
            }
        elif dificultad == "dificil":
            nueva_config = {
                "dificultad": "dificil",
                "min_valor": 1,
                "max_valor": 200,
                "max_intentos": 20
            }
        elif dificultad == "experto":
            nueva_config = {
                "dificultad": "experto",
                "min_valor": 1,
                "max_valor": 500,
                "max_intentos": 25
            }
        else:  # personalizado
            try:
                min_valor = int(entry_min.get())
                max_valor = int(entry_max.get())
                max_intentos = int(entry_intentos.get())
                
                if min_valor >= max_valor:
                    tkMessageBox.showerror("Error", "El valor minimo debe ser menor al maximo.")
                    return
                
                nueva_config = {
                    "dificultad": "personalizado",
                    "min_valor": min_valor,
                    "max_valor": max_valor,
                    "max_intentos": max_intentos
                }
            except ValueError:
                tkMessageBox.showerror("Error", "Ingresa valores numericos validos.")
                return
        
        # Guardar configuración
        config.guardar_configuracion(nueva_config)
        
        # Actualizar en la app principal
        app.configuracion = nueva_config
        
        tkMessageBox.showinfo("Configuracion Guardada", 
                             "Dificultad: " + nueva_config['dificultad'].upper() + "\n" +
                             "Rango: " + str(nueva_config['min_valor']) + " - " + str(nueva_config['max_valor']) + "\n" +
                             "Intentos max: " + str(nueva_config['max_intentos']))
        
        config_window.destroy()
        app.crear_menu_principal()
    
    # Botones
    btn_frame = tk.Frame(config_window, bg='#f0f0f0')
    btn_frame.pack(pady=20)
    
    tk.Button(btn_frame,
             text="APLICAR",
             command=aplicar_configuracion,
             bg='#2ecc71',
             fg='white',
             font=("Arial", 11),
             width=15).pack(side=tk.LEFT, padx=10)
    
    tk.Button(btn_frame,
             text="CANCELAR",
             command=config_window.destroy,
             bg='#e74c3c',
             fg='white',
             font=("Arial", 11),
             width=15).pack(side=tk.LEFT, padx=10)

def mostrar_estadisticas_gui(root, app):
    """Muestra las estadísticas en una ventana."""
    stats_window = tk.Toplevel(root)
    stats_window.title("Estadisticas del Juego")
    stats_window.geometry("500x400")
    stats_window.configure(bg='#f0f0f0')
    stats_window.transient(root)
    stats_window.grab_set()
    
    # Título
    tk.Label(stats_window,
            text="ESTADISTICAS DEL JUEGO",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50').pack(pady=20)
    
    # Frame principal con scrollbar
    main_frame = tk.Frame(stats_window, bg='#f0f0f0')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
    
    # Obtener estadísticas
    estadisticas = config.obtener_estadisticas()
    
    if not estadisticas:
        tk.Label(main_frame,
                text="No hay estadisticas registradas aun.\n¡Juega algunas partidas para generar estadisticas!",
                font=("Arial", 12),
                bg='#f0f0f0',
                fg='#7f8c8d').pack(pady=50)
    else:
        # Resumen
        total_partidas = len(estadisticas)
        total_intentos = sum(estadisticas.values())
        promedio = total_intentos / float(total_partidas) if total_partidas > 0 else 0
        
        resumen_text = "Total partidas: " + str(total_partidas) + "\n"
        resumen_text += "Promedio de intentos: " + ("%.1f" % promedio) + "\n"
        resumen_text += "Mejor (menos intentos): " + str(min(estadisticas.values()))
        
        resumen_frame = tk.Frame(main_frame, bg='#ecf0f1', relief=tk.GROOVE)
        resumen_frame.pack(fill=tk.X, pady=10)
        
        tk.Label(resumen_frame,
                text=resumen_text,
                font=("Arial", 11),
                bg='#ecf0f1',
                justify=tk.LEFT).pack(padx=10, pady=10)
        
        # Lista de partidas
        tk.Label(main_frame,
                text="ULTIMAS PARTIDAS:",
                font=("Arial", 12, "bold"),
                bg='#f0f0f0').pack(anchor=tk.W, pady=(10,5))
        
        # Frame para tabla
        table_frame = tk.Frame(main_frame, bg='white', relief=tk.SUNKEN)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Encabezados
        headers = ["#", "Jugador", "Intentos", "Fecha"]
        
        for i, header in enumerate(headers):
            tk.Label(table_frame,
                    text=header,
                    font=("Arial", 10, "bold"),
                    bg='#3498db',
                    fg='white',
                    width=12 if i==1 else 8,
                    anchor=tk.W if i==1 else tk.CENTER).grid(row=0, column=i, sticky="ew", padx=1, pady=1)
        
        # Datos (últimas 10)
        items = list(estadisticas.items())[-10:]
        
        for idx, (clave, intentos) in enumerate(reversed(items), 1):
            # Extraer nombre (quitar el _número)
            nombre = "_".join(clave.split("_")[:-1])
            
            # Crear fila
            tk.Label(table_frame,
                    text=str(idx),
                    bg='#ecf0f1' if idx % 2 == 0 else 'white').grid(row=idx, column=0, sticky="ew", padx=1, pady=1)
            
            tk.Label(table_frame,
                    text=nombre,
                    anchor=tk.W,
                    bg='#ecf0f1' if idx % 2 == 0 else 'white').grid(row=idx, column=1, sticky="ew", padx=1, pady=1)
            
            tk.Label(table_frame,
                    text=str(intentos),
                    bg='#ecf0f1' if idx % 2 == 0 else 'white').grid(row=idx, column=2, sticky="ew", padx=1, pady=1)
            
            tk.Label(table_frame,
                    text="Reciente",
                    bg='#ecf0f1' if idx % 2 == 0 else 'white').grid(row=idx, column=3, sticky="ew", padx=1, pady=1)
    
    # Botón cerrar
    tk.Button(stats_window,
             text="CERRAR",
             command=stats_window.destroy,
             bg='#3498db',
             fg='white',
             font=("Arial", 11),
             width=20).pack(pady=20)

def mostrar_ayuda_gui(root, app):
    """Muestra la ayuda e instrucciones."""
    help_window = tk.Toplevel(root)
    help_window.title("Ayuda e Instrucciones")
    help_window.geometry("600x500")
    help_window.configure(bg='#f0f0f0')
    help_window.transient(root)
    help_window.grab_set()
    
    # Frame con scrollbar
    main_frame = tk.Frame(help_window, bg='#f0f0f0')
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Canvas y scrollbar
    canvas = tk.Canvas(main_frame, bg='#f0f0f0', highlightthickness=0)
    scrollbar = tk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas, bg='#f0f0f0')
    
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )
    
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    
    # Título
    tk.Label(scrollable_frame,
            text="AYUDA E INSTRUCCIONES",
            font=("Arial", 16, "bold"),
            bg='#f0f0f0',
            fg='#2c3e50').pack(pady=10)
    
    # Contenido
    secciones = [
        ("COMO JUGAR", [
            "1. Piensa en un numero secreto",
            "2. La computadora intentara adivinarlo",
            "3. Responde honestamente a cada intento:",
            "   • 1/MENOR si tu numero es menor",
            "   • 2/MAYOR si tu numero es mayor", 
            "   • 3/CORRECTO si adivino correctamente"
        ]),
        
        ("ALGORITMO UTILIZADO", [
            "• Busqueda binaria (divide y venceras)",
            "• Siempre elige el numero del medio",
            "• Maxima eficiencia: O(log n)",
            "• Inteligencia artificial basica"
        ]),
        
        ("NIVELES DE DIFICULTAD", [
            "• FACIL: Numeros del 1 al 50 (10 intentos)",
            "• NORMAL: Numeros del 1 al 100 (15 intentos)",
            "• DIFICIL: Numeros del 1 al 200 (20 intentos)",
            "• EXPERTO: Numeros del 1 al 500 (25 intentos)",
            "• PERSONALIZADO: Tu eliges el rango"
        ]),
        
        ("CONSEJOS", [
            "• No cambies tu numero durante el juego",
            "• Responde honestamente para mejores resultados",
            "• Observa como el algoritmo se hace mas preciso",
            "• Experimenta con diferentes dificultades"
        ]),
        
        ("ACERCA DEL PROYECTO", [
            "ADIVINA EL NUMERO - Sistema Inteligente",
            "Version con Interfaz Grafica",
            "Desarrollado en Python 2.7 con Tkinter",
            "Estudiante: Brittany Jhulisa Sedamanos Leon"
        ])
    ]
    
    for titulo, items in secciones:
        # Frame de sección
        section_frame = tk.Frame(scrollable_frame, bg='#ecf0f1', relief=tk.GROOVE)
        section_frame.pack(fill=tk.X, pady=10, padx=10)
        
        # Título de sección
        tk.Label(section_frame,
                text=titulo,
                font=("Arial", 12, "bold"),
                bg='#ecf0f1',
                fg='#2c3e50').pack(anchor=tk.W, padx=10, pady=5)
        
        # Items
        for item in items:
            tk.Label(section_frame,
                    text=item,
                    font=("Arial", 10),
                    bg='#ecf0f1',
                    anchor=tk.W,
                    justify=tk.LEFT).pack(anchor=tk.W, padx=20, pady=2)
    
    # Configurar scroll
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Botón cerrar
    tk.Button(help_window,
             text="CERRAR",
             command=help_window.destroy,
             bg='#3498db',
             fg='white',
             font=("Arial", 11),
             width=20).pack(pady=20)
