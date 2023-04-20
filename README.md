# Sudoku Busca em Largura.

O código `bfs_solver` implementa um algoritmo para resolver o jogo Sudoku, utilizando a técnica de busca em largura.

Primeiro, é definido o tabuleiro inicial do jogo, representado por uma matriz numpy. Em seguida, são definidas as seguintes funções:

`print_board(board)`: função para imprimir o tabuleiro na saída padrão, com formatação apropriada para separar as sub-grades 3x3 do Sudoku.

`find_empty(board)`: função para encontrar a próxima célula vazia no tabuleiro. A função percorre a matriz do tabuleiro em busca da primeira célula com valor zero e retorna uma tupla contendo as coordenadas (linha, coluna) da célula encontrada. Caso não haja células vazias, a função retorna None.

`is_valid(board, num, row, col)`: função para verificar se é possível inserir o número num na célula (row, col) do tabuleiro board, de acordo com as regras do jogo. A função realiza três verificações:

1. Verifica se o número já está presente na linha row, exceto na célula (row, col) em questão.

2. Verifica se o número já está presente na coluna col, exceto na célula (row, col) em questão.

3. Verifica se o número já está presente na sub-grade 3x3 que contém a célula (row, col), exceto na própria célula.

Caso o número possa ser inserido na célula, a função retorna True. Caso contrário, retorna False.

`solve(board)`: função principal que implementa o algoritmo de busca em largura para resolver o jogo. A função recebe o tabuleiro inicial como argumento e retorna a solução encontrada ou None, caso não seja possível encontrar uma solução. A função utiliza uma fila (representada por uma lista) para armazenar os estados do tabuleiro a serem explorados. O estado inicial é adicionado à fila e, em seguida, o algoritmo entra em um loop:

1. Remove o primeiro estado da fila.

2. Encontra a primeira célula vazia no estado atual.

3. Testa todos os números de 1 a 9 para a célula vazia encontrada. Para cada número, verifica se é possível inseri-lo na célula, utilizando a função `is_valid()`.

4. Caso seja possível inserir o número na célula, cria uma cópia do estado atual com o número inserido e adiciona essa nova cópia à fila.

5. Repete o processo até que a fila esteja vazia (caso em que não foi possível encontrar uma solução) ou até que todas as células do tabuleiro estejam preenchidas com valores válidos (caso em que a solução foi encontrada).

6. Por fim, o código chama a função solve() com o tabuleiro inicial como argumento e imprime a solução encontrada, caso haja, ou uma mensagem informando que não foi possível encontrar uma solução.
