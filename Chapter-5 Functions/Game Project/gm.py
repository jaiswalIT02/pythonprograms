# This will check the no of items in list...
def listcheck(l):
    
    count1=0
    count2=0
    for item in l:
        if item== 1:
            count1=count1+1
        if item==2:
            count2=count2+1
    if count1==3:
        return 1
    if count2==3:
        return 2
    if count1>0 and count2>0:
        return 3
    return 0
        
#This function will decide who will win
def GameStatus(board):
    """Return 1 if player 1 wins
    Return 2 if player 2 wins
    Return 3 if draw
    Return 0 to continue
    """
    blockedlines=0
    l=[board[0],board[1],board[2]]
    n=listcheck(l)
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        blockedlines=blockedlines+1
        
    l=[board[3],board[4],board[5]]
    n=listcheck(l)
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        blockedlines=blockedlines+1
        
    l=[board[6],board[7],board[8]]
    n=listcheck(l)
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        blockedlines=blockedlines+1
    
    l=[board[0],board[3],board[6]]
    n=listcheck(l)
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        blockedlines=blockedlines+1
        
    l=[board[1],board[4],board[7]]
    n=listcheck(l)
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        blockedlines=blockedlines+1
        
    l=[board[2],board[5],board[8]]
    n=listcheck(l)
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        blockedlines=blockedlines+1
        
    l=[board[0],board[4],board[8]]
    n=listcheck(l)
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        blockedlines=blockedlines+1
        
    
    l=[board[6],board[4],board[2]]
    n=listcheck(l)
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        blockedlines=blockedlines+1
        
    if blockedlines==8:
        return 3
    return 0
def printBoard(board):
        print()
        for i in range(3):
            ch=toChar(board[i])
            print(ch,end="")
        print()
        for i in range(3,6):
            ch=toChar(board[i])
            print(ch,end="")
        print()
        for i in range(6,9):
            ch=toChar(board[i])
            print(ch,end="")
        print()
        
        
#This is symbol(position) of tictactoe game .....    
def toChar(n):
    if n==0:
        return ' - '
    if n==1:
        return ' O '
    return ' X '

def readMove(board,player):
    while True:
        
        n=int(input("{0} move Save this game".format(player)))
        if n==0:
            #Do the saving part
            print("Save the game")
            return 0
            import SaveToExcel as save
            save.readmove
            
        

        
        if n<1 or n>9 :
            continue
#If the players want to save the game in that position:
    
        n=n-1
        if board[n]!=0:
            continue
        return n
print("____________Welcome to Tictactoe Game______________")
players=[0,0]
players[0]=str(input("Enter the 1st Player:"))
players[1]=str(input("Enter the 2nd Player:"))
tictactoe=[0,0,0,0,0,0,0,0,0]
printBoard(tictactoe)
currentplayer=0

while True:   
    move=readMove(tictactoe,players[currentplayer])
    tictactoe[move]=currentplayer+1
    printBoard(tictactoe)
    status=GameStatus(tictactoe)
    if status==1:
        print("{0} Wins".format(players[0]))
        break
    if status==2:
        print("{0} Wins".format(players[1]))
        break
    if status==3:
        print("Draw")
        break
    currentplayer=1-currentplayer
    