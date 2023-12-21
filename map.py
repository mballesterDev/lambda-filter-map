import math

#map es como lamda pero con la funcion que queramos aplicar para el iterable

lista = list(range(1,11)) #lista del 1 al 10
print(lista)
elevarCuadrado = lambda num, : int(math.pow(num, 2))

listaElevada = list(map(elevarCuadrado, lista))
print (listaElevada)