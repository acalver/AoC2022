with open('data/day3.txt') as f:
    lines = f.read().splitlines() 
    
priorities = 0
for l in lines:
    
    bag1 = l[:len(l)//2]
    bag2 = l[len(l)//2:]
    
    bag1 = set([x for x in bag1])
    bag2 = set([x for x in bag2])

    double_item = bag1.intersection(bag2)
    item_value = ord(list(double_item)[0])

    if item_value <= 90:
        priorities += item_value - 38
    else:
        priorities += item_value - 96
        
print(priorities)

#%% Part 2

priorities = 0
for i in range(0,len(lines), 3):
    
    bag1 = lines[i]
    bag2 = lines[i+1]
    bag3 = lines[i+2]
    
    bag1 = set([x for x in bag1])
    bag2 = set([x for x in bag2])
    bag3 = set([x for x in bag3])

    sticker = bag1.intersection(bag2)
    sticker = sticker.intersection(bag3)
    item_value = ord(list(sticker)[0])

    if item_value <= 90:
        priorities += item_value - 38
    else:
        priorities += item_value - 96
        
print(priorities)