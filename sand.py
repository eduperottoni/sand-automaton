import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


def sand_animation():
    board_size = 100
    screen_board = np.zeros((board_size + 1, board_size + 1), dtype=int)

    # Bloco de areia na parte central superior do lattice
    for j in range(1, 21):
        for k in range(40, 61):
            screen_board[j, k] = 1

    for j in range(45, 55):
        screen_board[j, j] = 2

    # Paredes laterais
    screen_board[:board_size, board_size] = 2
    screen_board[board_size, :board_size] = 2

    # Exibe o estado inicial
    plt.ion()
    plt.figure()
    show_grid(screen_board)

    generations = 1000  # Número de iterações
    for gen in range(generations):
        screen2 = screen_board.copy()
        current_mass = np.sum(screen_board > 0)

        for j in range(board_size):
            for k in range(board_size):
                # Queda livre
                if screen_board[j, k] == 1 and screen_board[j + 1, k] == 0:
                    screen2[j, k] = 0
                if screen_board[j, k] == 0 and screen_board[j - 1, k] == 1:
                    screen2[j, k] = 1

                # Partícula empilhada cai para esquerda
                if (

                    screen_board[j, k] == 1
                    and screen_board[j - 1, k] == 0  # acima
                    and screen_board[j, k - 1] == 0  # esquerda
                    and screen_board[j, k + 1] >= 1  # direita
                    and screen_board[j + 1, k] >= 1  # abaixo
                    and screen_board[j + 1, k - 1] == 0
                ):
                    screen2[j, k] = 0
                if (
                    k < board_size - 1 and
                    screen_board[j, k] == 0
                    and screen_board[j - 2, k + 1] == 0  # acima do que vai cair
                    and screen_board[j - 1, k] == 0  # acima
                    and screen_board[j - 1, k + 2] >= 1  # direita do que vai cair
                    and screen_board[j, k + 1] >= 1  # direita
                    and screen_board[j - 1, k + 1] == 1 # o q vai cair
                ):
                    screen2[j, k] = 1

                # Partícula empilhada cai para direita
                if (
                    screen_board[j, k] == 1
                    and screen_board[j - 1, k] == 0  # acima
                    and screen_board[j, k + 1] == 0  # direita
                    # and screen_board[j, k - 1] >= 1  # esquerda
                    and screen_board[j + 1, k] >= 1  # abaixo
                    and screen_board[j + 1, k + 1] == 0
                ):
                    screen2[j, k] = 0
                if (
                    screen_board[j, k] == 0
                    and screen_board[j - 2, k - 1] == 0  # acima da que vai cair
                    and screen_board[j - 1, k] == 0  # acima
                    # and screen_board[j - 1, k - 2] >= 1  # esquerda do que vai cair
                    and screen_board[j, k - 1] >= 1  # esquerda
                    and screen_board[j - 1, k - 1] == 1  # o que vai cair
                ):
                    screen2[j, k] = 1

        # Verificação da massa
        next_mass = np.sum(screen2 > 0)
        if next_mass != current_mass:
            print(f"Lei de conservação de massa violada! Gen: {gen}, Current: {current_mass}, Next: {next_mass}")

        screen_board = screen2  # Atualiza o estado

        # Atualiza a visualização
        if gen % 4 == 0:
            show_grid(screen_board)

    plt.ioff()
    plt.show()


def show_grid(grid):
    """Função para exibir a grade atual."""
    plt.clf()
    cmap = ListedColormap(["gray", "orange", "black"])
    plt.imshow(grid, cmap=cmap, origin="upper")
    plt.axis("equal")
    plt.axis("on")
    plt.draw()
    plt.pause(0.01)

# Executa a simulação
sand_animation()