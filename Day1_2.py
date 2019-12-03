day1input = []
with open('day1input.txt', 'r') as day1input:
    day1 = day1input.readlines()
    
module_ms = [str.strip(n) for n in day1]

module_m =[int(ms) for ms in module_ms]

def required_fuel2(mass):
    fuel_needed = int(mass/3) - 2

    if fuel_needed <= 0:
        return 0
    else:
        return fuel_needed + required_fuel2(fuel_needed)


module_f2 = [required_fuel2(m) for m in module_m]
total_fuel_req2 = sum(module_f2)

print(total_fuel_req2)