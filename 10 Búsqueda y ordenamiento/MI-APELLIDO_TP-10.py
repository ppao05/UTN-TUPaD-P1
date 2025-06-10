import random #Hacemos uso de la libreria random
import time #Importamos time para medir los tiempos de busqueda

# Bases nitrogenadas posibles en modo de lista
bases = ['A', 'T', 'C', 'G']

# Longitudes posibles para las secuencias de ADN que elegimos
longitudes = [ 1000, 5000, 10000, 100000, 250000, 1000000]

#Rangos de edad (niños,adultos,mayores)
def generar_edad():
    prob = random.random() #Esto me generara un float aleatorio entre 0.0 y 1.0. En base a eso evaluo:
    if prob < 0.25: #Si el aleatorio generado es menor a 0.25, me generara una edad aleatoria en el rango (0,10) años 
        return random.randint(0, 10) #Y asi con los otros valores
    elif prob < 0.75:
        return random.randint(11, 50)
    else:
        return random.randint(51, 90)

# Función para generar una secuencia de ADN aleatoria
def generar_adn(longitud):
    return ''.join(random.choices(bases, k=longitud)) #Aca yo ingreso la longitud de "ATCG" que quiero y el me buscara aleatoriamente
#Desde la lista bases alguno de sus elementos y en k=longitud indicamos cuantos elementos queremos que nos devuelva. Luego lo unimos con join

# Generación de base de datos
n = 50
base_de_datos = []

for i in range(n):
    persona = {
        'id': i + 1,
        'sexo': random.choice(['Masculino', 'Femenino']),
        'edad': generar_edad(),
        'zona': random.choice(['Rural', 'Urbana']),
        'longitud_adn': random.choice(longitudes),
    }
    persona['adn'] = generar_adn(persona['longitud_adn'])
    base_de_datos.append(persona)
    
#----------------------------------------------------------------------------------------------------------------------------#
    
def busqueda_lineal(base_de_datos, objetivo): 
    encontrados = []
    for persona in base_de_datos:
        if objetivo in persona['adn']:
            encontrados.append(persona['id'])
            print(f"Mutación encontrada en la secuencia del paciente ID: {persona['id']}")
    
    if not encontrados:
        print("No se encontró ninguna coincidencia en la base de datos.")
        

#----------------------------------------------------------------------------------------------------------------------------#

print("Imaginemos que estas tres secuencias son predisponentes de X enfermedad. Para eso haremos uso de la búsqueda lineal")
print("\n") #Separador

print("Buscaremos: ","ATCGCGAA, ", "TTCGTGC", "y ", "ATTCGTCGA")
print("Primera búsqueda: ATCGCGAA ")
busqueda_lineal(base_de_datos, "ATCGCGAA" )
print("\n") #Separador

print("Segunda búsqueda: TTCGTGC ")
busqueda_lineal(base_de_datos, "TTCGTGC" )
print("\n") #Separador

print("Tercera búsqueda: ATCGCGAA ")
busqueda_lineal(base_de_datos, "ATTCGTCGA" )
print("\n") #Separador

print("A continuacion mostramos el tiempo que demora realizar esta busqueda ")
inicio_lineal = time.time()
resultado_lineal = busqueda_lineal(base_de_datos, "TTCGTGC")
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal
print(f"Tiempo de búsqueda = {tiempo_lineal:.6f} segundos")



#----------------------------------------------------------------------------------------------------------------------------#

#La siguiente funcion me filtra los pacientes mutados segun la secuencia por: edad, sexo, zonas y me devuelve la secuencia de ADN

def pacientes_mutados(base_de_datos, objetivo):
    edades = []
    sexo = []
    zonas = []
    adn = []
    for persona in base_de_datos:
        if objetivo in persona['adn']:
            edades.append(persona['edad'])
            sexo.append(persona['sexo'])
            zonas.append(persona['zona'])
            adn.append(persona['adn'])
    return edades, sexo, zonas, adn

    
pacientes_mutados(base_de_datos, "TTCGTGC")

#----------------------------------------------------------------------------------------------------------------------------#
print("\n") #Separador
#Vamos a filtrar por edad los pacientes mutados

pacientesMutadosPorEdad = pacientes_mutados(base_de_datos, "TTCGTGC")[0]
print(f"Edades de los pacientes con la secuencia mutada TTCGTGC {pacientesMutadosPorEdad} ")

#Ordenamos la lista de dos maneras: con sorted (de menor a mayor) y con quick_sort

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]
    menores = [x for x in lista[1:] if x <= pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + [pivote] + quick_sort(mayores) #Funcion para ordenar de menos a mayor

print(f"Lista ordenada con sorted: {sorted(pacientesMutadosPorEdad)}")
print(f'Lista ordenada con Quick sort: {quick_sort(pacientesMutadosPorEdad)}')

#Evaluo los tiempos de ambas maneras de ordenar

inicio_sorted = time.time()
listaDeSorted = sorted(pacientesMutadosPorEdad)
fin_sorted = time.time()
tiempo_sorted = fin_sorted - inicio_sorted

inicio_quick = time.time()
lista_quick = quick_sort(pacientesMutadosPorEdad)
fin_quick = time.time()
tiempo_quick = fin_quick - inicio_quick

print(f"Tiempo de ordenamiento sorted: {tiempo_sorted:10f}")
print(f"Tiempo de ordenamiento quick: {tiempo_quick:10f}")

#----------------------------------------------------------------------------------------------------------------------------#
print("\n") #Separador
#Con el siguiente codigo llego al numero de pacientes que presentan la mutacion discriminados por edad
def mutados_por_edad(secuencia):
 infantes = 0
 adultos = 0
 adultos_mayores_50 = 0
 for edad in pacientes_mutados(base_de_datos, secuencia)[0]:
   if edad > 0 and edad < 10:
       infantes += 1
   elif edad > 11 and edad <50:
     adultos += 1
   else:
     adultos_mayores_50 += 1
 print(f"La cantidad de infantes que presentan la secuencia mutada es {infantes}, de adultos es {adultos} y de adultos mayores de 50 es {adultos_mayores_50}")

mutados_por_edad("TTCGTGC")

print("\n") #Separador
#Ahora en los pacientes mutados necesitamos buscar cuantas A tienen y cuantas G tienen. Tambien sacar el porcentaje de cada una
#Para ello contaremos cuantas letras tienen y sacaremos %
secuencias_adn = pacientes_mutados(base_de_datos, "TTCGTGC")[3]

for posicion, adn in enumerate(secuencias_adn):
    total_bases = len(adn)
    cantidad_A = adn.count('A')
    cantidad_G = adn.count('G')

    porcentaje_A = (cantidad_A / total_bases) * 100
    porcentaje_G = (cantidad_G / total_bases) * 100

    

    print(f"Paciente {posicion + 1}:")
    print(f"Total de bases: {total_bases}")
    
    if porcentaje_A > 25:
      print("Este paciente tiene riesgo de desarrollar la enfermedad. A supera el %25")
    elif porcentaje_G < 25:
      print("Paciente con baja probabilidad de desarrollar la enfermedad. G es inferior a %25")
    else:
      print("Condicion clinica indeterminada en base a la proporcion de bases A y G")
      
    print(f"  A: {cantidad_A} ({round(porcentaje_A,2)}%)")
    print(f"  G: {cantidad_G} ({round(porcentaje_G,2)}%)\n")
