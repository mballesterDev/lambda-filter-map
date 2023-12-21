import random

"""Toma dos argumentos: la función de filtrado y la secuencia en la que se va a aplicar el filtrado(donde(tiene que ser iterable)).
La función de filtrado debe ser una función que devuelve un valor booleano (True o False). 
Esta función se aplicará a cada elemento de la secuencia 1 por 1."""

numerosDesordenaodos = []

for i in range (20):
    numero = random.randint(0, 100)
    numerosDesordenaodos.append(numero)


#hay que crear una funcion para pasarla como argumento

def mayorEdad(edad): # función para el filter
    if edad >= 50:
        return True

listaMayores = list(filter(mayorEdad, numerosDesordenaodos))    #usamos ek filter y list para combertitlo en lista
print(listaMayores)
listaMayores.sort() #lo oredenamos
listaMayores.insert(0, "Los mayores de 50 son = ")

menores50 = lambda edad: True if edad<50 else False #funcion pero utilizando lambda
listaMenores = list(filter(menores50, numerosDesordenaodos))
print(listaMenores)
listaMenores.sort()
listaMenores.insert(0, "Los menores de 50 son = ")



listaJunta = listaMenores.copy() #hacemos copia para que sea igual y dejar lista menores sin tocar por si queremos suarla luego
listaJunta.extend(listaMayores) #las juntamos
print(listaJunta)


