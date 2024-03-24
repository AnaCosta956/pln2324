from flask import Flask, render_template
import json
from flask import request, redirect
import re

app = Flask(__name__)

file = open("TPC6\\conceitos_com_traducao.json", "r", encoding="utf8")
conceitos = json.load(file)
  
lista_conceitos = list(conceitos.keys())


@app.route("/")
def home():
    q = request.args.get("q")
    if q is not None:
        q = q.lower()
        if q in conceitos:
            link = "/conceitos/" + q
            print(link)
            return redirect( link, code=302)
    
    return render_template('home.html')

@app.route("/conceitos")
def listar_conceitos():
    q = request.args.get("q")
    
    if q is not None:
        q = q.lower()
        if q in conceitos:
            link = "/conceitos/" + q
            print(link)
            return redirect( link, code=302)
    
    return render_template('conceitos_tudo.html' , termos = conceitos)

@app.route("/conceitos/<designacao>")
def consultar_conceitos(designacao):
    q = request.args.get("q")
    
    if q is not None:
        q = q.lower()
        if q in conceitos:
            link = "/conceitos/" + q
            print(link)
            return redirect( link, code=302)
    
    i_atual = lista_conceitos.index(designacao)
    termo_seguinte = lista_conceitos[i_atual+1]
    termo_anterior = lista_conceitos[i_atual-1]
        
    return render_template('conceito.html', desig=designacao, termo=conceitos[designacao], anterior = termo_anterior, seguinte = termo_seguinte)

app.run("localhost", port=8000, debug=True)