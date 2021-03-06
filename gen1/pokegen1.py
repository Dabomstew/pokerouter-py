from pokemon import Pokemon
import species
import globfunc
import moveset
import math

class PokemonGen1(Pokemon):
    def __init__(self, args, p_species=None):
        # args should be a list
        if p_species == None:
            # args[0] is species
            specname = globfunc.hashName(args[0])
            if specname not in species.speciesByName:
                raise ValueError("Invalid species")
            p_species = species.speciesByName[specname]
            args = args[1:]
        elif type(p_species) != species.Species:
            raise ValueError("Invalid species")
        self.species = p_species
        self.level = 5
        self.ivs = {'hp': 8, 'atk': 9, 'def': 8, 'spd': 8, 'spc': 8 }
        self.statEXP = {'hp': 0, 'atk': 0, 'def': 0, 'spd': 0, 'spc': 0 }
        self.statEXPInUse = {'hp': 0, 'atk': 0, 'def': 0, 'spd': 0, 'spc': 0}
        self.stats = {'hp': 0, 'atk': 0, 'def': 0, 'spd': 0, 'spc': 0 }
        self.totalExp = 0
        self.moves = []
        self.wild = False
        
        # init defaults
        defaultMoveset = True
        self.moves = moveset.defaultMoveset(self.species, self.level)
        self.calculateStats()
        
        # read arguments
        arg_index = 0
        while arg_index < len(args):
            current_arg = args[arg_index].lower()
            arg_index += 1
            if current_arg == '-lvl' or current_arg == '-level':
                if arg_index == len(args):
                    raise ValueError("Started an argument (level) but no value")
                self.level = max(min(int(args[arg_index]),100),1)
                arg_index += 1
                self.calculateStats()
                if defaultMoveset:
                    self.moves = moveset.defaultMoveset(self.species, self.level)
            elif current_arg == '-ivs':
                if arg_index == len(args):
                    raise ValueError("Started an argument (IVs) but no value")
                ivs = args[arg_index].split('/')
                arg_index += 1
                if len(ivs) != 4:
                    raise ValueError("Specified IVs but didn't provide 4")
                self.ivs['atk'] = max(min(int(ivs[0]),15),0)
                self.ivs['def'] = max(min(int(ivs[1]),15),0)
                self.ivs['spd'] = max(min(int(ivs[2]),15),0)
                self.ivs['spc'] = max(min(int(ivs[3]),15),0)
                self.recalcHPIV()
                self.calculateStats()
            elif current_arg == '-statxp' or current_arg == '-sxp':
                if arg_index == len(args):
                    raise ValueError("Started an argument (Stat XP) but no value")
                sxp = args[arg_index].split('/')
                arg_index += 1
                if len(sxp) != 5:
                    raise ValueError("Specified Stat XP but didn't provide 5 values")
                self.statEXP['hp'] = max(min(int(sxp[0]),65535),0)
                self.statEXP['atk'] = max(min(int(sxp[1]),65535),0)
                self.statEXP['def'] = max(min(int(sxp[2]),65535),0)
                self.statEXP['spd'] = max(min(int(sxp[3]),65535),0)
                self.statEXP['spc'] = max(min(int(sxp[4]),65535),0)
                self.updateUsedStatXP()
                self.calculateStats()
            elif current_arg == '-wild':
                self.wild = True
    
    def recalcHPIV(self):
        self.ivs['hp'] = (self.ivs['atk'] % 2) * 8 + (self.ivs['def'] % 2) * 4 + (self.ivs['spd'] % 2) * 2 + (self.ivs['spc'] % 2)
        
    def updateUsedStatXP(self):
        self.statEXPInUse['hp'] = self.statEXP['hp']
        self.statEXPInUse['atk'] = self.statEXP['atk']
        self.statEXPInUse['def'] = self.statEXP['def']
        self.statEXPInUse['spd'] = self.statEXP['spd']
        self.statEXPInUse['spc'] = self.statEXP['spc']
        
    def calculateStats(self):
        for stat in ('hp', 'atk', 'def', 'spd', 'spc'):
            self.stats[stat] = self.calculateStat(stat, self.species.getBase(stat), self.ivs[stat], self.statEXPInUse[stat])
            
    def calculateStat(self, stat, base, iv, statXP):
        if stat == 'hp':
            return self.calcStatNumerator(base, iv, statXP) * self.level / 100 + self.level + 10
        else:
            return self.calcStatNumerator(base, iv, statXP) * self.level / 100 + 5
            
    def calcStatNumerator(self, base, iv, statXP):
        return 2 * (base + iv) + self.sxpCalc(statXP)
    
    def sxpCalc(self, statXP):
        return min(255, int(math.ceil(math.sqrt(statXP)))) / 4
    
    def learnMove(self, move):
        if move not in self.moves:
            self.moves.append(move)
    
    def unlearnMove(self, move):
        if move in self.moves:
            self.moves.remove(move)
    
    def __repr__(self):
        return "%s LV%d stats %d/%d/%d/%d/%d moves %s" % (self.species.name, self.level, self.stats['hp'], self.stats['atk'], self.stats['def'], self.stats['spd'], self.stats['spc'], self.moves.__repr__())
