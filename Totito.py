from random import randrange
num = 0

def printBoard():
    print("+---------"*3, end="+\n", )
    print( "",tablero[0][0] , tablero[0][1],  tablero[0][2], sep="|        ") 
    print("+---------"*3, end="+\n", )
    print( "",tablero[1][0] , tablero[1][1],  tablero[1][2], sep="|        ") 
    print("+---------"*3, end="+\n", )
    print( "",tablero[2][0] , tablero[2][1],  tablero[2][2], sep="|        ")
    print("+---------"*3, end="+\n", )


def DisplayBoard(board):
    
    if board > 0 and board < 10:
        if boardVerifid[board] == "False":
            EnterMove()
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == board:
                    MakeListOfFreeFields(board)
                    tablero[i][j] = "O"
                    printBoard()
                    VictoryFor("O")
                    DrawMove()

    else:
        print("No es correcto")
        EnterMove()
    

def EnterMove():
    o = int(input("Ingresa tu movimiento:"))
    DisplayBoard(o)
        
    



def MakeListOfFreeFields(board):
    boardVerifid[board] = "False"
    


def VictoryFor(sign):
    aa = 0
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == "False":

                aa += 1
            if aa == 9:
                quit()
            
    if (tablero[0][0] == sign and tablero[0][1] == sign and tablero[0][2] == sign or 
        tablero[1][0] == sign and tablero[1][1] == sign and tablero[1][2] == sign or
        tablero[2][0] == sign and tablero[2][1] == sign and tablero[2][2] == sign or
        tablero[0][0] == sign and tablero[1][0] == sign and tablero[2][0] == sign or
        tablero[0][1] == sign and tablero[1][1] == sign and tablero[2][1] == sign or 
        tablero[0][2] == sign and tablero[1][2] == sign and tablero[2][2] == sign or
        tablero[0][0] == sign and tablero[1][1] == sign and tablero[2][2] == sign or
        tablero[0][2] == sign and tablero[1][1] == sign and tablero[2][0] == sign ) :
        if(sign == "O"):
            print("¡Has Ganado!")
            quit()
        if(sign == "X"):
            print("¡Has Perdido!")
            quit()

def DrawMove():
    board = randrange(10)
    if board == 0:
        DrawMove()
    if boardVerifid[board] == "False":
        DrawMove()
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == board:
                MakeListOfFreeFields(board)
                tablero[i][j] = "X"
                printBoard()
                VictoryFor("X")
                EnterMove()

#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#

tablero = [[i for i in range(3)] for j in range(3)]
for i in range(3):
    for j in range(3):
        num += 1
        tablero[i][j] = num

tablero[1][1] = "X"

boardVerifid = {
    1: "True" ,
    2: "True" ,
    3: "True" ,
    4: "True" ,
    5: "False" ,
    6: "True" ,
    7: "True" ,
    8: "True" ,
    9: "True" ,
}

printBoard()
EnterMove()
DrawMove()