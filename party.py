class Party(object):

    def __init__(self):
        self.partyPokemon = []
        self.currentMain = 1
        
    def append(self, pkmn):
        self.partyPokemon.append(pkmn)
    
    def getCurrentMain(self):
        return self.partyPokemon[self.currentMain - 1]
    
    def setMain(self, main):
        if main >= 1 and main <= len(self.partyPokemon):
            self.currentMain = main
    
    def getPokemon(self, number):
        return self.partyPokemon[number - 1]
    
    def __iter__(self):
        self.iterIndex = 0
        return self
    
    def next(self):
        if self.iterIndex >= len(self.partyPokemon):
            raise StopIteration
        else:
            self.iterIndex += 1
            return self.partyPokemon[self.iterIndex - 1]
        
    def __repr__(self):
        return self.partyPokemon.__repr__()
    
        
