class GameAction(object):
    def performAction(self, myParty):
        raise NotImplementedError
    
class LearnMove(GameAction):
    
    def __init__(self, move):
        self.move = move
        
    def performAction(self, myParty):
        myParty.getCurrentMain().learnMove(self.move)
        
class UnlearnMove(GameAction):
    
    def __init__(self, move):
        self.move = move
        
    def performAction(self, myParty):
        myParty.getCurrentMain().unlearnMove(self.move)

class SetMain(GameAction):
    
    def __init__(self, mainNo):
        self.mainNo = mainNo
        
    def performAction(self, myParty):
        myParty.setMain(self.mainNo)

