import os
from wand.image import Image
from wand.color import Color
import random
from data import Data
 

def apply_distortion(path, saving_path, bg_change):
    im = Image(filename=path)
    im.chop(int(random.randint(1, 5)), int(random.randint(1, 6)), int(random.randint(1, 300)), int(random.randint(1, 50)))
    im.swirl(round(random.uniform(-3.00, 3.00), 2))
    im.spread(0.1)
    if bg_change:
        im.shear(Color(Data.bg_color), round(random.uniform(-5.00, 5.00), 2), round(random.uniform(-1.50, 1.50), 2))
    else:
        im.shear("WHITE", round(random.uniform(-5.00, 5.00), 2), round(random.uniform(-1.50, 1.50), 2))
    im.wave(round(random.uniform(0.00, 0.50), 2), round(random.uniform(0.00, 0.40), 2))
    im.rotate(round(random.uniform(0.00, 0.30), 2))
    im.noise("gaussian", round(random.uniform(0.00, 1.25), 2))
    im.wave(round(random.uniform(0.00, 1), 2), round(random.uniform(0.00, 0.40), 2))
    # im.motion_blur(radius=round(random.uniform(-2.00, 2.00), 2), 
    #     sigma=round(random.uniform(-1.50, 1.50), 2), 
    #     angle=round(random.uniform(-2.00, 2.00), 2))
    im.format = 'png'
    im.save(filename=saving_path)


if __name__=="__main__":
    pass