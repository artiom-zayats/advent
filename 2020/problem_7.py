def load(filename):
    with open(filename) as f:
        content = f.read()
    content = content.split("\n")
    return content



def solution2(input_data,color_of_bag):
    colors_dict = {}
    for i,x in enumerate(input_data):
        k,vals = x.split("contain")
        vals = vals.split(",")
        k = "".join(k.split(" ")[:-2])
        temp = []
        for val in vals:
            val = val.split(" ")[:-1]
            num = val[1]
            color = "".join(val[2:])
            temp.append((num,color))
        vals = temp

        if k not in colors_dict:
            colors_dict[k] = {}
        for num,val in vals:
            if val not in colors_dict:
                colors_dict[k][val] = {}
            colors_dict[k][val] = num


    count = 0
    que = [("1",colors_dict[color_of_bag])]
    while que:
        mult,color_dict_poped = que.pop(0)
        for k_color,num_of_bags in color_dict_poped.items():
            if num_of_bags.isnumeric():
                temp = int(num_of_bags)*int(mult)
                if k_color in colors_dict:
                    que.append((str(temp),colors_dict[k_color]))

        count+= int(mult)

    return count-1


def solution1(input_data,color_of_bag):
    colors_dict = {}
    for i,x in enumerate(input_data):
        k,vals = x.split("contain")
        vals = vals.split(",")
        k = "".join(k.split(" ")[:-2])
        temp = []
        for val in vals:
            val = val.split(" ")[:-1]
            num = val[1]
            color = "".join(val[2:])
            temp.append((num,color))
        vals = temp

        for num,color in vals:
            if color not in colors_dict:
                colors_dict[color] = {}
                colors_dict[color][k] = num
            else:
                colors_dict[color][k] = num
    que = list(colors_dict[color_of_bag].keys())
    visited = set()
    count_set = set()
    while que:
        color = que.pop(0)
        visited.add(color)
        count_set.add(color)
        if color in colors_dict:
            add_to_que = list(colors_dict[color].keys())
            for x in add_to_que:
                if x not in visited:
                    que.append(x)

    return len(count_set)





def main():
    input_data = load("inputs/input_7.txt")
    print("Input: ",input_data)

    sol1 = solution1(input_data,"shinygold")
    print("Solution1: ",sol1)

    sol2 = solution2(input_data,"shinygold")
    print("Solution2: ",sol2)



if __name__ == '__main__':
    main()
