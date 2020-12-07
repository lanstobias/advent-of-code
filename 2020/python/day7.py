import pprint

# Part 1
rules = {}
def read_rules():
    with open('input/day7.txt') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            line = line.split(' bags contain ')
            top_bag = line[0]
            contained_in_bags = line[1].split(', ')
            for bag in contained_in_bags:
                if bag == 'no other bags.':
                    continue
                color = ' '.join(bag.split(' ')[1:-1:])
                if color not in rules:
                    rules[color] = set({})
                rules[color].add(top_bag)

read_rules()
num_bags = set()
def count_rules(color):
    if color not in rules:
        pass
    else:
        for rule in rules[color]:
            count_rules(rule)
            num_bags.add(rule)

count_rules('shiny gold')
print('Part 1: {}'.format(len(num_bags)))

# Part 2
rules2 = {}
def read_rules_2():
    with open('input/day7.txt') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            line = line.split(' bags contain ')
            top_bag = line[0]
            contained_bags = line[1].split(', ')
            for bag in contained_bags:
                if bag == 'no other bags.':
                    continue
                color = ' '.join(bag.split(' ')[0:-1:])
                if top_bag not in rules2:
                    rules2[top_bag] = set({})
                rules2[top_bag].add(color)


read_rules_2()
bag_sum = 0
def count_contained(color):
    bags = 0
    if color not in rules2:
        pass
    else:
        for bag in rules2[color]:
            nr = int(bag[0])
            bag = bag[2:]
            bags += (nr + (nr * count_contained(bag)))
    return bags

bag_sum = count_contained('shiny gold')
print('Part 2: {}'.format(bag_sum))
