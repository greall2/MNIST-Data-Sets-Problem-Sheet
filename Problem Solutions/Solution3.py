#Emerging Technologies
#MNIST DataSets Problem Sheet
#Ríona Greally - G00325504


#3. Output the image files as PNGs
# Use Python to output the image files as PNGs, saving them in a subfolder in your repository.
# Name the images in the format train-XXXXX-Y.png or test-XXXXX-Y.png where XXXXX is the image number (where it occurs in the data file) and Y is its label. For instance, the five-thousandth training image is labelled 2, so its file name should be train-04999-2.png. 
# Note the images are indexed from 0, so the five-thousandth image is indexed as 4999. See below for an example of it. Commit these image files to GitHub.hash symbol.

import gzip

import PIL.Image as pil
import numpy as np

def read_images_from_file(filename):
    with gzip.open(filename,'rb') as f:

        #Denotes the file type 
        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("magic is: ", magic)

        #Number of images in the file 
        noimg = f.read(4)
        noimg = int.from_bytes(noimg, 'big')
        print("Number of images", noimg)

        #Number of rows in the file
        norow = f.read(4)
        norow = int.from_bytes(norow, 'big')
        print("Number of rows", norow)

        #Number of Columns in file
        nocol = f.read(4)
        nocol = int.from_bytes(nocol, 'big')
        print("Number of columns", nocol)

        images = []


        #Reading in images from file into the array 
        for i in range(noimg):
          rows = []
          for r in range(norow):
              cols = []
              for c in range(nocol):
                  cols.append(int.from_bytes(f.read(1), 'big'))
              rows.append(cols)
          images.append(rows)
               
    return images 

#Function for reading in the labels
def read_labels_from_file(filename):
    with gzip.open(filename,'rb') as f:

        magic = f.read(4)
        magic = int.from_bytes(magic, 'big')
        print("magic is: ", magic)

        nolab = f.read(4)
        nolab = int.from_bytes(nolab, 'big')
        print("Number of labels", nolab)


        #simpler way of doiing it instead of 3 lines above
        labels = [f.read(i) for i in range(nolab)]

        labels = [int.from_bytes(label, 'big')for label in labels]

    return labels

train_labels = read_labels_from_file('../data/train-labels-idx1-ubyte.gz')
#test_labels = read_labels_from_file('../data/t10k-images-idx3-ubyte.gz')

train_images = read_images_from_file('../data/train-images-idx3-ubyte.gz')
#test_images = read_images_from_file('../data/t10k-images-idx3-ubyte.gz')


#the 3rd image in the set 
for row in train_images[2]:
    #printing . and # to create the image
    for col in row:
        print('.' if col <= 127 else '#' , end = '')
    print()


#converting to png file, opens image in new window and names the image based on it's index
num =2
name = 'train'
img = pil.fromarray(np.array(train_images[num]))
img = img.convert('RGB')
img.show()
img.save('../images/' + name + '-'+ str(num).zfill(5)+ '-' + str(train_labels[num])+ '.png')

