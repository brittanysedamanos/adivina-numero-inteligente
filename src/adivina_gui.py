# -*- coding: utf-8 -*-
"""
PROYECTO FINAL: ADIVINA EL NUMERO - SISTEMA INTELIGENTE
VERSION GRAFICA CON PALETA AZUL/GRIS - SIN CARACTERES ESPECIALES
"""

import Tkinter as tk
import ttk
import juego
import interfaz_gui
import config
import json
import random

# PALETA DE COLORES AZUL/GRIS
COLORES = {
    'azul_oscuro': '#2c3e50',
    'azul_medio': '#3498db',
    'azul_claro': '#5dade2',
    'gris_oscuro': '#34495e',
    'gris_medio': '#7f8c8d',
    'gris_claro': '#ecf0f1',
    'blanco': '#ffffff',
    'verde': '#27ae60',
    'rojo': '#e74c3c',
    'naranja': '#f39c12',
    'purpura': '#8e44ad'
}

class AdivinaNumeroGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Adivina el Numero - Sistema Inteligente")
        self.root.geometry("650x550")
        self.root.configure(bg=COLORES['azul_oscuro'])
        
        config.inicializar()
        self.configuracion = config.obtener_configuracion()
        
        self.nombre_jugador = ""
        self.juego_activo = False
        self.juego_obj = None
        self.intento_actual = 0
        
        self.crear_menu_principal()
        
    def crear_menu_principal(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        main_frame = tk.Frame(self.root, bg=COLORES['azul_oscuro'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        
        titulo_frame = tk.Frame(main_frame, bg=COLORES['azul_oscuro'])
        titulo_frame.pack(pady=(10, 20))
        
        tk.Label(titulo_frame,
                text="ADIVINA EL NUMERO",
                font=("Arial", 28, "bold"),
                bg=COLORES['azul_oscuro'],
                fg=COLORES['blanco']).pack()
        
        tk.Label(titulo_frame,
                text="Sistema Inteligente con Algoritmo Binario",
                font=("Arial", 12),
                bg=COLORES['azul_oscuro'],
                fg=COLORES['gris_medio']).pack(pady=5)
        
        separator = tk.Frame(main_frame, height=2, bg=COLORES['azul_medio'])
        separator.pack(fill=tk.X, pady=15, padx=50)
        
        btn_frame = tk.Frame(main_frame, bg=COLORES['azul_oscuro'])
        btn_frame.pack(pady=20)
        
        botones = [
            ("JUGAR NUEVA PARTIDA", self.iniciar_juego, COLORES['azul_medio']),
            ("CONFIGURAR DIFICULTAD", self.menu_configuracion, COLORES['gris_oscuro']),
            ("VER ESTADISTICAS", self.mostrar_estadisticas, COLORES['azul_claro']),
            ("AYUDA / INSTRUCCIONES", self.mostrar_ayuda, COLORES['purpura']),
            ("SALIR DEL JUEGO", self.root.quit, COLORES['rojo'])
        ]
        
        for texto, comando, color in botones:
            btn = tk.Button(btn_frame,
                          text=texto,
                          command=comando,
                          font=("Arial", 12, "bold"),
                          width=35,
                          height=2,
                          bg=color,
                          fg=COLORES['blanco'],
                          activebackground=self.oscurecer_color(color, 20),
                          activeforeground=COLORES['blanco'],
                          cursor='hand2',
                          relief=tk.RAISED,
                          bd=2)
            btn.pack(pady=8)
        
        info_frame = tk.Frame(main_frame, 
                             bg=COLORES['gris_claro'],
                             relief=tk.RIDGE,
                             bd=2)
        info_frame.pack(pady=25, fill=tk.X, padx=40)
        
        # SIN CARACTERES ESPECIALES
        info_text = "Dificultad actual: " + self.configuracion['dificultad'].upper() + "\n"
        info_text += "Rango: " + str(self.configuracion['min_valor']) + " - " + str(self.configuracion['max_valor']) + "\n"
        info_text += "Intentos maximos: " + str(self.configuracion['max_intentos'])
        
        tk.Label(info_frame,
                text=info_text,
                font=("Arial", 11),
                bg=COLORES['gris_claro'],
                fg=COLORES['azul_oscuro'],
                padx=15,
                pady=12).pack()
        
        footer = tk.Label(main_frame,
                         text="Desarrollado por Brittany Jhulisa Sedamanos Leon",
                         font=("Arial", 9),
                         bg=COLORES['azul_oscuro'],
                         fg=COLORES['gris_medio'])
        footer.pack(side=tk.BOTTOM, pady=10)
    
    def oscurecer_color(self, color, porcentaje):
        if color == COLORES['azul_medio']:
            return '#2980b9'
        elif color == COLORES['azul_claro']:
            return '#3498db'
        elif color == COLORES['gris_oscuro']:
            return '#2c3e50'
        elif color == COLORES['purpura']:
            return '#7d3c98'
        elif color == COLORES['rojo']:
            return '#c0392b'
        return color
    
    def iniciar_juego(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        main_frame = tk.Frame(self.root, bg=COLORES['azul_oscuro'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=25, pady=25)
        
        titulo_frame = tk.Frame(main_frame, bg=COLORES['azul_oscuro'])
        titulo_frame.pack(pady=(0, 15))
        
        tk.Label(titulo_frame,
                text="NUEVA PARTIDA",
                font=("Arial", 22, "bold"),
                bg=COLORES['azul_oscuro'],
                fg=COLORES['blanco']).pack()
        
        nombre_panel = tk.Frame(main_frame, 
                               bg=COLORES['gris_claro'],
                               relief=tk.GROOVE,
                               bd=2)
        nombre_panel.pack(pady=20, padx=50, fill=tk.X)
        
        tk.Label(nombre_panel,
                text="Ingresa tu nombre para comenzar:",
                font=("Arial", 12, "bold"),
                bg=COLORES['gris_claro'],
                fg=COLORES['azul_oscuro']).pack(pady=(15, 10))
        
        entrada_frame = tk.Frame(nombre_panel, bg=COLORES['gris_claro'])
        entrada_frame.pack(pady=(0, 15))
        
        self.entry_nombre = tk.Entry(entrada_frame,
                                   font=("Arial", 14),
                                   width=25,
                                   justify=tk.CENTER,
                                   bd=2,
                                   relief=tk.SUNKEN)
        self.entry_nombre.pack(side=tk.LEFT, padx=(0, 10))
        self.entry_nombre.bind("<Return>", lambda e: self.validar_nombre())
        self.entry_nombre.focus()
        
        tk.Button(entrada_frame,
                 text="COMENZAR",
                 command=self.validar_nombre,
                 bg=COLORES['verde'],
                 fg=COLORES['blanco'],
                 font=("Arial", 11, "bold"),
                 width=12,
                 height=1,
                 bd=2,
                 relief=tk.RAISED).pack(side=tk.LEFT)
        
        instrucciones_panel = tk.Frame(main_frame,
                                      bg=COLORES['gris_oscuro'],
                                      relief=tk.RAISED,
                                      bd=3)
        instrucciones_panel.pack(pady=15, padx=30, fill=tk.X)
        
        tk.Label(instrucciones_panel,
                text="INSTRUCCIONES DEL JUEGO",
                font=("Arial", 13, "bold"),
                bg=COLORES['gris_oscuro'],
                fg=COLORES['blanco']).pack(pady=(10, 5))
        
        instrucciones_text = "• Piensa en un numero entre " + str(self.configuracion['min_valor'])
        instrucciones_text += " y " + str(self.configuracion['max_valor']) + "\n"
        instrucciones_text += "• La computadora intentara adivinarlo\n"
        instrucciones_text += "• Responde con los botones: MENOR, MAYOR o CORRECTO\n"
        instrucciones_text += "• Dificultad: " + self.configuracion['dificultad'].upper()
        instrucciones_text += " (" + str(self.configuracion['max_intentos']) + " intentos maximo)"
        
        tk.Label(instrucciones_panel,
                text=instrucciones_text,
                font=("Arial", 10),
                bg=COLORES['gris_oscuro'],
                fg=COLORES['gris_claro'],
                justify=tk.LEFT).pack(padx=20, pady=(0, 15))
        
        tk.Button(main_frame,
                 text="VOLVER AL MENU",
                 command=self.crear_menu_principal,
                 bg=COLORES['gris_medio'],
                 fg=COLORES['blanco'],
                 font=("Arial", 10),
                 width=20,
                 bd=2,
                 relief=tk.GROOVE).pack(pady=20)
    
    def validar_nombre(self):
        import tkMessageBox
        nombre = self.entry_nombre.get().strip()
        if not nombre:
            tkMessageBox.showerror("Error", "Por favor ingresa tu nombre.")
            return
        
        self.nombre_jugador = nombre
        self.jugar_partida()
    
    def jugar_partida(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.juego_obj = juego.JuegoAdivinanza(self.nombre_jugador, self.configuracion)
        self.juego_activo = True
        self.intento_actual = 0
        
        main_frame = tk.Frame(self.root, bg=COLORES['azul_oscuro'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        header_frame = tk.Frame(main_frame, bg=COLORES['gris_oscuro'], height=60)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        header_frame.pack_propagate(False)
        
        info_left = tk.Frame(header_frame, bg=COLORES['gris_oscuro'])
        info_left.pack(side=tk.LEFT, padx=20)
        
        tk.Label(info_left,
                text="JUGADOR: " + self.nombre_jugador,
                font=("Arial", 11, "bold"),
                bg=COLORES['gris_oscuro'],
                fg=COLORES['blanco']).pack(anchor=tk.W)
        
        info_right = tk.Frame(header_frame, bg=COLORES['gris_oscuro'])
        info_right.pack(side=tk.RIGHT, padx=20)
        
        tk.Label(info_right,
                text="DIFICULTAD: " + self.configuracion['dificultad'].upper(),
                font=("Arial", 10),
                bg=COLORES['gris_oscuro'],
                fg=COLORES['gris_claro']).pack(anchor=tk.E)
        
        game_panel = tk.Frame(main_frame, 
                             bg=COLORES['gris_claro'],
                             relief=tk.RIDGE,
                             bd=4)
        game_panel.pack(fill=tk.BOTH, expand=True, pady=10)
        
        intentos_frame = tk.Frame(game_panel, bg=COLORES['gris_claro'])
        intentos_frame.pack(pady=25)
        
        self.intentos_label = tk.Label(intentos_frame,
                                      text="INTENTO #0",
                                      font=("Arial", 24, "bold"),
                                      bg=COLORES['gris_claro'],
                                      fg=COLORES['azul_medio'])
        self.intentos_label.pack()
        
        pregunta_frame = tk.Frame(game_panel, bg=COLORES['gris_claro'])
        pregunta_frame.pack(pady=20)
        
        self.pregunta_label = tk.Label(pregunta_frame,
                                      text="Preparando primer intento...",
                                      font=("Arial", 20),
                                      bg=COLORES['gris_claro'],
                                      fg=COLORES['azul_oscuro'])
        self.pregunta_label.pack()
        
        respuestas_panel = tk.Frame(game_panel, 
                                   bg=COLORES['gris_claro'],
                                   relief=tk.SUNKEN,
                                   bd=2)
        respuestas_panel.pack(pady=25, padx=50)
        
        tk.Label(respuestas_panel,
                text="TU NUMERO ES...?",
                font=("Arial", 12, "bold"),
                bg=COLORES['gris_claro'],
                fg=COLORES['gris_medio']).pack(pady=(15, 10))
        
        btn_frame = tk.Frame(respuestas_panel, bg=COLORES['gris_claro'])
        btn_frame.pack(pady=(0, 20))
        
        self.btn_menor = tk.Button(btn_frame,
                                  text="MENOR",
                                  command=lambda: self.procesar_respuesta(1),
                                  font=("Arial", 14, "bold"),
                                  width=8,
                                  height=2,
                                  bg=COLORES['rojo'],
                                  fg=COLORES['blanco'],
                                  activebackground='#c0392b',
                                  state=tk.DISABLED,
                                  bd=3,
                                  relief=tk.RAISED)
        self.btn_menor.pack(side=tk.LEFT, padx=15)
        
        self.btn_correcto = tk.Button(btn_frame,
                                     text="CORRECTO",
                                     command=lambda: self.procesar_respuesta(3),
                                     font=("Arial", 14, "bold"),
                                     width=10,
                                     height=2,
                                     bg=COLORES['verde'],
                                     fg=COLORES['blanco'],
                                     activebackground='#229954',
                                     state=tk.DISABLED,
                                     bd=3,
                                     relief=tk.RAISED)
        self.btn_correcto.pack(side=tk.LEFT, padx=15)
        
        self.btn_mayor = tk.Button(btn_frame,
                                  text="MAYOR",
                                  command=lambda: self.procesar_respuesta(2),
                                  font=("Arial", 14, "bold"),
                                  width=8,
                                  height=2,
                                  bg=COLORES['naranja'],
                                  fg=COLORES['blanco'],
                                  activebackground='#d68910',
                                  state=tk.DISABLED,
                                  bd=3,
                                  relief=tk.RAISED)
        self.btn_mayor.pack(side=tk.LEFT, padx=15)
        
        log_panel = tk.Frame(game_panel, 
                            bg=COLORES['blanco'],
                            relief=tk.SUNKEN,
                            bd=2)
        log_panel.pack(pady=20, padx=30, fill=tk.BOTH, expand=True)
        
        scrollbar = tk.Scrollbar(log_panel)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.info_text = tk.Text(log_panel,
                                height=8,
                                font=("Courier", 10),
                                bg=COLORES['blanco'],
                                fg=COLORES['azul_oscuro'],
                                state=tk.DISABLED,
                                yscrollcommand=scrollbar.set,
                                wrap=tk.WORD)
        self.info_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        scrollbar.config(command=self.info_text.yview)
        
        controles_frame = tk.Frame(main_frame, bg=COLORES['azul_oscuro'])
        controles_frame.pack(pady=15)
        
        self.btn_comenzar = tk.Button(controles_frame,
                                     text="COMENZAR ADIVINANZA",
                                     command=self.iniciar_ronda,
                                     font=("Arial", 12, "bold"),
                                     bg=COLORES['purpura'],
                                     fg=COLORES['blanco'],
                                     activebackground='#7d3c98',
                                     height=2,
                                     width=25,
                                     bd=3,
                                     relief=tk.RAISED)
        self.btn_comenzar.pack(side=tk.LEFT, padx=10)
        
        tk.Button(controles_frame,
                 text="VOLVER AL MENU",
                 command=self.finalizar_juego,
                 bg=COLORES['gris_medio'],
                 fg=COLORES['blanco'],
                 font=("Arial", 11),
                 width=15,
                 height=2,
                 bd=2,
                 relief=tk.GROOVE).pack(side=tk.LEFT, padx=10)
        
        self.actualizar_info("PREPARATE!")
        self.actualizar_info("Piensa en un numero secreto...")
        self.actualizar_info("Cuando estes listo, haz clic en COMENZAR ADIVINANZA")
        self.actualizar_info("="*50)
    
    def iniciar_ronda(self):
        self.btn_comenzar.config(state=tk.DISABLED, bg=COLORES['gris_medio'])
        self.btn_menor.config(state=tk.NORMAL)
        self.btn_mayor.config(state=tk.NORMAL)
        self.btn_correcto.config(state=tk.NORMAL)
        
        self.actualizar_info("COMIENZA EL JUEGO!")
        self.actualizar_info("La computadora intentara adivinar tu numero...")
        
        self.siguiente_intento()
    
    def siguiente_intento(self):
        if not self.juego_activo or self.intento_actual >= self.configuracion['max_intentos']:
            return
        
        self.intento_actual += 1
        intento = self.juego_obj.calcular_intento()
        
        self.intentos_label.config(text="INTENTO #" + str(self.intento_actual))
        self.pregunta_label.config(text="Es " + str(intento) + " tu numero?")
        
        self.actualizar_info("\n" + "="*50)
        self.actualizar_info("\nINTENTO #" + str(self.intento_actual))
        self.actualizar_info("\nLa computadora pregunta: Es " + str(intento) + " tu numero?")
        self.actualizar_info("\nSelecciona una opcion:")
        self.actualizar_info("  • MENOR si tu numero es mas pequeño")
        self.actualizar_info("  • MAYOR si tu numero es mas grande")
        self.actualizar_info("  • CORRECTO si adivino")
    
    def procesar_respuesta(self, respuesta):
        import tkMessageBox
        intento_actual = self.juego_obj.calcular_intento()
        
        resultado = self.juego_obj.procesar_respuesta(respuesta, intento_actual)
        
        if respuesta == 3:
            self.juego_activo = False
            self.btn_menor.config(state=tk.DISABLED, bg='#95a5a6')
            self.btn_mayor.config(state=tk.DISABLED, bg='#95a5a6')
            self.btn_correcto.config(state=tk.DISABLED, bg='#95a5a6')
            
            config.guardar_estadistica(self.nombre_jugador, self.intento_actual)
            
            self.actualizar_info("\n" + "*"*50)
            self.actualizar_info("\nVICTORIA!!!")
            self.actualizar_info("\nNumero adivinado: " + str(intento_actual))
            self.actualizar_info("Total de intentos: " + str(self.intento_actual))
            self.actualizar_info("\n" + "*"*50)
            
            tkMessageBox.showinfo("VICTORIA!", 
                                 "Numero adivinado en " + str(self.intento_actual) + " intentos!\n"
                                 "Felicidades " + self.nombre_jugador + "!")
            
            self.root.after(3000, self.finalizar_juego)
            
        elif self.intento_actual >= self.configuracion['max_intentos']:
            self.juego_activo = False
            self.actualizar_info("\nLIMITE DE INTENTOS ALCANZADO!")
            self.mostrar_fin_juego()
            
        else:
            rango_info = "Rango actual: " + str(self.juego_obj.min_valor)
            rango_info += " - " + str(self.juego_obj.max_valor)
            self.actualizar_info(rango_info)
            
            numeros_restantes = self.juego_obj.max_valor - self.juego_obj.min_valor + 1
            self.actualizar_info("Numeros posibles: " + str(numeros_restantes))
            
            self.siguiente_intento()
    
    def actualizar_info(self, mensaje):
        self.info_text.config(state=tk.NORMAL)
        self.info_text.insert(tk.END, mensaje + "\n")
        self.info_text.see(tk.END)
        self.info_text.config(state=tk.DISABLED)
    
    def mostrar_fin_juego(self):
        import tkMessageBox
        sugerencia = (self.juego_obj.min_valor + self.juego_obj.max_valor) // 2
        mensaje = "\n" + "-"*50
        mensaje += "\nJUEGO TERMINADO!"
        mensaje += "\nSugerencia: Tu numero podria ser " + str(sugerencia)
        mensaje += "\n" + "-"*50
        self.actualizar_info(mensaje)
        
        tkMessageBox.showinfo("Juego Terminado",
                             "Limite de intentos alcanzado.\n"
                             "Sugerencia: El numero podria ser " + str(sugerencia))
        
        self.root.after(3000, self.finalizar_juego)
    
    def finalizar_juego(self):
        self.juego_activo = False
        self.crear_menu_principal()
    
    def menu_configuracion(self):
        interfaz_gui.mostrar_configuracion(self.root, self)
    
    def mostrar_estadisticas(self):
        interfaz_gui.mostrar_estadisticas_gui(self.root, self)
    
    def mostrar_ayuda(self):
        interfaz_gui.mostrar_ayuda_gui(self.root, self)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AdivinaNumeroGUI()
    app.run()
