
##Actividad 1

edad = int(input("Ingrese su edad: "))

if edad > 18:
    print("Es mayor de edad")
else: 
    pass

##Actividad 2

nota = int(input("Ingrese su nota: "))

if nota >= 6: 
    print("Aprobado")
else:
    print("Desaprobado")

##Actividad 3

numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else: 
    print("Por favor, ingrese un número par:")

##Actividad 4

edad = int(input("Ingrese su edad: "))


if edad < 12: 
    print("Niño/a") 
elif edad >= 12 and edad <18:
    print("Adolescente")
elif edad >= 18 and edad <30:
    print("Adulto/a joven")
else:
    print("Adulto")

##Actividad 5

def verificar_contraseña(contraseña):
    if 8<= len(contraseña) <= 14:
        print("Ha ingresado una contraseña correcta")
    else:
        print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

contraseña = input("Ingrese su contraseña:")
verificar_contraseña(contraseña)

##Actividad 6

from statistics import mode, median, mean
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

if media > mediana:
    print("Hay sesgo positivo")
elif media < mediana:
    print("Hay sesgo negativo")
else:
    print("No hay sesgo")

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

##Actividad 7

texto = input("Introduce una frase o palarabra:")

if texto [-1].lower() in 'aeiou':
    texto+= '!'
    print(texto)
else:
    print(texto)

##Actividad 8



