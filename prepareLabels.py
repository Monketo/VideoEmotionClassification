import glob
import numpy as np
import cv2
from scipy.spatial import distance
from pylab import *
datasetRoot = "/home/ubuntu/CourseAI/datasets/facs/"

k=0
maxId = 0
for landmarkFile in glob.glob(datasetRoot+'labels/*/*/*.txt'):
    facs = np.loadtxt(landmarkFile)
    label = np.zeros(65)
    if len(facs.shape) < 2:
        facs = np.expand_dims(facs, axis=0)
    if facs.max() > maxId:
        maxId = facs.max()
    for attr in facs:
         label[int(attr[0])] = 1
    np.save(landmarkFile.replace('.txt', '.npy'), label)
    k+=1
    print k
    

print("Landmarks were created")


k=0
for emFile in glob.glob(datasetRoot+'emotions/*/*/*.txt'):
    em = np.loadtxt(emFile)
    label = np.zeros(7)
    if em.max() > maxId:
        maxId = em.max()
    label[int(em)-1] = 1
    np.save(emFile.replace('.txt', '.npy'), label)
    k+=1
    print k


print('Finished')