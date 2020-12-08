def load(filename):
    with open(filename) as f:
        content = f.read()
    content = content.split("\n")
    print("len",len(content))
    return content



def solution1(input_data):

    acc = 0
    i = 0
    positions = set()
    while i < len(input_data) and i not in positions:
        positions.add(i)
        op,num = input_data[i].split(" ")
        num = int(num)

        if op == "nop":
            i+=1
        elif op == "jmp":
            i+= num
        elif op == "acc":
            acc+= num
            i+=1
        else:
            print("Error")
            break
    return acc


def solution2(input_data):
    for i in range(len(input_data)):
        ix,acc = run_programm(input_data,i)
        if ix is not None:
            print("i->",i,"ix->",ix)
            if ix == len(input_data):
                return acc

def run_programm(input_data,pos):
    tmp = input_data.copy()
    op_x,num_x = tmp[pos].split(" ")
    if op_x == "acc":
        return None,None
    elif op_x == "nop":
        tmp[pos] = "jmp " + num_x
    elif op_x == "jmp":
        tmp[pos] = "nop " + num_x
    else:
        print("Error")
        return None,None
    acc = 0
    i = 0
    list_i = []
    positions = set()
    while i < len(tmp) and i not in positions:
        list_i.append(i)
        positions.add(i)
        op,num = tmp[i].split(" ")
        num = int(num)

        if op == "nop":
            i+=1
        elif op == "jmp":
            i+= num
        elif op == "acc":
            acc+= num
            i+=1
        else:
            print("Error")
            break
    return i,acc






def main():
    input_data = load("inputs/input_8.txt")
    print("Input: ",input_data)

    sol1 = solution1(input_data)
    print("Solution1: ",sol1)

    sol2 = solution2(input_data)
    print("Solution2: ",sol2)



if __name__ == '__main__':
    main()
