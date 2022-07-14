from Listas.Pelicula import Pelicula

class ListaDoblePeliculas():

	def __init__(self):
		self.raiz = Pelicula()
		self.ultimo = self.raiz


	def append(self, nuevaPelicula):
		if self.raiz.nombre is None:
			self.raiz = nuevaPelicula
		elif self.raiz.siguiente is None:
			self.raiz.siguiente = nuevaPelicula
			nuevaPelicula.anterior = self.raiz
			self.ultimo = nuevaPelicula
		else:
			self.ultimo.siguiente = nuevaPelicula
			nuevaPelicula.anterior = self.ultimo
			self.ultimo = nuevaPelicula

	def printPeliculas(self):
		nodoAux = self.raiz
		cadena = ''
		while True:
			if nodoAux.nombre is not None:
				cadena += '({} {} {})'.format(nodoAux.nombre,nodoAux.papel, nodoAux.anio, nodoAux.duracion)
				if nodoAux.siguiente is not None:
					cadena += "->"
					nodoAux = nodoAux.siguiente
				else:
					break
			else:
				break
		print(cadena)