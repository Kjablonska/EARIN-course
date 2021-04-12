import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000
ROWS, COLS = 8, 8
SQUARE_SIZE = WINDOW_WIDTH//COLS

GREEN = (199,231,207)
RED = (230,52,98)
WHITE = (238,245,219)
BLACK = (51,55,69)
YELLOW = (255, 173, 51)
BLUE = (153, 51, 255)

pygame.font.init()
KING = pygame.font.SysFont('Comic Sans MS', 80).render('K', False, RED)