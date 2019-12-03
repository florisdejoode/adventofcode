 # Floris de Joode 2019

day1input = []
with open('day1input.txt', 'r') as day1input:
    day1 = day1input.readlines()
    
module_ms = [str.strip(n) for n in day1]

module_m =[int(ms) for ms in module_ms]

def required_fuel(mass):
    fuel_needed = int(mass/3)-2
    
    return fuel_needed


module_f = [required_fuel(m) for m in module_m]

total_required_fuel = sum(module_f)

print(total_required_fuel)
 