import csv
import TDAGrafo


#Devuelve un diccionario con las ciudades leidas
def diccionario_de_CSV(archivo_csv):
    ciudades = {}
    leer_coordenadas = False

    with open(archivo_csv,'r') as f:
        for row in f:
            vec_row = row.split(",")
            if len(vec_row) == 1:
                leer_coordenadas = not leer_coordenadas
                continue

            una_ciudad = vec_row[0]
            vec_row[2] = vec_row[2].replace("\n", "")

            if leer_coordenadas:
                ciudades[una_ciudad] = {
                    "coordenadas": [vec_row[1], vec_row[2]],
                    "adyacentes": []
                }
            else:
                lst_adyacentes = ciudades[una_ciudad].get("adyacentes", [])
                lst_adyacentes.append([vec_row[1], int(vec_row[2])])

        return ciudades

def csv_armar_desde_grafo(grafo, archivo_csv):
    with open(archivo_csv, 'w') as csv:
        #Armo las ciudades
        csv.write(str(grafo.cantidad) + "\n")
        for vertice in grafo.obtener_vertices():
            csv.write(
                "{0},{1} \n".format(vertice, ",".join(grafo.obtener_info(vertice).datos))
            )

        tot_adyacencias = 0
        for vertice in grafo.obtener_vertices():
            tot_adyacencias = tot_adyacencias + grafo.cantidad_adyacentes(vertice)

        csv.write(str(tot_adyacencias) + "\n")
        for vertice in grafo.obtener_vertices():
            for adyacente in grafo.obtener_adyacentes(vertice):
                csv.write("{0},{1},{2} \n".format(vertice, adyacente, grafo.peso_arista(vertice, adyacente)))







#Funciones para exportar un kml, recibe un diccionario de vertices
#y lo exporta a formato kml.
def kml_armar_vertice(kml, nombre, coordenadas):
    kml.write("<Placemark> \n")
    kml.write("     <name>" + nombre + "</name> \n")
    kml.write("     <Point> \n")
    kml.write("         <coordinates>" + coordenadas + "</coordinates> \n")
    kml.write("     </Point> \n")
    kml.write("</Placemark> \n")

def kml_armar_arista(kml, coordenadas_ini, coordenadas_fin):
    kml.write("<Placemark> \n")
    kml.write("     <LineString> \n")
    kml.write("         <coordinates>" + coordenadas_ini + " " + coordenadas_fin + "</coordinates> \n")
    kml.write("     </LineString> \n")
    kml.write("</Placemark> \n")

def kml_armar_camino(dic_vertices_camino, archivo_kml, descripcion_kml):

    with open(archivo_kml, 'w') as kml:
        kml.write('<?xml version="1.0" encoding="UTF-8"?> \n')
        kml.write('<kml xmlns="http://earth.google.com/kml/2.1"> \n')
        kml.write('     <Document> \n')
        kml.write('         <name>Camino</name> \n')
        kml.write('         <description>' + descripcion_kml + '</description> \n')

        coords_vertice_anterior = None
        for vertice, valor in dic_vertices_camino.items():
            kml_armar_vertice(kml, vertice, ", ".join(valor))
            if coords_vertice_anterior:
                kml_armar_arista(kml, ", ".join(coords_vertice_anterior), ", ".join(valor))

            coords_vertice_anterior = valor

        kml.write('     </Document> \n')
        kml.write('</kml> \n')
