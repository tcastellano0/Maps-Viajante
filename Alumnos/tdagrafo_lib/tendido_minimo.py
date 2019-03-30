import heapq
import TDAGrafo

def arbol_tendido_minimo(grafo):
	inicio = obtener_vertice_aleatorio()
	visitados = []
	heap = [] #heapq
	for w in grafo.obtener_adyacentes(inicio):
		heap.heappush((grafo.peso_arista(v,w), v, w))
	arbol = TDAGrafo.Grafo()
	for v in grafo.obtener_vertices():
	#v es una cadena con el nombre del vertice
		vertice = grafo.obtener_info(v)
		arbol.agregar_vertice(v, vertice)
	while heap:
		(peso, v, w) = heap.heappop()
		if w in visitados:
			continue
		arbol.agregar_arista(v, w, grafo.peso_arista(v, w))
		visitados.append(w)
		for u in grafo.obtener_adyacentes(w):
			heap.heappush((grafo.peso_arista(w,u), w, u))
	return arbol

