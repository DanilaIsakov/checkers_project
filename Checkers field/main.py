import pygame
import sys
pygame.init()
from aspose.imaging import *
import os
import itertools

# initialize pygame
pygame.init()

# Form screen
screen = pygame.display.set_mode()

# get the default size
x, y = screen.get_size()

# quit pygame
pygame.display.quit()

# view size (width x height)

print(x, y)

new_size_pool = min(x, y) // 100 * 80
print(new_size_pool)
new_size_figure = new_size_pool // 8
print(new_size_figure)

if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}\pool\cor_board(2).png"):
    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}\pool\cor_board(2).png")

image = Image.load(f"{os.path.dirname(os.path.abspath(__file__))}\pool/board(2).png")
image.resize(new_size_pool, new_size_pool)
image.save(f"{os.path.dirname(os.path.abspath(__file__))}\pool\cor_board(2).png")

if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_damka_black.png"):
    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_damka_black.png")

image = Image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure/damka_black.png")
image.resize(new_size_figure, new_size_figure)
image.save(f"{os.path.dirname(os.path.abspath(__file__))}/figure\core_damka_black.png")

if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_damka_white.png"):
    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_damka_white.png")

image = Image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure/damka_white.png")
image.resize(new_size_figure, new_size_figure)
image.save(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_damka_white.png")

if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_shashka_black.png"):
    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_shashka_black.png")

image = Image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure/shashka_black.png")
image.resize(new_size_figure, new_size_figure)
image.save(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_shashka_black.png")

if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_shashka_white.png"):
    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_shashka_white.png")

image = Image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure/shashka_white.png")
image.resize(new_size_figure, new_size_figure)
image.save(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_shashka_white.png")

if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_black_win.png"):
    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_black_win.png")

image = Image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure/black_win.png")
image.resize(new_size_pool, new_size_pool)
image.save(f"{os.path.dirname(os.path.abspath(__file__))}/figure/cor_black_win.png")

if os.path.exists(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_white_win.png"):
    os.remove(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_white_win.png")

image = Image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure/white_win.png")
image.resize(new_size_pool, new_size_pool)
image.save(f"{os.path.dirname(os.path.abspath(__file__))}/figure/cor_white_win.png")

# Установка окна
width, height = new_size_pool, new_size_pool
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Шашки")

shashki_white = pygame.image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_shashka_white.png")
damka_white = pygame.image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_damka_white.png")
shashki_black = pygame.image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_shashka_black.png")
board = pygame.image.load(f"{os.path.dirname(os.path.abspath(__file__))}\pool\cor_board(2).png")
damka_black = pygame.image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure\core_damka_black.png")
white_win = pygame.image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_white_win.png")
black_win = pygame.image.load(f"{os.path.dirname(os.path.abspath(__file__))}/figure\cor_black_win.png")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Размер клетки на доске
cell_size = new_size_figure


# Класс для шашки
class Checker:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, BLACK, (self.x * cell_size + cell_size/2, self.y * cell_size + cell_size/2), cell_size // 2.15)

    def can_move_to(self, new_x, new_y):
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            if abs(new_x - self.x) == 1 and abs(new_y - self.y) == 1:
                if self.color == 'red' and (new_y - self.y) == 1:
                    return True
                elif self.color == 'black' and (new_y - self.y) == -1:
                    return True
                else:
                    return False
        return False

    def can_capture(self, new_x, new_y):
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            if abs(new_x - self.x) == 2 and abs(new_y - self.y) == 2:
                Flag = 0
                for n in range(len(checkers)):
                    if new_x == checkers[n].x and new_y == checkers[n].y:
                        Flag = 1
                if Flag == 0:
                    return True
                else:
                    return False
        return False


class King_checker:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, BLACK, (self.x * cell_size + cell_size/2, self.y * cell_size + cell_size/2), cell_size // 2.15)

    def can_move_to(self, new_x, new_y):
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            if abs(new_x - self.x) == abs(new_y - self.y):
                for n in range(len(checkers)):
                    if (new_x < checkers[n].x < self.x or new_x > checkers[n].x > self.x) and (new_y < checkers[n].y < self.y or new_y > checkers[n].y > self.y) and (abs(self.x - checkers[n].x) == abs(self.y - checkers[n].y)):
                        return False
                return True
        return False

    def can_capture(self, new_x, new_y):
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            if abs(new_x - self.x) >= 2 and abs(new_x - self.x) == abs(new_y - self.y):
                Flag = 0
                k_srub = 0
                for n in range(len(checkers)):
                    if new_x == checkers[n].x and new_y == checkers[n].y:
                        Flag = 1
                    if (self.x < checkers[n].x < new_x or new_x < checkers[n].x < self.x) and (self.y < checkers[n].y < new_y or new_y < checkers[n].y < self.y) and abs(checkers[n].x - self.x) == abs(checkers[n].y - self.y) and abs(checkers[n].x - new_x) == abs(checkers[n].y - new_y):
                        k_srub += 1
                if Flag == 0 and k_srub == 1:
                    return True
                else:
                    return False
        return False

current_color = 'black'

# Создание шашек
checkers = [Checker("red", 1, 0), Checker("red", 3, 0), Checker("red", 5, 0), Checker("red", 7, 0),
            Checker("red", 0, 1), Checker("red", 2, 1), Checker("red", 4, 1), Checker("red", 6, 1),
            Checker("red", 1, 2), Checker("red", 3, 2), Checker("red", 5, 2), Checker("red", 7, 2),
            Checker("black", 0, 5), Checker("black", 2, 5), Checker("black", 4, 5), Checker("black", 6, 5),
            Checker("black", 1, 6), Checker("black", 3, 6), Checker("black", 5, 6), Checker("black", 7, 6),
            Checker("black", 0, 7), Checker("black", 2, 7), Checker("black", 4, 7), Checker("black", 6, 7)]

current_player = "red"

selected_checker = None


def is_checker_at(x, y):
    for checker in checkers:
        if checker.x == x and checker.y == y:
            return True
    return False

flag_capture = 0  # для сруба
white_otkis = 0
black_otkis = 0

def win_white():
    screen.blit(white_win, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

def win_black():
    screen.blit(black_win, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

while True:
    current_color = current_player
    if white_otkis == 12: win_black()
    elif black_otkis == 12: win_white()
    else:
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row = y // cell_size
                col = x // cell_size

                for checker in checkers:
                    if checker.x == col and checker.y == row and checker.color == current_player and flag_capture==0:
                        selected_checker = checker
                        kol_vo_srub = 0  # срубы
                if not (selected_checker is None):
                    if selected_checker.__class__ == Checker:
                        if selected_checker.can_move_to(col, row) and not is_checker_at(col, row) and flag_capture == 0:
                            for i in range(len(checkers)):
                                break_1 = False
                                for j in range(len(checkers)):
                                    if checkers[j].y - checkers[i].y != 0 and checkers[j].x - checkers[i].x !=0:
                                        if (checkers[i].__class__==Checker and checkers[i].color == current_player and checkers[j].color != current_player and \
                                                checkers[i].can_capture(checkers[j].x + (checkers[j].x - checkers[i].x),
                                                                        checkers[j].y + (checkers[j].y - checkers[i].y))) or (checkers[i].__class__ == King_checker and checkers[i].color == current_player and checkers[j].color != current_player and \
                                                checkers[i].can_capture(checkers[j].x + ((checkers[j].x - checkers[i].x)//(abs(checkers[j].x - checkers[i].x))),
                                                                        checkers[j].y + ((checkers[j].y - checkers[i].y)//(abs(checkers[j].y - checkers[i].y))))):
                                            checkers.remove(checkers[i])
                                            if current_player == 'red': white_otkis += 1
                                            else: black_otkis += 1
                                            break_1 = True
                                            break
                                if break_1 == True:
                                    break
                            selected_checker.x = col
                            selected_checker.y = row
                            current_player = "black" if current_player == "red" else "red"
                            if selected_checker.color == 'red' and selected_checker.y == 7:
                                selected_checker.__class__ = King_checker
                            elif selected_checker.color == 'black' and selected_checker.y == 0:
                                selected_checker.__class__ = King_checker
                            selected_checker = None
                        elif selected_checker.can_capture(col, row):
                            captured_checker = None
                            for checker in checkers:
                                if (checker.x == (col + selected_checker.x) // 2) and (
                                        checker.y == (row + selected_checker.y) // 2):
                                    captured_checker = checker
                                    break
                            if captured_checker is not None and captured_checker.color != selected_checker.color:
                                checkers.remove(captured_checker)
                                selected_checker.x = col
                                selected_checker.y = row
                                flagg = 0
                                if current_player == 'black': white_otkis += 1
                                else: black_otkis +=1
                                for checker in checkers:
                                    if abs(col - checker.x) == 1 and abs(
                                            row - checker.y) == 1 and selected_checker.color != checker.color:
                                        if selected_checker.can_capture(checker.x + (checker.x - col),
                                                                        checker.y + (checker.y - row)):
                                            flag_capture = 1
                                            flagg = 1
                                if selected_checker.color == 'red' and selected_checker.y == 7:
                                    selected_checker.__class__ = King_checker
                                elif selected_checker.color == 'black' and selected_checker.y == 0:
                                    selected_checker.__class__ = King_checker
                                if flagg == 0:
                                    color_remember = selected_checker.color
                                    current_player = "black" if current_player == "red" else "red"
                                    selected_checker = None
                                    flag_capture = 0
                    else:
                        if selected_checker.can_move_to(col, row) and not is_checker_at(col, row) and flag_capture == 0:
                            for i in range(len(checkers)):
                                break_1 = False
                                for j in range(len(checkers)):
                                    if checkers[j].y - checkers[i].y != 0 and checkers[j].x - checkers[i].x !=0:
                                        if (checkers[i].__class__==Checker and checkers[i].color == current_player and checkers[j].color != current_player and \
                                                checkers[i].can_capture(checkers[j].x + (checkers[j].x - checkers[i].x),
                                                                        checkers[j].y + (checkers[j].y - checkers[i].y))) or (checkers[i].__class__ == King_checker and checkers[i].color == current_player and checkers[j].color != current_player and \
                                                checkers[i].can_capture(checkers[j].x + ((checkers[j].x - checkers[i].x)//(abs(checkers[j].x - checkers[i].x))),
                                                                        checkers[j].y + ((checkers[j].y - checkers[i].y)//(abs(checkers[j].y - checkers[i].y))))):
                                            checkers.remove(checkers[i])
                                            if current_player == 'red': white_otkis += 1
                                            else: black_otkis += 1
                                            break_1 = True
                                            break
                                if break_1 == True:
                                    break
                            selected_checker.x = col
                            selected_checker.y = row
                            current_player = "black" if current_player == "red" else "red"
                            selected_checker = None
                        elif selected_checker.can_capture(col, row):
                            captured_checker = None
                            for checker in checkers:
                                if (col < checker.x < selected_checker.x or selected_checker.x < checker.x < col) and (
                                        row < checker.y < selected_checker.y or selected_checker.y < checker.y < row) and abs(checker.x - col) == abs(checker.y - row):
                                    captured_checker = checker
                                    break
                            if captured_checker is not None and captured_checker.color != selected_checker.color:
                                checkers.remove(captured_checker)
                                selected_checker.x = col
                                selected_checker.y = row
                                flagg = 0
                                if current_player == 'black': white_otkis += 1
                                else: black_otkis +=1
                                for checker in checkers:
                                    if selected_checker.color != checker.color:
                                        if selected_checker.can_capture(checker.x + (checker.x - col),
                                                                        checker.y + (checker.y - row)):
                                            flag_capture = 1
                                            flagg = 1
                                if flagg == 0:
                                    current_player = "black" if current_player == "red" else "red"
                                    selected_checker = None
                                    flag_capture = 0                     

        screen.fill(WHITE)

        # Отрисовка доски
        screen.blit(board, (0, 0))

        # Отрисовка шашек

        for i in range(len(checkers)):

            if checkers[i].color == 'red' and checkers[i].__class__ == Checker:
                screen.blit(shashki_white, (checkers[i].x * cell_size, checkers[i].y * cell_size))  # коорды емае
            if checkers[i].color == 'black' and checkers[i].__class__ == Checker:
                screen.blit(shashki_black, (checkers[i].x * cell_size, checkers[i].y * cell_size))

            if checkers[i].color == 'red' and checkers[i].__class__ == King_checker:
                screen.blit(damka_white, (checkers[i].x * cell_size, checkers[i].y * cell_size))
            if checkers[i].color == 'black' and checkers[i].__class__ == King_checker:
                screen.blit(damka_black, (checkers[i].x * cell_size, checkers[i].y * cell_size))
        
        pygame.display.flip()
