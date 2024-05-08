import sys
# Инициализация Pygame
sys.path.append('c:\python37-32\lib\site-packages')
import pygame
pygame.init()

# Установка окна
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Шашки")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Размер клетки на доске
cell_size = width // 8

# Класс для шашки
class Checker:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        checker_color = RED if self.color == "red" else GREEN if self.color == "black" else BLACK
        pygame.draw.circle(screen, checker_color, (self.x * cell_size + cell_size // 2, self.y * cell_size + cell_size // 2), cell_size // 3)

    def can_move_to(self, new_x, new_y):
        if abs(new_x - self.x) == 1 and abs(new_y - self.y) == 1:
            return True
        return False

    def can_capture(self, new_x, new_y):
        if abs(new_x - self.x) == 2 and abs(new_y - self.y) == 2:
            return True
        return False

# Создание шашек
checkers = [Checker("red", 1, 0), Checker("red", 3, 0), Checker("red", 5, 0), Checker("red", 7, 0),
            Checker("red", 0, 1), Checker("red", 2, 1), Checker("red", 4, 1), Checker("red", 6, 1),
            Checker("red", 1, 2), Checker("red", 3, 2), Checker("red", 5, 2), Checker("red", 7, 2),
            Checker("black", 0, 5), Checker("black", 2, 5), Checker("black", 4, 5), Checker("black", 6, 5),
            Checker("black", 1, 6), Checker("black", 3, 6), Checker("black", 5, 6), Checker("black", 7, 6),
            Checker("black", 0, 7), Checker("black", 2, 7), Checker("black", 4, 7), Checker("black", 6, 7)]

current_player = "red"

selected_checker = None

# Функция для срубления шашки
def capture_checker(checker, captured_checker):
    checkers.remove(captured_checker)
    checker.x = captured_checker.x
    checker.y = captured_checker.y

def is_checker_at(x, y):
    for checker in checkers:
        if checker.x == x and checker.y == y:
            return True
    return False

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row = y // cell_size
            col = x // cell_size
            
            if selected_checker is None:
                for checker in checkers:
                    if checker.x == col and checker.y == row and checker.color == current_player:
                        selected_checker = checker
            else:
                if selected_checker.can_move_to(col, row) and not is_checker_at(col, row):
                    selected_checker.x = col
                    selected_checker.y = row
                    current_player = "black" if current_player == "red" else "red"
                    selected_checker = None
                elif selected_checker.can_capture(col, row):
                    captured_checker = None
                    for checker in checkers:
                        if (checker.x == (col + selected_checker.x) // 2) and (checker.y == (row + selected_checker.y) // 2):
                            captured_checker = checker
                            break
                    if captured_checker is not None and captured_checker.color != selected_checker.color:
                        capture_checker(selected_checker, captured_checker)
                        selected_checker.x = col
                        selected_checker.y = row
                        current_player = "black" if current_player == "red" else "red"
                        selected_checker = None

    screen.fill(WHITE)

    # Отрисовка доски
    for y in range(8):
        for x in range(8):
            color = WHITE if (x + y) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))

    # Отрисовка шашек
    for checker in checkers:
        checker.draw()

    pygame.display.flip()
    