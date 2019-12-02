import sys

instructions = []
with open('inputs/02') as f:
    instructions = list(map(int, f.read().rstrip('\n').split(',')))

def calculate(instructions, noun=12, verb=2):
    instructions[1] = noun
    instructions[2] = verb
    i = 0
    while True:
        instruction = instructions[i]
        if instruction == 99:
            break
        elif instruction == 1:
            o1 = instructions[instructions[i + 1]]
            o2 = instructions[instructions[i + 2]]
            instructions[instructions[i + 3]] = o1 + o2
            i += 4
        elif instruction == 2:
            o1 = instructions[instructions[i + 1]]
            o2 = instructions[instructions[i + 2]]
            instructions[instructions[i + 3]] = o1 * o2
            i += 4
    return instructions[0]

print('Part 1:', calculate(instructions.copy()))

target = 19690720
for noun in range(100):
    for verb in range(100):
        if calculate(instructions.copy(), noun, verb) == target:
            print('Part 2:', 100 * noun + verb)
            sys.exit(0)
