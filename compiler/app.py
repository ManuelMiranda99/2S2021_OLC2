from flask import Flask, request, render_template
from Grammar import grammar
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

@app.route("/", methods=['GET'])
def home_view():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

'''
print(5 + 5);
println(1 * 100 / 2);
println(5 > 0);
println(true);
println((5 == 10) == false);
println((5 == 10) && (1 != 1));
println((5 == 10) || (1 == 1));

a = (10 + 10) * (8 / (2+2));
b = "Que tal";
c = true;

println("Hola Mundo!");
println(a);
println(b);
println(c);
'''