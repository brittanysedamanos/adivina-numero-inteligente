# -*- coding: utf-8 -*-
"""
MODULO: Logica del juego
"""

class JuegoAdivinanza:
    def __init__(self, nombre_jugador):
        self.nombre_jugador = nombre_jugador
        self.min_valor = 1
        self.max_valor = 100
        self.intentos = 0
        self.juego_activo = True
    
    def calcular_intento(self):
        return (self.min_valor + self.max_valor) // 2
    
    def iniciar(self):
        print("\nPiensa en un numero entre 1 y 100...")
        print("Voy a adivinarlo usando matematicas...")
        
        while self.juego_activo and self.intentos < 10:
            self.intentos += 1
            intento = self.calcular_intento()
            
            print("\n--- INTENTO #" + str(self.intentos) + " ---")
            print("Es " + str(intento) + " tu numero?")
            print("1. Mi numero es MENOR")
            print("2. Mi numero es MAYOR")
            print("3. SI, es correcto!")
            
            try:
                respuesta = int(input("\nTu respuesta (1-3): "))
            except ValueError:
                print("Error: Ingresa un numero valido.")
                self.intentos -= 1
                continue
            
            if respuesta == 1:
                self.max_valor = intento - 1
                print("Rango actual: " + str(self.min_valor) + " - " + str(self.max_valor))
            elif respuesta == 2:
                self.min_valor = intento + 1
                print("Rango actual: " + str(self.min_valor) + " - " + str(self.max_valor))
            elif respuesta == 3:
                print("\n*** VICTORIA ***")
                print("Adivine tu numero: " + str(intento))
                print("Intentos necesarios: " + str(self.intentos))
                self.juego_activo = False
            else:
                print("Opcion no valida. Usa 1, 2 o 3.")
                self.intentos -= 1
            
            if self.min_valor > self.max_valor:
                print("\n¡Alerta! Limites cruzados. ¿Cambiaste tu numero?")
                self.juego_activo = False