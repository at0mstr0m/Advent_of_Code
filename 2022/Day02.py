data = [line for line in open('2022/Inputs/Day02Input.txt', 'r').read().splitlines()]
scores = {
    'A X': 4,
    'A Y': 8,
    'A Z': 3,
    'B X': 1,
    'B Y': 5,
    'B Z': 9,
    'C X': 7,
    'C Y': 2,
    'C Z': 6,
}
answer_one = sum([scores[e] for e in data])
print(f'Answer 1: {answer_one}')
reactions = {
    'A X': 'Z',
    'A Y': 'X',
    'A Z': 'Y',
    'B X': 'X',
    'B Y': 'Y',
    'B Z': 'Z',
    'C X': 'Y',
    'C Y': 'Z',
    'C Z': 'X',
}
for i in range(len(data)):
    e = data[i]
    reaction = reactions[e]
    turn = list(e)
    turn.pop()
    turn.append(reaction)
    data[i] = ''.join(turn)
answer_two = sum([scores[e] for e in data])
print(f'Answer 2: {answer_two}')
