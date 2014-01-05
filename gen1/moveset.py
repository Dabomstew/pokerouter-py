import poketype
import globfunc
import species

class Move:
    def __init__(self, m_name, m_type, m_pp, m_power, m_accuracy, m_indexNum):
        self.name = m_name
        self.type = m_type
        self.pp = m_pp
        self.power = m_power
        self.accuracy = m_accuracy
        self.indexNum = m_indexNum
        
    def __repr__(self):
        return self.name
        #return "%s with %d PP, %d PWR, %d ACC, %d INUM" % (self.name, self.pp, self.power, self.accuracy, self.indexNum)
        
class LevelMove:
    def __init__(self, level, move):
        self.level = level
        self.move = move
        
    def __repr__(self):
        return "%s at L%d" % (self.move.name, self.level)
        
moves = []
movesByName = {}
learnsets = []
numMoves = 0

def initMovesAndSets(gameid):
    f = open('./gen1/moves.txt', 'r')
    numMoves = int(f.readline().strip())
    for i in range(0, numMoves+1):
        m_name = f.readline().strip()
        m_type = poketype.fromString(f.readline())
        m_pp = int(f.readline().strip())
        m_power = int(f.readline().strip())
        m_accuracy = int(f.readline().strip())
        m_indexNum = i
        
        m = Move(m_name, m_type, m_pp, m_power, m_accuracy, m_indexNum)
        moves.append(m)
        movesByName[globfunc.hashName(m_name)] = m
    f.close()
    
    if gameid == 'yellow':
        initLearnsets('moveset_yellow.txt')
    else:
        initLearnsets('moveset_blue.txt')
    
    print moves
    print learnsets
        
def initLearnsets(filename):
    print species.allSpecies
    f = open('./gen1/'+filename, 'r')
    learnsets.append([])
    f.readline() # useless pokemon count
    for i in range(1, species.numPokes+1):
        learnset = []
        learntokens = f.readline().strip().split()
        k = len(learntokens)/2
        for j in range(0, k):
            lvl = int(learntokens[j*2])
            move = moves[int(learntokens[j*2+1])]
            learnset.append(LevelMove(lvl, move))
        learnsets.append(learnset)
    f.close()

def defaultMoveset(spec, level):
    idx = spec.pokedexNum
    retset = []
    for lmove in learnsets[idx]:
        if lmove.level <= level:
            if lmove.move not in retset:
                if len(retset) == 4:
                    retset = retset[1:]
                retset.append(lmove.move)
    return retset  