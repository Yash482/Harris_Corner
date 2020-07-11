import numpy as np
import cv2
import matplotlib.pyplot as plt
# matplotlib qt

img = cv2.imread("chess.jpg")
img_copy= np.copy(img)
img_copy = cv2.cvtColor(img_copy, cv2.COLOR_BGR2RGB)
#plt.imshow(img_copy)
gray = cv2.cvtColor(img_copy, cv2.COLOR_RGB2GRAY)
#plt.imshow(gray)

#convert the img to floating values
gray = np.float32(gray)

#Detect corner
dst = cv2.cornerHarris(gray, blockSize =2, ksize =3, k =0.04)


plt.imshow(dst, cmap ='gray')

