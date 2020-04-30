#############################################
#           Exploring cv2 to find           #
#               4 leaf clovers              #
#############################################
# Auth: Matthew Dimond
import cv2
import os

# Get me an image
IMDIR = "images/"
IMAGES = os.listdir(IMDIR)
img = cv2.imread(IMDIR+IMAGES[0], 0)
'''
thresh = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,15,2)
cv2.imwrite('thrsh.jpg', thresh)
contours, heirarchy = cv2.findContours(thresh,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours))
cv2.drawContours(img, contours, -1, (255, 0, 0), 3)
'''
edges = cv2.Canny(img, 100, 200)
cv2.imwrite('edges.jpg', edges)
contours, heirarchy = cv2.findContours(edges,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours))
contours = filter(lambda x: cv2.isContourConvex(x), contours)
cv2.drawContours(img, contours, -1, (255, 0, 0), 3)
# Write whatever it is to the file
cv2.imwrite('lol.jpg', img)
