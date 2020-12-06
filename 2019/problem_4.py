
def solution1(input_data):
    ans = set()
    que = [input_data[0][0]]
    while que:
        n = que.pop(0)
        if len(n) == len(input_data[1]):
            if len(set(list(n))) < len(n):
                if int(n)<=int(input_data[1]) and int(n)>=int(input_data[0]):
                    ans.add(n)
                    continue
        for i in range(int(n[-1])+1,10):
            temp = n[:-1]+str(i)
            if int(temp) <= int(input_data[1][:len(temp)]):
                que.append(temp)
        for i in range(int(n[-1]),10):
            temp = n+str(i)
            if int(temp) <= int(input_data[1][:len(temp)]):
                que.append(temp)
    return len(ans)

def solution2(input_data):
    ans = set()
    que = [input_data[0][0]]
    while que:
        n = que.pop(0)
        if len(n) == len(input_data[1]):
            if int(n)<=int(input_data[1]) and int(n)>=int(input_data[0]):
                digits = {}
                for x in n:
                    if x in digits:
                        digits[x] += 1
                    else:
                        digits[x] = 1
                for k in digits:
                    if digits[k] == 2:
                        ans.add(n)
                        continue

        for i in range(int(n[-1])+1,10):
            temp = n[:-1]+str(i)
            if int(temp) <= int(input_data[1][:len(temp)]):
                que.append(temp)
        for i in range(int(n[-1]),10):
            temp = n+str(i)
            if int(temp) <= int(input_data[1][:len(temp)]):
                que.append(temp)
    return len(ans)

def main():
    #input_data = ('24','78')
    input_data = ('240920','789857')
    print(input_data)

    sol1 = solution1(input_data)
    print("solution1",sol1)

    sol2 = solution2(input_data)
    print("solution2",sol2)




if __name__ == '__main__':
    main()
