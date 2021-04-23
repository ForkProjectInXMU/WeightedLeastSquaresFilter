import wls
import cv2
import numpy as np

img_In = cv2.imread('./79.JPG')
# I = double(img_In)
I = img_In/255.0
R = img_In[:, :, 0]
G = img_In[:, :, 1]
B = img_In[:, :, 2]
# R = double(R)
# G = double(G)
# B = double(B)
R = R/255.0
G = G/255.0
B = B/255.0

lumin_R = wls.wls_filter(R, 2, 2)
lumin_G = wls.wls_filter(G, 2, 2)
lumin_B = wls.wls_filter(B, 2, 2)
lumin = np.concatenate((lumin_R,lumin_G),axis=2)
lumin = np.concatenate((lumin,lumin_B),axis=2)
detail = I - lumin
cv2.imwrite(lumin,'result1.png');
cv2.imwrite(detail,'result2.png');

# 可以，经过测试这玩意儿根本跑不动，真就没用呗，还是用matlab吧
