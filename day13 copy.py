data = open('day13').read().strip().split('\n\n')
width = len(data[0].split('\n')[0])
length = len(data[0].split('\n'))
print(width, length)
result= 0


for pattern in data:
    rows = pattern.split('\n')
    print('rows', rows)
    for i in range(length - 2):
        match = True
        print('index', i)
        for r in range(max(i*2-width+2, 0), i +1):
            print('testing', r, i*2+1-r)
            if not rows[r] == rows[i*2+1-r]:
                print('false', i, r, rows)
                match = False
                break
            print('true', i, r)
        if match:
            print('match', rows, i)
            result += 100*(i + 1)
            break

print(result)


'''            2,3
            range(0,2)
            i = 0
            0,1

            i=1
            0,3
            1,2
            
            i=2
            0,5
            1,4
            2,3

            i=3
            1,6
            2,5
            3,4

            i=4
            3,6
            4,5


            i=5
            5,6
'''