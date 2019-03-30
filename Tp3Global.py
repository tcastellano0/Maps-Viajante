import sys


#Print generico de errores, return False porque ante errores
#debemos cortar el flujo.
def printError(descError):
	print("ERROR: " + descError, sys.stderr)

def printInfo(descInfo):
	print(descInfo, sys.stdin)
