theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }


boardkey=[]

for key in theBoard:
    boardkey.append(key)

def print_board(board):
    print(board['7'],'|',board['8'],'|',board['9'])
    print("-+-+-+-+-+-")
    print(board['4'],'|',board['5'],'|',board['6'])
    print("-+-+-+-+-+-")
    print(board['1'],'|',board['2'],'|',board['3'])

def game():
    turn='X'
    count=0
    for i in range(10):
        print_board(theBoard)
        print("This is your Turn ",turn,".Move to which palce?")
        move=input()

        if theBoard[move] == ' ':
            theBoard[move]=turn
            count+=1
        else:
            print("That place is already filled.\nMove to which place?")
            continue


        if count == 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                print_board(theBoard)
                print("Game Over")
                print("***********",turn,"Won ***********")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                print_board(theBoard)
                print("Game Over")
                print("***********", turn, "Won ***********")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                    print_board(theBoard)
                    print("Game Over")
                    print("***********", turn, "Won ***********")
                    break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                print_board(theBoard)
                print("Game Over")
                print("***********",turn,"Won ***********")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                print_board(theBoard)
                print("Game Over")
                print("***********", turn, "Won ***********")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                print_board(theBoard)
                print("Game Over")
                print("***********", turn, "Won ***********")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                print_board(theBoard)
                print("Game Over")
                print("***********", turn, "Won ***********")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                print_board(theBoard)
                print("Game Over")
                print("***********", turn, "Won ***********")
                break


        if count == 9:
            print("Game Over")
            print("This is Tie!!")

        if turn=='X':
            turn = 'O'
        else:
            turn='X'

    restart()

def restart():
    print("Do You Want to play again?")
    print("Enter y or Y if you want")
    choice=input()
    if choice=='y' or choice=='Y':
        game()


if __name__ =='__main__':
    game()