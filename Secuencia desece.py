while True:
 try:
      Numero = int(input("Escriba un numero entero positivo "))
 except ValueError:
            print("Entrada inválida. Debes ingresar un número entero.")
 if Numero < 0: 
       print ("Ingresa un numero entero")   
 while Numero >= 1:
            print(Numero)
            Numero -= 1  
                                                  