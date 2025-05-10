## Ejercicio 1

for i in range(101):
    print(i)

## Ejercicio 2

numero = input("Ingrese un número entero:")

cantidad_digitos = len(numero)

print(f"La cantidad de dígitos es: {cantidad_digitos}")

## Ejercicio 3 

num1 = int(input("Ingrese el primer número:"))

num2 = int(input("Ingresa el segundo número:"))

if num1 > num2:
    num1, num2 = num2, num1

suma = 0
contador = 0

for i in range(num1 + 1, num2):
    suma += i
    contador += 1

print(f"Hay {contador} números enteros entre {num1} y {num2}")
print(f"La suma de estos números es: {suma}")

## Ejercicio 4

total = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar):"))
    if numero == 0:
        break
    total +=numero
print(f"El total acumulado es: {total}")

## Ejercicio 5

import random

numero_secreto = random.randint(0,9)
intentos = 0

print ("Adivina qué número del 0 al 9 estoy pensando")

while True:
    adivinanza = int(input("Ingresa el número:"))
    intentos += 1

    if adivinanza == numero_secreto:
        print(f"MUY BIEN! Adivinaste el número {numero_secreto} en {intentos} intentos")
    elif adivinanza < numero_secreto:
        print("Número muy bajo, intenta nuevamente.")
    else:
        print("Número muy alto, intenta nuevamente")


## Ejercicio 6

print("Números pares entre 0y 100 en orden decreciente")

for i in range(100, -1, -2):
    print(i)


## Ejercicio 7

num1 = int(input("Ingrese un número mayor a 0"))

suma = 0
contador = 0

for i in range(0 + 1, num1):
    suma += i
    contador += 1

print(f"Hay {contador} números enteros entre 0 y {num1}")
print(f"La suma de estos números es: {suma}")

## Ejercicio 8 REVEER CÓDIGO

numeros = []
pares = 0
impares = 0
positivos = 0
negativos = 0

print("Imgrese hasta 100 números enteros. (Ingrese 'stop' para finalizar):")

while len(numeros) <100:
    entrada = input("Ingrese un número:")
    if entrada.lower() == 'stop':
        break
    
numero = int(entrada)
numeros.append(numero)
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares +=1
if numero > 0:
    positivos += 1
elif numero < 0:
    negativos += 1


print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

## Ejercicio 9 REVISA CÓDIGO

print("Ingrese hasta 100 números enteros. Escriba 'stop' para finalizar la entrada.")
while len(numeros) < 100:
    entrada = input("Ingrese un número:")
    if entrada.lower() == 'stop':
        break

numero = int(entrada)
numeros.append(numero)

if numeros:
    media = sum(numeros) / len(numeros)
    print(f"La media de los valores ingresados es: {media}")
else:
    print("No se ingresaron números.")

## Ejercicio 10

numero = input("Ingrese un número:")

numero_invertido = numero[::-1]

print(f"El número {numero} invertido es: {numero_invertido}")
