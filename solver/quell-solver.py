class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Wall(Cell):
    def __str__(self):
        return "#"

class Jewel(Cell):
    def __str__(self):
        return "*"

class Open(Cell):
    def __str__(self):
        return " "

class Drop(Cell):
    def __str__(self):
        return "O"

class Board:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.cells = [[[] for i in range(self.w)] for j in range(self.h)]
        self.dropX = 0
        self.dropY = 0

    def __str__(self):
        boardString = ""
        for row in self.cells:
            for cell in row:
                boardString += str(cell)
            boardString += "\n"
        return boardString.rstrip()

    def convertCharacterToCell(self, x, y, character):
        if character == "#":
            return Wall(x, y)
        elif character == "*":
            return Jewel(x, y)
        elif character == " ":
            return Open(x, y)
        elif character == "O":
            return Drop(x, y)

    def loadMap(self, cellString):
        cells = [list(row) for row in cellString.split("\n")]
        for y in range(len(cells)):
            for x in range(len(cells[y])):
                character = cells[y][x]
                if character == "O":
                    self.dropX = x
                    self.dropY = y
                    self.cells[y][x] = \
                            self.convertCharacterToCell(x, y, character)
                else:
                    self.cells[y][x] = \
                            self.convertCharacterToCell(x, y, character)
