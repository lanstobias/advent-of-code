def read_groups():
    groups = []
    with open('input/day6.txt') as f:
        lines = f.read()
        groups_raw = lines.split('\n\n')
        for group in groups_raw:
            if len(group) != 1:
                group_answers = group.split('\n')
            else:
                group_answers = group[0].replace('\n','')
            groups.append(group_answers)

    # Remove last item because of some parsing error i don't care to fix
    del groups[-1][-1]
    return groups

def count_answers(group):
    answers = set()
    for person in group:
        for answer in person:
            answers.add(answer)
    return len(answers)

def count_same_answers(group):
    answers = {}
    num_of_persons = len(group)
    for person in group:
        for answer in person:
            if answer not in answers:
                answers[answer] = 1
            else:
                answers[answer] += 1
    same_answers = []
    for answer, num_of_answers in answers.items():
        if num_of_answers  == num_of_persons:
            same_answers .append(num_of_answers)
    return len(same_answers )

sum_answers = 0
sum_same_answers = 0
for group in read_groups():
    sum_answers += count_answers(group)
    sum_same_answers += count_same_answers(group)

print('Part 1: {}'.format(sum_answers))
print('Part 2: {}'.format(sum_same_answers))
