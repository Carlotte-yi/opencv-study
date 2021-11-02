import cv2 as cv


img = cv.imread("[Natsu]80583135.jpg")
cv.imshow("read_img",img)
cv.waitKey(0)

cv.destroyAllWindows()