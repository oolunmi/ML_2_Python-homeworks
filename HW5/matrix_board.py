# right, top = row[0], col[0]
# bottom, right = row[2], col[3]




class Board:
    
    
    def __init__(self, matrix):
        self.board = matrix

        self.r = 0
        self.c = 0
        self.direction = 'R'
        self.rows = len(matrix) - 1
        self.cols = len(matrix[0]) - 1

        self.starting_position = 0, 0
        self.battleships_found = []
        
    
    @property
    def _position(self):
        return self.r, self.c
    
    def _is_x(self):
        r, c = self._position
        return self.board[r][c] == 'X'
    
    def _move(self):
        print(self.board[self.r][self.c])

        if self.direction == 'R':
            self.c += 1
        if self.direction == 'D':
            self.r += 1
        if self.direction == 'L':
            self.c -= 1
        if self.direction == 'U':
            self.r -= 1
    
    def move_in_square(self, start_pos):
        if self.direction == 'R':
            while self.c < self.cols:
                self._move()
            else:
                self.direction = 'D'
        if self.direction == 'D':
            while self.r < self.rows:
                self._move()
            else:
                self.direction = 'L'
        if self.direction == 'L':
            while self.c > 0:
                self._move()
            else:
                self.direction = 'U'
        if self.direction == 'U':
            while self.r > 0:
                self._move()
            else:
                self.direction = 'R'
            
            
            
b = Board([
    ["X",".",".","X"],
    [".",".",".","X"],
    [".",".",".","X"]]
)
b.rotate_recursively()
    
        
        
        