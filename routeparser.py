from gen1.pokegen1 import PokemonGen1
import gen1.init
import settings

class RouteParser(object):
    def parseFile(self, filename):
        f = open(filename, 'r')
        gameline = f.readline()
        gametokens = gameline.split()
        if len(gametokens)<2 or gametokens[0] != 'game':
            raise ValueError("First line of a route must be the game definition")
        gameid = gametokens[1]
        if gameid == 'red' or gameid == 'blue' or gameid == 'yellow':
            settings.pokemonObj = PokemonGen1
            settings.damageCalc = None
            settings.initFunc = gen1.init.gen1Init
            settings.generation = 1
        else:
            raise ValueError("Game not implemented yet")
        
        settings.initFunc(gameid)
        
        party = []
        partyMode = True
        for line in f:
            tokens = line.split()
            command = tokens[0].lower()
            if partyMode and command == 'pokemon':
                party.append(settings.pokemonObj(tokens[1:]))
                continue
            elif command == 'pokemon':
                raise ValueError("Trying to define a party Pokemon after party finished.")
            elif partyMode:
                partyMode = False
            
            # parse for non-partymode here
            print 'command = %s' % command
        
        print party
        f.close()