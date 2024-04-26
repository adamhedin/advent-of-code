data = open('day14').read().strip().split('\n')
symbols = {'rounded': 'O',
           'cube': '#',
           'empty': '.'}

m = [list(x) for x in data]
columns = [list(x) for x in list(map(''.join, zip(*data)))]
print(columns)
result = 0

def cycle(direction):
    for col in columns:
        empty_spaces = []
        for i, c in enumerate(col):
            match c:
                case 'O':
                    if empty_spaces:
                        col[i] = '.'
                        col[empty_spaces.pop(0)] = 'O'
                        empty_spaces.append(i)
                case '.':
                    empty_spaces.append(i)
                case '#':
                    empty_spaces = []
                case _:
                    break
        result += sum([(len(col)-i) if x == 'O' else 0 for i,x in enumerate(col)])

print(result)
    