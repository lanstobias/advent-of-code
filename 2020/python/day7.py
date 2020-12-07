import pprint

rules = {}
def read_rules():
    with open('input/day7_test.txt') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            line = line.split(' bags contain ')
            top_bag = line[0]
            contained_in_bags = line[1].split(', ')
            # print(top_bag)
            for bag in contained_in_bags:
                if bag == 'no other bags.':
                    continue
                color = ' '.join(bag.split(' ')[1:-1:])
                if color not in rules:
                    rules[color] = set({})
                rules[color].add(top_bag)

rules2 = {}
def read_rules_2():
    with open('input/day7_test.txt') as f:
        lines = [line.rstrip() for line in f]
        for line in lines:
            line = line.split(' bags contain ')
            top_bag = line[0]
            contained_bags = line[1].split(', ')
            print('top bag: {}'.format(top_bag))
            for bag in contained_bags:
                if bag == 'no other bags.':
                    continue
                color = ' '.join(bag.split(' ')[0:-1:])
                if top_bag not in rules2:
                    rules2[top_bag] = set({})
                rules2[top_bag].add(color)


# read_rules()
read_rules_2()
pprint.pprint(rules2)

# print('................')

# def print_contains(color):

# print_contains('shiny gold')

contained = set()
def print_contained(color):
    if color not in rules2:
        print(color)
    else:
        for rule in rules2[color]:
            rule = rule[2:]
            print(rule)
            print_contained(rule)
            contained.add(rule)

print_contained('shiny gold')
# print(len(contained))
