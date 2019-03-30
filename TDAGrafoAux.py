import copy
import Tp3Global
import TDAGrafo
import Archivo


#Recibe un diccionario y lo convierte en grafo.
def grafo_crear_desde_CSV(archivo_csv):
    grafo_en_diccionario = Archivo.diccionario_de_CSV(archivo_csv)
    grafo_nuevo = TDAGrafo.Grafo()

    for ciudad, info in grafo_en_diccionario.items():
        vertice_nuevo = TDAGrafo.Vertice()
        vertice_nuevo.datos = info.get("coordenadas")
        grafo_nuevo.agregar_vertice(ciudad, vertice_nuevo)

    for ciudad, info in grafo_en_diccionario.items():
        for v_ady in info.get("adyacentes"):
            vertice_adyancete = v_ady[0]
            peso = v_ady[1]
            grafo_nuevo.agregar_arista(ciudad, vertice_adyancete, peso)
            grafo_nuevo.agregar_arista(vertice_adyancete, ciudad, peso)
            

    return grafo_nuevo

def grafo_mostrar_camino(grafo, vertices_camino, archivo_kml, descripcion_kml):
    vertices = {}
    vertice_anterior = None
    peso_camino = 0
    for vertice in vertices_camino:
        vertices[vertice] = grafo.obtener_info(vertice).datos
        if vertice_anterior:
            peso_camino = peso_camino + grafo.peso_arista(vertice_anterior, vertice)
        vertice_anterior = vertice

    #Print y Exporta los datos al kml.
    print(" -> ".join(vertices_camino))
    print("Costo total: {0}".format(peso_camino))
    Archivo.kml_armar_camino(vertices, archivo_kml, descripcion_kml)

def grafo_exportar_csv(grafo, archivo_csv):
    Archivo.csv_armar_desde_grafo(grafo, archivo_csv)
