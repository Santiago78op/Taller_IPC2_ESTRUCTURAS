from Listas.Actor import Actor

class ListaSimpleEnlazada():

	def __init__(self):
		self.raiz = Actor()
		self.ultimo = self.raiz

	def append(self,nuevoActor):
		if self.raiz.nombre is None:
			self.raiz = nuevoActor
		elif self.raiz.siguiente is None:
			self.raiz.siguiente = nuevoActor
			self.ultimo = nuevoActor
		else:
			self.ultimo.siguiente = nuevoActor
			self.ultimo = nuevoActor

	def printActores(self):
		nodoAux = self.raiz
		cadena = ''
		while True:
			if nodoAux.nombre is not None:
				cadena += '({} {} {})'.format(nodoAux.nombre,nodoAux.edad, nodoAux.nacionalidad)
				if nodoAux.siguiente is not None:
					cadena += "->"
					nodoAux = nodoAux.siguiente
				else:
					break
			else:
				break
		print(cadena)

	def buscarActor(self, nombre):
		nodoAux = self.raiz

		while nodoAux.nombre != nombre:
			if nodoAux.siguiente is not None:
				nodoAux = nodoAux.siguiente
			else:
				return None
		return nodoAux