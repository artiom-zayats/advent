def load(filename):
    with open(filename) as f:
        content = f.read()

    passports = content.split("\n\n")
    passports = [x.split() for x in passports]

    return passports



def solution1(input_data):
    list_of_questions = []
    for group in input_data:
        group_set = set()
        for person in group:
            for q in person:
                group_set.add(q)
        list_of_questions.append(len(group_set))
    return sum(list_of_questions)

def solution2(input_data):
    list_of_questions = []
    for group in input_data:
        group_dict = {}
        for person in group:
            for q in person:
                if q in group_dict:
                    group_dict[q] += 1
                else:
                    group_dict[q] = 1

        count = 0
        for q in group_dict:
            if group_dict[q] == len(group):
                count+=1
        list_of_questions.append(count)
    return sum(list_of_questions)

def main():
    input_data = load("inputs/input_6.txt")
    print(input_data)

    sol1 = solution1(input_data)
    print("solution1",sol1)

    sol2 = solution2(input_data)
    print("solution2",sol2)



if __name__ == '__main__':
    main()
