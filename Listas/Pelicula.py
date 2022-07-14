class Pelicula():

	def __init__(self, nombre=None,papel=None,anio=None,duracion=None):
		self.nombre = nombre
		self.papel = papel
		self.anio = anio
		self.duracion = duracion
		self.siguiente = None
		self.anterior = None