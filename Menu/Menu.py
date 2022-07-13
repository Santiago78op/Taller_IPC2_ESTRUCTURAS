from colorama import Fore
from Listas.Actor import Actor
from Listas.ListaSimpleEnlazada import ListaSimpleEnlazada
import xml.etree.ElementTree as ET

class Menu:

	def __init__(self):
		self.soyVaraible = ''

	def menu(self):
		opcion = ''
		lista_Actores = ListaSimpleEnlazada()
		while opcion != '8':
			print(Fore.CYAN + "----------------------Menu----------------------")
			print(Fore.CYAN + "1 -- Crear Actor")
			print(Fore.CYAN + "2 -- Imprimir Actores")
			print(Fore.CYAN + "3 -- Buscar Actor")
			print(Fore.CYAN + "4 -- Actualizar Actor")
			print(Fore.CYAN + "8 -- Salir")

			opcion = input(Fore.YELLOW + "Selecciona una opcion del menu:\n")

			if opcion == '1':
				datos_Actor = input(Fore.BLUE + "Ingrese el actor con el siguiente formato nombre-edad-nacionalidad:\n")
				datos = datos_Actor.split('-')
				nuevoActor = Actor(datos[0],datos[1],datos[2])
				lista_Actores.append(nuevoActor)
			elif opcion == '2':
				lista_Actores.printActores()
			elif opcion == '3':
				nombre = input(Fore.BLUE + "Ingrese el nombre del actor: ")
				actor = lista_Actores.buscarActor(nombre)
				if actor is None:
					print(Fore.RED + "Error no tengo este actor")
				else:
					cadena = '{} {} {}'.format(actor.nombre, actor.edad, actor.nacionalidad)
					print(Fore.GREEN,cadena)


