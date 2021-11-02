import cv2 as cv


img = cv.imread("[Natsu]80583135.jpg")
cv.imshow("read_img",img)
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

cv.waitKey(0)

cv.destroyAllWindows()