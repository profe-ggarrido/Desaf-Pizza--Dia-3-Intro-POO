from pizza import Pizza
import os
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
limpiar_consola()

#Peticion a)
#tamaño y precio 
print("****************************************************************************************")
print("")
print(f"ATENCION, las pizzas de tamaño {Pizza.tamano} y subieron de precio a ${Pizza.precio:,.2f}")
print("\u266A \u266B \u266C  EL  COSTO DE LA VIDA SUBE OTRA VEZ \u266A \u266B \u266C ")
print("")
#Peticion b)
print(f" Si señores !!! aun tenemos SALSA DE TOMATES!!!!", Pizza.validar_elemento("salsa de tomate",["salsa de tomate", "salsa bbq"]))
print("")
#Peticion c)
pizza1 = Pizza()  # se crea la instancia
print(f"\u266A \u266B \u266C  AHORITA LA PIZZAS SOLO ESTAN TAMAÑO \u266A \u266B \u266C ",pizza1.tamano)

print("U+2388")
pizza1.pedir()
print(pizza1.es_una_pizza_valida)

#Peticion d)
print(f" Vegetales: {pizza1.vegetales} Tipo de masa: {pizza1.tipo_masa} Es una pizza valida : {pizza1.es_una_pizza_valida}")
#Peticion e)
# Petición e)
print(f"La clase Pizza es una pizza válida: {Pizza.es_una_pizza_valida}")
