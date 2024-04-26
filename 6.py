data = open('day6').read().strip().split('\n')

def partone():
    time, distance = [list(map(int, x.split(': ')[1].strip().split())) for x in data]
    pairs = list(zip(time, distance))
    print(pairs)

    res = 1
    for time, distance in pairs:
        ways = 0
        for t in range(1, time):
            if (time - t)*t > distance:
                ways += 1
        res*=ways
    print(res)

def parttwo():
    time, distance = [int(''.join(x.split(': ')[1].strip().split())) for x in data]
    res = 1
    ways = 0
    for t in range(1, time):
        if (time - t)*t > distance:
            ways += 1
    res*=ways
    print(res)

parttwo()