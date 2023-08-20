import re
import pygame
from random import uniform, randint
check_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#easy puzzle
# puzzle_array = [
#         [0, 0, 4, 0, 5, 0, 0, 0, 0],
#         [9, 0, 0, 7, 3, 4, 6, 0, 0],
#         [0, 0, 3, 0, 2, 1, 0, 4, 9],
#         [0, 3, 5, 0, 9, 0, 4, 8, 0],
#         [0, 9, 0, 0, 0, 0, 0, 3, 0],
#         [0, 7, 6, 0, 1, 0, 9, 2, 0],
#         [3, 1, 0, 9, 7, 0, 2, 0, 0],
#         [0, 0, 9, 1, 8, 2, 0, 0, 3],
#         [0, 0, 0, 0, 6, 0, 1, 0, 0]
#         ]
# solution
# [2, 6, 4, 8, 5, 9, 3, 1, 7]
# [9, 8, 1, 7, 3, 4, 6, 5, 2]
# [7, 5, 3, 6, 2, 1, 8, 4, 9]
# [1, 3, 5, 2, 9, 7, 4, 8, 6]
# [8, 9, 2, 5, 4, 6, 7, 3, 1]
# [4, 7, 6, 3, 1, 8, 9, 2, 5]
# [3, 1, 8, 9, 7, 5, 2, 6, 4]
# [6, 4, 9, 1, 8, 2, 5, 7, 3]
# [5, 2, 7, 4, 6, 3, 1, 9, 8]
#medium puzzle
puzzle_array = [
        [8, 0, 7, 2, 1, 0, 4, 0, 5],
        [1, 0, 0, 5, 7, 0, 0, 2, 0],
        [0, 2, 0, 0, 3, 0, 7, 6, 0],
        [0, 0, 6, 7, 8, 0, 0, 9, 0],
        [7, 0, 5, 0, 0, 3, 0, 8, 0],
        [0, 8, 1, 0, 0, 2, 0, 5, 0],
        [9, 0, 0, 8, 2, 0, 0, 1, 0],
        [0, 1, 2, 9, 6, 0, 0, 7, 0],
        [0, 7, 8, 0, 5, 1, 0, 0, 2]
        ]
#solution
# [8, 6, 7, 2, 1, 9, 4, 3, 5]
# [1, 4, 3, 5, 7, 6, 8, 2, 9]
# [5, 2, 9, 4, 3, 8, 7, 6, 1]
# [2, 3, 6, 7, 8, 5, 1, 9, 4]
# [7, 9, 5, 1, 4, 3, 2, 8, 6]
# [4, 8, 1, 6, 9, 2, 3, 5, 7]
# [9, 5, 4, 8, 2, 7, 6, 1, 3]
# [3, 1, 2, 9, 6, 4, 5, 7, 8]
# [6, 7, 8, 3, 5, 1, 9, 4, 2]
#hard puzzle
# puzzle_array = [
#         [1, 0, 0, 0, 0, 9, 4, 0, 8],
#         [6, 0, 9, 1, 0, 0, 5, 0, 0],
#         [3, 8, 5, 0, 0, 0, 0, 9, 0],
#         [2, 0, 0, 9, 0, 8, 0, 4, 0],
#         [0, 9, 0, 5, 3, 0, 0, 1, 0],
#         [0, 0, 8, 0, 4, 1, 9, 0, 0],
#         [0, 0, 3, 0, 9, 0, 1, 5, 0],
#         [0, 1, 0, 8, 0, 0, 0, 0, 9],
#         [0, 6, 0, 0, 1, 5, 0, 0, 3]
#         ]
game_square_dict = {}
screen_x = 1960
screen_y = 1080
pygame.init()
screen = pygame.display.set_mode((screen_x, screen_y))
clock = pygame.time.Clock()
game_running = True
# c = (0, 150, 255)
c = 'black'

quit_image = pygame.image.load('assets/quit_button.png')
solve_image = pygame.image.load('assets/solve_button.png')


screen.fill('white')

def draw_board():

    x_start = int(screen_x*0.10)
    y_start = int(screen_y*0.25)

    for x in range(x_start, x_start+500, 50):

        pygame.draw.line(screen,c, (x_start+500, x), (x_start+950,x), 2)
        pygame.draw.line(screen,c, (x+500, x_start), (x+500, x_start+450), 2)
        # pygame.display.update()

