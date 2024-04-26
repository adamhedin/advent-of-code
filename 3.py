with open('day3') as inputfile:
    rows = [list('.' + line.strip() + '.' ) for line in inputfile]


rows.append(['.']*142)
rows.insert(0, ['.']*142)

symbols = list(set([x for xs in rows for x in xs if not x.isdigit() and x != '.']))


gears = {(1,2): []}

result = 0
test = [x for xs in rows for x in xs]


def check_adjecent(row_i, col_i, number):
    length = len(str(number))
    adj_cor = [(row_i, col_i - 1), (row_i, col_i + length)] + [(row_i - 1, i) for i in range(col_i - 1, col_i + length + 1)] + [(row_i + 1, i) for i in range(col_i - 1, col_i + length + 1)]
    for r, c in adj_cor:
        if (r, c) in gears:
            gears[(r, c)].append(number)
    if rows[row_i][col_i - 1] in symbols or rows[row_i][(col_i + length)] in symbols:
        return True
    for i in range(col_i - 1, col_i + length + 1):
        if rows[(row_i - 1)][i] in symbols or rows[(row_i + 1)][i] in symbols: 
            return True
    return False

for row_i, row in list(enumerate(rows)):
    for col_i, char in list(enumerate(row)):
        if char == '*':
            gears[(row_i, col_i)] = []

for row_i, row in list(enumerate(rows)):
    prevchar = ''
    number = ''
    for col_i, char in list(enumerate(row)):
        if char.isdigit():
            number = number + char
        else:
            if number:
                if check_adjecent(row_i, col_i - len(number), number):
                    result += int(number)
            number = ''

part2result = 0
for k, gear in gears.items():
    if len(gear) == 2:
        part2result += int(gear[0])*int(gear[1])
    
        
print(gears)
print(part2result)