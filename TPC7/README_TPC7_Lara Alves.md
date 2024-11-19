Este projeto é uma aplicação em Python desenvolvida para processar e analisar informações meteorológicas diárias. 
A ferramenta permite calcular estatísticas como a temperatura média, a amplitude térmica e a precipitação, além de criar gráficos que ilustram 
a evolução desses dados ao longo do tempo. Com um menu interativo, a aplicação oferece diversas funcionalidades, como o cálculo da temperatura 
média diária com base nos valores mínimo e máximo registados, a possibilidade de guardar e carregar tabelas meteorológicas em ficheiros, 
a identificação da menor temperatura mínima registada, e o cálculo da amplitude térmica diária, que corresponde à diferença entre as 
temperaturas máxima e mínima.

Outras opções incluem a exibição do dia com a maior precipitação registada e o valor correspondente, a listagem de dias com precipitação acima 
de um valor fornecido pelo utilizador e a determinação do maior período consecutivo com precipitação inferior a esse mesmo limite. Além disso, 
a aplicação é capaz de gerar gráficos de linha para as temperaturas mínima e máxima e gráficos de barras para a precipitação, facilitando a 
visualização e interpretação dos dados.

O programa funciona de maneira simples: ao ser iniciado, apresenta um menu com as opções disponíveis. O utilizador pode selecionar a 
funcionalidade desejada introduzindo o número correspondente, sendo que algumas opções, como os filtros de precipitação, requerem valores 
definidos pelo utilizador. A estrutura dos dados meteorológicos é baseada em listas de tuplas organizadas no formato ((ano, mês, dia), 
temperatura mínima, temperatura máxima, precipitação). 
Um exemplo seria: [((2022, 1, 20), 2, 16, 0), ((2022, 1, 21), 1, 13, 0.2), ((2022, 1, 22), 7, 17, 0.01)].

Esta aplicação foi projetada para simplificar a análise meteorológica, integrando cálculos, armazenamento de dados e visualizações gráficas 
numa interface intuitiva. É uma solução prática para identificar tendências climáticas e realizar estudos baseados em dados históricos.