from flask import Flask, render_template
import json
from flask import request, redirect

app = Flask(__name__)

file = open("TPC7\conceitos_com_traducao.json", "r", encoding="utf8")
conceitos = json.load(file)
file.close()
lista_conceitos = list(conceitos.keys())


@app.route("/")
def home():
       
    return render_template('home.html')

@app.route("/conceitos")
def listar_conceitos():
    return render_template('conceitos_tudo.html' , termos = conceitos)


@app.route("/conceitos", methods=["POST"])
def adicionar_conceito():
    designacao = request.form.get("designacao")
    descricao = request.form.get("descricao")
    traducao = request.form.get("en")
    conceitos[designacao] = {"desc": descricao, "en": traducao}
    
    return render_template('conceitos_tudo.html' , termos = conceitos)

@app.route("/conceitos/search", methods=["POST"])
def resultados_procura():
    q = request.form.get("q").lower()
    res = {}
    if q is not None:
        for chave in conceitos:
            if q in chave.lower() or q in conceitos[chave]['desc'].lower():
                res[chave] = conceitos[chave]
    else:
        res = conceitos
    return render_template("resultados_pesquisa.html", termos = res, pesquisa = q)

@app.route("/conceitos/<designacao>", methods=["DELETE"])
def delete_conceito(designacao):
    del conceitos[designacao]
    return render_template('conceitos_tudo.html' , termos = conceitos)

@app.route("/conceitos/<designacao>")
def consultar_conceitos(designacao):
    lista_conceitos = list(conceitos.keys())
   
    if designacao in conceitos:
        
        i_atual = lista_conceitos.index(designacao)
        if i_atual == 0:
            print("inicio")
            termo_seguinte = lista_conceitos[1]
            termo_anterior = lista_conceitos[-1]
        elif i_atual == (len(lista_conceitos) -1):
            termo_seguinte = lista_conceitos[0]
            termo_anterior = lista_conceitos[i_atual-1]
        else:
            termo_seguinte = lista_conceitos[i_atual+1]
            termo_anterior = lista_conceitos[i_atual-1]
        
        return render_template('conceito.html', desig=designacao, termo=conceitos[designacao], anterior = termo_anterior, seguinte = termo_seguinte)
    
    else:
        return render_template("erro.html", tipo="Conceito não existe na base de dados")
    
@app.route('/table')
def table():
    return render_template("table.html", conceitos = conceitos)

app.run("localhost", port=8000, debug=True)