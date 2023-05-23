#las listas van con corchete [square brackets] son modificables
#contiene valores duplicados, varios tipos de datos
thislist= ["uno", "dos", "tres","cuatro","cinco","seis"]
print (thislist)    # imprimir
print(type(thislist)) #devolver el tipo de valor 
print(len(thislist)) #len() devuelve el numero de datos 
print(thislist[1]) # imprime el valor solicitado 
print(thislist[-1]) # imprime el  ultimo valor de la lista
print(thislist[2:5])  #This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
print(thislist[:4]) #This will return the items from index 0 to index 4.
print(thislist[2:])# retornara a partir del item 2 al final 
print(thislist[-4:-1]) #devuelve el index -4 

thislist = list(("uno","dos","tres")) #constructor list() crea una lista sobre la tupla
print(type(thislist)) 


thislist=["uno","dos","tres","cuatro"]
if "tres" in thislist: # si hay un tres en la lista
    print("si hay tres en la lista") #devuelve un true e imprime el str






