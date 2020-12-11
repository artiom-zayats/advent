def load(filename):
    with open(filename) as f:
        content = f.read()
    content = content.split("\n")
    content = [int(x) for x in content]
    print("len",len(content))
    return content





def solution1_1(input_data):
    sorted_input = sorted(input_data)
    def find_adapter(cur, ix, d1, d2, d3):

        if ix == len(sorted_input):
            return (d1,d2,d3+1)
        #print("cur",cur,"number",sorted_input[ix],"diff",sorted_input[ix] - cur,"ix",ix)
        #print(f"d1-{d1},d2-{d2},d3-{d3}")

        if sorted_input[ix] - cur == 1:
            return find_adapter(cur+1,ix+1,d1+1,d2,d3)
        if sorted_input[ix] - cur == 2:
            return find_adapter(cur+2,ix+1,d1,d2+1,d3)
        if sorted_input[ix] - cur == 3:
            return find_adapter(cur+3,ix+1,d1,d2,d3+1)


    ans = find_adapter(0,0,0,0,0)
    print("d1,d2,d3",ans)
    return ans[0]*ans[2]

def solution1(input_data):
    sorted_input = sorted(input_data)
    sorted_input =  sorted_input
    ls = []
    d1,d2,d3 = 0,0,1
    for i in range(0,len(sorted_input)-1):
        if (sorted_input[i+1] - sorted_input[i]) == 1:
            d1+=1
        if (sorted_input[i+1] - sorted_input[i]) == 2:
            d2+=1
        if (sorted_input[i+1] - sorted_input[i]) == 3:
            d3+=1
        ls.append(sorted_input[i+1]-sorted_input[i])
    # print(ls)
    print("d1,d2,d3", d1,d2,d3)
    return d1*d3


def solution2(input_data):
    sorted_input = sorted(input_data)
    sorted_input = [0]+ sorted_input
    diff = []
    for i in range(len(sorted_input)-1):
        diff.append(sorted_input[i+1]-sorted_input[i])
    i = 0
    count = []
    c = 0
    while i < len(diff):
        if diff[i] == 1:
            c+=1
        else:
            if c > 0:
                count.append(c)
            c = 0
        i+=1
    if c>0:
        count.append(c)

    ans = 1
    for x in count:
        if x == 2:
            ans *= 2
        if x == 3:
            ans*= 4
        if x == 4:
            ans*= 7
    return ans




def solution2slow(start,input_data):
    sorted_input = sorted(input_data)
    sorted_input = [start] + sorted_input
    que = [(start, [0])]
    count = 0
    visited = set()
    visited.add(tuple([0]))
    i = 0
    while que:
        i+=1
        ix, path = que.pop(0)
        visited.add(tuple(path))
        if ix == len(sorted_input) - 1:
            count += 1
            visited.add(tuple(path))
            continue

        for x in [ix + 1, ix + 2, ix + 3, ix + 4]:
            if x < len(sorted_input) and sorted_input[x] - sorted_input[ix] <= 3:
                new_path = path+[sorted_input[x]]
                if tuple(new_path) not in visited:
                    que.append((x, new_path))
    print("iter",i)
    return count



def solution2fib_dict(input_data):
    sorted_input = sorted(input_data)
    sorted_input = [0] + sorted_input
    print("sorted",sorted_input)

    arrangements = {sorted_input[0]:1}
    for x in sorted_input[1:]:
        print(f"number:{x} check back {x-1},{x-2},{x-3}")
        sm = 0
        for a in [x-1,x-2,x-3]:
            if a not in arrangements:
                sm+=0
            else:
                print(f"possibility exist:{a}")
                sm+=arrangements[a]
        arrangements[x]=sm
        #arrangements[x] = sum([arrangements.get(a,0) for a in [x-1,x-2,x-3]])

    print(arrangements[sorted_input[-1]])

    return None







def main():
    input_data = load("inputs/input_10_test.txt")
    print("Input: ",input_data)

    # sol1 = solution1(input_data)
    # print("Solution1: ",sol1)

    print("Solution2: ",solution2(input_data))
    #print("Solution 2 slow",solution2slow(0,input_data))
    print("Solution2 cant: ", solution2fib_dict(input_data))



if __name__ == '__main__':
    main()
