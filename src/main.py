from PIL import Image

def clamp(a, minimum, maximum): # Simple clamp function
    return min(max(a, minimum), maximum)

### Pixel functions ###
# All in the form foo(px, x, y)

def greyscale(px, x ,y):
    average = (px[x, y][0] + px[x, y][1] + px[x, y][2])//3
    px[x, y] = (average, average, average)

### Pixel utilities ###

def mapPixel(image, func, show=False): # Maps a function on each pixel individually
    with Image.open(image) as im:
        im.show()
        imageSize = im.size
        px = im.load()
        for x in range(imageSize[0]):
            for y in range(imageSize[1]):
                func(px, x, y)
        if show:
            im.show()