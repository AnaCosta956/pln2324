#negrito: designação
#texto normal: descrição do termo 

#\f: quebra de página

import re
f = open("TPC3\dicionario_medico.txt", "r", encoding="utf-8")
texto = f.read()

texto = re.sub(r"([^\.])\n\n([^\f])", r"\1.\n\n\2", texto) 

texto = re.sub(r"\fSabin, vacina", "Sabin, vacina", texto)
texto = re.sub(r"\fJ\n",r"J\n", texto)
texto = re.sub(r"(ficações terminais dos brônquios, apresentando cal)\n", r"\1\nSem descrição.\n\n", texto)
texto = re.sub(r"( - do lat.)\n\n\f", r"\1\n", texto)

texto = re.sub(r"\n\n\f([A-Z])", r"\n\1", texto) 
texto = re.sub(r"([^\.])\n\n\f([a-z0-9])", r"\1\n\2", texto)
texto = re.sub(r"(\.)\n\n\f([a-z])", r"\1\n\n\2", texto)

texto = re.sub(r"(\.\n\n)(.+)", r"\1@\2", texto) 

termos = re.findall(r"@(.+)\n([^@]+)", texto)


header = "<p><img src='images.jpg'  width='150' height='70' /> <bold>Dicionário Médico</bold></p>"
descricao = "<h3>Este é um dicionário médico desenvolvido em pln</h3>"

body="<body>"
for i, termo in enumerate(termos):
    body += f"<p style='font-size: 30px; color: #01CE7E;'><strong> {i+1}: {termo[0]} </strong></p>"
    body += f"<p style='font-size: 20px;'> {termo[1]} </p>"
    body += "<hr/>"

body += "</body>"

html = header+descricao+body

file_out = open("TPC3\TP3.html", "w", encoding="utf-8")
file_out.write(html)
file_out.close()
