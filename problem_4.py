def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    print("total lines:", len(content))
    passports = []
    temp = []
    for x in content:
        if x == "\n":
            passports.append(temp)
            temp = []
        else:
            temp.append(x.strip())
    return passports


fields = {
    "byr":1,
    "iyr":1,
    "eyr":1,
    "hgt":1,
    "hcl":1,
    "ecl":1,
    "pid":1,
}

def solution(input_data):
    count = 0
    for passport in input_data:
        passport = " ".join(passport)
        passport = passport.split(" ")
        keys = set()
        for x in passport:
            val = x.split(":")
            if val[0] in fields:
                keys.add(val[0])
        if keys == set(fields.keys()):
            count+=1
    return count




def main():
    input_data = load("inputs/input_4.txt")
    print(input_data)
    sol = solution(input_data)
    print(sol)


if __name__ == '__main__':
    main()
