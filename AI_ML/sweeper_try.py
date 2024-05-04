import pygame
import random





pygame.init()

WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
BLACK = (0, 0, 0)

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

TILE_SIZE = 50


NUM_ROWS = WINDOW_HEIGHT // TILE_SIZE
NUM_COLS = WINDOW_WIDTH // TILE_SIZE
NUM_MINES = 8


window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Minesweeper")


def create_board():
    board = [[0 for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
    for _ in range(NUM_MINES):
        row = random.randint(0, NUM_ROWS - 1)
        col = random.randint(0, NUM_COLS - 1)
        while board[row][col] == 9:  
            row = random.randint(0, NUM_ROWS - 1)
            col = random.randint(0, NUM_COLS - 1)
        board[row][col] = 9  
     
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < NUM_ROWS and 0 <= col + j < NUM_COLS and board[row + i][col + j] != 9:
                    board[row + i][col + j] += 1
    return board


board = create_board()

def draw_board():
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            tile_rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            if revealed[row][col]:
                if board[row][col] == 0:
                    pygame.draw.rect(window, GRAY, tile_rect)
                elif board[row][col] == 9:
                    pygame.draw.rect(window, BLACK, tile_rect)
                    pygame.draw.circle(window, WHITE, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 4)
                else:
                    font = pygame.font.Font(None, 20)
                    text = font.render(str(board[row][col]), True, BLACK)
                    window.blit(text, (col * TILE_SIZE + TILE_SIZE // 3, row * TILE_SIZE + TILE_SIZE // 3))
            else:
                if (row, col) in safe_tiles:  
                    pygame.draw.rect(window, (255, 0, 0), tile_rect)  
                else:
                    pygame.draw.rect(window, WHITE, tile_rect)  

    for x in range(0, WINDOW_WIDTH, TILE_SIZE):
        pygame.draw.line(window, BLACK, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
        pygame.draw.line(window, BLACK, (0, y), (WINDOW_WIDTH, y))


def reveal_adjacent(row, col):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= row + i < NUM_ROWS and 0 <= col + j < NUM_COLS and not revealed[row + i][col + j]:
                revealed[row + i][col + j] = True
                if board[row + i][col + j] == 0:
                    reveal_adjacent(row + i, col + j)

safe_tiles = []
def find_safe_tiles():
    
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if revealed[row][col] and board[row][col] > 0 and board[row][col] != 9:
                num_unrevealed_adjacent = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= row + i < NUM_ROWS and 0 <= col + j < NUM_COLS and not revealed[row + i][col + j]:
                            num_unrevealed_adjacent += 1
                if num_unrevealed_adjacent == board[row][col]:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= row + i < NUM_ROWS and 0 <= col + j < NUM_COLS and not revealed[row + i][col + j]:
                                safe_tiles.append((row + i, col + j))
    return safe_tiles



flp = 0
running = True
revealed = [[False for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]
font = pygame.font.Font(None, 66)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TRANSPARENT = (0, 0, 0, 0)


first_move = True
row,col=88,88
while running:
    
    window.fill(WHITE)
    draw_board()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // TILE_SIZE
            col = x // TILE_SIZE
            
            if board[row][col] == 9:
                flp = 1
                for r in range(NUM_ROWS):
                    for c in range(NUM_COLS):
                        revealed[r][c] = True
            else:
                revealed[row][col] = True
                if board[row][col] == 0:
                    reveal_adjacent(row, col)

            if flp:
                text = font.render("Game Over!", True, BLACK)
                text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
                text_bg = pygame.Surface((text.get_width(), text.get_height()))
                text_bg.fill(WHITE)
                window.blit(text_bg, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
                window.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT // 2 - text.get_height() // 2))
    
            else:
                if(rw!=row and cl!=col):
                    rw=row
                    cl=col
                    safe_tiles = find_safe_tiles()
                    if safe_tiles:
                        print("Mines Found!:", safe_tiles)


            
    rw=69
    cl=69
    

    pygame.display.flip()

pygame.quit()
