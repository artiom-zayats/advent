import copy

def load(filename):
    with open(filename) as f:
        content = f.read()
    content = content.split("\n")
    content = [[x for x in word] for word in content]

    #print("len",len(content))
    return content


def day2(map):
    new_map = copy.deepcopy(map)
    X = len(map)
    Y = len(map[0])
    for x in range(X):
        for y in range(Y):

            #STONE
            if map[x][y] == ".":
                continue

            #OCUPIED
            if map[x][y] == "#":
                count = 0
                for dx, dy in [(-1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)]:
                    ddx = dx
                    ddy = dy
                    while 0<=x+dx < X and 0<=y+dy < Y:
                        #print(f"({x},{y})#-looking", dx, dy,f"({x+dx},{y+dy})", map[dx + x][dy + y])
                        if map[x+dx][y+dy] == ".":
                            dx+=ddx
                            dy+=ddy
                            continue
                        if map[x + dx][y + dy] == "#":
                            count += 1
                            break
                        if map[x + dx][y + dy] == "L":
                            break
                if count >= 5:
                    new_map[x][y] = "L"

            ## EMPTY
            if map[x][y] == "L":
                count = 0
                for dx, dy in [(-1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)]:
                    ddx = dx
                    ddy = dy
                    while 0<=x+dx < X and 0<=y+dy < Y:
                        #print(f"({x},{y})L-looking", dx, dy,f"({x+dx},{y+dy})", map[dx + x][dy + y])
                        if map[x+dx][y+dy] == ".":
                            dx+=ddx
                            dy+=ddy
                            continue
                        if map[x + dx][y + dy] == "#":
                            count += 1
                            break
                        if map[x + dx][y + dy] == "L":
                            break
                if count == 0:
                    new_map[x][y] = "#"
    return new_map

def day1(map):
    new_map = copy.deepcopy(map)
    X = len(map)
    Y = len(map[0])
    for x in range(X):
        for y in range(Y):

            #STONE
            if map[x][y] == ".":
                continue

            #OCUPIED
            if map[x][y] == "#":
                count = 0
                for dx, dy in [(-1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)]:
                    if 0<=x+dx < X and 0<=y+dy < Y:
                        if map[x + dx][y + dy] == "#":
                            count += 1
                if count >= 4:
                    new_map[x][y] = "L"

            ## EMPTY
            if map[x][y] == "L":
                count = 0
                for dx, dy in [(-1, 1), (1, -1), (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1)]:
                    if 0<=x+dx < X and 0<=y+dy < Y:
                        if map[x + dx][y + dy] == "#":
                            count+=1
                if count == 0:
                    new_map[x][y] = "#"
    return new_map

def changed(map,new_map):
    X = len(map)
    Y = len(map[0])
    for x in range(X):
        for y in range(Y):
            if map[x][y] != new_map[x][y]:
                return True
    return False

def count_occupied_seat(map):
    X = len(map)
    Y = len(map[0])
    count = 0
    for x in range(X):
        for y in range(Y):
            if map[x][y] == "#":
                count+=1
    return count

def solution1(input_data):
    map = input_data
    i = 0
    while True:
        new_map = day1(map)
        if not changed(map,new_map):
            break
        map = copy.deepcopy(new_map)
        i+=1

    print("last day",i)
    return count_occupied_seat(map)


def solution2(input_data):
    map = input_data
    i = 0
    while True:
        new_map = day2(map)
        if not changed(map,new_map):
            break
        map = copy.deepcopy(new_map)
        i+=1


    print("last day",i)
    return count_occupied_seat(new_map)


def main():
    input_data = load("inputs/input_11.txt")
    #print("Input: ",input_data)

    # sol1 = solution1(input_data)
    # print("Solution1: ",sol1)

    sol2 = solution2(input_data)
    print("Solution2: ",sol2)



if __name__ == '__main__':
    main()
