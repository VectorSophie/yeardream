import  pandas as pd
import numpy as np

import PIL
import matplotlib.image as img
import matplotlib.pyplot as plt

from elice_utils import EliceUtils
elice_utils = EliceUtils()

def load_data(path):
    return pd.read_csv(path)

def load_images(path, names):
    
    images=[]
    
    for name in names:
        img_path = path + name
        image = PIL.Image.open(img_path)  
        images.append(image)
    
    return images

def images2numpy(images, size):
    
    output = []
    for image in images:
        image_resized = image.resize(size)  
        output.append(np.array(image_resized))  
    return output

def sampleVisualize(np_images):

    fileName = "./data/images/1000092795.jpg"
    ndarray = img.imread(fileName)
    
    plt.imshow(ndarray)
    plt.show()    
    plt.savefig("plot.png")
    
    print("\n1-1. 'fileName' 이미지(원본): ")
    elice_utils.send_image("plot.png")
    
    print('\n1-2. Numpy array로 변환된 원본 이미지:', ndarray)
    print('\n1-3. Numpy array로 변환된 원본 이미지의 크기:', np.array(ndarray).shape)
    
    plt.imshow(np_images[0])
    plt.show()
    plt.savefig("plot_re.png")
    
    print("\n2-1. 'fileName' 이미지(resize 후): ")
    elice_utils.send_image("plot_re.png")
    
    print('\n2-2. Numpy array로 변환된 resize 후 이미지:', np_images[0])
    print('\n2-3. Numpy array로 변환된 resize 후 이미지 크기:', np.array(np_images[0]).shape)    
    
    print('\n3. Numpy array로 변환된 resize 후 이미지 10장의 크기:', np.array(np_images).shape)

def main():
    
    CSV_PATH = "./data/data.csv"
    IMG_PATH = "./data/images/"
    IMG_SIZE = (300,300)
    MAX_LEN = 30
    BATCH_SIZE = 2
    
    name_caption = load_data(CSV_PATH)
    names = name_caption['file_name']
    
    images = load_images(IMG_PATH, names)
    np_images = images2numpy(images, IMG_SIZE)
    
    sampleVisualize(np_images)
    
    return images, np_images
    
if __name__=='__main__':
    main()