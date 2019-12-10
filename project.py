import cv2

image = cv2.imread("nv0041.jpg")
image = cv2.resize(image, (200,200))

cv2.imshow("image",image)
cv2.waitKey(0)
