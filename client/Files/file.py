import re

#Abrira un archivo y devolvera el contenido, o un error si no existe dicho archivo
def abrirArchivo(direccion):
    try:
        with open(direccion,'r') as f:
            #print("Contenido: ");
            #print(f.read());      
            return f.read();
    except:
        print("No existe el archivo: ",direccion)
        return 0;
    

#Metodo que separa el contenido en oraciones y devolvera un arreglo de las mismas
def separarOraciones(contenido):
    data = contenido.split(".");
    return data;


    

