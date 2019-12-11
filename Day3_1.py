origin = (0,0)
def manhatten(pt1, pt2):
    x_delta = abs(pt1[0] - pt2[0])
    y_delta = abs(pt1[1] - pt2[1])
    delta = x_delta + y_delta

    return delta

def getcoords(wire_instructions):
    pos = [0,0]
    coords = []

    for step in wire_instructions:
        direction = step[0]
        amount = int(step[1:])

        if direction == 'R':
            x, y = 1, 0
        elif direction == 'D':
            x, y = 0, -1
        elif direction == 'L':
            x, y = -1, 0
        elif direction == 'U':
            x, y = 0, 1

        for _ in range(amount):
            pos[0] += x
            pos[1] += y
            coords.append(tuple(list.copy(pos)))

    return coords

def main():
    wire1 = []
    wire2 = []
    
    with open('day3input.txt') as day3input:
        alltxt = day3input.readlines()
        wire1txt = alltxt[0]
        wire2txt = alltxt[1]

        wire1 = wire1txt.split(',')
        wire2 = wire2txt.split(',')

    wire1coords = getcoords(wire1)
    wire2coords = getcoords(wire2)

    wire1set = set(wire1coords)
    wire2set = set(wire2coords)

    cross_coords = wire1set.intersection(wire2set)

    cross_distances = []

    for coord in cross_coords:
        cross_distances.append(manhatten(origin,coord))

    print('The intersection with the lowest manhatten distance from origin is ',str(min(cross_distances)), 'steps away')

if __name__ == "__main__":
    main()