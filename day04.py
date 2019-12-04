import collections


def is_valid(pw):
    pw_str = str(pw)
    if collections.Counter(pw_str).most_common(1)[0][1] < 2:
        return False
    for i, c in enumerate(pw_str):
        if i == 0:
            continue
        if int(c) < int(pw_str[i - 1]):
            return False
    return True


if __name__ == '__main__':
    pw_range = None
    with open('inputs/04') as f:
        pw_range = tuple(map(int, f.read().rstrip('\n').split('-')))
    r = list(range(pw_range[0], pw_range[1] + 1))

    valid_p1 = list(filter(is_valid, r))
    print('Part 1', len(valid_p1))
    print(
        'Part 2',
        len(list(filter(
            lambda pw: 2 in collections.Counter(str(pw)).values(),
            valid_p1
        )))
    )
