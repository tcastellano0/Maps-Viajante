import sys
import Consola

def main():


    if(len(sys.argv) == 3):
        consola_actual = Consola.Consola(sys.argv[1], sys.argv[2])
        consola_actual.responder_stdin()

    sys.exit(0)



#---------------------------------
if __name__ == '__main__':
    main()
