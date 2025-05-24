## Ejercicio 1

def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)
    
numero = int(input("Ingrese un número para calcular su factorial: "))

if numero < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    for i in range(1, numero + 1):
        factorial = calcular_factorial(i)
        print(f"El factorial de {i} es: {factorial}")

## Ejercicio 2

def calcular_fibonacci(n):
    if n <= 1:
        return n
    else:
        return calcular_fibonacci(n - 1) + calcular_fibonacci (n - 2)
    
posicion = int(input("Inngrese un número entero positivo para calcular la serie de Fibonacci:"))
if posicion < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    print(f"Serie de Finacci hasta la posición {posicion}")
    for i in range(posicion + 1):
        print(f"Fibonacci({i}): {calcular_fibonacci(i)}")

## Ejercicio 3

def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / calcular_potencia(base, -exponente)
    else:
        return base * calcular_potencia(base, exponente -1)
    
base = float(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))
resultado = calcular_potencia(base, exponente)
print(f"{base} elevado a {exponente} es: {resultado}")

## Ejercicio 4

def decimal_a_binario(numero):
    if numero == 0:
        return "0"
    elif numero == 1:
        return "1"
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)
    
numero = int(input("Introduce un número entero positivo:"))

if numero < 0:
    print("Por favor, introduce un número entero positivo.")
else:
    resultado = decimal_a_binario(numero)
    print(f"El número {numero} en binario es: {resultado}")

## Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

palabra = input("Introduce una palabra sin espacios ni tildes: ").strip().lower()
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")

## Ejercicio 6

def suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        return ((numero % 10) + suma_digitos(numero // 10))
    
numero = int(input("Introduce un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

## Ejercicio 7

def contador_bloques(numero):
    if numero == 1:
        return 1
    else:
        return (numero + contador_bloques(numero - 1))
    
nivel_inferior = int(input("Introduce el número de bloques en el nivel más bajo de la pirámide:"))

total_bloques = contador_bloques(nivel_inferior)
print(f"El número total de bloques necesarios para construir la pirámide es: {total_bloques}")

## Ejercicio 8

def contador_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contador_digito(numero // 10, digito)
    
numero = int(input("Introduce un número entero positivo:"))
digito = int(input("Introduce el dígito que deseas contar de 0 al 9:"))

apariciones = contador_digito(numero, digito)
print(f"El dígito {digito} aparece {apariciones} veces en el número {numero}.")

