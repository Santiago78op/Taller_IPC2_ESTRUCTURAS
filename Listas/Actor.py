from Listas.ListaDoblePeliculas import ListaDoblePeliculas

class Actor():

	def __init__(self, nombre=None,edad=None,nacionalidad=None):
		self.nombre = nombre
		self.edad = edad
		self.nacionalidad = nacionalidad
		self.siguiente = None
		self.listaPeliculas = ListaDoblePeliculas()
