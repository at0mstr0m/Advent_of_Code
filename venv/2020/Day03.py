rawdata = open('Inputs/Day03input.txt', 'r').read().split('\n')
patterns = []
for pattern in rawdata:
    patterns.append(pattern * 100)

def count_tree_encounters(right: int, down: int, area: list) -> int:
    trees = 0
    char = 0
    for line in range(0,len(area),down):                    # starting position always at the top-left area[0][0]
        if (area[line][char]) == '#':                       # if tree is found, increment variable
            trees += 1
        char += right                                       # step right
    return trees                                            # returns number of trees

print('Answer 1:', count_tree_encounters(3,1,patterns))
print('Answer 2:', count_tree_encounters(1,1,patterns) *
                   count_tree_encounters(3,1,patterns) *
                   count_tree_encounters(5,1,patterns) *
                   count_tree_encounters(7,1,patterns) *
                   count_tree_encounters(1,2,patterns))
