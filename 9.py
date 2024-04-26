data = open('day9').read().strip().split('\n')
histories = [list(map(int, x.split())) for x in data]
values = []
part_two = True
for history in histories:
    current_values = history
    iterations = [current_values]
    while set(current_values) != set([0]):
        current_values = [y - x for (x, y) in list(zip(current_values, current_values[1:]))]
        iterations.append(current_values)
    value = 0
    while iterations:
        value = iterations.pop()[0 if part_two else -1] - (value if part_two else + value)
    values.append(value)
print(sum(values))