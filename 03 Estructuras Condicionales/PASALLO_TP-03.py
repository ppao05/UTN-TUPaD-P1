
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

nombre = input("Ingrese su nombre:")

def menu ():
    print('1-nombre en minúscula')
    print('2-nombre en mayúscula')
    print('3-nombre con primera letra mayúscula')
    opc = int(input("Ingrese una opción:"))
    return opc

opción = menu()
if opción == 1:
    print(nombre.lower())
elif opción == 2:
    print(nombre.upper())
elif opción == 3:
    print(nombre.capitalize())

##Actividad 9

magnitud = float(input("Introduce la magnitud del terremoto:"))

if magnitud < 3:
    print("Muy leve. (Imperceptible)")
elif magnitud >= 3 and magnitud < 4:
    print("Moderado. (Sentido por personas, pero genralmente no causa daños)")
elif magnitud >=5 and magnitud < 6:
    print("Fuerte. (Puede causar daños en estructuras débiles)")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte. (Puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo. (Puede causar graves daños a gran escala)")

##Actividad 10

hemisferio = input("Ingrese 'N' si se encuentra en el hemisferio Norte o ingrese 'S' si se encuentra en el hemisferio Sur:")
mes = int(input("Ingrese el número de mes:"))
día = int(input("Ingrese el número del día:"))

if hemisferio == 'N':
    if (mes == 12 and día >=21) or (mes <= 3 and día <=20):
        print("Usted se encuentra en invierno")
    elif (mes == 3 and día >= 21) or (mes <=6 and día <=20):
        print("Usted se encuentra en primavera")
    elif (mes == 6 and día >= 21) or (mes <= 9 and día <=20):
        print("Usted se encuentra en verano")
else:
    print("Usted se encuentra en otoño")

if hemisferio == 'S':
    if (mes == 12 and día >=21) or (mes <= 3 and día <= 20):
        print("Usted se encuentra en verano")
    elif (mes == 3 and día >= 21) or (mes <= 6 and día <=20):
        print("Usted se encuentra en otoño")
    elif (mes == 6 and día >= 21) or (mes <= 9 and día <=20):
        print("Usted se encuentra en invierno")
else:
    print("USted se encuentra en primavera")

