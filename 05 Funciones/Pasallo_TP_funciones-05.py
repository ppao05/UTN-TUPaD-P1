## Ejercicio 1

imprimir_hola_mundo = ("Hola Mundo!")

print(f"{imprimir_hola_mundo}")

## Ejercicio 2

def saludar_usuario(nombre):
    return(f"Hola {nombre}!")

nombre = input("Ingrese su nomnbre:")

saludo = saludar_usuario(nombre)

print(saludo)

## Ejericicio 3

def informacion_personal(nombre, apellido, edad, residencia):
    return(f"Soy {nombre} {apellido}, tengo {edad} y vivo en {residencia}")

nombre = input("Ingrese su nombre:")
apellido = input("Ingrese su apellido:")
edad = input("Ingrese su edad:")
residencia = input("Ingrese lugar de residencia:")

informacion = informacion_personal(nombre, apellido, edad, residencia)

print(informacion)

## Ejercicio 4

import math

def calcular_area_circulo(radio):
    return(math.pi*(radio**2))

def calcular_perimetro_circulo(radio):
    return((2*math.pi)*(radio))

radio = float (input("Ingrese el radio:"))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"El área del círculo es: {area} y el perímetro es: {perimetro} ")

## Ejercicio 5

def segundos_a_horas(segundos):
    horas = segundos / 3600
    return(f"{horas} horas")

segundos = float(input("Ingrese la cantidad de segundos:"))

resultado = segundos_a_horas(segundos)
print(f"{segundos} equivalen a {resultado} horas")

## Ejercicio 6

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar:"))
tabla_multiplicar(numero)

## Ejercicio 7

def operaciones_basicas(a, b):
    return suma, resta, multiplicacion, division

a = float(input("Ingrese el primer número:"))
b = float(input("Ingrese el segundo número:"))

suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b if b != 0 else "Error: División por cero"


resultados = operaciones_basicas(a, b)
print(f"La suma de ambos números es: {suma}")
print(f"La resta de ambos números es: {resta}") 
print(f"La multiplicación de ambos números es: {multiplicacion}")
print(f"La división de ambos números es: {division}")

## Ejercicio 8

def calcular_IMC(peso, altura):
    return round(IMC, 2)


peso = float(input("Ingrese su peso en kg:"))
altura = float(input("Ingrese su altura en metros:"))

IMC = round(peso / (altura ** 2), 2)

print(f"Su IMC es: {IMC}")

## Ejercicio 9

def celsius_a_farenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en grados Celsius:"))
farenheit = celsius_a_farenheit(celsius)

print(f"El equivalente en farenheit es: {farenheit}°F")

## Ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número:"))
b = float(input("Ingrese el segundo número:"))
c = float(input("Ingrese el tercer número:"))

promedio = calcular_promedio(a, b, c)

print(f"El promedio de los tres números es: {promedio}")


