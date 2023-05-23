thistuple = ("uno", "dos","tres")
print(len(thistuple)) #metodo len para la tupla


thistuple= tuple(("uno", "dos","tres")) #un parenteis para el metodo 
#y el otro para la tupla
print(thistuple)


thistuple = ("uno", "dos","tres")
print(thistuple[0]) #accede al valor de la tupla


thistuple = ("uno", "dos","tres")
print(thistuple[-1]) #-1 se refiere al último elemento, -2 se refiere al penúltimo elemento, etc.

thistuple = ("uno", "dos","tres","cuatro","cinco","seis")
print(thistuple[2:5]) #Nota: La búsqueda comenzará en el índice 2 (incluido) y terminará en el índice 5 (no incluido).



thistuple = ("uno", "dos","tres","cuatro","cinco","seis")
if "dos"  in thistuple:
    print("si")
else:
    print("no")


x =("apple", "banana","cherry")
y = list(x)  #pasar tupla a lista 
y[1] = "kiwi" # type: ignore  #corre bien en el w3scohols revisar
# cambia el valor de la posicion 1 
x=tuple(y) #reversar a tupla para luego imprimirla 
print(x)



thistuple = ("apple", "banana", "cherry")
y = list(thistuple)   # convertir tupla en lista para añadir valor
y.append("orange")  #type: ignore  #corre bien en el w3scohols revisar
thistuple = tuple(y) #reversar a tupla para luego imprimirla 
print(thistuple)


thistuple = ("apple", "banana", "cherry")
y= ("orange",)   #añade  de tupla a tupla
thistuple += y  # += añade item a la tupla
print(thistuple)


thistuple = ("apple", "banana", "cherry")
y= list(thistuple)  # convertir tupla en lista para quitar valor
y.remove("apple")   #quitar valor apple
thistuple = tuple(y)  # convertir a tupla de nuevo
print(thistuple)



thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #type: ignore da error porque se borro thistuple



#desenpacar tuplas (unpack tuple)

fruits = ("apple", "banana", "cherry")
(green,yelow,red) = fruits
print(green)
print(yelow)
print(red)



# si el numero de variables es menor al de la tupla se usa asterisco * para ajustar al de la tupla
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yelow,*red) = fruits  # * cuando la tupla supera el numero de valores 
print(green)   #variable
print(yelow)   #variable
print(red)     #variable


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(verde, *naranja, amarillo)= fruits # el asterisco en otro valor python asignará otro espacio hasta que cohincida 
print(verde)
print(naranja)
print(amarillo)

# iterar una tupla 
#recorrer la tupla con ciclo for
thistuple = ("apple", "banana", "cherry")
for x in thistuple: #recorrer los elementos e imprime los valores
    print(x)

#recorre los elementos de la tupla con referencia al numer de index
fruits = ("apple", "banana", "cherry")
for i in range(len(thistuple)): #recorre el rango de los valorses de la tupla
    print(thistuple[i])  #imprime la tupla en uncion a i que recorre los valores 

#ciclo while 
thistuple = ("apple", "banana", "cherry")
i = 0   #inicia el ciclo 
while i < len(thistuple): #cuenta de i hasta la cantidad de valores
  print(thistuple[i])  #imprime la tupla con la cantidad del contador 
  i = i + 1   #inicia el contador

#unir dos tuplas 
tuple1 = ("a","b","c","d")
tuple2  = (1,2,3)
tuple3= tuple1+tuple2 #unir dos tuplas (concatenar)
print(tuple3)


#multiplicar tuplas

fruits = ("apple", "banana", "cherry")
mytuple= fruits*2  #multiplica por 2
print(mytuple)

#las tuplas usan dos funciones count(), index  ()

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x=thistuple.count(5) #indica el numerode cincos que hay en la tupla
print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x= thistuple.index(8)  #indica la primera aparicion del 8 e indica su posicion  
print(x)  #en dado caso de no aparecer arroja error