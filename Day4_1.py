puzzle_range = range(240920,789857+1)

def extractDigits(i):
    r = []
    c = i
    
    
    while c >= 10:
        r.append(c % 10)
        c = c // 10
        
    r.append(c)
    r.reverse()
    return r

def sameAdjacentCheck(l):
    for i in range(len(l)-1):
        if l[i] == l[i + 1]:
            return True
    
    return False

def noDecreaseCheck(l):
    for i in range(len(l) - 1):
        if l[i+1] < l[i]:
            return False
        
    return True


def main():
    possiblePasswords = []
    for i in puzzle_range:
        digits = extractDigits(i)
    
        if sameAdjacentCheck(digits) & noDecreaseCheck(digits):
            possiblePasswords.append(i)

    print("Amount of possible passwords =",str(len(possiblePasswords)))

if __name__ == "__main__":
    main()
