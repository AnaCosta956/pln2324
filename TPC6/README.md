## Sumário
O trabalho proposto para esta semana consistia na melhoria da página de consulta dos termos individuais. 

## Decisões de implementação
De forma a permitir a visualização agradável da informação acerca dos termos, incluindo da sua descrição e traduções, foram utilizados exemplos do site ‘Bootstrap’. 
Na página de cada conceito, como referido anteriormente, são apresentados a sua descrição e, caso as possua, as suas traduções em diferentes línguas. Para atingir esta funcionalidade, foi utilizado um ciclo for, no ficheiro html, possível graças à ferramenta ‘Jinja’, para iterar as chaves presentes no dicionário.

Para além disso, foram implementados três botões, sendo que dois deles permitem ir até à página do termo alfabeticamente anterior e posterior e o terceiro permite voltar à página de todos os termos.

Por fim, foi implementada uma barra de pesquisa, que permite inserir a designação de um termo e se esta estiver escrita corretamente, maiúsculo e minúsculo é ignorado, o utilizador é redirecionado para a página desse termo.

## Problemas/ Dificuldades
Existem termos cujas designações possuem o caracter “/”, o que interfere com a criação do link de acesso. Sabendo que são apenas 3 termos nesta situação, decidi alterar manualmente, no ficheiro json, a "/" para ",".
