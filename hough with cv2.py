# 来自cv2的模板程序

import numpy as np
import cv2

img = cv2.imread('image.png', 0) # 灰度图像
img = cv2.medianBlur(img, 5)

cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) # 一种格式，增加精度

circles = cv2.HoughCircles( img, cv2.HOUGH_GRADIENT, dp=1,
                            minDist=20, # 圆心之间最小距离
                            param1=50, param2=30, # 边缘强度
                            minRadius=0, maxRadius=0 )
circles = np.uint16(np.around(circles))

# 找到的是圆心xy和半径
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg, (i[0], i[1]), i[2], (0,255,0), 2)
    # draw the center of the circle
    cv2.circle(cimg, (i[0], i[1]), 2, (0,0,255), 3)
    
cv2.imshow('detected circles', cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
