elves = []
indiv_elf = []

f = open('data/day1.txt')
for l in f.readlines():
    l = l.strip('\n')
    
    if len(l) == 0:
        elves.append(indiv_elf)
        indiv_elf = []
    else:
        l = int(l)
        indiv_elf.append(l)
        
f.close()


totals = [sum(x) for x in elves]

print(max(totals))


#%% Part 2

totals.sort(reverse=True)

print(sum(totals[:3]))
