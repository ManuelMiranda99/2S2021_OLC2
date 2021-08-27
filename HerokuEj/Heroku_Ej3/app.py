from flask import Flask, request, render_template

from Grammar import grammar
from Export import output
from Symbol.Environment import *

app = Flask(__name__)

# ESTE SERA UNA APLICACION DE FLASK WEB. Esta contendrá todos los archivos HTML necesarios para mostrar todo
# LA FORMA DE REALIZAR EL DEPLOY A HEROKU LO PUEDEN VER ACA: https://www.geeksforgeeks.org/deploy-python-flask-app-on-heroku/
@app.route("/execute", methods=['POST'])
def home():
    try:
        output.init()
        inpt = request.json['input']
        
        newEnv = Environment(None)
        output.ast = grammar.parse(inpt)
        try:
            for instr in output.ast:
                instr.execute(newEnv)
        except:
            print("Error al ejecutar instrucciones")
        return { 'msg': output.output, 'code': 200 }
    except:
        return { 'msg': 'ERROR', 'code': 500 }

@app.route("/getTree", methods=['GET'])
def getTree():
    try:
        if output.ast == None:
            return { 'msg': 'No se ha analizado una entrada', 'code': 200 }
        try:
            idRoot = 'root'
            labelRoot = 'root'
            output.addNode(idRoot, labelRoot)
            for instr in output.ast:
                instrId = instr.getDot()
                output.addEdges(idRoot, instrId)
        except:
            print("Error al generar árbol")
        return { 'msg': output.graph.source, 'code': 200 }
    except:
        return { 'msg': 'ERROR', 'code': 500 }

@app.route("/hola")
def hola():
    return { "msg" : "Hola"}

@app.route("/", methods=['GET'])
def home_view():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()