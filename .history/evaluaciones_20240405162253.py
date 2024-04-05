from pizza import Pizza
import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
limpiar_consola()

#Peticion a)
#tamaño y precio 
print("****************************************************************************************")
print("")
print(f"ATENCION, las pizzas de tamaño {Pizza.tamano} subieron de precio ${Pizza.precio:,.2f}")
print("")
#Peticion b)
print(f" Si señores !!! aun tenemos SALSA DE TOMATES!!!!", Pizza.validar_elemento("salsa de tomate",["salsa de tomate", "salsa bbq"]))

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
