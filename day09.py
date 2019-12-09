from collections import defaultdict


def get_parameter(identifier, mode, instructions, relative_base):
    if mode == '0':
        return instructions[int(identifier)]
    elif mode == '1':
        return int(identifier)
    elif mode == '2':
        return instructions[relative_base + int(identifier)]
    else:
        raise Exception('This shouldn\'t happen')


def get_parameters(first_position, count, modes, instructions, relative_base):
    if len(modes) < count:
        modes += '0000'
    for i in range(count):
        yield get_parameter(
            instructions[first_position + i],
            modes[i],
            instructions,
            relative_base
        )


def write_value(instructions, parameter, position, modes, relative_base, value):
    mode = modes[position] if len(modes) > position else '0'
    if mode == '0':
        instructions[parameter] = value
    elif mode == '2':
        instructions[relative_base + parameter] = value
    else:
        raise Exception('This shouldnt happen...')


def calculate(instructions: list, inputs: list):
    i = 0
    outputs = []
    relative_base = 0
    while True:
        instruction = str(instructions[i])
        opcode = int(instruction[-2:])
        modes = instruction[:-2][::-1]
        print(opcode, modes)
        if opcode == 99:
            return outputs
        elif opcode == 1:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions, relative_base))
            write_value(instructions, i + 3, 2, modes, relative_base, o1 + o2)
            i += 4
        elif opcode == 2:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions, relative_base))
            write_value(instructions, i + 3, 2, modes, relative_base, o1 * o2)
            i += 4
        elif opcode == 3:
            write_value(instructions, i + 1, 0, modes, relative_base, inputs.pop(0))
            i += 2
        elif opcode == 4:
            outputs.append(
                list(get_parameters(i + 1, 1, modes, instructions, relative_base))[0]
            )
            i += 2
        elif opcode == 5:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions, relative_base))
            i = o2 if o1 != 0 else i + 3
        elif opcode == 6:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions, relative_base))
            i = o2 if o1 == 0 else i + 3
        elif opcode == 7:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions, relative_base))
            write_value(instructions, i + 3, 2, modes, relative_base, 1 if o1 < o2 else 0)
            i += 4
        elif opcode == 8:
            o1, o2 = list(get_parameters(i + 1, 2, modes, instructions, relative_base))
            write_value(instructions, i + 3, 2, modes, relative_base, 1 if o1 == o2 else 0)
            i += 4
        elif opcode == 9:
            o1 = list(get_parameters(i + 1, 1, modes, instructions, relative_base))[0]
            relative_base += o1
            i += 2


if __name__ == '__main__':
    instructions = defaultdict(int)
    with open('inputs/05') as f:
        for i, instruction in enumerate(map(int, f.read().rstrip('\n').split(','))):
            instructions[i] = instruction

    print(calculate(instructions, [1]))
