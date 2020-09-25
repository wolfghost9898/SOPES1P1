from flask import Flask,jsonify,request
from task.Files import abrirArchivo
import json
from flask_pymongo import PyMongo


app = Flask(__name__)

app.debug = True 

######################################### BASE DE DATOS ####################################################
app.config['MONGO_DBNAME'] = 'PROYECTO1'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/PROYECTO1'

mongo = PyMongo(app)



################################################### RUTAS ##############################################
'''
RUTA PARA OBTENER TODA LA INFROMACION DEL SERVIDOR
'''
@app.route("/",methods=['GET'])
def index():
    data = abrirArchivo('/proc/cpu-module')
    if (data == 0):
        return jsonify({'status':400, 'data':'no existe un archivo de informacion para el cpu'})
    
    data = json.loads(data)
    hz = data["HZ"]
    total = data["tiempo"]
    segundos = data["segundos"]

    porcentaje = ((total / hz) / segundos) * 100

    #print(data)

    dataMemoria = abrirArchivo('/proc/memoria-module')
    if (dataMemoria == 0):
            return jsonify({'status':400, 'data':'no existe un archivo de informacion para la memoria'})
    
    dataMemoria = json.loads(dataMemoria)
    #print(dataMemoria)
    return jsonify({
        'status':200, 
        'cpu': porcentaje,
        'total' : dataMemoria['total'],
        'libre' : dataMemoria['libre'],
        'ram' : dataMemoria['uso']
        })

'''
RUTA PARA GUARDAR UNA NUEVA ORACION
usuario -> nombre del usuario
oracion -> oracion correspondiente al usuario
'''
@app.route("/guardarOracion", methods=['POST'])
def addOracion():
    usuario = request.json['usuario']
    oracion = request.json['oracion']
    data = mongo.db.data 
    data_id = data.insert({'usuario' : usuario, 'oracion' : oracion})
    return jsonify({
        'status': 200,
        'data' : 'insertado con exito'
    })


'''
RUTA PARA OBTENER TODAS LAS ORACIONES
ALMACENADAS EN EL SERVIDOR
'''
@app.route("/getAll",methods=['GET'])
def getOraciones():
    data = mongo.db.data
    output = []
    for s in data.find():
        output.append({'usuario' : s['usuario'], 'oracion' : s['oracion']})
    return jsonify({
        'status' : 200,
        'result' : output
        })






if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)