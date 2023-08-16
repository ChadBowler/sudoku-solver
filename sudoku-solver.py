import re
check_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
puzzle_array = [
        [5, 0, 3, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 6, 0, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 1, 0, 0, 9, 0, 0, 8],
        [0, 0, 6, 0, 4, 0, 0, 7, 9]
        ]
game_square_dict = {}


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
        for x in game_square_dict.items():
            print(x.self.big_square)
    
    def test_possibilities(self):
        if self.value == 0:
            pattern = f'\({self.x}, \d\)'
            for key, value in game_square_dict.items():
                if re.match(pattern, str(key)):
                    # print(key, value)
                    
                    for i, x in enumerate(self.check_array):
                        
                        if str(self.check_array[i]) == str(value):
                            self.check_array.remove(self.check_array[i])
                            print(self.check_array)

            pattern = f'\(\d, {self.y}\)'
            for key, value in game_square_dict.items():
                if re.match(pattern, str(key)):
                    # print(key, value)
                    
                    for i, x in enumerate(self.check_array):
                        if str(self.check_array[i]) == str(value):
                            self.check_array.remove(self.check_array[i])
                            print(self.check_array)
        # self.print_big_squares()                    
    

def print_all():
    for key, value in enumerate(game_square_dict): 
        print(f'square: {key}, fff {value}')    

def check_possibilites():
    #   this = game_square_dict[0, 1]
    #   print(this)
    #   this.test_possibilities()
      for key, value in enumerate(game_square_dict):
        
        game_square_dict[value].test_possibilities()
        # print(f'square: {keys}, fff {value}') 


      

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

    check_possibilites()
    # print_all()



if __name__=='__main__':
    initialize_classes()

# print(puzzle_array)
