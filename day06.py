def path_length(orbits, key, steps=0, path=[]):
    if key in orbits:
        return path_length(orbits, orbits[key], steps + 1, path + [key])
    else:
        return steps, path


if __name__ == '__main__':
    map_data = []
    with open('inputs/06') as f:
        map_data = f.read().splitlines()

    orbits = {}
    for statement in map_data:
        o1, o2 = statement.split(')')
        orbits[o2] = o1

    total = 0
    for key in orbits.keys():
        length, path = path_length(orbits, key)
        total += length

    print('Part 1:', total)

    # find start and end object
    start = orbits['YOU']
    end = orbits['SAN']
    _, start_path = path_length(orbits, start)
    _, end_path = path_length(orbits, end)
    for i, obj in enumerate(start_path):
        if obj in end_path:
            print('Part 2:', i + end_path.index(obj))
            break
