import re


def load(filename):
    with open(filename) as f:
        content = f.read()
    # you may also want to remove whitespace characters like `\n` at the end of each line

    passports = content.split("\n\n")
    passports = [x.split() for x in passports]

    return passports


def byr(x):
    if len(x)==4 and x.isnumeric() and 1920<=int(x)<=2002:
        return True
    else:
        return False

def iyr(x):
    if len(x) == 4 and x.isnumeric() and 2010 <= int(x) <= 2020:
        return True
    else:
        return False

def eyr(x):
    if len(x) == 4 and x.isnumeric() and 2020 <= int(x) <= 2030:
        return True
    else:
        return False

def hgt(x):
    if x[-2:] == "cm" and 150<=int(x[:-2])<=193:
        return True
    if x[-2:]=="in" and 59<=int(x[:-2])<=76:
        return True
    return False

def hcl(x):
    match = re.search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', x)
    if match:
        return True
    return False

def ecl(x):
    if x in set(["amb" ,"blu", "brn", "gry", "grn", "hzl", "oth"]):
        return True
    return False

def pid(x):
    if len(x)==9 and x.isnumeric():
        return True
    return False

fields = {
    "byr":byr,
    "iyr":iyr,
    "eyr":eyr,
    "hgt":hgt,
    "hcl":hcl,
    "ecl":ecl,
    "pid":pid,
}

def solution(input_data):
    count = 0
    for passport in input_data:
        passport = " ".join(passport)
        passport = passport.split(" ")
        keys = set()
        for x in passport:
            val = x.split(":")
            k = val[0]
            v = val[1]
            if k in fields:
                if fields[k](v):
                    keys.add(k)
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
