import csv
import operator
import string

import cv2
import numpy as np
import os

labelNameList = []


def colourHistogram(imgName, subfolder, isTrained):
    # load the image
    image = cv2.imread(imgName)
    # split the image into 3 channels
    channels = cv2.split(image)
    feature = 'empty'
    featureList = []
    bgr = ['b', 'g', 'r']
    i = 0
    for (ch, cl) in zip(channels, bgr):
        i += 1

        histogram = cv2.calcHist([ch], [0], None, [256], [0, 256])
        featureList.extend(histogram)

        # find the peak pixel values for R, G, and B
        maxVal = np.argmax(histogram)

        if i == 1:
            blue = str(maxVal)
        elif i == 2:
            green = str(maxVal)
        elif i == 3:
            red = str(maxVal)
            feature = red + ',' + green + ',' + blue

    if isTrained:
        with open('trained.data', 'a+') as f:
            f.write(feature + ',' + subfolder + '\n')
    else:
        name = imgName.split('/')
        labelNameList.append(name.pop())  # get last element of the list to find the name of the image
        with open('tested.data', 'a+') as f:
            f.write(feature + '\n')


# Euclidean Distance of two objects (q1, q2) and i is the current attribute
def calculateEuclideanDistance(q1, q2):
    d = 0
    for i in range(len(q1)):
        d += (q1[i] - q2[i]) ** 2
    return d ** 0.5


# get k nearest neighbours
def knn(trainedFeature, testImage, k):
    distanceList = []
    neighbourList = []
    for i in range(len(trainedFeature)):
        dist = calculateEuclideanDistance(testImage, trainedFeature[i])
        distanceList.append((trainedFeature[i], dist))
    distanceList.sort(key=operator.itemgetter(1))
    for i in range(k):
        neighbourList.append(distanceList[i][0])
    return neighbourList

# neighbour's votes


def responseOfNeighbours(neighbours):
    neighboursList = {}
    for i in range(len(neighbours)):
        res = neighbours[i][-1]
        if res in neighboursList:
            neighboursList[res] += 1
        else:
            neighboursList[res] = 1
    votes = sorted(neighboursList.items(), key=operator.itemgetter(1), reverse=True)
    return votes[0][0]


################################################
#                   MAIN                       #
################################################

# check if data is already exists and delete if exists
# (delete data coming from previous run)

if os.path.exists('trained.data'):
    os.remove('trained.data')

if os.path.exists('tested.data'):
    os.remove('tested.data')

# path of sub folder having training images
redPath = './colour_dataset/red/'
blackPath = './colour_dataset/black/'
orangePath = './colour_dataset/orange/'
yellowPath = './colour_dataset/yellow/'
greenPath = './colour_dataset/green/'
bluePath = './colour_dataset/blue/'
whitePath = './colour_dataset/white/'
violetPath = './colour_dataset/violet/'

# feature extraction using colour histogram and create trained.data file
for i in os.listdir(redPath):
    colourHistogram(redPath + i, 'red', True)

for i in os.listdir(blackPath):
    colourHistogram(blackPath + i, 'black', True)

for i in os.listdir(orangePath):
    colourHistogram(orangePath + i, 'orange', True)

for i in os.listdir(yellowPath):
    colourHistogram(yellowPath + i, 'yellow', True)

for i in os.listdir(greenPath):
    colourHistogram(greenPath + i, 'green', True)

for i in os.listdir(bluePath):
    colourHistogram(bluePath + i, 'blue', True)

for i in os.listdir(whitePath):
    colourHistogram(whitePath + i, 'white', True)

for i in os.listdir(violetPath):
    colourHistogram(violetPath + i, 'violet', True)

# path of test images sub folders
redPathTest = './test_images/red/'
blackPathTest = './test_images/black/'
orangePathTest = './test_images/orange/'
yellowPathTest = './test_images/yellow/'
greenPathTest = './test_images/green/'
bluePathTest = './test_images/blue/'
whitePathTest = './test_images/white/'
violetPathTest = './test_images/violet/'

# feature extraction of test images
labelList = []
for i in os.listdir(redPathTest):
    colourHistogram(redPathTest + i, 'unknown', False)
    labelList.append('red')

for i in os.listdir(blackPathTest):
    colourHistogram(blackPathTest + i, 'unknown', False)
    labelList.append('black')

