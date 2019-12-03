import asyncio


async def build_paths(wires):
    # expand wire paths to coordinates
    paths = []
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
        paths.append(wire_coords)
    return paths


async def part1(wires):
    paths = await build_paths(wires)
    intersections = set(paths[0]).intersection(paths[1])
    return min(map(lambda i: abs(i[0]) + abs(i[1]), intersections))


async def part2(wires):
    paths = await build_paths(wires)
    intersections = set(paths[0]).intersection(paths[1])
    return min(map(
        lambda i: paths[0].index(i) + paths[1].index(i) + 2,
        intersections
    ))


if __name__ == '__main__':
    wires = []
    with open('inputs/03') as f:
        wires = list(map(lambda l: l.rstrip('\n').split(','), f.readlines()))
    print('Part 1:', asyncio.run(part1(wires)))
    print('Part 2:', asyncio.run(part2(wires)))
