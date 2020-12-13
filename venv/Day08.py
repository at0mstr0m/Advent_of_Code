raw_input = open('Inputs\Day08Input.txt', 'r').read().splitlines()

def get_accumulator_before_loop(instructions:list) -> int:
    accumulator = 0
    visited_lines = []
    i = 0
    while i < len(instructions):
        if i in visited_lines:
            break
        visited_lines.append(i)
        operation, argument = instructions[i].split(' ')
        argument = int(argument)
        if operation == "acc":
            accumulator += argument
        elif operation == "jmp":
            i += argument - 1
        i += 1
    return accumulator

print('Answer 1:', get_accumulator_before_loop(raw_input))

def terminates_normally(instructions:list) -> bool:
    visited_lines = []
    i = 0
    while i < len(instructions):
        if i in visited_lines:
            return False
        visited_lines.append(i)
        operation, argument = instructions[i].split(' ')
        argument = int(argument)
        if operation == "jmp":
            i += argument - 1
        i += 1
    return True

for i in range(len(raw_input)):                     # exchange all 'jmp' and 'nop' operatioins and check for validity
    test_input = raw_input.copy()
    operation, argument = test_input[i].split(' ')
    if operation == 'jmp':
        operation = 'nop'
    elif operation == 'nop':
        operation = 'jmp'
    test_input[i] = operation + ' ' + argument
    if terminates_normally(test_input):
        print('Answer 2:', get_accumulator_before_loop(test_input))

