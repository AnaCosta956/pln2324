## Sumário
Esta semana foi proposta a implementação da funcionalidade busca por palavras que existam quer na designação, quer na descrição dos termos. 

## Decisões de implementação
Desta vez, e ao contrário do que implementei no trabalho de casa anterior, a busca devolve como resultado todos os termos que possuam a palavra ou palavras que forem inseridas na barra de pesquisa na designação ou descrição. 

Para tal, a cada pesquisa, foi necessário percorrer o dicionário de conceitos e verificar se as palavras utilizadas na pesquisa fazem parte da designação ou da descrição de cada termo. Caso se verifique, o termo é adicionado ao dicionário res. No fim, é carregada a página com os resultados, na qual pode ser visualizada a designação e descrição dos termos que resultaram da pesquisa. Também é possível abrir a página de cada um dos termos, de forma a obter toda a informação acerca dele.