## Sumário
O trabalho desta semana consistiu na atualização do programa, criado durante as aulas, de forma que a tradução, em inglês, dos termos apareça na etiqueta. 

## Decisões de Implementação
Primeiramente, foi utilizada a função *findall* de forma a criar uma lista com os tuplos dos termos em português e inglês, presentes no ficheiro "termos_traduzidos". A esta lista foi aplicado o método *dict* de modo a criar o dicionário "designacao_traduzida", cujas chaves são a designação do termo em português e o valor corresponde à sua tradução. \
De seguida, foi utilizado um ciclo *for* e o bloco *try except* para adicionar ao conceitos_traducao a descrição de cada termo, presentes no ficheiro "conceitos_medico", bem como a sua tradução, proveniente do dicionário "designação_traducao". Foi necessário utilizar  o bloco *try except*, visto que nem todos os termos presentes em "conceitos_medicos" tinham tradução, nestes casos foi definido que o valor da tradução seria Unknown. \
Por fim, no elemento âncora foi necessário adicionar ao *title* o termo traduzir.


## Dificuldades
Uma vez que a maioria do código foi desenvolvido ao longo das aulas não foram encontradas situações de grande dificuldade, o único incoveniente foi a existência de termos sem tradução.