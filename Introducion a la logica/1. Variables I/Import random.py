import random

def adivina_el_numero():
    """Genera un número aleatorio y permite al usuario adivinarlo, mostrando el número de intentos.
    Pregunta al usuario si desea seguir jugando al final."""

    while True:  # Bucle principal para permitir múltiples juegos
        numero_secreto = random.randint(1, 100)
        intentos = 0
        print (numero_secreto)

        while True:  # Bucle para un solo juego
            try:
                adivinanza = int(input("Adivina el número (entre 1 y 100): "))
            except ValueError:
                print("Entrada inválida. Debes ingresar un número entero.")
                continue

            intentos += 1

            if adivinanza < numero_secreto:
                print("El número es más grande.")
            elif adivinanza > numero_secreto:
                print("El número es más pequeño.")
            else:
                print(f"¡Adivinaste! El número era {numero_secreto}.")
                print(f"Te tomó {intentos} intentos.")
                break  # Sal del bucle del juego actual

        # Preguntar si desea seguir jugando
        seguir_jugando = input("¿Deseas seguir jugando? (sí/no): ").lower()
        if seguir_jugando != 'si':
            break  # Sal del bucle principal si no quiere seguir jugando
        if seguir_jugando != 'no':
            break  # Sal del bucle principal si no quiere seguir jugando
# Inicia el juego
adivina_el_numero()