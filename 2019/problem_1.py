def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [int(x.strip()) for x in content]
    return content


def find_fuel(fuel):
    ans = 0
    while fuel > 0:
        temp = fuel//3
        temp-=2
        if temp > 0:
            ans+=temp
        fuel = temp

    return ans


def solution(numbers):
    ans = 0
    for x in numbers:
        ans += find_fuel(x)
    return ans


def main():
    x = load("inputs/input_1.txt")
    print(x)

    ans = solution(x)
    print(ans)

if __name__ == '__main__':
    main()
