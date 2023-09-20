
rgbconst = 255


accuracy = 255
speed = 5


mult = accuracy / rgbconst

for x in range(int(accuracy / speed + 1)):
    for y in range(int(accuracy / speed + 1)):
        for z in range(int(accuracy / speed + 1)):
            print(f'[{x*speed}, {y*speed}, {z*speed}],')