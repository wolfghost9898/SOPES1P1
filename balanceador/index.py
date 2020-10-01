import os
from flask import Flask,jsonify,request
import json
from flask_cors import CORS, cross_origin
import requests
from task.Save import *


app = Flask(__name__)
app.debug = True 
CORS(app)

servidorA = "http://18.222.14.62/"
servidorB = "http://3.17.62.246/"


'''
RUTA PARA Ejecutar el balanceador
usuario -> nombre del usuario
oracion -> oracion correspondiente al usuario
'''
@app.route("/balanceador", methods=['POST'])
def addOracion():
    usuario = request.json['usuario']
    oracion = request.json['oracion']


    responseA = requests.get(servidorA)
    responseB = requests.get(servidorB)
    
    #print(responseA.json())
    #Si hay un error con el servidor A y en el B se notifica
    if(responseA.status_code != 200 and responseB.status_code != 200):
        return errorGuardar()
    
    #El servidor A esta caido
    if(responseA.status_code != 200):
        return guardarServidorB(servidorB,{'usuario':usuario,'oracion':oracion})
    #El servidor B esta caido
    if(responseB.status_code != 200):
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