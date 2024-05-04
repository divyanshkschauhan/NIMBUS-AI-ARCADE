import pygame
import random
import sys
from collections import deque


WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
TILE_SIZE = 100
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
FONT_SIZE = 40
FONT_COLOR = BLACK

ROWS = 3
COLS = 3


TARGET_BOARD = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 0]]

def is_solved(board):
    return board == TARGET_BOARD

def draw_board(board):
    for row in range(ROWS):
        for col in range(COLS):
            number = board[row][col]
            if number != 0:
                pygame.draw.rect(screen, WHITE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                font = pygame.font.Font(None, FONT_SIZE)
                text = font.render(str(number), True, FONT_COLOR)
                text_rect = text.get_rect(center=(col * TILE_SIZE + TILE_SIZE / 2, row * TILE_SIZE + TILE_SIZE / 2))
                screen.blit(text, text_rect)


def find_empty_tile(board):
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == 0:
                return row, col
    return None, None


def get_neighbors(board):
    neighbors = []
    empty_row, empty_col = find_empty_tile(board)

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = empty_row + dr, empty_col + dc
        if 0 <= new_row < ROWS and 0 <= new_col < COLS:
            new_board = [row[:] for row in board] 
            new_board[empty_row][empty_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[empty_row][empty_col]
            neighbors.append(new_board)

    return neighbors


def bfs_solve(board):
    queue = deque([(board, [])])
    visited = set()

    while queue:
        current_board, path = queue.popleft()

        if is_solved(current_board):
            return path

        visited.add(tuple(map(tuple, current_board))) 

        for neighbor in get_neighbors(current_board):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [neighbor]))


def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Number Sliding Puzzle Solver")

    board = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8]]  



    while True:
        screen.fill(BLACK)
        draw_board(board)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                clicked_col = mouse_pos[0] // TILE_SIZE
                clicked_row = mouse_pos[1] // TILE_SIZE

                empty_row, empty_col = find_empty_tile(board)
                if abs(clicked_row - empty_row) + abs(clicked_col - empty_col) == 1:
                    board[empty_row][empty_col] = board[clicked_row][clicked_col]
                    board[clicked_row][clicked_col] = 0

        

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            solution = bfs_solve(board)
            for step in solution:
                board = step
                screen.fill(BLACK)
                draw_board(board)
                pygame.display.update()
                pygame.time.delay(500) 


if __name__ == "__main__":
    main()
