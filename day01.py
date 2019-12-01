def calculate_fuel(mass):
    return int(mass / 3) - 2

modules = []
with open('inputs/01') as f:
    modules = list(map(lambda l: int(l.rstrip('\n')), f.readlines()))

print('Part 1:', sum(map(calculate_fuel, modules)))

p2 = 0
for mass in modules:
    current_fuel = calculate_fuel(mass)
    total_fuel = current_fuel
    while True:
        current_fuel = calculate_fuel(current_fuel)
        if current_fuel <= 0:
            break
        else:
            total_fuel += current_fuel
    p2 += total_fuel

print('Part 2:', p2)
