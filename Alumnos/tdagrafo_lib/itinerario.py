def itinerario_wrapper(grafo, ciudad_1, ciudad_2, viaje, peso):
	if not ciudad_1 and not ciudad_2:
		return peso, viaje
	for c_1 in ciudad_1:
		if c_1 not in ciudad_2:
			viaje.append(c_1)
			if len(viaje) > 1:
				peso += grafo.peso_arista(viaje[-1], c_1)
			while c_1 in ciudad_1:
				pos = ciudad_1.index(c_1)
				ciudad_1[pos] = None

	for c_2 in ciudad_2:
		while c_2 in ciudad_2:
			pos = ciudad_2.index(c_2)
			if ciudad_1[pos] == None:
				cant = ciudad_2.count(c_2)
				if cant == 1:
					viaje.append(c_2)
					peso += grafo.peso_arista(viaje[-1], c_2)
				ciudad_2[pos] = None
			else:
				break
	return itinerario(grafo, ciudad_1, ciudad_2, viaje, peso)





def itinerario(grafo, ciudad_1, ciudad_2):
	viaje = []
	peso = 0
	return itinerario_wrapper(grafo, ciudad_1, ciudad_2, viaje, peso)
