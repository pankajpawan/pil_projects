from PIL import Image
import os

for f in os.listdir('./images'):
    img = Image.open('./images/'+f)
    width = float(img.size[0])
    height = float(img.size[1])
    if width > 1600:
        ratio = width/height
        new_width = 1600 
        new_height = int(new_width/ratio)
        print(new_width,new_height)
        img2 = img.resize((new_width, new_height))
        img2.save('new_'+f)
