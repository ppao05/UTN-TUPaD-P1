
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


