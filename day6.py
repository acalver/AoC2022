with open('data/day6.txt') as f: 
    lines = f.read()
    
def marker_system(puzzle_input, marker_position):
    for i in range(0, len(puzzle_input)):
        marker = set(lines[i:i+marker_position])
        
        if len(marker) == marker_position:
            return(i+marker_position)
            
#Part 1
print(marker_system(lines, 4))

#Part 2
print(marker_system(lines, 14))