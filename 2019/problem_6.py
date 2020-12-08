from collections import defaultdict

def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content



def solution1(input_data):
    orbits = defaultdict(list)
    for orbit in input_data:
        a,b = orbit.split(")")
        orbits[a].append(b)

    que = [("COM",0)]
    visited = {'COM'}
    total_orbits = 0
    while que:
        orbit,depth = que.pop()
        total_orbits += depth
        for o in orbits[orbit]:
            if o not in visited:
                visited.add(o)
                que.append((o,depth+1))
    return total_orbits


def solution2(input_data):
    orbits = defaultdict(list)
    orbits2 = defaultdict(set)
    for x in input_data:
        parent,child = x.split(")")
        orbits[parent].append(child)
        orbits2[child].add(parent)
        orbits2[parent].add(child)
        if child == "YOU":
            start = parent

    que = [(start,0,["YOU"])]
    while que:
        orbit,count,visited = que.pop()
        if "SAN" in orbits[orbit]:
            return count
        for o in orbits2[orbit]:
            if o not in visited:
                que.append((o,count+1,visited+[o]))






def main():
    input_data = load("inputs/input_6.txt")
    print("input: ",input_data)

    sol1 = solution1(input_data)
    print("solution1",sol1)

    sol2 = solution2(input_data)
    print("solution2",sol2)




if __name__ == '__main__':
    main()
