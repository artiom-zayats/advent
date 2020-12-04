def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [(x.strip()) for x in content]
    print("total lines:",len(content))
    return content

def num_of_valid(passwords):
    ans = 0
    for x in passwords:
        rule,letter,password = x.split(" ")

        if (is_valid_2(rule,letter[0],password)):
            ans +=1

    return ans

def is_valid_1(rule,letter,password):
    rule_min,rule_max = rule.split("-")
    rule_min = int(rule_min)
    rule_max = int(rule_max)

    c = 0
    for l in password:
        if letter == l:
            c+=1

    if rule_min <= c <= rule_max:
        return True
    else:
        return False

def is_valid_2(rule,letter,password):
    rule_min,rule_max = rule.split("-")
    rule_min = int(rule_min)
    rule_max = int(rule_max)

    if password[rule_min-1] == letter or password[rule_max-1]==letter:
        if password[rule_min - 1] == letter and password[rule_max - 1] == letter:
            return False
        else:
            return True
    return False





def main():
    x = load("inputs/input_2.txt")
    print(x)
    num = num_of_valid(x)
    print(num)

if __name__ == '__main__':
    main()
