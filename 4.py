cards = list(open('day4'))
cards = [(card.split(':')[1].split('|')[0].split(), card.split(':')[1].split('|')[1].split()) for card in cards]
res= 0

def partone():
    res= 0
    for game in cards:
        points = 0
        for num in game[1]:
            if num in game[0]:
                points = max(1, points *2)
        res += points
    print(res)

result = 0
def scratch(game):
    score= 1
    points = 0
    for num in cards[game][1]:
        if num in cards[game][0]:
            points += 1
    for i in range(1, min(points, 211)):
        score += scratch(game + i)
    return score

for i in range(len(cards)):
    result += scratch(i)
print(result)