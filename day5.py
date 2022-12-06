with open('data/day5.txt') as f:
    crates = f.read().splitlines()
    
initial = crates[:8]
numbering = crates[8].split()
numbering = [int(i) for i in numbering]
procedure = crates[10:]
    
from textwrap import wrap
stacks = []
for c in initial:
    
    c = wrap(c, 4, drop_whitespace=False)
    c = [cr.replace('[', '') for cr in c]
    c = [cr.replace(']', '') for cr in c]
    c = [cr.replace(' ', '') for cr in c]
    stacks.append(c)


stacks_whole = dict()
#set up first layer of crates
for i in numbering:
    stacks_whole[i] = [stacks[len(stacks)-1][i-1]]

#stack crates onto stacks
for j in range(len(stacks)-2, -1, -1):
    
    for i in numbering:
        stacks_whole[i].append(stacks[j][i-1])

    
for k in stacks_whole.keys():
    stacks_whole[k] = list(filter(None, stacks_whole[k]))
    
import re

for p in procedure:
    task = re.findall(r'\d+', p)
    task = [int(i) for i in task]
    
    for num in range(task[0]):
        stacks_whole[task[2]].append(stacks_whole[task[1]].pop(-1))
    
    
for k in stacks_whole.keys():
    print(stacks_whole[k][len(stacks_whole[k])-1])
    

#%% Part 2


