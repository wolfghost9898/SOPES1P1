import os 
from Files.file import *

flagArchivo = 0; #Variable que me indica si pude o no, abrir un archivo
data = [] ;


#Se encargara de limpiar la pantalla
def limpiarPantalla():
    if os.name == "posix":
        os.system("clear");
    else:
        os.system("cls");


#Metodo para obtener una opcion valida
def pedirOpcion():
    num = 0;
    while(True):
        try:
            num = int(input("Ingresa una Opcion: "));
            break;
        except ValueError:
            print("Ingrese un numero entero");
    return num;

def main():
    flagArchivo = 0;
    data = [];
    limpiarPantalla();
    while(True):
        print("1. Ingresar Ruta");
        print("2. Ingresar URL");
        print("3. Ver datos");
        print("4. Enviar Datos");

        numero = pedirOpcion();
        limpiarPantalla();
        
        #-------------------------------- OPCION PARA ABRIR UN NUEVO ARCHIVO --------------------------------------------------------
        if(numero == 1):
            direccion = input("Ingresa la ruta del archivo a analizar: ");
            contenido = abrirArchivo(direccion);
            if contenido != 0:
                flagArchivo = 1;
                data = separarOraciones(contenido);
            else:
                flagArchivo = 0;
                data = [];

        elif (numero == 3):
            if flagArchivo == 1:
                print(data);
                input();
            else: 
                print("No se ha leido ningun archivo todavia");
                input();
        else:
            break;

    

main();