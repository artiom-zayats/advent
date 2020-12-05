def load(filename):
    with open(filename) as f:
        content = f.read()
    # you may also want to remove whitespace characters like `\n` at the end of each line

    passports = content.split("\n\n")
    passports = [x.split() for x in passports]

    return passports[0]


def bin_2_num(bin_word,up,down):
    low = 0
    high = 2**len(bin_word)
    for letter in bin_word:
        mid = (high+low)//2
        if letter == up:
            high = mid
        elif letter == down:
            low = mid
        else:
            print("Error")
            break
    return low

def find_min_max(input_data):
    mx = 0
    mn = float("inf")
    for x in input_data:
        id = row_col_id(x)[2]
        mx = max(id,mx)
        mn = min(id,mn)
    return mn,mx

def solution1(input_data):
    return find_min_max(input_data)[1]

def solution2(input_data):
    #find missing number
    mn,mx = find_min_max(input_data)
    list_ids = set(list(range(mn,mx+1)))
    print(list_ids)
    for x in input_data:
        row,col,id = row_col_id(x)
        list_ids.remove(id)
    return list_ids


def row_col_id(x):
      row = bin_2_num(x[:7],up="F",down="B")
      col = bin_2_num(x[7:],up="L",down="R")
      id = row*8 + col
      return row,col,id

def main():
    input_data = load("inputs/input_5.txt")
    print(input_data)

    print("Test Intput",[row_col_id(x) for x in ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']])

    sol1 = solution1(input_data)
    print("solution1",sol1)

    sol2 = solution2(input_data)
    print("solution2",sol2)



if __name__ == '__main__':
    main()
