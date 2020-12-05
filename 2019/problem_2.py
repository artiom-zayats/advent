def load(filename):
    with open(filename) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content


#19690720

def solution(numbers):
    target = 19690720
    for noun in range(100):
        for verb in range(100):
            if int_compute(numbers,noun,verb) == 19690720:
                return (100*noun)+verb
    return None

def int_compute(numbers,a,b):
    numbers = numbers[0].split(",")
    numbers = [int(x) for x in numbers]
    numbers[1]=a
    numbers[2]=b
    i=0
    while i<len(numbers):
        if numbers[i] == 99:
            break
        elif numbers[i] == 1:
            temp = numbers[numbers[i+2]] + numbers[numbers[i+1]]
            numbers[numbers[i+3]] = temp

            i+=4
        elif numbers[i] == 2:
            temp = numbers[numbers[i + 2]] * numbers[numbers[i + 1]]
            numbers[numbers[i + 3]] = temp
            i+=4
        else:
            print(numbers[i],"position",i,"Error")
            break
    return numbers[0]

def main():
    x = load("inputs/input_2.txt")
    print(x)

    ans = solution(x)
    print("solution is:",ans)

if __name__ == '__main__':
    main()
