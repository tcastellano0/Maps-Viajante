import TDAGrafo
import heapq

#Devuelve una lista del recorrido a hacer para resolver
#de forma aproximada el problema del viajante, pero
#mucho mas rapido.
def viajante_aprox(grafo, origen):
	visitados = []
	return viajante_aprox_wrapper(grafo, origen, visitados)

def viajante_aprox_wrapper(grafo, origen, visitados):
	heap = [] #heapq
	
	visitados.append(origen)
	peso_viaje = 0
	for w in grafo.obtener_adyacentes(origen):
		if w not in visitados:
			heapq.heappush(heap, (grafo.peso_arista(origen,w), origen, w))
	while len(visitados) != grafo.GetCantidad():
		(peso, v, w) = heapq.heappop(heap)
		if w in visitados:
			continue
		visitados.append(w)
		peso_viaje += grafo.peso_arista(v,w)
		for u in grafo.obtener_adyacentes(w):
			if u not in visitados:
				heapq.heappush(heap, (grafo.peso_arista(w, u), w, u))
	v_actual = visitados[-1]
	peso_viaje += grafo.peso_arista(v_actual, origen)
	visitados.append(origen)
	return peso_viaje, visitados

def viajante_opt(grafo, origen):
	visitados = []
	heap = [] #heapq
	peso_acum = 0
	visitados.append(origen)
	return viajante_opt_wrapper(grafo, origen, visitados, heap, peso_acum)

#Es una funcion recursiva
#En cada llamado meto en un heap los caminos minimos para recorrer todo el arbol partiendo de un cierto origen, visitando
#solo los vertices que aun no han sido visitados. Y creo una copia de "visitados" y le agrego ese "origen".
#Desencolo del heap el camino mas corto y vuelvo a llamar a la funcion.
#Corta cuando visite todos los vertices del grafo y le agrego el origen. El peso de la ultima arista ya fue agregado en cada caso.
def viajante_opt_wrapper(grafo, origen, visitados, heap, peso_acum):
	if len(visitados) == grafo.GetCantidad():
		visitados.append(origen)
		return peso_acum, visitados

	for v in grafo.obtener_adyacentes(origen):
		(peso, camino) = viajante_aprox_wrapper(grafo, v, visitados)
		camino.pop()
		peso -= grafo.peso_arista(camino[-1], v)
		peso += peso_acum
		#Falta agregar el primer peso
		peso += grafo.peso_arista(camino[-1], origen)
		camino.append(origen)
		peso_acum += grafo.peso_arista(visitados[-1], v)
		visitados_aux = visitados[:]
		visitados_aux.append(v)
		heapq.heappush(heap, (peso, peso_acum, visitados_aux))

	(peso, peso_acum, visitados_aux) = heapq.heappop(heap)
	viajante_opt_wrapper(grafo, visitados_aux[-1], visitados_aux, heap, peso_acum)


