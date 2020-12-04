def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [(x.strip()) for x in content]
    print("total lines:", len(content))
    return content


def find_num_trees(input_data,X,Y):
    L = len(input_data[0])
    y = 0
    x = 0
    count = 0
    while y < len(input_data):
        if input_data[y][x] == "#":
            count+=1
        x+=X
        if x >= L:
            x = x-L
        y+=Y
    return count

def solution(input_data):
    ans = 1
    for x,y in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
        ans*=find_num_trees(input_data,X=x,Y=y)
    return ans



def main():
    input_data = load("inputs/input_3.txt")
    print(input_data)
    sol = solution(input_data)
    print(sol)


if __name__ == '__main__':
    main()
