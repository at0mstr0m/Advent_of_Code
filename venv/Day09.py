raw_input = [int(number) for number in open('Inputs\Day09Input.txt', 'r').read().splitlines()]

def is_valid(num:int, preamble:list) -> bool:
    for i in range(len(preamble)):
        for j in range(i + 1, len(preamble)):
            if preamble[i] + preamble[j] == num:
                return True
    return False

for i in range(25,len(raw_input)):      # start at 25 after preamble
    preamble = [raw_input[i] for i in range(i - 25, i)]
    if not is_valid(raw_input[i], preamble):
        print('Answer 1:', raw_input[i])
        for j in range(i):
            summands = []
            summands.append(raw_input[j])
            for k in range(j + 1, i):
                summands.append(raw_input[k])
                if sum(summands) > raw_input[i]:
                    break
                if sum(summands) == raw_input[i]:
                    print('Answer 2:', min(summands) + max(summands))
