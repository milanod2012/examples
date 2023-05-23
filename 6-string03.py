age=36
txt="my name is john, and i am {}"
print(txt.format(age))

# se declara las variables quantity, itemno, para contcatenar numericos 
#en la cadena de texto
#se iimprime por orden de las variables 
"""quantity = 3   
itemno = 567
price = 49.95
myorder= "i want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
"""


#en este caso se imprime asignandole el orden de las variables
quantity = 3
itemno = 567
price = 49.95
myorder = "i want to pay {2} dollars for {0} pieces of item {1}"
print(myorder.format(quantity, itemno, price))

txt= "we are so-called \" vikings\"from the nort"  #se concatena
print(txt)   # usando \ fuera del "" con string






