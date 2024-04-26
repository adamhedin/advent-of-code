data = open('day13').read().strip().split('\n\n')
result= 0

def find_matches(rows, type_rows):
    if not type_rows:
        rows = list(map(''.join, zip(*rows)))
    limit = len(rows)
    print('\n\npattern', rows, '\n', type_rows, limit)
    for i in range(limit - 1):
        match = True
        print('index', i)
        for r in range(max(i*2+2-limit, 0), i +1):
            print('testing', i, r, i*2+1-r)
            
            if i*2+1-r >= limit or not rows[r] == rows[i*2+1-r]:
                print('false', i, r, i*2+1-r, rows)
                match = False
                break
            print('true', i, r)
        if match:
            print('match', rows, i)
            if type_rows:
                print('result', 100*(i + 1), type_rows, result)
                return 100*(i + 1)
            else:
                print('result', i + 1, type_rows, result)
                return i + 1
    return 0
                
print('data', data)
result = 0 
for pattern in data:
    res = find_matches(pattern.split('\n'), True)
    if not res:
        res = find_matches(pattern.split('\n'), False)
    if not res:
        print('STOP', pattern)
        break
    
    result += res

print(result)
