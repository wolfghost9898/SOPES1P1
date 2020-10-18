import os
from flask import Flask,jsonify,request
import json
from flask_cors import CORS, cross_origin
import requests
from task.Save import *
from requests.exceptions import ConnectionError


app = Flask(__name__)
app.debug = True 
CORS(app)

servidorA = "http://13.58.77.109:4200/"
servidorB = "http://3.137.205.185:4200/"


'''
RUTA PARA Ejecutar el balanceador
usuario -> nombre del usuario
oracion -> oracion correspondiente al usuario
'''
@app.route("/balanceador", methods=['POST'])
def addOracion():
    usuario = request.json['usuario']
    oracion = request.json['oracion']

    statusA = True
    statusB = True
    try:
        responseA = requests.get(servidorA)
    except ConnectionError:
        statusA = False
    try:
        responseB = requests.get(servidorB)
    except ConnectionError:
        statusB = False
    
    #print(responseA.json())
    #Si hay un error con el servidor A y en el B se notifica
    if(statusA == False and statusB == False):
        return errorGuardar()
    
    #El servidor A esta caido
    if(statusA == False):
        return guardarServidorB(servidorB,{'usuario':usuario,'oracion':oracion})
    #El servidor B esta caido
    if(statusB == False):
        return guardarServidorA(servidorA,{'usuario':usuario,'oracion':oracion})
    

    oracionesA = requests.get(servidorA + 'getAll')
    oracionesA = oracionesA.json()
    oracionesA = oracionesA["result"]

    oracionesB = requests.get(servidorB + 'getAll')
    oracionesB = oracionesB.json()
    oracionesB = oracionesB["result"]


    ######################### COMPARAR CANTIDAD DE DATOS ###########################################    
    if(len(oracionesA) > len(oracionesB)):
        print("B tiene menos datos que A")
        return guardarServidorB(servidorB,{'usuario':usuario,'oracion':oracion})
    
    if(len(oracionesA) < len(oracionesB)):
        print("A tiene menos datos que B")
        return guardarServidorA(servidorA,{'usuario':usuario,'oracion':oracion})
    
    
    


    ############## COMPARAR SPECS DEL SERVIDOR ##################################
    dataA = responseA.json();
    dataB = responseB.json();

    memoriaRAMA = dataA['ram']
    memoriaRAMB = dataB['ram']

    cpuA = dataA['cpu']
    cpuB = dataB['cpu']

    #Si el servidor B tiene menos Ram utilizada que el servidor A -> Almacenamos en B
    if(memoriaRAMA > memoriaRAMB):
        print("Menos RAM B")
        return guardarServidorB(servidorB,{'usuario':usuario,'oracion':oracion})

        #Si el servidor A tiene menos Ram utilizada que el servidor B -> Almacenamos en A
    if(memoriaRAMA < memoriaRAMB):
        print("Menos RAM A")
        return guardarServidorA(servidorA,{'usuario':usuario,'oracion':oracion})
    
    #Si el servidor B tiene menos cpu utilizado que el servidor A -> Almacenamos en B
    if(cpuA > cpuB):
        print("MENOS CPU B")
        return guardarServidorB(servidorB,{'usuario':usuario,'oracion':oracion})
    
    #Si el servidor A tiene menos cpu utilizado que el servidor B -> Almacenamos en A
    if(cpuA < cpuB):
        print("MENOS CPU A")
        return guardarServidorA(servidorA,{'usuario':usuario,'oracion':oracion})

    #Si todo es igual guardamos en A
    print("Todo Igual")
    return guardarServidorA(servidorA,{'usuario':usuario,'oracion':oracion})
    






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)