import species
import moveset
import alias
def gen1Init(gameid):
    species.init()
    moveset.initMovesAndSets(gameid)
    alias.init(gameid)