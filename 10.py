symbols = {
    '|': ((-1, 0), (1, 0)), 
    '-': ((0, -1), (0, 1)), 
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)), 
    '7': ((0, -1), (1, 0)), 
    'F': ((1, 0), (0, 1)),
    '.': (), 
    'S': [(1, 0), (-1, 0), (0, 1), (0, -1)], 
}

rows = open('day10').read().strip().split('\n')
edges = {}
start = (None, None)
gridsize = len(rows)

for r, row in enumerate(rows):
    for c, symbol in enumerate(row):
        edges[(r, c)] = [(r + r_, c + c_) for r_, c_ in symbols[symbol] if 0 <=r + r_ <= gridsize and 0 <=c + c_ <= gridsize]
        if symbol == 'S':
            start = (r, c)
draw = []
for i in range(gridsize):
    y = []
    for s in range(gridsize):
        y.append('.')
    draw.append(y)
discovered = {k: {'found' : False, 'parent': (None, None), 'distance': 0} for k,v in edges.items()}
def bfs(root):
   
    queue = []
    draw[root[0]][root[1]] = 'S'
    discovered[root]['found'] = True
    discovered[root]['distance'] = 0
    queue.append(root)
    while queue:
        v = queue.pop(0)
        for w in edges[v]:
            
            if not discovered[w]['found']:
                discovered[w]['found'] = True
                discovered[w]['parent'] = v
                discovered[w]['distance'] = discovered[v]['distance'] + 1
                draw[w[0]][w[1]] = str(discovered[v]['distance'] + 1)
                queue.append(w)

    test = open('test', 'w')
    for t in draw:
        test.write(''.join(t) + '\n')
bfs(start)

distances = [discovered[k]['distance'] for k in discovered.keys() if discovered[k]['found']]
print(max(distances))

#6831hdd 