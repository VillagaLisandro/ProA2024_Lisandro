from Personaje_clase import Personaje


personaje = []
def menu():
  menuInicio = '''
  #########################################      
  #     1 - crear personaje               #
  #     2 - mostrar personaje             #
  #     3 - salir                         # 
  ######################################### '''
  print(menuInicio)
  opcion = int(input("ingrese su opcion elegida"))
  from typing import List
  from Personaje_clase import Personaje 
  
  p1 = Personaje("superman", 189, 90, 105)
  print(f"el personajese llama {p1.nombre}") 
  return opcion 
cantidadPersonaje = 0 
nuevo_personaje = Personaje(nombre, altura, velocidad, resistencia, fuerza)
personaje.append(nuevo_personaje)
while True:
     opcion =  menu()          
     if opcion == 1:
         cantidadPersonaje = cantidadPersonaje + 1
         nombre = str(input("ingrese el nombre de su personaje:)")
         altura = int(input(""))
         velocidad = int(input("ingrese la velocidad del personaje"))
         resistencia = int(input(""))
         fuerza = int(input(""))
        
     elif opcion == 2:
         cantidadPersonaje += 1
         print(f"El personaje {nuevo_personaje.nombre} fue creado  con exito")
         print(f"cantidad de personajes creados:{cantidadPersonaje}")
         print(personaje)  
     elif opcion == 3:  
         print("gracias por utilizar este programa")
         

         