import re

bagexp = re.compile("^(\d+) ([a-z ]+) bags?\.?$")

def count_bags(bag):
    count, description = bagexp.match(bag).groups()
    return (int(count), description)

def extract_rule(rule):
    main_bag, contents = rule.split(" bags contain ")
    if contents == "no other bags.":
        return main_bag, []
    return main_bag, [count_bags(bag) for bag in contents.split(', ')]

raw_input = open('Inputs\Day07input.txt', 'r').read().splitlines()
rules = dict([extract_rule(line) for line in raw_input])

def contains_gold(bag_name):
    if bag_name == "shiny gold":
        return True
    return any(contains_gold(name) for _, name in rules[bag_name])

print('Answer 1:', sum((contains_gold(name) and 1 or 0) for name in rules if name != "shiny gold"))

def count_bags_containing(bag_name):
    return 1 + sum(count * count_bags_containing(name) for count, name in rules[bag_name])

print('Answer 2:', count_bags_containing("shiny gold") - 1)
