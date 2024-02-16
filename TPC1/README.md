## Sumário
Algoritmo capaz de processar um ficheiro de texto, incluindo retirar caractéres que não são letras, e contruir um dicionário de classes de anagramas, sendo que a chave de cada entrada corresponde aos caractéres que formam o anagrama ordenados alfabeticamente.  

### Decisões de implementação
Foi criada a função organizador que recebe uma string e a transforma numa lista de caractéres. É utilizado o método *sort* para organizar esta lista alfabeticamente e, utilizando um ciclo *for*, os elementos desta são concatenados de forma a formar uma nova string, cujos caracteres estão ordenados. 
De forma a ser mais fácil identificar os anagramas presentes no dicionário, são guardadas as chaves com mais de duas palavras no dicionário res.