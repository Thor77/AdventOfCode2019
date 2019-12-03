wires = []
with open('inputs/03') as f:
    wires = list(map(lambda l: l.rstrip('\n').split(','), f.readlines()))

# expand wire paths to coordinates
coords = []
for wire in wires:
    curr_x = 0
    curr_y = 0
    wire_coords = []
    for instruction in wire:
        direction = instruction[0]
        length = int(instruction[1:])
        steps = range(length)
        if direction == 'R':
            path = list(map(lambda i: (curr_x + i + 1, curr_y), steps))
            curr_x += length
        elif direction == 'L':
            path = list(map(lambda i: (curr_x - i - 1, curr_y), steps))
            curr_x -= length
        elif direction == 'U':
            path = list(map(lambda i: (curr_x, curr_y + i + 1), steps))
            curr_y += length
        elif direction == 'D':
            path = list(map(lambda i: (curr_x, curr_y - i - 1), steps))
            curr_y -= length
        wire_coords.extend(path)
    coords.append(wire_coords)

intersections = set(coords[0]).intersection(coords[1])

print('Part 1:', min(map(lambda i: abs(i[0]) + abs(i[1]), intersections)))
print('Part 2:', min(map(
    lambda i: coords[0].index(i) + coords[1].index(i) + 2,
    intersections
)))
