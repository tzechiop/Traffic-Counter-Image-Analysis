# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:02:25 2016

@author: thasegawa
"""

import os
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import cv2

def load_all_images(dir):

    imgs = []
    for file_name in os.listdir(dir):
        if (os.path.splitext(file_name)[-1] == '.png') and ('processed' in file_name):
            # Remember that I had to flip the iPhone image, also the image was in BGR colorspace so I had to convert to RGB
            #img = cv2.cvtColor(cv2.imread(os.path.join(dir, file_name)), cv2.COLOR_BGR2RGB)[::-1, ::-1, :]
            img = cv2.imread(os.path.join(dir, file_name))
            imgs.append(img)

    return imgs

def build_gif(imgs, show_gif=True, save_gif=True):

    fig = plt.figure()
    fig.set_size_inches(1080, 1980, True)
    ims = []
    for img in imgs[300:400]:
        im = plt.imshow(img, cmap='viridis', animated=True)
        ims.append([im])
    
    ani = animation.ArtistAnimation(fig, ims, interval=250, blit=True,
                                    repeat_delay=1000)
                                
    if save_gif:
        ani.save('dynamic_images.mp4', dpi = 100)

    if show_gif:
        plt.show()

    return