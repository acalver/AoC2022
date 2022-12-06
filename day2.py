with open('data/day2.txt') as f: 
    lines = f.read().splitlines()
    
    
score = 0
for game in lines:
    opponent = game[0]
    player = game[2]
    
    if opponent == 'A':
        if player == 'X':
            score += 4
        if player == 'Y':
            score += 8
        if player == 'Z':
            score += 3
            
    if opponent == 'B':
        if player == 'X':
            score += 1
        if player == 'Y':
            score += 5
        if player == 'Z':
            score += 9
            
    if opponent == 'C':
        if player == 'X':
            score += 7
        if player == 'Y':
            score += 2
        if player == 'Z':
            score += 6
            
            
print(score)
#%% Part 2

score = 0
for game in lines:
    opponent = game[0]
    player = game[2]
    
    if opponent == 'A':
        if player == 'X':
            score += 3 + 0
        if player == 'Y':
            score += 1 + 3
        if player == 'Z':
            score += 2 + 6
            
    if opponent == 'B':
        if player == 'X':
            score += 1 + 0
        if player == 'Y':
            score += 2 + 3
        if player == 'Z':
            score += 3 + 6
            
    if opponent == 'C':
        if player == 'X':
            score += 2 + 0
        if player == 'Y':
            score += 3 + 3
        if player == 'Z':
            score += 1 + 6
            
            
print(score)