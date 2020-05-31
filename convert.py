from PIL import Image
from PIL import glob
import random
import os


dirName = 'trainA'

try:
    # Create target Directory
    os.mkdir('./datasets/soccer/' + dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")

for f in glob.iglob("./datasets/soccer/seg/*"):

    picture = Image.open(f).convert('RGB')

    # Get the size of the image
    width, height = picture.size

    def noise(red, green, blue):
        rand = random.randint(0, 50)
        randRed = rand if red else 0
        randGreen = rand if green else 0
        randBlue = rand if blue else 0
        return (randRed, randGreen, randBlue)

    # Process every pixel
    for x in range(width):
        for y in range(height):
            current_color = picture.getpixel((x, y))
            if current_color[0] > 50 and current_color[1] > 50 and current_color[2] < 50:
                red, green, blue = noise(1, 1, 0)
                picture.putpixel((x,y), (current_color[0] - red, current_color[1] - green, current_color[2] - blue)) # add noise to yellow
            elif current_color[0] > 50 and current_color[1] < 50 and current_color[2] < 50:
                red, green, blue = noise(1, 0, 0)
                picture.putpixel((x,y), (current_color[0] - red, current_color[1] - green, current_color[2] - blue)) # add noise to red
            elif current_color[0] < 50 and current_color[1] > 50 and current_color[2] < 50:
                red, green, blue = noise(0, 1, 0)
                picture.putpixel((x,y), (current_color[0] - red, current_color[1] - green, current_color[2] - blue)) # add noise to white
            elif current_color[0] > 50 and current_color[1] > 50 and current_color[2] > 50:
                red, green, blue = noise(1, 1, 1)
                picture.putpixel((x,y), (current_color[0] - red, current_color[1] - green, current_color[2] - blue)) # add noise to green
                
    picture.save("./datasets/soccer/" + dirName + "/noise_{:08d}.png")