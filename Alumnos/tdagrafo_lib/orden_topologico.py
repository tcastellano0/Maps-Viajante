import TDAGrafo

try:
	import Queue as queue
except ImportError:
	#python 3
	import queue

#Implementacion del orden_topologico con BFS
#Devuelve una lista con un orden topologico del grafo. Si no
#existe devuelvo None. Para esta funcion el grafo pasado por
#parametro debe ser dirigido.
def orden_topologico(grafo):
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

