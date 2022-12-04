import re 

with open('data/day4.txt') as f:
    camp = f.read().splitlines() 
    
    
camp = [x.split(',') for x in camp]

overlap_1 = 0
overlap_2 = 0
for c in camp:
    
    elf1_start = re.findall(r'\d+', c[0])[0]
    elf1_end = re.findall(r'\d+', c[0])[1]
    
    elf2_start = re.findall(r'\d+', c[1])[0]
    elf2_end = re.findall(r'\d+', c[1])[1]


    elf1_area = set(range(int(elf1_start), int(elf1_end) +1))
    elf2_area = set(range(int(elf2_start), int(elf2_end) +1))

    if len(elf1_area) >= len(elf2_area):
        combined = elf1_area.union(elf2_area)
        part_1 = len(combined) == len(elf1_area)
        part_2 = len(combined) < len(elf1_area) + len(elf2_area)
        
    else:
        combined = elf2_area.union(elf1_area)
        part_1 = len(combined) == len(elf2_area)
        part_2 = len(combined) < len(elf1_area) + len(elf2_area)
    
    if part_1:
        overlap_1 += 1
        
    if part_2:
        overlap_2 += 1
        
print(overlap_1)

print(overlap_2)