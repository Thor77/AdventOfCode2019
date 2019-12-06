def find_path(orbits, key):
    path = []
    while key in orbits:
        path.append(key)
        key = orbits[key]
    return path


if __name__ == '__main__':
    map_data = []
    with open('inputs/06') as f:
        map_data = f.read().splitlines()

    orbits = {
        o[1]: o[0]
        for o in map(lambda md: md.split(')'), map_data)
    }

    print('Part 1:', sum(map(lambda k: len(find_path(orbits, k)), orbits.keys())))

    # find start and end object
    start = orbits['YOU']
    end = orbits['SAN']
    start_path = find_path(orbits, start)
    end_path = find_path(orbits, end)
    for i, obj in enumerate(start_path):
        if obj in end_path:
            print('Part 2:', i + end_path.index(obj))
            break
