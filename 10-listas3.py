thislist = ["uno","dos","tres","cuatro","cinco"]
thislist.sort()   #sort() ordena los valores por tipo de caracter
print(thislist) # en orden alfabetico y numerico

thislist = [10,50,75,88,89]
thislist.sort(reverse=True)  #orden numerico invertido
print(thislist)


thislist = ["uno","dos","tres","Cuatro","Cinco"]
thislist.sort(key=str.upper)  #ordena por orden de mayuscula a minuscula
print(thislist)


thislist = ["uno","dos","tres","cuatro","cinco"]
mylist=thislist.copy() #copia de una lista a otra
print(mylist)

thislist = ["uno","dos","tres","cuatro","cinco"]
mylist= list(thislist)  #copia lista y le asigna el metodo list()   
print(mylist)


thislist = ["uno","dos","tres","cuatro","cinco"]
thislist.reverse() # invierte los items de la lista
print(thislist)


list1=[1,2,3,4,5]
list2=["a","b","c","d"]  #unir (concatenar dos listas)
list3= list1+list2
print(list3)

list4=["a","b","c","d"]
list5=[1,2,3,4,5]

for x in list5:
    list5.append(x)
print(list4)

list6=["a","b","c","d"]
list7=[1,2,3,4,5]
list6.extend(list6)
print(list6)