def load(filename):
    with open(filename) as f:
        content = f.read()
    content = content.split("\n")
    content = [int(x) for x in content]
    print("len",len(content))
    return content


def solution1(input_data):
    pass

def solution2(input_data):
    pass


def main():
    input_data = load("inputs/haha.txt")
    print("Input: ",input_data)

    sol1 = solution1(input_data)
    print("Solution1: ",sol1)

    sol2 = solution2(input_data)
    print("Solution2: ",sol2)



if __name__ == '__main__':
    main()
