def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


def solution1(input_data):
    input_data = input_data[0].split(",")
    input_data = [int(x) for x in input_data]
    print("Len of InputDate: ", len(input_data))
    IntComp(input_data)

def solution2(input_data):
    input_data = input_data[0].split(",")
    input_data = [int(x) for x in input_data]
    print("Len of InputDate: ", len(input_data))
    IntComp(input_data)


def num_to_params_cod(number):
    number = str(number)
    op = number[-2:]
    rest = number[:-2][::-1]
    modes = []
    for x in rest:
        modes.append(int(x))
    return int(op),modes+[0]



def IntComp(numbers):
    i = 0
    while i<len(numbers):
        #print("i: ",i)
        op,modes = num_to_params_cod(numbers[i])
        print("index:",i,"op: ",op,"modes: ",modes)
        print(numbers[i:i+4])
        if op == 99:
            print("Done: 99")
            break
        elif op == 1:
            a,b = None,None
            if modes[0] == 0:
                a = numbers[numbers[i + 1]]
            else:
                a = numbers[i+1]
            if len(modes) == 1 or modes[1] == 0 :
                b = numbers[numbers[i + 2]]
            else:
                b = numbers[i + 2]
            #print(f"Mult {a}*{b} = {a+b}")
            numbers[numbers[i+3]] = a + b
            i+=4
        elif op == 2:
            a,b = None,None
            if modes[0] == 0:
                a = numbers[numbers[i + 1]]
            else:
                a = numbers[i+1]
            if len(modes) == 1 or modes[1] == 0 :
                b = numbers[numbers[i + 2]]
            else:
                b = numbers[i + 2]
            #print(f"Mult {a}*{b} = {a*b}")
            numbers[numbers[i+3]] = a * b
            i+=4
        elif op == 3:
            print("What is your input value?")
            choice = input()
            choice = int(choice)
            #print(f"Writing {choice} to {numbers[i+1]}")
            numbers[numbers[i+1]] = choice
            i+=2
        elif op == 4:
            if modes[0] == 0:
                print("Ouput:",numbers[numbers[i+1]])
            else:
                print("Ouput:",numbers[i+1])
            i+=2
        elif op ==5:
            param = None
            if modes[0] == 0:
                if numbers[numbers[i+1]] != 0:
                    param = True
                else:
                    param = False
            if modes[0] == 1:
                if numbers[i+1] != 0:
                    param = True
                else:
                    param = False
            if len(modes)==1 or modes[1] == 0:
                i = numbers[numbers[i+2]]
            else:
                i = numbers[i+2]

        elif op ==5:
            param = None
            if modes[0] == 0:
                if numbers[numbers[i+1]] != 0:
                    param = True
                else:
                    param = False
            if modes[0] == 1:
                if numbers[i+1] != 0:
                    param = True
                else:
                    param = False
            if param:
                if len(modes)==1 or modes[1] == 0:
                    i = numbers[numbers[i+2]]
                else:
                    i = numbers[i+2]
            else:
                i+=3
        elif op ==6:
            param = None
            if modes[0] == 0:
                if numbers[numbers[i+1]] == 0:
                    param = True
                else:
                    param = False
            if modes[0] == 1:
                if numbers[i+1] != 0:
                    param = True
                else:
                    param = False
            if param:
                if len(modes)==1 or modes[1] == 0:
                    i = numbers[numbers[i+2]]
                else:
                    i = numbers[i+2]
            else:
                i+=3

        elif op == 7:
            if modes[0] == 0:
                a = numbers[numbers[i + 1]]
            else:
                a = numbers[i+1]
            if len(modes) == 1 or modes[0] == 0:
                b = numbers[numbers[i + 2]]
            else:
                b = numbers[i+2]
            if a < b:
                numbers[numbers[i+3]] = 1
            else:
                numbers[numbers[i+3]] = 0
            i+=4

        elif op == 7:
            if modes[0] == 0:
                a = numbers[numbers[i + 1]]
            else:
                a = numbers[i+1]
            if len(modes) == 1 or modes[0] == 0:
                b = numbers[numbers[i + 2]]
            else:
                b = numbers[i+2]
            if a == b:
                numbers[numbers[i+3]] = 1
            else:
                numbers[numbers[i+3]] = 0
            i+=4


        else:
            print("position",i,"Error",op)
            break
    print("Position 0:", numbers[0])
    return numbers[0]

def main():
    input_data = load("inputs/input_5.txt")
    print("input: ",input_data)

    # sol1 = solution1(input_data)
    # print("solution1",sol1)

    sol2 = solution2(input_data)
    print("solution2",sol2)




if __name__ == '__main__':
    main()
