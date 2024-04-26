data = open('day11').read().strip().split('\n')
galaxy_symbol, empty_space = '#', '.'
parttwo = True
expansion = 1000000 if parttwo else 2

def space_expansion(x):
    x = [[row]*expansion if not galaxy_symbol in row else row for row in x]
    for i, row in enumerate(x):
        if isinstance(row, list):
            for y in range(1, expansion):    
                x[i] = row[0]
                x.insert(i+y, row[y])
    return x

row_to_col = lambda x : list(map(''.join,zip(*x)))
rows = space_expansion(data)
cols = space_expansion(row_to_col(rows))
rows = row_to_col(cols)
galaxies = [(r, c) for r, row in enumerate(rows) for c, value in enumerate(row) if value is galaxy_symbol ]
distance = 0

for i, galaxy in enumerate(galaxies):
    index = i + 1
    while index < len(galaxies):
        current_galaxy = galaxies[index]
        #print(i, galaxy, index, current_galaxy, list(zip(current_galaxy, galaxy)))
        
        distance += sum([abs(x - y) for x,y in list(zip(current_galaxy, galaxy))])
        index += 1

    

print(distance)