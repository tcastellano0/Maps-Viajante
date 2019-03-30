import random

class Grafo(object):
	#Lo vamos a representar como un diccionario de diccionarios.
	def __init__(self):
		self.vertices = {}
		self.cantidad = 0

	#Recibe una cadena con el nombre del vertice (v_nombre)
	#la cual sera pasada como clave del diccionario
	#Y el segundo parametro es el objeto vertice.
	def agregar_vertice(self, v_nombre, vertice):
		self.vertices[v_nombre] = vertice
		self.cantidad += 1

	#Recibe el nombre del vertice que se quiere eliminar
	#como cadena.
	def borrar_vertice(self, v_nombre):
		for v in self.vertices.keys():
			vertice = self.vertices[v]
			if v_nombre in vertice._adyacentes():
				self.borrar_arista(v, v_nombre)
		self.vertices.pop(v_nombre)
		self.cantidad -= 1

		

	"""def borrar_vertice(self, v_nombre):
		for vertice in self.vertices:
			v = self.vertices[vertice]
			if v_nombre in v.obtener_adyacentes():
				v.quitar_arista(v_nombre)
		self.vertices.pop(v_nombre)
		self.cantidad -= 1"""

	#Recibe como cadena el nombre de un vertice. Devuelve True
	#en caso de que el vertice pertenezca al grafo, False si no.
	def vertice_pertenece(self, vertice):
		if vertice in self.vertices:
			return True
		return False

	#Pruebo en los 2 vertices por si el grafo es no dirigido
	#Recibe el nombre, como cadena, de 2 vertices.
	#Si estos están conectados devuelve True, sino False
	def estan_conectados(self, v_1, v_2):
		if not self.vertice_pertenece(v_1) or not self.vertice_pertenece(v_2):
			return False
		vertice_1 = self.vertices[v_1]
		if vertice_1.es_adyacente(v_2):
			return True
		vertice_2 = self.vertices[v_2]
		if vertice_2.es_adyacente(v_1):
			return True
		return False

	#Devuelve el peso de una arista entre 2 vertices.
	#0 si no estan conectados.
	def peso_arista(self, v_1, v_2):
		if not self.estan_conectados(v_1, v_2):
			return 0
		vertice_1 = self.vertices[v_1]
		if vertice_1.es_adyacente(v_2):
			return vertice_1.peso_union(v_2)
		vertice_2 = self.vertices[v_2]
		return vertice_2.peso_union(v_1)

	#Devuelve una secuencia desordenada con los nombres de
	#todos los vertices
	def obtener_vertices(self):
		return self.vertices.keys()

	#Devuelve una secuencia desordenada con todos los vertices
	#(las clases)
	def obtener_vertices_pro(self):
		return self.vertices.values()

	#Devuelve un vertice aleatorio perteneciente al grafo.
	def obtener_vertice_aleatorio(self):
		return list(self.vertices)[0]

	#Devuelve una secuencia desordenada con los vertices
	#adyacentes al vertice pasado por parametro
	def obtener_adyacentes(self, vertice):
		v = self.vertices[vertice]
		return v._adyacentes()

	def obtener_info(self, vertice):
		return self.vertices[vertice]

	def agregar_arista(self, vertice, v_ady, peso):
		v = self.vertices[vertice]
		v.agregar_adyacente(v_ady, peso)

	def borrar_arista(self, vertice, v_ady):
		vertice = self.vertices[vertice]
		vertice.quitar_arista(v_ady)

	def GetCantidad(self):
		return self.cantidad

	def cantidad_adyacentes(self, vertice):
		return self.vertices[vertice].cant_adyacentes


class Vertice(object):

	def __init__(self):
		self.datos = []
		self.adyacentes = {}
		self.cant_adyacentes = 0

	#Recibe el nombre del vertice adyacente, como cadena y el
	#peso de la union.
	#Se agrega al diccionario como clave el vertice y el peso
	#como valor asociado a esa clave.
	def agregar_adyacente(self, v_ady, peso):
		self.adyacentes[v_ady] = peso
		self.cant_adyacentes += 1

	#Elimina la union del vertice con el pasado por parametro.
	def quitar_arista(self, v_ady):
		self.adyacentes.pop(v_ady)

	#Devuelve True en caso de que el vertice en el que estamos
	#"parados" este conectado con el pasado por parametro.
	#False en caso contrario.
	def es_adyacente(self, vertice):
		if vertice in self.adyacentes:
			return True
		return False

	#Devuelve el peso de la union con el vertice pasado por
	#parametro.
	def peso_union(self, vertice):
		return self.adyacentes[vertice]

	#Devuelve una secuencia desordenada de todos los vertices
	#adyacentes al vertice en el que estamos "parados".
	def _adyacentes(self):
		return self.adyacentes.keys()

	def obtener_aristas(self):
		return self.adyacentes.items()
