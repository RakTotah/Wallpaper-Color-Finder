from PIL import Image
import os

def clamp(a, minimum, maximum): # Simple clamp function
    return min(max(a, minimum), maximum)

### Pixel functions ###
# All in the form foo(px, x, y)

def greyscale(px, x ,y, im):
    average = (px[x, y][0] + px[x, y][1] + px[x, y][2])//3
    px[x, y] = (average, average, average)

def gaussianBlur(px, x, y, im, strength=3):
    imageSize = im.size
    cellDomain = []
    averages = []
    for i in range(-1*strength//2, strength//2 + 1):
        for j in range(-1*strength//2, strength//2 + 1):
            if x+i < imageSize[0] and y+j < imageSize[1]:
                cellDomain.append(px[x+i, y+j])
    for i in range(3):
        averages.append(sum([ a[i] for a in cellDomain ])//len(cellDomain))
    px[x, y] = tuple(averages)

def printPixel(px, x, y, im):
    print(px[x, y])

### Pixel utilities ###

# Maps a function on each pixel individually
def mapPixel(image, func, showBefore=False, showAfter = False): 
    with Image.open(image) as im:
        if showBefore:
            im.show()
        imageSize = im.size
        px = im.load()
        for x in range(imageSize[0]):
            for y in range(imageSize[1]):
                print((x, y))
                func(px, x, y, im)
        if showAfter:
            im.show()
    return im

# Performs a function on one pixel
def onePixel(image, x, y, func): 
    with Image.open(image) as im:
        imageSize = im.size
        px = im.load()
        func(px, x, y)
        return im