for i in os.listdir(orangePathTest):
    colourHistogram(orangePathTest + i, 'unknown', False)
    labelList.append('orange')

for i in os.listdir(yellowPathTest):
    colourHistogram(yellowPathTest + i, 'unknown', False)
    labelList.append('yellow')

for i in os.listdir(greenPathTest):
    colourHistogram(greenPathTest + i, 'unknown', False)
    labelList.append('green')

for i in os.listdir(bluePathTest):
    colourHistogram(bluePathTest + i, 'unknown', False)
    labelList.append('blue')

for i in os.listdir(whitePathTest):
    colourHistogram(whitePathTest + i, 'unknown', False)
    labelList.append('white')

for i in os.listdir(violetPathTest):
    colourHistogram(violetPathTest + i, 'unknown', False)
    labelList.append('violet')

# open dataset (load into program)
trainedFeatures = []
with open('trained.data') as f:
    line = csv.reader(f)
    dataset = list(line)

    for x in range(len(dataset)):
        for y in range(3):
            dataset[x][y] = float(dataset[x][y])
        trainedFeatures.append(dataset[x])

testFeatures = []
with open('tested.data') as f:
    line = csv.reader(f)
    dataset = list(line)
    for x in range(len(dataset)):
        for y in range(3):
            dataset[x][y] = float(dataset[x][y])
        testFeatures.append(dataset[x])

predictionList = []
k = 3  # knn's k
for x in range(len(testFeatures)):
    neighbours = knn(trainedFeatures, testFeatures[x], k)
    result = responseOfNeighbours(neighbours)
    predictionList.append(result)

# print prediction results for each test image

print('Image name  \t   |  \t   Prediction')
print('------------------------------------')

for i in range(len(predictionList)):
    print('{:<15}'.format(labelNameList[i]), '{:>5}'.format(':'), '{:>10}'.format(predictionList[i]))
    if (i + 1) % 10 == 0:
        print()

# compare results
nrRed, nrBlack, nrOrange, nrYellow, nrGreen, nrBlue, nrWhite, nrViolet = 0, 0, 0, 0, 0, 0, 0, 0
# we have 10 test images for each class
for i in range(len(labelList)):
    if labelList[i] == 'red':
        if labelList[i] == predictionList[i]:
            nrRed += 1

    elif labelList[i] == 'black':
        if labelList[i] == predictionList[i]:
            nrBlack += 1

    elif labelList[i] == 'orange':
        if labelList[i] == predictionList[i]:
            nrOrange += 1

    elif labelList[i] == 'yellow':
        if labelList[i] == predictionList[i]:
            nrYellow += 1

    elif labelList[i] == 'green':
        if labelList[i] == predictionList[i]:
            nrGreen += 1

    elif labelList[i] == 'blue':
        if labelList[i] == predictionList[i]:
            nrBlue += 1

    elif labelList[i] == 'white':
        if labelList[i] == predictionList[i]:
            nrWhite += 1

    elif labelList[i] == 'violet':
        if labelList[i] == predictionList[i]:
            nrViolet += 1

print('\n\nComparing results...\n')
print('Class   |   Correct predition / Total tests  |  Accuracy')
print('-----', '\t|\t-------------------------------   --------')
print('Red     |           ', nrRed, '/ 10', '{:>23}'.format((nrRed/10)*100), '%')
print('Black   |           ', nrBlack, '/ 10', '{:>23}'.format((nrBlack/10)*100), '%')
print('Orange  |           ', nrOrange, '/ 10', '{:>23}'.format((nrOrange/10)*100), '%')
print('Yellow  |           ', nrYellow, '/ 10', '{:>23}'.format((nrYellow/10)*100), '%')
print('Green   |           ', nrGreen, '/ 10', '{:>23}'.format((nrGreen/10)*100), '%')
print('Blue    |           ', nrBlue, '/ 10', '{:>23}'.format((nrBlue/10)*100), '%')
print('White   |           ', nrWhite, '/ 10', '{:>23}'.format((nrWhite/10)*100), '%')
print('Violet  |           ', nrViolet, '/ 10', '{:>23}'.format((nrViolet/10)*100), '%')
sum = nrRed+nrBlack+nrOrange+nrYellow+nrGreen+nrBlue+nrWhite+nrViolet
print('Total   |           ', sum , '/ 80', '{:>23}'.format((sum/80)*100), '%')