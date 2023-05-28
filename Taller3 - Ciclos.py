print("""Miscelánea de Ejercicios – Python 
 -Ciclos- 
1. Imprimir todos los múltiplos de 3 que hay entre 1 y 100.
2. Imprimir los números impares entre 0 y 100.
3. Imprimir los números pares entre 0 y 100.
4. Escribir un programa en Python que imprima por pantalla los números del 1 al 3.
5. Escribir un programa en Python que imprima por pantalla los números del 10 al 1.
6. Escribir un programa en Python que imprima en pantalla los cuadrados de los números del 1 al 30.
7. Escribir un programa en Python que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla.
8. Escribir un programa en Python que lea un número entero desde teclado y realice la suma de los cien números siguientes, mostrando el resultado en pantalla (ej: el usuario digita 5, se debe sumar 5+6+7+8+... hasta que complete cien números) 
9. Halle el número factorial de un número ingresado por el usuario.
10. Escriba un programa que lea temperaturas expresadas en grados Fahrenheit y las convierta a grados Celsius. El programa finalizará cuando lea un valor de temperatura igual a 999. La fórmula c = 5/9(f - 32)    
11. Imprima los números primos hasta un número ingresado por el usuario.
12. Muestre en pantalla la tabla de multiplicar que el usuario desee.
13. Ingresar un conjunto de números positivos. Calcular y escribir su promedio sabiendo que se ingresará un valor menor que 0 para indicar el fin del conjunto de números.
14. Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente. 
15. Realizar un algoritmo que muestre los valores de todas las piezas del dominó de forma ordenada: 0-0  0-1  1-1 etc.
 """)
ejercicio = 0

while ejercicio < 99:
  ejercicio = int(input("Digite el ejercicio a realizar: "))
      #Imprimir todos los múltiplos de 3 que hay entre 1 y 100
  if ejercicio == 1:
     
     for i in range(3,100,3):
      print(i)

      #Imprimir los números impares entre 0 y 100
  elif ejercicio == 2:
     for impar in range(1,100,3):
      print(impar)

      #Imprimir los números pares entre 0 y 100
  elif ejercicio == 3:
    for par in range(0,100,2):
      print(par)
      # Escribir un programa en Python que imprima por pantalla los números del 1 al 3.
  elif ejercicio == 4:
    for i in range(1,4):
       print(i)

      # Escribir un programa en Python que imprima por pantalla los números del 10 al 1
  elif ejercicio == 5:
    for i in range(10,0,-1):
      print(i)

      #Escribir un programa en Python que imprima en pantalla los cuadrados de los números del 1 al 30
  elif ejercicio == 6:
    for cuadrado in range(1,31):
        print(pow (cuadrado,2))
      
      #Escribir un programa en Python que sume los cuadrados de los cien primeros números naturales, mostrando el resultado en pantalla
  elif ejercicio == 7:
    suma = 0
    for num in range(1,101):
        suma += pow(num, 2)
    print(suma)

      #Escribir un programa en Python que lea un número entero desde teclado y realice la suma de los cien números siguientes, mostrando el resultado en pantalla
  elif ejercicio == 8:
    num = int(input("Digite un Numero: "))
    sum = 0
    for i in range(num, (num + 101)):
      sum += i
    print(sum)
      
      #Halle el número factorial de un número ingresado por el usuario
  elif ejercicio == 9:
     num = int(input("Digite un Numero: "))
     fact = 1
     for i in range(1, num + 1):
       fact = fact * i
     print("El Factorial del numero ingresado es: ", fact)
      
       #Escriba un programa que lea temperaturas expresadas en grados Fahrenheit y las convierta a grados Celsius. El programa finalizará cuando lea un valor de temperaturaigual a 999. La fórmula c = 5/9(f -32)
  elif ejercicio == 10:
    while True:
      print("Digite 999 para Finalizar")
      fah = float(input("Digite una temperatura en grados Fahrenheit: "))
      if fah == 999:
        break
      cel = (5 / 9) * (fah - 32)
      print("La temperatura en grados Celsius es: ", cel)
 
        #Imprima los números primos hasta un número ingresado por el usuario:
  elif ejercicio == 11:
         num = int(input("Digite un Número: "))
         print("Números primos hasta", num, "son")
         for i in range(2, (num + 1)):
             primo = True
             for a in range(2, int(i ** 0.5)+ 1): 
                if i % a == 0:
                   primo = False
                   break
             if primo:
                print(i)

        #Muestre en pantalla la tabla de multiplicar que el usuario desee
  elif ejercicio == 12:
         num = int(input("Digite un Número para Generar Tabla de Multiplicar: " ))
         print("Tabla del", num)
         for i in range(1, 11):
             prod = num * i
             print(num, "x", i, "=", prod)
             #prod: es el producto de la multiplicacion

        #Ingresar un conjunto de números positivos. Calcular y escribir su promedio sabiendo que se ingresará un valor menor que 0 para indicar el fin del conjunto de números.
  elif ejercicio == 13:
    numeros = []
    while True:
        print("Si ingresa un numero negativo finalizara el proceso")
        num = float(input("Digite un número positivo: "))
        if num <= 0:
          break
        numeros.append(num)
    
    if len(numeros) > 0:
        prom = sum(numeros) / len(numeros)
        print("El promedio de los números ingresados es:", prom)
    else:
       print("No se ingresaron números positivos.")


         # Dados dos números naturales, el primero menor que el segundo, generar y mostrar todos los números comprendidos entre ellos en secuencia ascendente. 
  elif ejercicio == 14:
       num_negativo = int(input("Digite el primer número Menor: "))
       num_positivo = int(input("Digite el segundo número Mayor: "))
       print("Los números comprendidos entre", num_negativo, "y", num_positivo, "en secuencia ascendente:")
       for i in range(num_negativo + 1, num_positivo):
            print(i) 

        # Realizar un algoritmo que muestre los valores de todas las piezas del dominó de forma ordenada: 0-0  0-1  1-1
  elif ejercicio == 15:
       print("Valores del dominó de forma ordenada:")
       for i in range(7):
           for a in range(i, 7):
               print(i, "-", a)