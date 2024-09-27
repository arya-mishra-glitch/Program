board=[['__','__','__'],['__','__','__'],['__','__','__']]


def print_board():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()
print("To play, first enter the row number(1,2,3) and then the column number(1,2,3).")


def move1():
    row=int(input("Enter the row: "))
    column=int(input("Enter the column: "))
    if row<4 and column<4:
        #If condition chekcs if input provided by player is okay
        if board[row-1][column-1]=='__':
            #Checking if the place specified by player is empty
            return row-1, column-1
        else:
            print("Already occupied!")
            return move1()
    else:
        print("Invalid input.")
        return move1()
    

def winner():
    win_conditions=[[board[0][0],board[0][1], board[0][2]],
                    [board[1][0],board[1][1], board[1][2]],
                    [board[2][0],board[2][1], board[2][2]],
                    [board[0][0],board[1][0], board[2][0]],
                    [board[0][1],board[1][1], board[2][1]],
                    [board[0][2],board[1][2], board[2][2]],
                    [board[0][0],board[1][1], board[2][2]],
                    [board[0][2],board[1][1], board[2][0]]]

    if ['X','X','X'] in win_conditions:
        return 'X'

    if ['O','O','O'] in win_conditions:
        return 'O'
    

def check_draw():
    count=0
    for row in board:
        for j in row:
            if j=='__':
                count+=1
            else:
                pass
    if count>0:
        return False
    else:
        return True


chance=0
#if even, player 1 plays 'X'
#if odd, player 2 plays 'O'
while True:
    print_board()
    if chance%2==0:
        print("Player one 'X' plays.")
        i,j=move1()
        board[i][j]='X'
        win=winner()
        #check if win conditions are met
        draw=check_draw()
        if win=='X':
            print_board()
            print("X wins.")
            break
        if draw==True:
            print_board()
            print("Its a tie.")
            break
    
    else:
        #chance is odd, so player two plays
        print("PLayer two 'O' plays.")
        i,j=move1()
        board[i][j]='O'
        win=winner()
        #check if win conditions are met
        draw=check_draw()
        if win=='O':
            print_board()
            print("O wins.")
            break
        if draw==True:
            print_board()
            print("Its a tie.")
            break    
    chance+=1
    