
board = [['x','o',''],
         ['o','x','x'],
         ['o','','']]

print("Would you like to play as 'X or 'O' (X/O): ")
character_selection = input()
print(f"You have chosen to play as {character_selection}")
#print(f"You have selected{character_selection}")

def print_board(gameboard):
    print("\n")
    for i in range(len(gameboard)):
        for j in range(len(gameboard[i])):
            print('{:^1}'.format(gameboard[i][j]) + " | ", end ="")
        if i != len(gameboard)-1:
            print("\n_   _   _")
    print("\n")

print_board(board)
