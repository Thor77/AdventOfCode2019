def path_length(objects, key):
    if key in objects:
        for connection in objects.get(key, []):
            return 1 + path_length(objects, connection)
    else:
        return 1


map_data = []
with open('inputs/06') as f:
    map_data = f.read().splitlines()

objects = {}
for statement in map_data:
    o1, o2 = statement.split(')')
    objects.setdefault(o1, []).append(o2)

i = 0
for key in objects.keys():
    result = path_length(objects, key)
    print(result)
    i += result

print(i, objects)
