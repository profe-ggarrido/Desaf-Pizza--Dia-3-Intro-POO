from pizza import Pizza

#Peticion a)
#tamaño y precio 
print(f"Todas las pizzas tienen un tamaño {Pizza.tamano} y un precio {Pizza.precio}")
#Peticion b)
print(f" aaa", Pizza.validar_elemento("salsa de tomate",["salsa de tomate", "salsa bbq"]))
#Peticion c)
pizza1 = Pizza()
print(pizza1.tamano)
pizza1.pedir()
print(pizza1.es_una_pizza_valida)

#Peticion d)
print(f" Vegetales: {pizza1.vegetales} Tipo de masa: {pizza1.tipo_masa} Es una pizza valida : {pizza1.es_una_pizza_valida}")
#Peticion e)
# Petición e)
print(f"La clase Pizza es una pizza válida: {Pizza.es_una_pizza_valida}")
