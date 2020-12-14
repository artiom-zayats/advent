import math


def load(filename):
    with open(filename) as f:
        content = f.read()
    content = content.split("\n")
    content = [x for x in content]
    print("len",len(content))
    return content


class Ship():
    def __init__(self):
        self.xy = 0
        self.d = 1
    def move(self,command):
        cmd = command[0]
        n = int(command[1:])
        if cmd == 'F':
            self.xy += self.d * n
        elif cmd == 'L':
            self.d *= 1j ** (n // 90)
        elif cmd == 'R':
            self.d /= 1j ** (n // 90)
        elif cmd == 'N':
            self.xy += n * 1j
        elif cmd == 'S':
            self.xy -= n * 1j
        elif cmd == 'E':
            self.xy += n
        elif cmd == 'W':
            self.xy -= n
    def manhattan_from_zero(self):
        return abs(self.xy.real)+abs(self.xy.imag)


class Waypoint():
    def __init__(self):
        self.xy = 0
        self.d = 10 + 1j
    def move(self,command):
        cmd = command[0]
        n = int(command[1:])
        if cmd == 'F':
            self.xy += self.d * n
        elif cmd == 'L':
            self.d *= 1j ** (n // 90)
        elif cmd == 'R':
            self.d /= 1j ** (n // 90)
        elif cmd == 'N':
            self.d += n * 1j
        elif cmd == 'S':
            self.d -= n * 1j
        elif cmd == 'E':
            self.d += n
        elif cmd == 'W':
            self.d -= n
    def manhattan_from_zero(self):
        return abs(self.xy.real)+abs(self.xy.imag)


def solution1(input_data):

    ship = Ship()
    for x in input_data:
        ship.move(x)
        #print(x,ship.position())

    return ship.manhattan_from_zero()


def solution2(input_data):
    ship = Waypoint()
    for x in input_data:
        ship.move(x)
        # print(x,ship.position())

    return ship.manhattan_from_zero()


def main():
    input_data = load("inputs/input_12.txt")
    print("Input: ",input_data)

    sol1 = solution1(input_data)
    print("Solution1: ",sol1)

    sol2 = solution2(input_data)
    print("Solution2: ",sol2)



if __name__ == '__main__':
    main()
