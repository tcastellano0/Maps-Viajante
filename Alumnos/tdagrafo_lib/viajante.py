import TDAGrafo
import heapq

#Calcula el minimo camino posible, desde el "nuevo_origen", pasando
#por todos los vertices que faltan, hasta el "origen"
#El "grafo_aux" pasado por parametro es un grafo que solo tiene los vertices
#por los que aun no se pasaron. El "grafo" es el original.

def minimo_camino(grafo, grafo_aux, origen, nuevo_origen):
	(minimo, viaje_actual) = viajante_aproximado(grafo_aux, nuevo_origen)
	v_ult = viaje_actual[-2]
	minimo -= grafo.peso_arista(v_ult, nuevo_origen)
	viaje_actual.pop()
	minimo += grafo.peso_arista(v_ult, origen)
	viaje_actual.append(origen)
	return minimo, viaje_actual

#Es una funcion recursivo.
#En cada llamada busco el camino minimo posible yendo de ese vertice a 
#cualquiera de los otros que no visite. Encolo todos los caminos en un heap.
#Desencolo el menos pesado, avanzo un vertice y repito.
#Si el camino actual es mayor a algun otro, ese otro sera el desencolado del heap.
#Y en la proxima llamada recursiva comenzara desde ese vertice tomando ese camino 
#(seria como volver para atras en caso de que exista la posibilidad de que sea mas corto)
#En cada paso se actualiza el grafo para que el camino no vuelva a vertices ya visitados
def viajante_wrapper(grafo, grafo_actual, v_act, origen, visitados, heap, peso_acum):
	if v_act == visitados[-1]:
		visitados.append(origen)
		peso_acum += grafo.peso_arista(v_act, origen)
		return peso_acum, visitados
	grafo_aux = grafo_actual
	grafo_aux.borrar_vertice(v_act)
	for v in grafo_aux.obtener_adyacentes(v_act):
		(peso, viaje) = minimo_camino(grafo, grafo_aux, origen, v)
		visitados.extend(viaje)
		peso += peso_acum
		heapq.heappush(heap, (peso, visitados, grafo_aux, v_act))
	(peso, visitados, grafo_aux, v_act) = heapq.heappop(heap)
	pos = visitados.index(v_act)
	v_act = visitados[pos + 1]
	viajante_wrapper(grafo, grafo_aux, v_act, origen, visitados, heap, peso)



#Creo un heap, una lista de visitados y llamo a una funcion wrapper
#en la que modificara la lista visitados. 
#Esta tendra el orden en que deben ser visitados las ciudades.
#Devuelvo la lista y el peso total del viaje.
def viajante(grafo, origen):
	visitados = []
	heap = []
	peso = 0
	visitados.append(origen)
	(peso, visitados) = viajante_wrapper(grafo, grafo, origen, origen, visitados, heap, peso)
	return peso, visitados