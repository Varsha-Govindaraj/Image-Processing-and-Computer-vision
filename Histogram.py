import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread(r"C:\Users\Varsha G\OneDrive\Pictures\today.webp" )
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("original Image",image)
cv2.imshow("grayscale Image",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
brightness=50
bright_image=cv2.add(gray,brightness)
cv2.imshow("original",gray)
cv2.imshow("Brightness Enhanced",bright_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
equalized=cv2.equalizeHist(gray)
cv2.imshow("original",gray)
cv2.imshow("Histogram Equalized",equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
min_value=np.min(gray)
max_value=np.max(gray)
stretched=((gray-min_value)/(max_value-min_value))*255
stretched=stretched.astype(np.uint8)
cv2.imshow("original",gray)
cv2.imshow("stretched",stretched)
cv2.waitKey(0)
