passwords = open('Day02input.txt','r').read().split('\n')
result1 = 0
result2 = 0

for password in passwords:
    policy, word = password.split(':')              # seperate password from policy
    policy = policy.strip()                         # remove spaces
    word = word.strip()                             # remove spaces
    letter = policy[-1]                             # extract letter password must contain
    policy = policy[:-2]                            # remove letter and space
    least, max = policy.split('-')                  # seperate least and max quantity of letter
    least = int(least)                              # cast string to int
    max = int(max)                                  # cast string to int
    appearances = 0                                 # stores how often letter is contained in word
    for char in word:                               # go through word
        if char == letter:                          # if letter is contained
            appearances += 1                        # increment appearances by 1 per apperance
    if least <= appearances <= max:                 # check if number of letter appearances is within borders of policy
        result1 += 1                                # if yes increment result

print('Answer 1:', result1)

def check(first: int, last: int, letter:str, word: str) -> bool:
    if word[first] == letter:
        if word[last] == letter:
            return False                            # returns False if word[first] AND word[last] == letter
        return True                                 # returns True if only word[first] == letter
    if word[last] == letter:
        return True                                 # returns True if only word[last] == letter
    return False                                    # returns False if nothing applies


for password in passwords:
    policy, word = password.split(':')              # seperate password from policy
    policy = policy.strip()                         # remove spaces
    letter = policy[-1]                             # extract letter password must contain
    policy = policy[:-2]                            # remove letter and space
    first, last = policy.split('-')                 # seperate least and max quantity of letter
    first = int(first)                              # cast string to int
    last = int(last)                                # cast string to int
    if check(first, last, letter, word):    # check if password is within borders of policy
        result2 += 1                                # if yes increment result

print('Answer 2:', result2)
