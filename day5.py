with open('data/day5.txt') as f:
    crates = f.read()
    
initial = crates[:325]
    

for i in initial:
    print(i, end='')
    
    
    
    
    
procedure = crates.splitlines()[10:]
