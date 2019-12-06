def path_length(orbits, key, steps=0):
    if key in orbits:
        return path_length(orbits, orbits[key], steps + 1)
    else:
        return steps


if __name__ == '__main__':
    map_data = []
    with open('inputs/06') as f:
        map_data = f.read().splitlines()

    orbits = {}
    for statement in map_data:
        o1, o2 = statement.split(')')
        if o2 in orbits:
            raise 'This shouldn\'t happen'
        orbits[o2] = o1

    total = 0
    for key in orbits.keys():
        length = path_length(orbits, key)
        total += length

    print('Part 1:', total)
