import collections
from collections import defaultdict
import math


def load(filename):
    with open(filename) as f:
        content = f.read()
    content = content.split("\n")
    content = [x for x in content]
    print("len",len(content))
    return content

def solution1(input_data):
    timestamp = int(input_data[0])
    busses = {}
    for x in input_data[1].split(","):
        if x.isnumeric():
            busses[int(x)] = None

    min_wait = float("inf")
    for bus in busses.keys():
        mult = timestamp//bus
        bus_timestamp = mult*bus
        if bus_timestamp < timestamp:
            wait = (bus_timestamp + bus) - timestamp
            min_wait = min(wait,min_wait)
            busses[bus] = wait

    #find ans
    for bus,wait in busses.items():
        if wait == min_wait:
            return bus*wait




def solution2(input_data):
    timestamp = int(input_data[0])


    busses = {}
    for i,x in enumerate(input_data[1].split(",")):
        if x.isnumeric():
            busses[int(x)] = i


    delays = {}
    for i,x in enumerate(input_data[1].split(",")):
        if x.isnumeric():
            delays[i] = int(x)

    out = ""
    import string
    letters = list(string.ascii_lowercase)
    for i,k in enumerate(busses.keys()):
        out+= f"(x+{busses[k]})/{k} = {letters[i]}"
        if i != len(busses)-1:
            out+= " and "

    print("Plug this here https://www.wolframalpha.com/")
    print(out)

    #https://en.wikipedia.org/wiki/Chinese_remainder_theorem

    timestamp = 0

    #input for WA



    # while True:
    #     check = 0
    #     print(f"-----{timestamp}-----")
    #     for bus,delay in busses.items():
    #             test = get_delay(timestamp,bus)
    #             #print(bus,test,delay,"test",test-delay)
    #             if test == delay:
    #                 check+=1
    #     if check == len(busses):
    #         break
    #
    #     timestamp+= 7







    print(busses)


    return timestamp

def get_delay(timestamp,bus):
    mult = timestamp // bus
    bus_timestamp = mult * bus
    wait = 0
    if bus_timestamp < timestamp:
        wait = (bus_timestamp + bus) - timestamp
    return wait

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


def main():
    input_data = load("inputs/input_13_test.txt")
    print("Input: ",input_data)

    sol1 = solution1(input_data)
    print("Solution1: ",sol1)

    sol2 = solution2(input_data)
    print("Solution2: ",sol2)



if __name__ == '__main__':
    main()
