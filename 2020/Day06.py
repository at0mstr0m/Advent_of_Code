from collections import Counter

with open('Inputs/Day06input.txt', 'r') as f:
    raw_input = f.read().split('\n\n')

group_answers = [input.split('\n') for input in raw_input]
anyone_yes = 0
everyone_yes = 0

for group in group_answers:
    answers = "".join(group)                        # build one unified string of all answers
    num_of_groupmembers = len(group)                # count groupmembers
    yes_counter = Counter(answers)                  # collect all positive answers
    anyone_yes += len(yes_counter)                  # count all positive answers
    for letter, quantity in yes_counter.items():    # go through answers
        if quantity == num_of_groupmembers:         # everyone in group said yes to certain quastion, if question is counted as often as there are groupmembers
            everyone_yes += 1

print('Answer 1:', anyone_yes)
print('Answer 2:', everyone_yes)