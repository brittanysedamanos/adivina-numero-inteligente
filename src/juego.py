# -*- coding: utf-8 -*-
"""
MODULO: Logica del juego - Version mejorada con configuracion
"""

import math

class JuegoAdivinanza:
    """Clase que maneja toda la logica del juego."""
    
    def __init__(self, nombre_jugador, configuracion):
        """Inicializar el juego con configuracion especifica."""
        self.nombre_jugador = nombre_jugador
        self.configuracion = configuracion
        
        self.min_valor = configuracion["min_valor"]
        self.max_valor = configuracion["max_valor"]
        self.max_intentos = configuracion["max_intentos"]
        
        self.intentos = 0
        self.juego_activo = True
        self.historial_intentos = []
    
    def calcular_intento(self):
        """Calcular el siguiente intento usando busqueda binaria."""
        intento = (self.min_valor + self.max_valor) // 2
        return intento
    
    def procesar_respuesta(self, respuesta, intento):
        """Procesar la respuesta del usuario."""
        if respuesta == 1:  # Numero es menor
            if intento <= self.min_valor:
                print("¡Inconsistencia detectada! No puede haber un numero menor.")
                return False
            self.max_valor = intento - 1
            print("Rango actual: " + str(self.min_valor) + " - " + str(self.max_valor))
            
        elif respuesta == 2:  # Numero es mayor
            if intento >= self.max_valor:
                print("¡Inconsistencia detectada! No puede haber un numero mayor.")
                return False
            self.min_valor = intento + 1
            print("Rango actual: " + str(self.min_valor) + " - " + str(self.max_valor))
            
        elif respuesta == 3:  # ¡Correcto!
            print("\n" + "="*40)
            print("¡¡¡VICTORIA!!!")
            print("="*40)
            print("Numero adivinado: " + str(intento))
            print("Total de intentos: " + str(self.intentos))
            
            # Calcular eficiencia
            import math
            rango_total = float(self.configuracion["max_valor"] - self.configuracion["min_valor"] + 1)
            max_teorico = int(math.ceil(math.log(rango_total) / math.log(2)))
            if max_teorico > 0:
                eficiencia = ((max_teorico - self.intentos) / float(max_teorico)) * 100
                eficiencia_final = max(eficiencia, 0)
                print("Eficiencia del algoritmo: %.1f%%" % eficiencia_final)
            else:
                print("Eficiencia del algoritmo: 0.0%")
            
            print("="*40)
            self.juego_activo = False
            return True
            
        else:  # Respuesta invalida
            print("Opcion no valida. Usa 1, 2 o 3.")
            return False
        
        return True
    
    def mostrar_resumen_rango(self):
        """Muestra informacion sobre el rango actual."""
        total_numeros = self.max_valor - self.min_valor + 1
        print("\nNumeros posibles restantes: " + str(total_numeros))
    
    def iniciar(self):
        """Metodo principal que ejecuta el juego."""
        print("\nHola " + self.nombre_jugador + "!")
        print("Piensa en un numero entre " + str(self.min_valor) + " y " + str(self.max_valor) + "...")
        print("Voy a adivinarlo usando busqueda binaria...")
        print("Maximo de intentos: " + str(self.max_intentos))
        
        # Ciclo principal del juego
        while self.juego_activo and self.intentos < self.max_intentos:
            self.intentos += 1
            intento_actual = self.calcular_intento()
            self.historial_intentos.append(intento_actual)
            
            print("\n--- INTENTO #" + str(self.intentos) + " ---")
            print("¿Es " + str(intento_actual) + " tu numero?")
            print("1. Mi numero es MENOR")
            print("2. Mi numero es MAYOR")
            print("3. ¡SI, es correcto!")
            
            # Mostrar informacion del rango cada 3 intentos
            if self.intentos % 3 == 0:
                self.mostrar_resumen_rango()
            
            # Obtener respuesta del usuario
            try:
                respuesta_usuario = int(raw_input("\nTu respuesta (1-3): "))
            except ValueError:
                print("Error: Debes ingresar un numero.")
                self.intentos -= 1
                continue
            
            # Procesar la respuesta
            if not self.procesar_respuesta(respuesta_usuario, intento_actual):
                if respuesta_usuario not in [1, 2, 3]:
                    self.intentos -= 1  # No contar intento invalido
            
            # Verificar consistencia
            if self.min_valor > self.max_valor:
                print("\n¡Alerta! Los limites se cruzaron.")
                print("¿Cambiaste tu numero durante el juego?")
                self.juego_activo = False
        
        # Si se alcanzo el limite de intentos
        if self.intentos >= self.max_intentos:
            print("\nLimite de intentos alcanzado (" + str(self.max_intentos) + " intentos maximo).")
            
            # Sugerir el numero mas probable
            sugerencia = (self.min_valor + self.max_valor) // 2
            print("Creo que tu numero podria ser: " + str(sugerencia))
