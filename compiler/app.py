from flask import Flask, request, render_template
from Grammar.Grammar import grammar
from Grammar.Optimization import optimization
from Symbol.Environment import Environment
from Symbol.Generator import Generator

app = Flask(__name__)

@app.route("/compile", methods=['POST'])
def compile():
    try:
        inpt = request.json['input']

        genAux = Generator()
        genAux.cleanAll()
        generator = genAux.getInstance()

        newEnv = Environment(None)
        ast = grammar.parse(inpt)
        try:
            for instr in ast:
                instr.compile(newEnv)
        except:
            print("Error al compilar instrucciones")
        return { 'msg': generator.getCode(), 'code': 200 }
    except:
        print('Error')
        return { 'msg': 'ERROR', 'code': 500 }

@app.route("/optimize", methods=['POST'])
def optimize():
    try:
        inpt = request.json['input']

        instructions = optimization.parse(inpt)
        
        instructions.Mirilla()

        out = instructions.getCode()

        return { 'msg': out, 'code': 200 }
    except:
        print('Error')
        return { 'msg': inpt, 'code': 500 }

@app.route("/", methods=['GET'])
def home_view():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')