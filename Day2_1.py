#Floris de Joode 2019    
def intcode_run(intcode, pos=0):

    result = list.copy(intcode)

    opcode = result[pos]

    if opcode == 99:
        return result

    x_pos = result[pos+1]
    y_pos = result[pos+2]
    r_pos = result[pos+3]

    x = result[x_pos]
    y = result[y_pos]

    if opcode == 1:
        result[r_pos] = x + y
        return intcode_run(result, pos + 4)
    elif opcode == 2:
        result[r_pos] = x * y
        return intcode_run(result, pos + 4)

def main():
    with open('day2input.txt', 'r') as day2input:
        intcode_string = day2input.readlines()[0]

    intcode_list = [int(s) for s in intcode_string.split(',')]

    intcode_list[1] = 12
    intcode_list[2] = 2
    solved_intcode = intcode_run(intcode_list)
    print(solved_intcode)
    print('result = ' + str(solved_intcode[0]))

if __name__ == "__main__":
    main()