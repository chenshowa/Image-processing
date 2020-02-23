# artifactual duplicate image
# mirror and rotate image from specify folder

reshape_size = 150
rotate_angle = [90 , 180, 270]
rotate_angle_mirror = [0, 90 , 180, 270]


import cv2
import os
from PIL import Image

folder = r"DB_image\caffe\NN"
def copy_images_from_folder(folder):
    
    for filename in os.listdir(folder):
        img = Image.open(os.path.join(folder,filename))
        img = img.resize((reshape_size, reshape_size))
        img.save(os.path.join(folder,filename))
        mirror_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        if img is not None:

            for i in rotate_angle:
                img.rotate(i).save(os.path.join(folder,str(i) + filename))
            for i in rotate_angle_mirror:
                mirror_img.rotate(i).save(os.path.join(folder,"mirror_" + str(i) + filename))
                

    return 0

folder = r"DB_image\caffe\NN"
copy_images_from_folder(folder)