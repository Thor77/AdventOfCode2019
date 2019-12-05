instructions = []
with open('inputs/05') as f:
    instructions = list(map(int, f.read().rstrip('\n').split(',')))


def get_parameter(identifier, mode, instructions):
    if mode == '0':
        return instructions[int(identifier)]
    elif mode == '1':
        return int(identifier)
    else:
        raise 'This shouldn\'t happen'


def get_parameters(first_position, count, modes, instructions):
    if len(modes) < count:
        modes += '0000'
    for i in range(count):
        yield get_parameter(
            instructions[first_position + i], modes[i], instructions
        )


def calculate(instructions, controller_id):
    i = 0
    output = 0
    while True:
        instruction = str(instructions[i])
        opcode = int(instruction[-2:])
        modes = instruction[:-2][::-1]
        if opcode == 99:
            return output
        elif opcode == 1:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions))
            instructions[instructions[i + 3]] = o1 + o2
            i += 4
        elif opcode == 2:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions))
            instructions[instructions[i + 3]] = o1 * o2
            i += 4
        elif opcode == 3:
            instructions[instructions[i + 1]] = controller_id
            i += 2
        elif opcode == 4:
            output = list(get_parameters(i + 1, 1, modes, instructions))[0]
            i += 2
        elif opcode == 5:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions))
            i = o2 if o1 != 0 else i + 3
        elif opcode == 6:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions))
            i = o2 if o1 == 0 else i + 3
        elif opcode == 7:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions))
            instructions[instructions[i + 3]] = 1 if o1 < o2 else 0
            i += 4
        elif opcode == 8:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions))
            instructions[instructions[i + 3]] = 1 if o1 == o2 else 0
            i += 4


print('Part 1:', calculate(instructions.copy(), 1))
print('Part 2:', calculate(instructions.copy(), 5))
