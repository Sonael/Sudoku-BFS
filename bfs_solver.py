import numpy as np

# Define a função para encontrar a próxima célula vazia
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

# Define a função para validar se um número é possível em uma célula
def is_valid(board, num, row, col):
    # Verifica a linha
    for j in range(9):
        if board[row][j] == num and j != col:
            return False
    # Verifica a coluna
    for i in range(9):
        if board[i][col] == num and i != row:
            return False
    # Verifica a sub-grade 3x3
    sub_row = row // 3
    sub_col = col // 3
    for i in range(sub_row*3, sub_row*3 + 3):
        for j in range(sub_col*3, sub_col*3 + 3):
            if board[i][j] == num and (i, j) != (row, col):
                return False
    return True

# Define a função para resolver o jogo usando busca em largura
def solve(board):
    # Adiciona o estado inicial à fila
    queue = [board]
    while queue:
        # Remove o primeiro estado da fila
        current_board = queue.pop(0)
        # Encontra a primeira célula vazia
        empty_cell = find_empty(current_board)
        if not empty_cell:
            # Se não houver células vazias, o jogo está resolvido
            return current_board
        else:
            row, col = empty_cell
            # Testa todos
            for num in range(1, 10):
                if is_valid(current_board, num, row, col):
                    # Cria uma cópia do tabuleiro atual com o número inserido
                    new_board = current_board.copy()
                    new_board[row][col] = num
                    # Adiciona o novo estado à fila
                    queue.append(new_board)
    # Caso não encontre solução, retorna None
    return None

# Define a função para imprimir o tabuleiro
def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")