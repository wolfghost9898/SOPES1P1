from flask import Flask,jsonify


app = Flask(__name__)

app.debug = True 


################################################### RUTAS ##############################################
@app.route("/",methods=['GET'])
def index():
    return jsonify({'status':200, 'data':'uwu'})

if __name__ == "__main__":
    app.run()