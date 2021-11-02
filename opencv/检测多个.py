import cv2 as cv

def face_detect_demo():
    gary = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('D:/opencv/opencv-4.5.4/data/haarcascades/haarcascade_frontalface_default.xml')
    face = face_detect.detectMultiScale(gary)
    for x,y,w,h in face:
        cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
    cv.imshow('result',img)

#读取图像
img = cv.imread("27.jpg")
resize_img = cv.resize(img,dsize=(886,1920))
print('原始大小：',img.shape)
print('修改后大小',resize_img.shape)
#检测函数
face_detect_demo()
#等待
while True:
    if ord('q') == cv.waitKey(0):
        break

cv.destroyAllWindows()