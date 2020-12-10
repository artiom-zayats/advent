def load(filename):
    with open(filename) as f:
        content = f.read()
    content = content.split("\n")
    content = [int(x) for x in content]
    print("len",len(content))
    return content


def find2sum(numbers,target):
    d = {}
    for n in numbers:
        if n in d:
            return n,d[n]
        else:
            d[target-n]=n
    return None

def find_number(pre,input_data):
    for i in range(len(input_data)-pre):
        #print(i, input_data[i + pre], input_data[i:i + pre])
        vals = find2sum(input_data[i:i+pre],input_data[i+pre])
        if not vals:
            return i+pre
        else:
            #print(f"{vals[0]} + {vals[1]} = {input_data[i+pre]}")
            pass
    return -1

def solution1(input_data):
    ix = find_number(pre=25,input_data=input_data)
    if ix != -1:
        return input_data[ix]
    return "Not Found"

def find_list_that_sums(input_data,test_num):
    sm = 0
    i,j = 0,1
    sm = sum(input_data[i:j])
    while i < len(input_data) or j<len(input_data):
        if sm == test_num:
            return i,j
        if sm + input_data[j+1] > test_num:
            sm = sm - input_data[i]
            i = i+1
        else:
            sm = sm + input_data[j]
            j = j+1
    return None




def solution2(input_data):
    test_num = solution1(input_data)
    start,finish = find_list_that_sums(input_data,test_num)
    ans = input_data[start:finish]
    return min(ans)+max(ans)


def main():
    input_data = load("inputs/input_9.txt")
    print("Input: ",input_data)

    sol1 = solution1(input_data)
    print("Solution1: ",sol1)

    sol2 = solution2(input_data)
    print("Solution2: ",sol2)



if __name__ == '__main__':
    main()
