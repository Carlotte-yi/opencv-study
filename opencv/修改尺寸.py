import cv2 as cv


img = cv.imread("[Natsu]80583135.jpg")


#修改尺寸
resize_img = cv.resize(img,dsize=(520,360))
#显示原图
cv.imshow('img',img)
#显示修改后的
cv.imshow('resize_img',resize_img)
#打印原图尺寸大小
print('未修改:',img.shape)
#打印修改后的大小
print('修改后',resize_img.shape)

while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()