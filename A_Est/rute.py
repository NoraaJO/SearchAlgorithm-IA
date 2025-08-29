class Rute:
    def __init__(self, State, Parent, ValueH, Moves = 0):
        self.State = State
        self.parent = Parent
        self.Son = None;
        self.Value = ValueH+Moves;
        self.cantMove = Moves;

    def setSon(self, Son):
        self.Son = Son;

    def getSon(self):
        return self.Son;

    def getValue(self):
        return self.Value;

    def getParent(self):
        return self.parent;
    
    def getState(self):
        return self.State
    
    def getCantMoves(self):
        return self.cantMove;

    def isObjective(self):
        return (len(self.State ) == 1)
    
    def __str__(self):
        return f"Valor {self.Value} Estado {self.State}"