import settings
class Type(object):
    pass

NORMAL = Type()
FIGHTING = Type()
FLYING = Type()
GRASS = Type()
WATER = Type()
FIRE = Type()
ELECTRIC = Type()
GHOST = Type()
PSYCHIC = Type()
BUG = Type()
POISON = Type()
ROCK = Type()
GROUND = Type()
DRAGON = Type()
ICE = Type()
STEEL = Type()
DARK = Type()
QUESTION = Type()
NONE = Type()

def isValid(typeToCheck):
    if type(typeToCheck) != Type:
        return False
    if settings.generation == 1 and (typeToCheck == STEEL or typeToCheck == DARK):
        return False
    if (settings.generation == 1 or settings.generation == 5) and typeToCheck == QUESTION:
        return False
    return True

def fromString(typeString):
    if type(typeString) != str:
        raise ValueError("Invalid input to type.fromString()")
    typeup = typeString.upper().strip()
    if typeup == 'NORMAL':
        return NORMAL
    elif typeup == 'FIGHTING':
        return FIGHTING
    elif typeup == 'FLYING':
        return FLYING
    elif typeup == 'GRASS':
        return GRASS
    elif typeup == 'WATER':
        return WATER
    elif typeup == 'FIRE':
        return FIRE
    elif typeup == 'ELECTRIC':
        return ELECTRIC
    elif typeup == 'GHOST':
        return GHOST
    elif typeup == 'PSYCHIC':
        return PSYCHIC
    elif typeup == 'BUG':
        return BUG
    elif typeup == 'POISON':
        return POISON
    elif typeup == 'ROCK':
        return ROCK
    elif typeup == 'GROUND':
        return GROUND
    elif typeup == 'DRAGON':
        return DRAGON
    elif typeup == 'ICE':
        return ICE
    elif typeup == 'STEEL':
        return STEEL
    elif typeup == 'DARK':
        return DARK
    elif typeup == '???' or typeup == 'QUESTION':
        return QUESTION
    else:
        return NONE