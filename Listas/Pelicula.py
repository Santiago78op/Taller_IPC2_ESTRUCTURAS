class Pelicula():

	def __init__(self, nombre=None,papel=None,anio=None,duracion=None):
		self.nombre = nombre
		self.papelm = papel
		self.anio = anio
		self.duracion = duracion
		self.siguente = None
		self.anterior = None