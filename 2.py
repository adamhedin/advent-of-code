import fileinput 

input = fileinput.input(files ='day2')
max = {'red': 12, 'green': 13, 'blue': 14}

def partone():
    result = 0
    for game in input:
        id = int(game.split(': ')[0].split('Game ')[1])
        ok = True
        for set in game.split(': ')[1].split('; '):
            for round in set.split(', '):
                value = int(round.split()[0])
                color = round.split()[1]
                if value > max[color]:
                    ok = False
                    break
        if ok:
            result += id
    return result

def parttwo():
    result = 0
    for game in input:
        res = 1
        localmax = {'red': 0, 'green': 0, 'blue': 0}
        id = int(game.split(': ')[0].split('Game ')[1])
        for set in game.split(': ')[1].split('; '):
            for round in set.split(', '):
                value = int(round.split()[0])
                color = round.split()[1]
                if value > localmax[color]:
                    localmax[color] = value
        for value in localmax.values():
            res *= value

        result += res

    return result

        
print(parttwo())