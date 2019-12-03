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

answer = 19690720
found_answer = False
noun_answer = 0
verb_answer = 0

noun_pos = 1
verb_pos = 2

with open('day2input.txt', 'r') as day2input:
    intcode_string = day2input.readlines()[0]

intcode_init = [int(s) for s in intcode_string.split(',')]

for noun in range(1,100):
    if found_answer:
        break
    for verb in range(1,100):
        if found_answer:
            break
        
        intcode_attempt = intcode_init
        intcode_attempt[noun_pos] = noun
        intcode_attempt[verb_pos] = verb
        
        intcode_result = intcode_run(intcode_attempt)
        output = intcode_result[0]
        print(output)
        
        if output == answer:
            print('Found Answer!')
            found_answer = True
            noun_answer = noun
            verb_answer = verb

print('noun:',noun_answer)
print('verb:', verb_answer)
print('*'*100)
print('Puzzle answer 100*noun + verb:', 100*noun_answer + verb_answer)