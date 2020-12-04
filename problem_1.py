def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [int(x.strip()) for x in content]
    return content

def find2sum(numbers):
    d = {}
    for n in numbers:
        if n in d:
            return n,d[n]
        else:
            d[2020-n]=n



def main():
    x = load("inputs/input_1.txt")
    print(x)
    a,b = find2sum(x)
    print(a,b,a+b,a*b)

if __name__ == '__main__':
    main()
