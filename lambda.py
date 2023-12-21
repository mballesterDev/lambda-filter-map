def multiplicación(num1, num2): #sintaxis tradicional de una funcion 
    return num1*num2

multiplicación= lambda num1, num2: num1 * num2 #solo podemos relizar una expresión es para operaciones rápidas
#prámetros

#para llamarlo es necesario guardarlo en una variable
resultado1=(multiplicación(2,3))
resultado2=(multiplicación(10,3))

#o si queremos hacerlo aun más rápido
(lambda num1, num2: print(num1 * num2)) (7, 5)

#no tienen que llevar obligatoriamente argumentos
saludo = lambda: print("Hola humano")
saludo()

restar= lambda num1, num2 : num1-num2
print(restar(10,1))

(lambda num1, num2 : print(num1-num2)) (10,5)

#tambien se puede usar para condiciones
#para iterables
menores50 = lambda edad: True if edad<50 else False 

