## Sumário
Programa para processamento e extração de termos, constituidos por designação e descrição, de um dicionário médico. Após a criação da lista de termos foi desenvolvido um ficheiro html de forma a ser possível visualizar os mesmos.

## Decisões de implementação
De forma a ser possível identificar as designações e, consequentemente o início de cada temo, foi definido que deveria ser adicionado o "@" antes de cada uma delas. No entanto, antes de realizar a adição deste marcador procedeu-se à realização de transformações para uniformizar o padrão do documento. Concretamente, foi adicionado um ponto final, quando este não existia, no fim das descrições dos termos, para tal, foi utilizado o padrão "[^.]\n\n[^\f]". Foi essencial excluir situações com \f, pois estas tratam-se de situações excecionais com abordagens de tratamento diferentes. 
No que se refere às instâncias de pagebreak, representadas no documento txt, pelo padrão "\n\n\f", foi possível perceber que este pode ocorrer, de forma mais comum, em 4 situações:
    - entre frases da descrição, sendo que antes do \n\n\f se encontra um ponto final e depois o início de uma nova frase, que começa por uma letra maiúscula;
        Exemplo:
            quimiotaxia
            Afinidade ou repulsa de células ou organismos vivos, no sentido positivo ou negativo, para substâncias químicas.

            A quimiotaxia positiva regula a leucocitose, a quimioterapia, sobretudo a quimioterapia específica, e outros fenômenos biológicos.

    -entre a designação do termo e a sua descrição;
        Exemplo:
            atrepsia

            Atrofia do lactente; caquexia em conseqüência de danos nutritivos.

    Decisão de tratamento implementada:
        Para ambos os casos anteriores foi percetivel que, após o \n\n\f, a existência de uma letra maiúscula ou número correspondia ao restante ou ao início da descrição, portanto, utilizando o re.sub, procedeu-se à eliminação do \n\f.

    -entre frases da descrição, sendo que antes do \n\n\f não se encontra um ponto final, a frase continua após a quebra;
        Exemplo:
            Aquiles, tendão de
            O mais forte tendão do corpo humano, situado póstero-inferiormente em cada perna, estendendo-se ao osso

            calcâneo.

        Decisão de tratamento implementada:
            Considerando que antes do padrão \n\n\f não existe um ponto final, conclui-se que a descrição não está completa e, portanto, o que se segue corresponde ao resto da mesma, sendo que começa por uma letra minúscula. Foi utilizado o padrão "([^\.])\n\n\f([a-z])" para identificar estas situações e eliminar o \n\f.  

    -entre dois termos;
        Exemplo:
            apogeusia
            Distúrbio no sentido do gosto.

            apoginia
            Perda da capacidade reprodutora do órgão feminino.
        
        Decisão de tratamento implementada:
            Neste caso, a existência de um ponto final antes do padrão \n\n\f e de uma letra minúscula depois permite afirmar que o pagebreak ocorre entre dois termos, sendo necessário apenas retirar o \f, pois a separação entre termos definida é o \n\n.

Apesar de estes cenários abrangerem a maioria dos casos presentes no documento, foram identificadas 4 excessões, que, por impossibilidade de encontrar outra solução que não comprometesse as decisões anteriores, foram tratadas especificamente antes das alterações referidas previamente. Estas exceções são apenas as que foram identificados, sendo possível que existem mais ocorrências de erros. 

Após todo o tratamento, todos os termos começam com um @ e terminam com um ".", o que permitiu utilizar o padrão "@(.+)\n([^@]+)" para separar os termos, sendo que a função devolve um tuplo com dois elemento, o 1º corresponde à designação e o 2º à descrição.

Para visualizar o conteúdo do dicionário, foi criado um ficheiro html.

## Dificuldades
A existência de erros de formatação no documento como frases a meio, sem ponto final, ou termos sem descrição, tornaram a descoberta de padrões que definissem os termos muito difícil. Como referido anteriormente, acredito que ainda existam erros no documento, mas devido ao seu tamanho extenso era impossível avaliar todos os termos individualmente.
