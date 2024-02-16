def organizador(a):
    a = list(a)
    a.sort()
    b = ""
    for letra in a:
        b=b+letra
    return b



filename = "C:\\Users\\anaca\Documents\GitHub\plneb-2324\data\CIH Bilingual Medical Glossary English-Spanish.txt"
file = open (filename, encoding="utf8")
text = file.read()

#Remover caractéres que não são letras
remover="\|!()[]+*-.;:,_/#$%&=?'1234567890"

for elemento in remover:
    text = text.replace(elemento, "")

text = text.lower()

tokens = text.split()
#Retirar palavras repetidas
tokens = list(set(tokens))

anagramas = {}
res = []
for token in tokens:
    chave = organizador(token)
    if chave in list(anagramas.keys()):
        anagramas[chave].append(token)
        res.append(chave)
    else:
        anagramas[chave] = [token]

res.sort()
for solucao in res:
    print(solucao, ":", anagramas[solucao])
