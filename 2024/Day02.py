raw_data = open('2024/Inputs/Day02Input.txt', 'r').read().splitlines()
reports = [[int(n) for n in x.split(' ')] for x in raw_data]

# check if all numbers are gradually increasing or gradually decreasing
def check(numbers):
    is_sorted = numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)
    if (not is_sorted):
        return False
    # check if any two adjacent numbers differ by at least one and at most three.
    differences = [abs(numbers[i] - numbers[i+1]) for i in range(len(numbers)-1)]
    if (max(differences) > 3 or min(differences) < 1):
        return False
    return True

print(f'Answer 1: {sum([check(report) for report in reports])}')

# check if the list of numbers can be rescued by removing one number
def rescue(numbers):
    for i in range(len(numbers)):
        if (check(numbers[:i] + numbers[i+1:])):
            return True
    return False

print(f'Answer 2: {sum([check(report) or rescue(report) for report in reports])}')
