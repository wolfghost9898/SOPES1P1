# PROYECTO 1 SISTEMAS OPERATIVOS 1

## API
Aplicacion Desarrollada en el Lenguaje de Programacion Python, utilizando Flesk como framework, encargada de hacer peticiones a una base de datos no relacional (mongoDB), y a su vez, permite consultar archivos generados por los modulos, que nos permite ver la informacion del cpu y la memoria del servidor

## BALANCEADOR
Aplicacion Desarrollada en el Lenguaje de Programacion Python, utilizando Flesk como framework, encargada de gestionar las peticiones, como su nombre lo indica, es un balanceador de carga.
Basandose en ciertos criterios toma la decision de redigir las peticiones al servidor A o B

## CLIENT
Aplicacion de consola Desarrollada en python, la aplicacion es capaz de leer un archivo y separarlos en oraciones, asignandole un usuario aleatorio a cada oracion, estas oraciones son enviadas a una URL que el usuario puede indicar la URL donde desea hacer la peticion, en este caso seria a la IP del balanceador de cargas, mostrando siempre el resultado de cada peticion

## FRONTEND
Aplicacion web desarrollada en ReactJS, la aplicacion web es capaz de visualizar en tiempo real las oraciones almacenadas en el Servidor A y en el Servidor B, asi como mostrar el % de utilizacion de CPU y de memoria  de cada servidor en tiempo Real.

## MODULOS
Modulos desarrollados en C, estos modulos obtienen el porcentaje de utilizacion de la memoria ram y del cpu del servidor. Para su instalacion se tiene que hacer uso de los comandos:
    
    - make
    - insmod <nombre>