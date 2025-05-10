## Ejercicio 1

numeros_multiplos_de_4 = list(range(4, 101, 4))

print(numeros_multiplos_de_4)

## Ejercicio 2

lista_elementos = ["manzana", "ciruela", "mandarina", "naranja", "higo"]

posicion_3 = lista_elementos[3]

print(posicion_3)

## Ejercicio 3

lista_vacia = []

lista_vacia.append("lapicera")
lista_vacia.append("cuaderno")
lista_vacia.append("borrador")

print(lista_vacia)

## Ejercicio 4

animales = ["perro", "gato", "conejo", "pez"]

animales[2] = "loro"
animales[3] = "oso"

print(animales)

##Ejercicio 5

numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

##Lo que realiza el código anterior es remover el número más alto de los elemntos de la lista numeros

##Ejercicio 6

lista_ejercicio6 = list(range(10, 31, 5))

posicion_1 = lista_ejercicio6[0]
posicion_2 = lista_ejercicio6[1]

print(posicion_1, posicion_2)

##Ejercicio 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "Alpine"
autos[2] = "Colapinto"

print(autos)

##Ejercicio 8

dobles = []

dobles.append(10)
dobles.append(20)
dobles.append(30)

print(dobles)

##Ejercicio 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")


indice_fideos = compras[1].index("fideos")

compras[1][indice_fideos] = "tallarines"

compras[0].remove("pan")

print(compras)

##Ejercicio 10

lista_anidada = [[15], ["True"], [25.5, 57.9, 30.6], ["False"]]

print(lista_anidada)
