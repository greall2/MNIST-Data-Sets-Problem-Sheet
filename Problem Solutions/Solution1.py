#Emerging Technologies
#MNIST DataSets Problem Sheet
#Ríona Greally - G00325504


#1. Read the data files
# Download the image and label files. Have Python decompress and read them byte by byte into appropriate data structures in memory.

import gzip


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
test_labels = read_labels_from_file('../data/t10k-images-idx3-ubyte.gz')

train_images = read_images_from_file('../data/train-images-idx3-ubyte.gz')
test_images = read_images_from_file('../data/t10k-images-idx3-ubyte.gz')