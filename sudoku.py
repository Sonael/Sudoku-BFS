import numpy as np
from bfs_solver import solve, print_board

# Define o tabuleiro inicial do jogo
board = np.array([[0, 0, 0, 2, 0, 0, 0, 6, 3],
 [3, 0, 0, 0, 0, 5, 4, 0, 1],
 [0, 0, 1, 0, 0, 3, 9, 8, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 8],
 [0, 0, 0, 6, 0, 1, 0, 0, 0],
 [7, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 2, 6, 0, 9, 0, 3, 0, 0],
 [0, 4, 0, 5, 0, 0, 0, 0, 0],
 [0, 9, 0, 0, 0, 0, 0, 0, 0]]
)

# [[5, 3, 0, 0, 7, 0, 0, 0, 0],
# [6, 0, 0, 1, 9, 5, 0, 0, 0],
# [0, 9, 8, 0, 0, 0, 0, 6, 0],
# [8, 0, 0, 0, 6, 0, 0, 0, 3],
# [4, 0, 0, 8, 0, 3, 0, 0, 1],
# [7, 0, 0, 0, 2, 0, 0, 0, 6],
# [0, 6, 0, 0, 0, 0, 2, 8, 0],
# [0, 0, 0, 4, 1, 9, 0, 0, 5],
# [0, 0, 0, 0, 8, 0, 0, 7, 9]]
#Chama a função para resolver o jogo
solution = solve(board)

if solution is not None:
    print("Solução encontrada:")
    print_board(solution)
else:
    print("Não foi possível encontrar uma solução.")
