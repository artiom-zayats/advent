def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [int(x.strip()) for x in content]
    return content

def find2sum(numbers,target):
    d = {}
    for n in numbers:
        if n in d:
            return n,d[n]
        else:
            d[target-n]=n
    return None

def find3sum(numbers,target):

    numbers = sorted(numbers)
    for i in range(len(numbers)-2):
        ans = find2sum(numbers[i:],target - numbers[i])
        if ans:
            return numbers[i],ans[0],ans[1]


    return None



def main():
    x = load("inputs/input_1.txt")
    print(x)

    a,b,c = find3sum(x,2020)
    print(a,b,c,a+b+c,a*b*c)

if __name__ == '__main__':
    main()
