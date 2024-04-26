from collections import Counter

data = open('day7').read().strip()
hands = [x.split() for x in data.split('\n')]
values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

def find_type(hand):
    hand = hand
    if Counter(hand).most_common(1)[0][0] == 'J':    
        hand = hand.replace('J', Counter(hand).most_common(3)[1][0] if len(Counter(hand).most_common()) > 1 else 'J')
    else:
        hand = hand.replace('J', Counter(hand).most_common(3)[0][0])
    c = Counter(hand).most_common(3)
    j = Counter(hand)['J']

    if c[0][1] == 5:
        return 0
    elif c[0][1] == 4:
        return 1
    elif c[0][1] == 3 and c[1][1] == 2 and c[0][1] + c[1][1] == 5:
        return 2
    elif c[0][1] == 3:
        return 3
    elif c[0][1] >= 2 and c[1][1] >= 2 and c[0][1] + c[1][1] == 4:
        return 4
    elif c[0][1] == 2:
        return 5
    else:
        return 6
    

def parttwo():
    values.remove('J')
    values.append('J')


for hand in hands:
    hand.append(find_type(hand[0]))
parttwo()
hands.sort(key=lambda x: (x[2], values.index(x[0][0]), values.index(x[0][1]), values.index(x[0][2]), values.index(x[0][3]), values.index(x[0][4])))
print(hands)
print(sum([(len(hands)-c)*int(e[1]) for c, e in enumerate(hands)]))