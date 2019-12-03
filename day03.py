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
        if direction == 'R':
            for _ in range(length):
                curr_x += 1
                wire_coords.append((curr_x, curr_y))
        elif direction == 'L':
            for _ in range(length):
                curr_x -= 1
                wire_coords.append((curr_x, curr_y))
        elif direction == 'U':
            for _ in range(length):
                curr_y += 1
                wire_coords.append((curr_x, curr_y))
        elif direction == 'D':
            for _ in range(length):
                curr_y -= 1
                wire_coords.append((curr_x, curr_y))
    coords.append(wire_coords)

intersections = list(map(
    lambda c: (c, abs(c[0]) + abs(c[1])),
    set(coords[0]).intersection(coords[1])
))
print('Part 1:', min(intersections, key=lambda c: c[1])[1])

position_steps = [
    coords[0].index(intersection[0]) + coords[1].index(intersection[0]) + 2
    for intersection in intersections
]
print('Part 2:', min(position_steps))
