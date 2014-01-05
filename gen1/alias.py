
aliasMap = {}

def init(gameid):
    filename = 'aliases_blue.txt'
    if gameid == 'yellow':
        filename = 'aliases_yellow.txt'
    
    f = open('./gen1/' + filename, 'r');
    for line in f:
        parts = line.split()
        if len(parts) != 2:
            continue
        aliasMap[parts[0]] = parts[1]
    f.close()
    
def aliasFunc(command):
    if command in aliasMap:
        return aliasMap[command]
    return command
