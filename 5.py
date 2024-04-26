import re

input = open('day5').read().strip()

S = input.split('\n\n')

seedssss = S[0].split(': ')[1].split(' ')
seeds = dict.fromkeys(seedssss)
for seed in seedssss:
    seeds[seed] = {'seed': int(seed)}


def partone():
    for s in S[1:]:
        att = s.split(' map:\n')[0].split('-')
        new = s.split(':\n')[1].split('\n')
        source = att[0]
        destination = att[2]
        for array in new:
            dest, src, lgt = [int(x) for x in array.split(' ')]
            for seed, value in seeds.items():
                if value[source] in range(src, src + lgt):
                    seeds[seed][destination] = value[source] + dest - src
                elif not destination in value:
                    value[destination] = value[source]

    print(min([v['location'] for k,v in seeds.items()]))


def parttwo():
    locations = [x for x in range(0, answerspan)]
    seeds = dict.fromkeys(locations)
    for seed in locations:
        seeds[seed] = {'location': int(seed)}
    
    it = iter(seedssss)
    initial_seeds = list(zip(it, it))

    for cat in reversed(S[1:]):
        att = cat.split(' map:\n')[0].split('-')
        new = cat.split(':\n')[1].split('\n')
        source = att[2]
        destination = att[0]
        for array in new:
            dest, src, lgt = [int(x) for x in array.split(' ')]
            for seed, value in seeds.items():
                if value[source] in range(src, src + lgt):
                    seeds[seed][destination] = value[source] + dest - src
                elif not destination in value:
                    value[destination] = value[source]
    exist = []
    for k, v in seeds.items():
        for span in initial_seeds:
            #[x for x in seeds if span[0] <= v['seed'] <= span[0] + span[1]]

            if int(span[0]) <= v['seed'] <= int(span[0]) + int(span[1]):
                exist.append(v)
    print(exist)

it = iter(seedssss)
initial_seeds = list(zip(it, it))
answerspan = 10000000

def parttwo_2():
    answer = 0
    for x in range(0, answerspan):
        answer = x
        for s in reversed(S[1:]):
            new = s.split(':\n')[1].split('\n')
            for array in new:
                dest, src, lgt = [int(x) for x in array.split(' ')]
                if src <= answer <= src +lgt:
                    answer = answer + dest - src
                    break
        for seed in initial_seeds:
            if int(seed[0]) <= answer <= int(seed[0]) + int(seed[1]):
                return x
    return False
    

print(parttwo_2())
seed_to_soil = S[1].split(':\n')[1].split('\n')
soil_to_fertilizer = S[2].split(':\n')[1].split('\n')
fertilizer_to_water = S[3].split(':\n')[1].split('\n')
water_to_light = S[4].split(':\n')[1].split('\n')
light_to_temperature = S[5].split(':\n')[1].split('\n')
temperature_to_humidity = S[6].split(':\n')[1].split('\n')
humidity_to_location = S[7].split(':\n')[1].split('\n')
