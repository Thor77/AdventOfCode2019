import itertools
import queue
import threading


def get_parameter(identifier, mode, instructions):
    if mode == '0':
        return instructions[int(identifier)]
    elif mode == '1':
        return int(identifier)


def get_parameters(first_position, count, modes, instructions):
    if len(modes) < count:
        modes += '0000'
    for i in range(count):
        yield get_parameter(
            instructions[first_position + i], modes[i], instructions
        )


def calculate(instructions, input_queue, output_queue):
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
            instructions[instructions[i + 1]] = input_queue.get()
            i += 2
        elif opcode == 4:
            output = list(get_parameters(i + 1, 1, modes, instructions))[0]
            output_queue.put(output)
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


def initialize_queue(items):
    q = queue.Queue()
    for item in items:
        q.put(item)
    return q


def calculate_with_phase_settings(instructions, phase_settings):
    last_output = 0
    for phase_setting in phase_settings:
        last_output = calculate(
            instructions.copy(),
            initialize_queue([phase_setting, last_output]),
            queue.Queue()
        )
    return last_output


def part2(instructions, phase_settings):
    q0 = queue.Queue()
    q0.put(phase_settings[0])
    q0.put(0)

    q1 = queue.Queue()
    q1.put(phase_settings[1])

    q2 = queue.Queue()
    q2.put(phase_settings[2])

    q3 = queue.Queue()
    q3.put(phase_settings[3])

    q4 = queue.Queue()
    q4.put(phase_settings[4])

    amp_a = threading.Thread(
        target=calculate, args=[instructions.copy(), q0, q1]
    )
    amp_a.start()

    amp_b = threading.Thread(
        target=calculate, args=[instructions.copy(), q1, q2]
    )
    amp_b.start()

    amp_c = threading.Thread(
        target=calculate, args=[instructions.copy(), q2, q3]
    )
    amp_c.start()

    amp_d = threading.Thread(
        target=calculate, args=[instructions.copy(), q3, q4]
    )
    amp_d.start()

    amp_e = threading.Thread(
        target=calculate, args=[instructions.copy(), q4, q0]
    )
    amp_e.start()

    # collect output
    amp_e.join()
    return q0.get_nowait()


if __name__ == '__main__':
    instructions = []
    with open('inputs/07') as f:
        instructions = list(map(int, f.read().rstrip('\n').split(',')))

    highest_output = 0
    for a, b, c, d, e in itertools.permutations(range(5)):
        output = calculate_with_phase_settings(
            instructions.copy(), [a, b, c, d, e]
        )
        if output > highest_output:
            highest_output = output
    print('Part 1:', highest_output)

    highest_output = 0
    for perm in itertools.permutations(range(5, 10)):
        output = part2(instructions.copy(), perm)
        if output > highest_output:
            highest_output = output
    print('Part 2:', highest_output)
