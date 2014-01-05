from gen1.pokegen1 import PokemonGen1
import gen1.init
import gen1.alias
import gen1.moveset
import settings
import party
import globfunc
import gameaction

class RouteParser(object):
    def parseFile(self, filename):
        f = open(filename, 'r')
        gameline = f.readline()
        gametokens = gameline.split()
        if len(gametokens) < 2 or gametokens[0] != 'game':
            raise ValueError("First line of a route must be the game definition")
        gameid = gametokens[1]
        if gameid == 'red' or gameid == 'blue' or gameid == 'yellow':
            settings.pokemonObj = PokemonGen1
            settings.damageCalc = None
            settings.initFunc = gen1.init.gen1Init
            settings.generation = 1
            settings.aliasFunc = gen1.alias.aliasFunc
            settings.moveDict = gen1.moveset.movesByName
        else:
            raise ValueError("Game not implemented yet")
        
        settings.initFunc(gameid)
        
        myParty = party.Party()
        partyMode = True
        actionList = []
        for line in f:
            tokens = line.split()
            if len(tokens) == 0:
                continue
            command = tokens[0].lower()
            if partyMode and command == 'pokemon':
                myParty.append(settings.pokemonObj(tokens[1:]))
                continue
            elif command == 'pokemon':
                raise ValueError("Trying to define a party Pokemon after party finished.")
            elif partyMode:
                partyMode = False
            
            # parse for non-partymode here
            if command == 'learnmove' or command == 'lm':
                # move
                if len(tokens) == 1:
                    raise ValueError("No move specified")
                moveName = globfunc.hashName(tokens[1])
                if moveName not in settings.moveDict:
                    raise ValueError("Invalid move")
                actionList.append(gameaction.LearnMove(settings.moveDict[moveName]))
            elif command == 'unlearnmove' or command == 'um' or command == 'forget':
                # move
                if len(tokens) == 1:
                    raise ValueError("No move specified")
                moveName = globfunc.hashName(tokens[1])
                if moveName not in settings.moveDict:
                    raise ValueError("Invalid move")
                actionList.append(gameaction.UnlearnMove(settings.moveDict[moveName]))
            elif command == 'setmain' or command == 'use':
                # move
                if len(tokens) == 1:
                    raise ValueError("No new main specified")
                newMain = int(tokens[1])
                if newMain > len(myParty.partyPokemon):
                    raise ValueError("Invalid Setmain: You don't have that many Pokemon.")
                if newMain <= 0:
                    raise ValueError("Invalid Setmain: The Pokemon should be number 1-n.")
                actionList.append(gameaction.SetMain(newMain))
            else:
                # try to parse as trainer
                if settings.aliasFunc != None:
                    command = settings.aliasFunc(command)
                print 'trainer ' + command
        
        print myParty
        print actionList
        # run
        for action in actionList:
            action.performAction(myParty)
        
        print myParty
        f.close()
