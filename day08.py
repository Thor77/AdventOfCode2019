import math
import collections

digits = []
with open('inputs/08') as f:
    digits = list(f.read().rstrip('\n'))

width = 25
height = 6

layers = []
while len(digits) != 0:
    layer = []
    for _ in range(width * height):
        layer.append(digits.pop(0))
    layers.append(layer)

min_zeros = math.inf
min_counter = []
for layer in layers:
    counter = collections.Counter(layer)
    if counter['0'] < min_zeros:
        min_zeros = counter['0']
        min_counter = counter

print('Part 1:', min_counter['1'] * min_counter['2'])

layers.reverse()
image = layers[0]
for layer in layers[1:]:
    for i, pixel in enumerate(layer):
        if pixel == '2':
            continue
        else:
            image[i] = pixel

m = {'0': ' ', '1': '#', '2': ' '}
i = 0
for pixel in image:
    print(m[pixel], end='')
    if i == width - 1:
        print('')
        i = 0
    else:
        i += 1
print('')
