import cv2

image=cv2.imread("r.png")
gray_img= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("grey",gray_img)
cv2.imshow("popopop",image)
cv2.waitKey(0)
cv2.destroyAllWindows()