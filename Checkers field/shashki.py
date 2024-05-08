import pygame
import sys
#срубы больше чем 1, дамка не срубает 2 подряд, есть хук, за поле не уходим
# Инициализация Pygame
pygame.init()

# Установка окна
width, height = 1080, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Шашки")

shashki_white = pygame.image.load('D:\projects_pycharm\shashki\shashka_white.png')
damka_white = pygame.image.load('D:\projects_pycharm\shashki\damka_white.png')
shashki_black = pygame.image.load('D:\projects_pycharm\shashki\shashka_black.png')
board = pygame.image.load('D:\projects_pycharm\shashki/aboard(2).png')
damka_black = pygame.image.load('D:\projects_pycharm\shashki\damka_black.png')
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
        pygame.draw.circle(screen, checker_color, (self.x * cell_size + 57, self.y * cell_size + 57), cell_size //3 )

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
                for n in range (len(checkers)):
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
        checker_color = RED if self.color == "red" else GREEN if self.color == "black" else BLACK
        pygame.draw.circle(screen, checker_color, (self.x * cell_size + 57, self.y * cell_size + 57), cell_size // 3)

    def can_move_to(self, new_x, new_y):
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            if abs(new_x - self.x) ==  abs(new_y - self.y):
                for n in range (len(checkers)):
                    if (new_x < checkers[n].x < self.x or new_x > checkers[n].x > self.x) and (new_y < checkers[n].y < self.y or new_y > checkers[n].y > self.y):
                        return False 
                return True
        return False
        

    def can_capture(self, new_x, new_y):
        if 0 <= new_x <= 7 and 0 <= new_y <= 7:
            if abs(new_x - self.x) >= 2 and abs(new_x - self.x) == abs(new_y - self.y):
                Flag = 0
                k_srub = 0
                for n in range (len(checkers)):
                    if new_x == checkers[n].x and new_y == checkers[n].y:
                        Flag = 1
                    if (self.x < checkers[n].x < new_x or new_x < checkers[n].x < self.x) and (self.y < checkers[n].y < new_y or new_y < checkers[n].y < self.y):
                        k_srub += 1
                if Flag == 0 and k_srub == 1: 
                    return True
                else:
                    return False
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

hod_good = 0 #для AI
debil_hod = 0 #для AI

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
flag_capture = 0 #для сруба
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
            
            for checker in checkers:
                if checker.x == col and checker.y == row and checker.color == current_player:
                    selected_checker = checker
                    print(selected_checker)
                    kol_vo_srub = 0 #срубы
            if not(selected_checker is None):
                if selected_checker.__class__ == Checker:
                    if selected_checker.can_move_to(col, row) and not is_checker_at(col, row) and flag_capture == 0:
                        for i in range(len(checkers)):
                            break_1 = False
                            for j in range(len(checkers)):
                                if checkers[i].color == current_player and checkers[j].color != current_player and checkers[i].can_capture(checkers[j].x + (checkers[j].x - checkers[i].x), checkers[j].y + (checkers[j].y - checkers[i].y)):
                                    checkers.remove(checkers[i])
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
                        hod_good+=1
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
                            hod_good += 1
                            flagg = 0
                            for checker in checkers:
                                if abs(col-checker.x) == 1 and abs(row-checker.y) == 1 and selected_checker.color != checker.color:
                                    if selected_checker.can_capture(checker.x+(checker.x-col),checker.y+(checker.y-row)):
                                        flag_capture = 1
                                        flagg = 1
                            if selected_checker.color == 'red' and selected_checker.y == 7:
                                selected_checker.__class__ = King_checker 
                            elif selected_checker.color == 'black' and selected_checker.y == 0:
                                selected_checker.__class__ = King_checker
                            if flagg == 0:
                                color_remember=selected_checker.color
                                current_player = "black" if current_player == "red" else "red" 
                                selected_checker = None
                                flag_capture = 0 
                else:
                    if selected_checker.can_move_to(col, row) and not is_checker_at(col, row) and flag_capture == 0:
                        for i in range(len(checkers)):
                            break_1 = False
                            for j in range(len(checkers)):
                                if checkers[i].color == current_player and checkers[j].color != current_player and checkers[i].can_capture(checkers[j].x + (checkers[j].x - checkers[i].x), checkers[j].y + (checkers[j].y - checkers[i].y)):
                                    checkers.remove(checkers[i])
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
                            if (col < checker.x < selected_checker.x or selected_checker.x < checker.x < col) and (row < checker.y < selected_checker.y or selected_checker.y < checker.y < row):
                                captured_checker = checker
                                break
                        if captured_checker is not None and captured_checker.color != selected_checker.color:
                            capture_checker(selected_checker, captured_checker)
                            selected_checker.x = col
                            selected_checker.y = row
                            hod_good+=1
                            flagg = 0
                            for checker in checkers:
                                if selected_checker.color != checker.color:
                                    if selected_checker.can_capture(checker.x+(checker.x-col),checker.y+(checker.y-row)):
                                        flag_capture = 1
                                        flagg = 1
                            if flagg == 0:
                                current_player = "black" if current_player == "red" else "red" 
                                selected_checker = None
                                flag_capture = 0

    screen.fill(WHITE)

    
    # Отрисовка доски
    for y in range(8):
        for x in range(8):
            color = WHITE if (x + y) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
    
    screen.blit(board, (0,0))
    
    
    # Отрисовка шашек
    for checker in checkers:
        checker.draw()
    for i in range(len(checkers)):
        
        if checkers[i].color == 'red' and checkers[i].__class__ == Checker:
            screen.blit(shashki_white,(checkers[i].x * cell_size + 10 , checkers[i].y * cell_size + 10)) #коорды емае
        if checkers[i].color == 'black' and checkers[i].__class__ == Checker:
            screen.blit(shashki_black,(checkers[i].x * cell_size + 10, checkers[i].y * cell_size + 10))
            
        if checkers[i].color == 'red' and checkers[i].__class__ == King_checker:
            screen.blit(damka_white,(checkers[i].x * cell_size + 10, checkers[i].y * cell_size + 10))
        if checkers[i].color == 'black' and checkers[i].__class__ == King_checker:
            screen.blit(damka_black,(checkers[i].x * cell_size + 10, checkers[i].y * cell_size + 10))
    
    pygame.display.flip()