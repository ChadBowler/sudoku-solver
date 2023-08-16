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
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

    def __repr__(self):
        return f"{self.value}"
    
    def test_possibilities(self):
        if self.value == 0:
            pattern = '\(0, \d\)'
            for key, value in game_square_dict.items():
                if re.match(pattern, str(key)):
                    print(key, value)

def check_possibilites():
      game_square_dict[0, 1].test_possibilities()

def initialize_classes():
    
    for i, value in enumerate(puzzle_array):
        for j, value in enumerate(puzzle_array[i]):
            game_square_dict[i, j] = Game_square(i, j, value)

    # print(game_square_dict)
    check_possibilites()
            


if __name__=='__main__':
    initialize_classes()

# print(puzzle_array)
