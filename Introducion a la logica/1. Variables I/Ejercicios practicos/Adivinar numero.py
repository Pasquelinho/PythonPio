import random
Numero = random.randint (0,100)
Contador = 0

while True:
    try:
      Numerooculto = int(input("Ingrese un numero entero entre (1 y el 100):"))
    except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")
    if Numerooculto < 0:
            print ("Por favor ingresa un numero entero")
            continue
    if Numerooculto > Numero:
      Contador += 1
      print ("El numero es mayor")
    elif Numerooculto < Numero:
       Contador += 1
       print ("El numero es menor") 
    else:
            Numerooculto = Numero 
            print (f"Felicidades adivinaste el numero era, {Numerooculto}.")
            print (f"Te tomo {Contador} intentos")
            break
   
       


     
    
        
