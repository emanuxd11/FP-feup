def map(pos, steps):
    return (pos[0] + steps.split('-').count("right") - 
    steps.split('-').count("left"), pos[1] + 
    steps.split('-').count("up") - 
    steps.split('-').count("down"))

print(map((0, 0), "up-up-left-right-up-up"))