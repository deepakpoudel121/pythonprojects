def print_board(board):
    print("")
    for row in range(len(board)):
        for col in range(len(board[row])):
            print(f" {board[row][col]}", end="")
            if col != len(board[row]) - 1:
                print(" | ", end='')
                
        if row == len(board) - 1:
            print("\n")
        else:
            print("\n")
            print("---------------")


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def play_board(board, symbol):
    row = int(input("Enter the row (1-3): "))
    col = int(input("Enter the column (1-3): "))
    
 
    row -= 1
    col -= 1
    
    row_len = len(board)
    col_len = len(board[0])  

 
    if row < 0 or row >= row_len or col < 0 or col >= col_len:
        print("Please enter a valid row and column (1-3): ")
        play_board(board, symbol)
        return
    elif board[row][col] != " ":  
        print("The space is occupied")
        play_board(board, symbol) 
        return
    
    board[row][col] = symbol


print_board(board)
play_board(board, "X")
print_board(board)