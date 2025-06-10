
## Generación de conjuntos de dígitos únicos a partir de DNIs

def obtener_conjunto_digitos(dni_str):
    return set(int(digito) for digito in dni_str if digito.isdigit())

DNIs = []
conjuntos = []

print("Ingrese los DNIs sin puntos y espacios (escriba 'fin' para terminar):")
DNI = input("Ingrese un DNI: ").strip()
while DNI != 'fin':
    DNIs.append(DNI)
    conjuntos.append(obtener_conjunto_digitos(DNI))
    DNI = input("Ingrese un DNI: ").strip()

print("\nConjuntos de dígitos únicos: ")
for i, conj in enumerate(conjuntos):
    print(f"Conjunto {i + 1}: {conj}")


## Paso 2: Operaciones entre pares de conjuntos

from itertools import combinations


print("\nOperaciones entre pares de conjuntos:")
for (i, A), (j, B) in combinations(enumerate(conjuntos), 2):
    print(f"\nConjuntos {i + 1} y {j + 1}:")
    print(f"A = {A}, B = {B}")
    print(f"A ∪ B = {A.union(B)}")
    print(f"A ∩ B = {A.intersection(B)}")
    print(f"A - B = {A.difference(B)}")
    print(f"B - A = {B.difference(A)}")
    print(f"A ⊕ B = {A.symmetric_difference(B)}")

## Paso 3: Frecuencia y suma de dígitos

print("\nFrecuencia de dígitos y suma por DNI:")
for i, DNI in enumerate(DNIs):
    frecuencia = {str(digito): 0 for digito in range(10)}
    suma = 0
    for digito in DNI:
        if digito.isdigit():
            frecuencia[digito] += 1
            suma += int(digito)
    print(f"DNI {i + 1}: {DNI}, Frecuencia: {frecuencia}, Suma: {suma}")

## Paso 4: Evaluación de expresiones lógicas.

## Evaluar condición lógica entre tres conjuntos

if len(conjuntos) >= 3:
    A = conjuntos[0]
    B = conjuntos[1]
    C = conjuntos[2]
    # Verifica si A tiene más elementos que B y C tiene al menos un número impar
    if len(A) > len(B) and any(num % 2 != 0 for num in C):
        print("\nSe cumple la condición de combinación específica: A tiene más elementos que B y C tiene al menos un número impar.")
    else:
        print("\nNo se cumple la condición de combinación específica.")

## Evaluación de condición lógica 2

# Verifica si ningún conjunto tiene el número 0

if all(0 not in conjunto for conjunto in conjuntos):
    print("\nSe considera un grupo sin ceros: ningún conjunto tiene el número 0.")
else:
    print("\nAl menos un conjunto contiene el número 0.")

