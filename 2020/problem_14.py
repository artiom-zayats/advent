def load(filename):
    with open(filename) as f:
        content = f.read()
    content = content.split("\n")
    content = [x for x in content]
    print("len",len(content))
    return content

memory = {}

def apply_mask(mask,number):
    num_bin = f'{number:036b}'
    new_bin = []
    for i,x in enumerate(mask):
        if x == "X":
            new_bin.append(num_bin[i])
        else:
            new_bin.append(x)
    new_bin  = "".join(new_bin)
    return int(new_bin,2)


def apply_mask_adress(mask,address):
    address_bin = f'{address:036b}'
    new_bin = []
    for i,x in enumerate(mask):
        if x == "0":
            new_bin.append(address_bin[i])
        if x == "X":
            new_bin.append("X")
        if x == "1":
            new_bin.append("1")
    new_bin  = "".join(new_bin)
    return new_bin


def set_value(address, number):
    if address.count('X') == 0:
        memory[address] = number
        return
    set_value(address.replace('X', '0', 1), number)
    set_value(address.replace('X', '1', 1), number)

def write_to_mem(mem,number):
    memory[mem] = number

def solution1(input_data):
    i = 0
    mask = None
    mems = []
    while i < len(input_data):

        test = input_data[i].split(" = ")
        if test[0] == "mask":
            if mask:
                do_chunk(mask,mems)
            mask = test[1]
            mems = []
        else:
            mems.append(input_data[i].split(" = "))
        i+=1
    #do the last one
    do_chunk(mask,mems)

    sum = 0
    for k,v in memory.items():
        sum+=v
    return sum


def do_chunk(mask,mem_list):
    for x in mem_list:
        number = int(x[1])
        address = x[0][4:]
        address = int(address[:-1])
        new_number = apply_mask(mask,number)
        write_to_mem(address,new_number)

def do_chunk2(mask,mem_list):
    for x in mem_list:
        number = int(x[1])
        address = x[0][4:]
        address = int(address[:-1])
        bin_address = apply_mask_adress(mask,address)
        set_value(bin_address,number)

def solution2(input_data):
    i = 0
    mask = None
    mems = []
    while i < len(input_data):
        test = input_data[i].split(" = ")
        if test[0] == "mask":
            if mask:
                do_chunk2(mask,mems)
            mask = test[1]
            mems = []
        else:
            mems.append(input_data[i].split(" = "))
        i+=1
    #do the last one
    do_chunk2(mask,mems)

    sum = 0
    for k,v in memory.items():
        #print(k,v)
        sum+=v
    return sum


def main():
    input_data = load("inputs/input_14.txt")
    print("Input: ",input_data)

    sol1 = solution1(input_data)
    print("Solution1: ",sol1)

    sol2 = solution2(input_data)
    print("Solution2: ",sol2)



if __name__ == '__main__':
    main()
