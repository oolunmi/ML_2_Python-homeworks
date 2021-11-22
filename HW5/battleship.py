board_1=[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
board_2=[["."]]

def battleships_count(board):
    count=0
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c]=="X": 
              if (board[r][c-1]!="X" or c==0) and (board[r-1][c]!="X" or r==0):
                count+=1
    return count

print(battleships_count(board_2))