def quit_function():
    pass

def print_all():
    for key, value in enumerate(game_square_dict): 
        print(f'square: {key}, fff {value}')    

def solve_puzzle():
     while True: 
        zero_count = 0
        for key, value in enumerate(game_square_dict):
            game_square_dict[value].test_possibilities()

        for i, value in enumerate(puzzle_array):
            if 0 in puzzle_array[i]:
                zero_count += 1
            
        for i, j in enumerate(puzzle_array):
            print(puzzle_array[i])
        print()
        if zero_count == 0:
            break

def initialize_classes():
    
    for i, value in enumerate(puzzle_array):
        for j, value in enumerate(puzzle_array[i]):
            if i < 3 and j < 3:
                big_square = 1
            elif i < 3 and 2 < j < 6:
                big_square = 2
            elif i < 3 and 5 < j:
                big_square = 3
            elif 2 < i < 6 and j < 3:
                big_square = 4
            elif 2 < i < 6 and 2 < j < 6:
                big_square = 5
            elif 2 < i < 6 and 5 < j:
                big_square = 6
            elif i > 5 and j < 3:
                big_square = 7
            elif i > 5 and 2 < j < 6:
                big_square = 8
            elif i > 5 and 5 < j:
                big_square = 9
            game_square_dict[i, j] = Game_square(i, j, big_square, value)

    solve_puzzle()


class Button:
    def __init__(self, x, y, img, function):
        self.img = img
        self.rect = self.img.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.function = staticmethod(function)

    def draw(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked:
                self.clicked = True
                self.function()
            if not pygame.mouse.get_pressed()[0]:
                self.clicked = False
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Game_square:
    def __init__(self, x, y, big_square, value):
        self.x = x
        self.y = y
        self.value = value
        self.big_square = big_square
        self.check_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __repr__(self):
        return f"{self.value}"
    
    def print_big_squares(self):
        for x, y in enumerate(game_square_dict):
            print(game_square_dict[y].big_square)
    
    def test_possibilities(self):
        print(self.check_array)
        if self.value == 0:
            pattern = f'\({self.x}, \d\)'
            for key, value in game_square_dict.items():
                if game_square_dict[key] == self:
                    continue
                if re.match(pattern, str(key)):
                    for i, x in enumerate(self.check_array):
                        if str(self.check_array[i]) == str(value):
                            self.check_array.remove(self.check_array[i])
                        if len(self.check_array) == 1:
                            puzzle_array[self.x][self.y] = self.check_array[0]
                            self.value = self.check_array[0]
                            for i, j in enumerate(puzzle_array):
            
                                print(puzzle_array[i])
                            print()

            pattern = f'\(\d, {self.y}\)'
            for key, value in game_square_dict.items():
                if game_square_dict[key] == self:
                    continue
                if re.match(pattern, str(key)):
                    for i, x in enumerate(self.check_array):
                        if str(self.check_array[i]) == str(value):
                            self.check_array.remove(self.check_array[i])
                        if len(self.check_array) == 1:
                            puzzle_array[self.x][self.y] = self.check_array[0]
                            self.value = self.check_array[0]
                            for i, j in enumerate(puzzle_array):
                                print(puzzle_array[i])
                            print()

            for key, value in game_square_dict.items():
                if game_square_dict[key] == self:
                    continue
                if game_square_dict[key].big_square == self.big_square:
                    for i, x in enumerate(self.check_array):
                        if str(self.check_array[i]) == str(game_square_dict[key].value):
                            self.check_array.remove(self.check_array[i])
                            if len(self.check_array) == 1:
                                puzzle_array[self.x][self.y] = self.check_array[0]
                                self.value = self.check_array[0]
                                print(self.check_array[0])
                                for i, j in enumerate(puzzle_array):
                                    print(puzzle_array[i])
                                print()            
    


quit_button = Button(screen_x*0.55, screen_y*0.65, quit_image, quit_function)
sovle_button = Button(screen_x*0.25, screen_y*0.65, solve_image, initialize_classes)
draw_board()
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    
    
    
    sovle_button.draw()
    quit_button.draw()
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
    
if __name__=='__main__':
    initialize_classes()

