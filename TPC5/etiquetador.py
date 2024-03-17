import json
import re
file_conceitos = open("TPC5\\conceitos_medico.json", encoding="utf-8")
conceitos = json.load(file_conceitos)
file_conceitos.close()

f = open("TPC5\\termos_traduzidos.txt", "r",  encoding="utf8")
traducao = f.read()
f.close()
designacao_traduzida = dict(re.findall("(.+) @ (.+)", traducao))

conceitos_traducao = {}
for chave in conceitos:
    conceitos_traducao[chave] = {}
    conceitos_traducao[chave]["desc"] = conceitos[chave]
    #nem todas as designações estão traduzidas, para não dar erro
    try:
        conceitos_traducao[chave]["en"] = designacao_traduzida[chave]
    except:
        conceitos_traducao[chave]["en"] = "Unknown"

file_livro = open("TPC5\\Aparelho_Digestivo.txt", encoding="utf-8")
texto = file_livro.read()
file_livro.close()

palavras = texto.split(" ")

blacklist =["e", "pelo", "os", "para", "são", "de", "J", "este"]

conceito_min = {chave.lower(): conceitos_traducao[chave] for chave in conceitos_traducao}


def etiquetador(matched):
    palavra = matched[0]
    original = palavra
    palavra = palavra.lower()

    if palavra in conceito_min and palavra not in blacklist:
        descricao = conceito_min[palavra]["desc"]
        traducao = conceito_min[palavra]["en"]
        
        etiqueta = f"<a href='' title='en: {traducao} ;\nDescrição: {descricao}'> {original}</a>"
        return etiqueta
    else:
        return original


expressao = r"[^\s.-]+"
texto = re.sub(r"\n", r"<br>", texto)
texto = re.sub(expressao, etiquetador, texto, flags=re.IGNORECASE)
texto = re.sub(r"\f", r"<hr/>", texto)

file_out = open("livro.html", "w", encoding="utf8")
print(texto, file = file_out)

