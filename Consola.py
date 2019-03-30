import sys
import FuncCom
import Tp3Global

COMANDO_IR = "ir"
COMANDO_IR_CANTPARAMS = 2
COMANDO_VIAJE = "viaje"
COMANDO_VIAJE_CANTPARAMS = 2
COMANDO_ITINERARIO = "itinerario"
COMANDO_ITINERARIO_CANTPARAMS = 1
COMANDO_REDUCIR_CAMINOS = "reducir_caminos"
COMANDO_REDUCIR_CAMINOS_CANTPARAMS = 1

#Este objeto maneja toda la logica de la consola, por ejemplo el print
#de errores, validaciones que le hagamos a las lineas que entren, etc
#fijate que tiene un estado, un comando_actual que es el comando que se va a
#ejecutar en esa linea y despues comandos, que son los comando programados en
#Comandos, de esta forma encapsule el grafo solo en el otro objeto y no tenemos
#que pasarlo por parametro en todas las funciones.

class Consola(object):

    def __init__(self, _archivo_csv, _archivo_kml):
        self.tiene_error = False
        self.comando_actual = ""
        self.comandos = FuncCom.Comandos(_archivo_csv, _archivo_kml)

    def responder_stdin(self):
        for linea in sys.stdin:
            self.responder_linea(linea)
            if self.tiene_error:
                break;

    def responder_linea(self, linea):
        if linea == "\n":
            self.error_invalido()
            return

        vec_linea = linea.split(" ", 1)
        self.comando_actual = vec_linea[0]
        self.ejecutar_comando(vec_linea)

    def ejecutar_comando(self, vec_linea):
        vec_linea = vec_linea[1].split(", ")
        cant_params = len(vec_linea)
        vec_linea[cant_params - 1] = vec_linea[cant_params - 1].replace("\n", "")

        if self.comando_actual == COMANDO_IR:
            if cant_params != COMANDO_IR_CANTPARAMS:
                self.error_params()
                return

            self.comandos.camino_minimo(vec_linea[0], vec_linea[1])

        elif self.comando_actual == COMANDO_VIAJE:
            if cant_params != COMANDO_VIAJE_CANTPARAMS:
                self.error_params()
                return

            if vec_linea[0] == "optimo":
                self.comandos.viajante(vec_linea[1])
            elif vec_linea[0] == "aproximado":
                self.comandos.viajante_aproximado(vec_linea[1])
            else:
                self.error_invalido()

        elif self.comando_actual == COMANDO_ITINERARIO:
            if cant_params != COMANDO_ITINERARIO_CANTPARAMS:
                self.error_params()
                return

            self.comandos.itinerario(vec_linea[0])
            #correr comando aca

        elif self.comando_actual == COMANDO_REDUCIR_CAMINOS:
            if cant_params != COMANDO_REDUCIR_CAMINOS_CANTPARAMS:
                self.error_params()
                return

            self.comandos.arbol_tendido_minimo(vec_linea[0])

        else:
            self.error_invalido()

    def mostrar_mensaje(self, desc_mensaje):
        Tp3Global.printInfo(desc_mensaje)

    def error_params(self):
        self.error("Parametros invalidos para el comando {0}".format(self.comando_actual))

    def error_invalido(self):
        self.error("Ingreso un comando invalido")

    def error(self, desc_error):
        self.tiene_error = True
        Tp3Global.printError(desc_error)
