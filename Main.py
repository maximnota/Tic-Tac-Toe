from iPyQT import *

matrix = []
num_rows = 0
num_columns = 0

Player_1 = 1
Player_2 = 2

isPlayer1Turn = True
isPlayer2Turn = False

Player_1Won = False
Player_2Won = False

texts = []
RowsMatrix = []

window = CustomWindow(250, 250, "Tic Tac Toe")
window.create()

def generateTicTacToe(height, width):
    global num_rows, num_columns
    num_rows = height
    num_columns = width
    for row in range(height):
        a = []
        for column in range(width):
            a.append("-")
        matrix.append(a)


def changeValue(Row, Column, value):
    matrix[Row][Column] = value

def printMatrixValue():
    for row in range(num_rows):
        for column in range(num_columns):
            print(matrix[row][column], end=" ")
        print()

def showMatrixValue():
    global RowsMatrix, texts
    RowsMatrix = []  
    for row in range(num_rows):
        row_text = ''
        for column in range(num_columns):
            text = str(matrix[row][column])
            row_text += text + ' '
        RowsMatrix.append(row_text)

    for text in texts:
        window.HideObject("Text", text)
    texts = []

    for row_text in RowsMatrix:
        text1 = window.addText(str(row_text), 25, "Center-top")
        texts.append(text1)


def checkRows(player):
    global Trow, TColumn

    if player == 1:
        print("Player 1")
        row_elements = matrix[Trow]
        if all(element == 'X' for element in row_elements):
            Player_1Won = True
            print("Player 1 wins in this row!")
        else:
            Player_2Won = True
            print("Player 1 does not win in this row")

    elif player == 2:
        print("Player 2")
        row_elements = matrix[Trow]
        if all(element == 'O' for element in row_elements):
            print("Player 2 wins in this row!")
        else:
            print("Player 2 does not win in this row")


def checkColumns(player):
    global Trow, TColumn

    if player == 1:
        print("Player 1")
        column_elements = [matrix[row][TColumn] for row in range(num_rows)]
        if all(element == 'X' for element in column_elements):
            print("Player 1 wins in this column!")
            winScreen(1)
        else:
            print("Player 1 does not win in this column")

    elif player == 2:
        print("Player 2")
        column_elements = [matrix[row][TColumn] for row in range(num_rows)]
        if all(element == 'O' for element in column_elements):
            print("Player 2 wins in this column!")
            winScreen(1)
        else:
            print("Player 2 does not win in this column")


def winScreen(player):
    window.HideAll()
    window.addText(f"Player {player} has won!", 25, "Center-top")


def Game():
    global isPlayer1Turn, isPlayer2Turn
    try:
        global Trow, TColumn
        Trow = int(window.getTextFieldValue(RowTextField))
        TColumn = int(window.getTextFieldValue(ColumnTextField))

        if isPlayer1Turn:
            changeValue(Trow, TColumn, "X")
            showMatrixValue()
            checkRows(1)
            checkColumns(1)
            isPlayer1Turn = False
            isPlayer2Turn = True
            window.changeWindowTitle("Player 2")

        elif isPlayer2Turn:
            changeValue(Trow, TColumn, "O")
            showMatrixValue()
            checkRows(2)
            checkColumns(2)
            isPlayer2Turn = False
            isPlayer1Turn = True
            window.changeWindowTitle("Player 1")

    except ValueError:
        print("Please enter valid numeric values for row and column.")

def mainUI():
    global RowTextField, ColumnTextField
    window.addText("Row", 25, "Center-top")
    RowTextField = window.addTextField(25, 50, "Center-top")
    window.addText("Column", 25, "Center-top")
    ColumnTextField = window.addTextField(25, 50, "Center-top")
    window.addButton("Play move", Game)

generateTicTacToe(3, 3)
mainUI()
showMatrixValue()
window.init()