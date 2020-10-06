import os 
import requests
import random
from Files.file import *

flagArchivo = 0; #Variable que me indica si pude o no, abrir un archivo
data = [] ;
flagDireccion = 0 #Nos indicara si esta ingresada la direccion o no
direccionURL = ""

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
    flagDireccion = 0
    data = [];
    usuarios = ["Carlos","Ana","Juan","Luis","Maria","Gabriela"];
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
        #-------------------------------- ALMACENAMOS LA DIRECION URL PARA HACER LAS PETICIONES --------------------------------------
        elif(numero == 2):
            direccionURL = input("Ingresa una url valida para realizar la peticion")
            flagDireccion = 1
        #----------------------- MOSTRAR DATA DEL ARCHIVO ----------------------------
        elif (numero == 3):
            if flagArchivo == 1:
                print(data);
                input();
            else: 
                print("No se ha leido ningun archivo todavia");
                input();
        #------------------------- ENVIAR LA PETICION-----------------------------------
        elif (numero == 4):
            if flagArchivo == 1:
                if flagDireccion == 1:
                    for element in data:
                        newData = {'usuario' : random.choice(usuarios), 'oracion' : element}
                        resultado = requests.post(direccionURL, json = newData)
                        print(newData)
                        if(resultado.status_code != 200):
                            print("Error al enviar la oracion al servidor")
                        else:
                            print("Respuesta del Servidor:")
                            resultado = resultado.json()
                            print(resultado)
                        
                    input()
                else:
                    print("No se ha ingresado una URL valida");
                    input();  
            else:
                print("No se ha leido ningun archivo todavia");
                input();
        #-------------------------- REPETIR --------------------------------------------
        else:
            break;
        
        

    

main();