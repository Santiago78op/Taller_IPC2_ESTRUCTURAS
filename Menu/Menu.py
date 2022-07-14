from colorama import Fore
from Listas.Actor import Actor
from Listas.Pelicula import Pelicula
from Listas.ListaSimpleEnlazada import ListaSimpleEnlazada
from Listas.ListaDoblePeliculas import ListaDoblePeliculas
import xml.etree.ElementTree as ET

class Menu:

	def __init__(self):
		self.soyEtiqueta = ''
		# Variable -> etiquete


	def menu(self):
		opcion = ''
		lista_Actores = ListaSimpleEnlazada()
		while opcion != '8':
			print(Fore.CYAN + "----------------------Menu----------------------")
			print(Fore.CYAN + "1 -- Crear Actor")
			print(Fore.CYAN + "2 -- Imprimir Actores")
			print(Fore.CYAN + "3 -- Buscar Actor")
			print(Fore.CYAN + "4 -- Agregar Pelicula a Actor")
			print(Fore.CYAN + "5 -- Imprimier Peliculas del Actor")
			print(Fore.CYAN + "6 -- Cargar Archivo")
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
			elif opcion == '4':
				nombre = input(Fore.BLUE + "Ingrese el nombre del actor")
				actor = lista_Actores.buscarActor(nombre)
				if actor is None:
					print(Fore.RED + "El actor no existe")
				else:
					pelicula = input(Fore.BLUE + "Ingrese la peliculas en el siguiente formato nombre-papel-anio-duracion:\n")
					datos = pelicula.split('-')
					nuevaPelicula = Pelicula(datos[0], datos[1], datos[2], datos[3])
					actor.listaPeliculas.append(nuevaPelicula)
					print(Fore.GREEN + "Se registro la pelicula")
			elif opcion == '5':
				nombre = input(Fore.BLUE + "Ingrese el nombre del actor")
				actor = lista_Actores.buscarActor(nombre)
				if actor is None:
					print(Fore.RED + "El actor no existe")
				else:
					actor.listaPeliculas.printPeliculas()
			elif opcion == '6':
				ruta = input(Fore.BLUE + "Ingrese el nombre del archivo \n")
				lista_Actores = self.cargarArchivo(ruta)
				print(Fore.GREEN + "Se cargo archivo con exito! \n")


	def cargarArchivo(self,ruta):
		tree = ET.parse(ruta)
		actores = tree.getroot()

		lista_Actores = ListaSimpleEnlazada()

		for actor in actores:
			nuevoActor = Actor(actor.attrib['nombre'],actor.attrib['edad'],actor.attrib['nacionalidad'])
			lista_Actores.append(nuevoActor)
			for pelicula in actor.iter('pelicula'):
				nuevoPelicula = Pelicula(pelicula.attrib['nombre'],pelicula.attrib['papel'],pelicula.attrib['anio'],pelicula.text)
				nuevoActor.listaPeliculas.append(nuevoPelicula)

		return lista_Actores



