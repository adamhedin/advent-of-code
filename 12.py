from collections import Counter
from itertools import permutations


data = open('day12').read().strip().split('\n')
symbols = {
    '.': 'operational',
    '#': 'damaged',
    '?': 'unknown'
}

def create_solutiones(solutions, line):
    sol = solutions.copy()
    if line:
        c, line_new = line[0], line[1:]
        if len(line) < 2:
            line_new = ''
        print('t01234512341234', sol, c, line, line_new, 'asfasdf',['#' + x[1:] for x in solutions])
        if c == '?':
            
            sol += create_solutiones(['#' + x for x in solutions], line_new)
            print('calling')
            sol += create_solutiones(['.' + x for x in solutions], line_new)
        else:
            print('solved', sol)

            sol += create_solutiones([c + x for x in solutions], line_new)
    print('done')
    return sol
        
total = 0
for row in data:
    line, arrangements = row.split(' ')
    groups = [x for x in line.split('.') if '.' not in x and x]
    arrangements = list(map(int, arrangements.split(',')))
    max_values = [s.count('#') + s.count('?')for s in groups]
    solutions = ['']
    while line:
        c, line_new = line[0], line[1:]
        if len(line) < 2:
            line_new = ''
        if c == '?':
            new = [x + '#' for x in solutions] + [x + '.' for x in solutions]
        else: 
            new = [x + c for x in solutions]
        line, solutions = line_new, new
    solutions = ['.' + x + '.' for x  in solutions]
    solutions = [[len(y) for y in x.split('.') if y] for x  in solutions]
    arrangements
    results = len([x for x in solutions if x == arrangements])
    total += results

print(total)