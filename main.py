from flask import Flask, jsonify, render_template
import unidecode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

  
@app.route('/<letra>')
def pegarletra(letra):
    arq = open("dicionario.txt").read().splitlines()

    xablau = list(filter(lambda x: x[0] == letra, arq))
  
                  
    semacento = []
    for i in xablau:
      semacento.append(unidecode.unidecode(i))
      
    return jsonify({"palavras": semacento})

@app.route('/<letra>/<final>')
def pegarletra2(letra, final):
    arq = open("dicionario.txt").read().splitlines()

    xablau = list(filter(lambda x: x[0]  == letra and x[4] == final , arq))
  
                  
    semacento = []
    for i in xablau:
      semacento.append(unidecode.unidecode(i))
      
    return jsonify({"palavras": semacento})


app.run(host='0.0.0.0')