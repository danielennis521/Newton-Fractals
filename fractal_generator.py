from PIL import Image
import numpy as np

file1 = open('fractal.txt', 'r')
n = 0
colors = []

while True:
    line = file1.readline()
    if not line:
        break
    else:
        colors.append([])
        counts = line.split(',')
        for i in counts[:-1]:
            colors[n].append((5,5,int(i) * 5))
        n+=1
file1.close()
print(len(colors))

array = np.array(colors, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('oooo_pretty_2.png')
