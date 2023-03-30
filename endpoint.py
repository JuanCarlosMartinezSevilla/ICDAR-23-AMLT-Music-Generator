import argparse
from main import Main
import random
import cv2
import numpy as np


def readCameraImage():
    img = cv2.imread("cameraExample.png", cv2.IMREAD_GRAYSCALE)
    return img

def readImage():
    img = cv2.imread("example.png", cv2.IMREAD_GRAYSCALE)
    return img

def readGT():
    with open('example.krn') as f:
        lines = f.readlines()
    return lines

def endpoint(batch_size):
    args = argparse.ArgumentParser()
    batch_images = []
    batch_images_camera = []
    batch_gt = []
    while batch_size > 0:
        args.measures = random.randint(2, 6)
        args.voices = 1
        args.lyrics = 1
        args.camera = True
        args.background = False
        
        #args.camera = True
        Main.main(args)

        batch_images.append(readImage())
        batch_images_camera.append(readCameraImage())
        batch_gt.append(readGT())

        batch_size -= 1

    return batch_images, batch_images_camera, batch_gt

if __name__ == '__main__':
    
    print(endpoint(batch_size=2))
