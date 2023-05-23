thislist= ["uno", "dos", "tres","cuatro","cinco","seis"]
thislist[1]= "dosmil" # se cambio el valor [1] de la lista  
print(thislist) 


thislist= ["uno", "dos", "tres","cuatro","cinco","seis"]
thislist[1:3] = ["dosmil","tresmil"] # se cambio el valor [1] y [3](cuenta de izq a derecha)
print(thislist) 


thislist = ["uno", "dos", "tres","cuatro","cinco","seis"]
if "dos" in thislist: #condicional con lista 
    print("yes")
else:
    print("no")

#insertar item

thislist = ["uno", "dos", "tres","cuatro","cinco","seis"]   #inserta en la lista un nuevo valor
thislist.insert(6,"cero") #en este metodo puede especificar donde se inserta
print(thislist)

thislist=["uno","dos","tres"]
thislist.append("cuatro")  #append inserta solamente al final de la lista
print(thislist)


thislist=["uno", "dos","tres","cuatro"]
thislist1=["cinco", "seis","siete"]
thislist.extend(thislist1)   #extend extiende una lista, las une
print(thislist)             #tambien sirve para tupla, set, diccionarios



thislist=["uno", "dos","tres","cuatro"]
thislist.remove("tres")   #elimina un elemento de la lista
print(thislist)


thislist=["uno","dos","tres","cuatro"]
thislist.pop() # pop remueve el indice indice especifico
print(thislist) # si no se le asigna un valor a pop(), removera el ultimo item por defecto


thislist=["uno","dos","tres","cuatro"]
del thislist[2] #del remueve el valor especifico de la lista 
print(thislist)


thislist=["uno","dos","tres"]
thislist.clear() #imprime la lista en blanco clear() no se le puede colocar valores
print(thislist)


#ciclo for

thislist=["uno","dos","tres","cuatro"]
for x in thislist:  #ciclo for que recorra la lista
    print(x)


thislist=["uno","dos","tres","cuatro"]
for i in range(len(thislist)): #recorre la lista mediante el indice 
    print(thislist[i])

#ciclo while


thislist=["uno","dos","tres","cuatro"]
i=0
while i < len(thislist):
    print(thislist[i])
    i=i+1

# ciclo for resumiendo codigo (comprension de listas)
thislist=["uno","dos","tres","cuatro"]
[print(x) for x in thislist]


# imprime los indices que contengan los caracteres mencionados en el if

numbers=["primero","segundo","tercero","cuarto", "quinto"]
lista=[]
for x in numbers:
        if "n" in x:
            lista.append(x)
print(lista)





