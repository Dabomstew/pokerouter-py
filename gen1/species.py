import expcurve
import poketype
import globfunc

class Species:
    def __init__(self, s_name, s_curve, s_type1, s_type2, s_baseHP, s_baseAtk, s_baseDef, s_baseSpc, s_baseSpd, s_killExp, s_pokedexNum):
        self.name = s_name
        self.curve = s_curve
        self.type1 = s_type1
        self.type2 = s_type2
        self.baseHP = s_baseHP
        self.baseAtk = s_baseAtk
        self.baseDef = s_baseDef
        self.baseSpc = s_baseSpc
        self.baseSpd = s_baseSpd
        self.killExp = s_killExp
        self.pokedexNum = s_pokedexNum
        
    def getBase(self, stat):
        if stat == 'hp':
            return self.baseHP
        elif stat == 'atk':
            return self.baseAtk
        elif stat == 'def':
            return self.baseDef
        elif stat == 'spd':
            return self.baseSpd
        elif stat == 'spc':
            return self.baseSpc
        raise ValueError("Invalid stat")
        
    
allSpecies = []
speciesByName = {}
numPokes = 0

def init():
    f = open('./gen1/species.txt', 'r')
    global numPokes
    numPokes = int(f.readline().strip())
    for i in range(0, numPokes+1):
        s_name = f.readline().strip()
        s_curve = expcurve.fromString(f.readline())
        s_type1 = poketype.fromString(f.readline())
        s_type2 = poketype.fromString(f.readline())
        s_baseHP = int(f.readline().strip())
        s_baseAtk = int(f.readline().strip())
        s_baseDef = int(f.readline().strip())
        s_baseSpc = int(f.readline().strip())
        s_baseSpd = int(f.readline().strip())
        s_killExp = int(f.readline().strip())
        s_pokedexNum = i
        
        s = Species(s_name, s_curve, s_type1, s_type2, s_baseHP, s_baseAtk, s_baseDef, s_baseSpc, s_baseSpd, s_killExp, s_pokedexNum)
        allSpecies.append(s)
        speciesByName[globfunc.hashName(s_name)] = s
    f.close()
