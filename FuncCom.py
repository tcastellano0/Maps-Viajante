import sys
import math
import heapq
try:
	import Queue as queue
except ImportError:
	#python 3
	import queue
import TDAGrafo
import TDAGrafoAux
import Viajante

#Este objeto ya conoce el grafo, entonces no tenemos que estar
#pasandolo por parametro en todos lados, simplemente es self.grafo y ya
#tenes acceso al grafo completo

class Comandos(object):
	def __init__(self, _archivo_csv, _archivo_kml):
		self.archivo_csv = _archivo_csv
		self.archivo_kml = _archivo_kml
		self.grafo = TDAGrafoAux.grafo_crear_desde_CSV(self.archivo_csv)

	def camino_minimo(self, desde, hasta):
		grafo = self.grafo
		dist = {}
		padres = {}

		for v in grafo.obtener_vertices():
			dist[v] = math.inf

		padres[desde] = None
		dist[desde] = 0
		heap = [] #heapq
		heapq.heappush(heap, (dist[desde], desde))

		while heap:
			(peso, v) = heapq.heappop(heap)
			if v == hasta:
				break
			for w in grafo.obtener_adyacentes(v):
				if (dist[v] + grafo.peso_arista(v,w)) < dist[w]:
					padres[w] = v
					dist[w] = dist[v] + grafo.peso_arista(v,w)
					heapq.heappush(heap, (dist[w], w))

		camino = []
		vertice = hasta

		while vertice:
			camino.insert(0, vertice)
			if padres.get(vertice, None) == None:
				break
			vertice = padres[vertice]

		descripcion_archivo = "Camino Minimo - [ " + desde  + " - " + hasta + " ]"
		TDAGrafoAux.grafo_mostrar_camino(grafo, camino, self.archivo_kml, descripcion_archivo)

	#Calcula el minimo camino posible, desde el "nuevo_origen", pasando
	#por todos los vertices que faltan, hasta el "origen"
	#El "grafo_aux" pasado por parametro es un grafo que solo tiene los vertices
	#por los que aun no se pasaron. El "grafo" es el original.

	"""def minimo_camino(self, grafo, grafo_aux, origen, nuevo_origen):
		(minimo, viaje_actual) = self.viajante_aproximado(grafo_aux, nuevo_origen)
		v_ult = viaje_actual[-2]
		minimo -= grafo.peso_arista(v_ult, nuevo_origen)
		viaje_actual.pop()
		minimo += grafo.peso_arista(v_ult, origen)
		viaje_actual.append(origen)
		return minimo, viaje_actual
	"""
	#Es una funcion recursivo.
	#En cada llamada busco el camino minimo posible yendo de ese vertice a
	#cualquiera de los otros que no visite. Encolo todos los caminos en un heap.
	#Desencolo el menos pesado, avanzo un vertice y repito.
	#Si el camino actual es mayor a algun otro, ese otro sera el desencolado del heap.
	#Y en la proxima llamada recursiva comenzara desde ese vertice tomando ese camino
	#(seria como volver para atras en caso de que exista la posibilidad de que sea mas corto)
	#En cada paso se actualiza el grafo para que el camino no vuelva a vertices ya visitados
	"""def viajante_wrapper(self, grafo, grafo_actual, v_act, origen, visitados, heap, peso_acum):
		if v_act != origen:
			if v_act == visitados[-1]:
				visitados.append(origen)
				peso_acum += grafo.peso_arista(v_act, origen)
				return peso_acum, visitados
		grafo_aux = grafo_actual
		adyacentes = grafo_aux.obtener_adyacentes(v_act)
		grafo_aux.borrar_vertice(v_act)
		for v in adyacentes:
			(peso, viaje) = self.minimo_camino(grafo, grafo_aux, origen, v)
			visitados.extend(viaje)
			peso += peso_acum
			heapq.heappush(heap, (peso, visitados, grafo_aux, v_act))
		(peso, visitados, grafo_aux, v_act) = heapq.heappop(heap)
		pos = visitados.index(v_act)
		v_act = visitados[pos + 1]
		self.viajante_wrapper(grafo, grafo_aux, v_act, origen, visitados, heap, peso)
	"""


	#Creo un heap, una lista de visitados y llamo a una funcion wrapper
	#en la que modificara la lista visitados.
	#Esta tendra el orden en que deben ser visitados las ciudades.
	#Devuelvo la lista y el peso total del viaje.
	"""def viajante(self, origen):
		grafo = self.grafo
		visitados = []
		heap = []
		peso = 0
		visitados.append(origen)
		(peso, visitados) = self.viajante_wrapper(grafo, grafo, origen, origen, visitados, heap, peso)

		descripcion_archivo = "Viaje optimo - [ " + origen + " ]"
		TDAGrafoAux.grafo_mostrar_camino(grafo, visitados, self.archivo_kml, descripcion_archivo)
	"""
	def viajante(self, origen):
		grafo = self.grafo
		(peso, visitados) = Viajante.viajante_opt(grafo, origen)
		descripcion_archivo = "Viaje optimo - [ " + origen + " ]"
		TDAGrafoAux.grafo_mostrar_camino(grafo, visitados, self.archivo_kml, descripcion_archivo)



	"""def viajante_aproximado(self, grafo, origen):
		#grafo = self.grafo
		visitados = []
		heap = [] #heapq

		visitados.append(origen)
		peso_viaje = 0
		for w in grafo.obtener_adyacentes(origen):
			if w not in visitados:
				heapq.heappush(heap, (grafo.peso_arista(origen,w), origen, w))
		while heap:
			(peso, v, w) = heapq.heappop(heap)
			if w in visitados:
				continue
			visitados.append(w)
			peso_viaje += grafo.peso_arista(v,w)
			for u in grafo.obtener_adyacentes(w):
				if u not in visitados:
					heapq.heappush(heap, (grafo.peso_arista(w,u), w, u))
		v_actual = visitados[-1]
		peso_viaje += grafo.peso_arista(v_actual, origen)
		visitados.append(origen)

		descripcion_archivo = "Viaje aproximado - [ " + origen + " ]"
		TDAGrafoAux.grafo_mostrar_camino(grafo, visitados, self.archivo_kml, descripcion_archivo)
	"""
	def viajante_aproximado(self, origen):
		grafo = self.grafo
		(peso, visitados) = Viajante.viajante_aprox(grafo, origen)
		descripcion_archivo = "Viaje aproximado - [ " + origen + " ]"
		TDAGrafoAux.grafo_mostrar_camino(grafo, visitados, self.archivo_kml, descripcion_archivo)

	def orden_topologico(self):
		grafo = self.grafo
		grados = {}

		for v in grafo.obtener_vertices():
			grados[v] = 0
		for v in grafo.obtener_vertices():
			for w in grafo.obtener_adyacentes(v):
				grados[w] += 1
		resul = []
		cola = queue.Queue(grafo.cantidad())
		for v in grafo:
			if grados[v] == 0:
				cola.put(v)
		while not cola.empty():
			v = cola.get()
			resul.append(v)
			for w in grafo.obtener_adyacentes(v):
				grados[w] -=1
				if grados[w] == 0:
					q.encolar(w)
		if len(resul) != grafo.cantidad():
			return None
		return resul

	def itinerario(self, archivo_recomendaciones):
		grafo = self.grafo
		viaje = []
		ciudad_1 = []
		ciudad_2 = []

		with open(archivo_recomendaciones, 'r') as f:
			for row in f:
				vec_row = row.split(",")
				ciudad_1.append(vec_row[0])
				ciudad_2.append(vec_row[1].replace("\n", ""))

		tot_ciudades = len(ciudad_1) + len(ciudad_2)
		tot_ciudades_recorridas = 0

		while tot_ciudades != tot_ciudades_recorridas:
			for c1 in ciudad_1:
				if c1 == None:
					continue

				if c1 not in ciudad_2:
					if c1 not in viaje:
						viaje.append(c1)

					pos = ciudad_1.index(c1)
					ciudad_1[pos] = None
					tot_ciudades_recorridas += 1

			for c2 in ciudad_2:
				if c2 == None:
					continue

				pos = ciudad_2.index(c2)
				if ciudad_1[pos] == None: #Visite su anterior
					cant = ciudad_2.count(c2)
					if cant == 1:
						viaje.append(c2)
					ciudad_2[pos] = None
					tot_ciudades_recorridas += 1

		descripcion_archivo = "Itinerario"
		TDAGrafoAux.grafo_mostrar_camino(grafo, viaje, self.archivo_kml, descripcion_archivo)

	def arbol_tendido_minimo(self, archivo_csv):
		grafo = self.grafo
		peso_camino = 0
		inicio = grafo.obtener_vertice_aleatorio()
		visitados = []
		heap = [] #heapq

		visitados.append(inicio)

		for w in grafo.obtener_adyacentes(inicio):
			heapq.heappush(heap, (grafo.peso_arista(inicio, w), inicio, w))

		arbol = TDAGrafo.Grafo()

		for v in grafo.obtener_vertices():
			vertice = TDAGrafo.Vertice()
			vertice.datos = grafo.obtener_info(v).datos
			arbol.agregar_vertice(v, vertice)

		while heap:
			(peso, v, w) = heapq.heappop(heap)
			if not  w in visitados:
				visitados.append(w)
				peso_camino += peso
				arbol.agregar_arista(v, w, peso)
				for u in grafo.obtener_adyacentes(w):
					heapq.heappush(heap, (grafo.peso_arista(w, u), w, u))

		print("Peso total: {0}".format(peso_camino))
		TDAGrafoAux.grafo_exportar_csv(arbol, archivo_csv)
