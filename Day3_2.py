origin = (0,0)
def manhatten(pt1, pt2):
    x_delta = abs(pt1[0] - pt2[0])
    y_delta = abs(pt1[1] - pt2[1])
    delta = x_delta + y_delta

    return delta

def getCoords(wire_instructions):
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

def stepsTakenToCoord(coord, wirepath):
    steps = 0
    for c in range(len(wirepath)):
        steps += 1
        if wirepath[c] == coord:
            break

    return steps

def main():
    wire1 = []
    wire2 = []
    
    with open('day3input.txt') as day3input:
        alltxt = day3input.readlines()
        wire1txt = alltxt[0]
        wire2txt = alltxt[1]

        wire1 = wire1txt.split(',')
        wire2 = wire2txt.split(',')

    wire1coords = getCoords(wire1)
    wire2coords = getCoords(wire2)

    wire1set = set(wire1coords)
    wire2set = set(wire2coords)

    cross_coords = wire1set.intersection(wire2set)

    wire1steps_tox = {}
    for coord in cross_coords:
        wire1steps_tox[coord] = stepsTakenToCoord(coord, wire1coords)

    wire2steps_tox = {}
    for coord in cross_coords:
        wire2steps_tox[coord] = stepsTakenToCoord(coord, wire2coords)

    combined_steps = {coord: wire1steps_tox.get(coord)+wire2steps_tox.get(coord) for coord in set(wire1steps_tox) & set(wire2steps_tox)}

    lowest = 1E10
    lowest_coord = [0,0]
    for crossing in combined_steps:
        if combined_steps.get(crossing) < lowest:
            lowest = combined_steps.get(crossing)
            lowest_coord = crossing

    print(combined_steps)
    print("The lowest amount of steps is >>" + str(lowest) + "<<", "at coord",str(lowest_coord))

if __name__ == "__main__":
    main()