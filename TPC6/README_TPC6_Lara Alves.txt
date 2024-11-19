Este projeto é uma aplicação interativa para organizar informações escolares. Permite criar turmas, adicionar alunos, listar e consultar informações, além de salvar ou carregar turmas de arquivos. O sistema é insensível a maiúsculas e minúsculas, garantindo facilidade de uso.

Estrutura de Dados
A escola é representada por uma lista de turmas, sendo cada turma uma tupla composta pelo nome da turma e uma lista de alunos. Os alunos, por sua vez, são definidos por uma tupla que contém o nome, um ID exclusivo e uma lista de três notas.

Funcionalidades
MostrarMenu(): Exibe as opções do menu interativo para o utilizador navegar pelas funcionalidades da aplicação.
existeturma(nome_turma, escola): Verifica se uma turma já está cadastrada, ignorando diferenças entre maiúsculas e minúsculas.
CriarTurma(nome_turma, escola): Adiciona uma nova turma à lista de turmas da escola, desde que ainda não exista, utilizando a função existeturma() para validação.
inserir_aluno(nome_turma, aluno): Adiciona um aluno a uma turma específica, garantindo que o ID do aluno seja único antes da inclusão.
listar(nome_turma): Lista todos os alunos de uma turma específica, mostrando o nome, ID e notas. Caso a turma não seja encontrada, exibe uma mensagem de erro.
consultar_aluno(id_aluno, nome_turma): Pesquisa um aluno pelo ID numa turma e apresenta suas informações ou uma mensagem indicando que não foi encontrado.
guardar_turma(nome_turma, fnome): Salva os dados de uma turma num arquivo de texto, utilizando o formato Nome,ID#NotaTPC,NotaProj,NotaTeste para cada linha.
recuperar_turma(fnome): Carrega os dados de uma turma a partir de um arquivo e devolve uma lista com os alunos e as suas respetivas informações.
Menu(): Controla o fluxo principal do programa, chamando as funções apropriadas com base na escolha do utilizador.

Como Usar
Para começar, basta executar o código. O menu será exibido com várias opções disponíveis. Pode criar turmas, adicionar alunos, listar os seus dados, fazer consultas por ID, salvar turmas em arquivos, carregar turmas já existentes, ou sair da aplicação.

Por exemplo, ao selecionar a opção de listar alunos e fornecer o nome da turma turmaA, o programa exibirá todos os alunos e as suas notas, tratando turmaA, TURMAA ou turmaa como iguais.

Notas Adicionais
O sistema foi desenvolvido para garantir simplicidade e funcionalidade. Nomes de turmas são tratados sem distinção entre maiúsculas e minúsculas, e os IDs dos alunos são sempre únicos dentro de cada turma para evitar duplicação.

Conclusão
O Sistema de Gestão de Alunos oferece uma solução prática e eficiente para organizar informações escolares. A estrutura modular permite fácil manutenção e ampliações futuras, tornando-o ideal para diversas necessidades académicas.