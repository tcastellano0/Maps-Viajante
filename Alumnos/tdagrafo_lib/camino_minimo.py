import TDAGrafo
import heapq

INFINITO = 999999999999

def camino_minimo(grafo, desde, hasta):
	dist = {}
	padres = {}
	for v in grafo:
		dist[v] = INFINITO
	dist[desde] = 0
	heap = [] #heapq
	heap.heappush((desde, dist[desde]))
	while heap:
		(v, peso) = heappop()
		if v == hasta:
			return #algo
		for w in grafo.adyacentes(v):
			if (dist[v] + grafo.peso_arista(v,w)) < dist[w]:
				padre[w] = v
				dist[w] = dist[v] + grafo.peso_arista(v,w)
				heap.heappush((w, dist[w]))
	return None

