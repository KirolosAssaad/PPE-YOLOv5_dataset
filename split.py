# split the data into training, testing, and validation sets

import numpy as np
import pandas as pd
import os
import shutil
import random
from imutils import paths

# set the path to the original input directory of images
ORIG_INPUT_DATASET = "images"

# set the base path to the new directory that will contain
# our images after computing the training and testing split
BASE_PATH = "restructuredDataset"

# define the names of the training, testing, and validation
# directories
TRAIN = "train"
TEST = "test"
VAL = "valid"

# set the percentage of images used for testing
TEST_SPLIT = 0.2

# set the percentage of images used for validation
VAL_SPLIT = 0.1

# grab the paths to all input images in the original input
# directory and shuffle them
imagePaths = list(paths.list_images(ORIG_INPUT_DATASET))
random.seed(42)
random.shuffle(imagePaths)

# compute the total number of images in the directory
totalImages = len(imagePaths)

# compute the testing split
testSplit = int(totalImages * TEST_SPLIT)

# compute the validation split
valSplit = int(totalImages * VAL_SPLIT)

# define the training, testing, and validation lists
trainPaths = imagePaths[testSplit + valSplit:]
testPaths = imagePaths[:testSplit]
valPaths = imagePaths[testSplit:testSplit + valSplit]

# construct a list of datasets
datasets = [
    ("train", trainPaths, TRAIN),
    ("test", testPaths, TEST),
    ("val", valPaths, VAL)
]

# loop over the datasets and copy the images to the new
# directory of images 
for (dType, imagePaths, baseOutput) in datasets:
    # show which data split we are creating
    print("Building {} split".format(dType))

    # if the base output directory does not exist, create it
    if not os.path.exists(os.path.sep.join([BASE_PATH, baseOutput])):
        os.makedirs(os.path.sep.join([BASE_PATH, baseOutput]))

    # loop over the input image paths
    for inputPath in imagePaths:

        print(inputPath)
        # extract the filename of the input image and extract
        # the class label ("cat" or "dog") from the filename
        filename = inputPath.split(os.path.sep)[-1]

        # construct the path to the copy of the image
        p = os.path.sep.join([BASE_PATH, baseOutput, "images", filename])

        # copy the image
        shutil.copy2(inputPath, p)

        # construct the path to the labels file
        labelPath = os.path.sep.join([BASE_PATH, baseOutput, "labels", filename.replace(".png", ".txt")])

        # copy the labels file
        shutil.copy2(("labels/"+(inputPath.replace(".png", ".txt"))[6::]), labelPath)

