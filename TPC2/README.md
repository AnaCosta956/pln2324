## Sumário
Conjunto de algoritmos de procura de padrões em *strings*, utilizando expressões regulares e funções como o *search, match* e *findall* do módulo *re*, e de manipulação das mesmas utilizando a função *sub* e *split*, também do módulo *re*.

## Decisões de implementação
No exercício 2, foram considerados como sinais válidos de pontuação, que representam o fim de frase, o ".", "!" e o "?", sendo que a frase pode terminar em mais do que um deles. Por exemplo: "Ok?!".

No exercício 7, considerando que se deseja avaliar a validade da string, dada à função, como nome de variável e não se a string contem um elemento que as condições foi necessário utilizar o caractéres "^" e "$" e no início e fim, respetivamente, da expressão regular. Por exemplo: "! A1n1_a", se a expressão regular utilizada fosse "[A-Za-z]\w*" a string seria considerada válida como nome de variável apesar de possuir um espaço e um "!".

No exercício 9, para que vários espaços fossem substituidos por apenas um *underscore* foi utilizado na, expressão regular, o caractere "+", ou seja, um ou mais espaços serão substituidos por apenas um *underscore*.

No exercício 10, se os elementos da lista corresponderem ao formato de um código-postal, \d\d\d-\d\d\d\d, verificado utilizando a função search, é utilizado o split pelo - para os dividir em dois elementos que serão guardados num tuplo. Foi utilizado a função search em lugar de match por forma a evitar que o codigo seja considerado inválido caso seja entroduzido com um espaço no início. 

