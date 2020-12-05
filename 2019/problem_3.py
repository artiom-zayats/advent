import math


def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content

directions = {
"R":(1,0),
"U":(0,-1),
"L":(-1,0),
"D":(0,1)
}

def trace_wire(wire_directions,wire_cords):
    wire_directions = wire_directions.split(",")
    x,y = 0,0
    for direction in wire_directions:
        d,num = direction[0],int(direction[1:])
        for step in range(num):
            xx,yy = directions[d]
            x += xx
            y += yy
            wire_cords.append((x,y))
    return wire_cords



def solution(inputs_data):
    list_of_cords = []
    for i,x in enumerate(inputs_data):
        list_of_cords.append(trace_wire(x,[]))

    #find interaction points
    intersections = set(list_of_cords[0]).intersection(set(list_of_cords[1]))
    print(intersections)

    #find distance of intersections:
    min_dist = math.inf
    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])
        min_dist = min(dist,min_dist)


    return min_dist



def main():
    x = load("inputs/input_3.txt")
    #print(x)

    ans = solution(x)
    print("solution is:",ans)

if __name__ == '__main__':
    main()
