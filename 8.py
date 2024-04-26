from math import lcm

directionorder, nodes = open('day8').read().strip().split('\n\n')
nodes = [node.split(' = ') for node in nodes.split('\n')]
nodes = {k:v.translate({ord(i): None for i in '()'}).split(', ') for k, v in nodes}
parttwo = True

directionorder = list(directionorder)
dest = 'ZZZ'
current = 'AAA'
ways = {'L': 0, 'R': 1}
steps = 0
directions = directionorder.copy()
if parttwo:
    current = set([k for k in nodes.keys() if k[2] == 'A'])
    dest = set([k for k in nodes.keys() if k[2] == 'Z'])
    stepset = []
    for current in [k for k in nodes.keys() if k[2] == 'A']:
        while current not in dest:
            current = nodes[current][ways[directions.pop(0)]]
            steps += 1
            if not directions:
                directions = directionorder.copy()
        stepset.append(steps)
        directions = directionorder.copy()
        steps = 0
    print(stepset)
    print(lcm(*stepset))

else: 
    while current != dest:
        current = nodes[current][ways[directions.pop(0)]]
        steps += 1
        if not directions:
            directions = directionorder.copy()

    print(steps)