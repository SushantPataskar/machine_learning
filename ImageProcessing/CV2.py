import cv2
import os
import numpy as np
#import matplotlib.pyplot as plt

folder=r'E:\Coastal_Karnataka_Tour\Pictures'
pic_path=os.path.join(folder,'01_Malpe beach.jpg') 

#vid_path=os.path.join(folder,'20221205_123637.mp4')
# vid_path0=0
# vid_path1=1 #webcam video

#Read Image
img=cv2.imread(pic_path)
cv2.imshow('Beach',img)
# cv2.waitKey(0)

# #Resize the image
# def rescale(frame,scale):
#     width=int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)

#     dimension=(width,height)
#     return cv2.resize(frame,dimension,interpolation=cv2.INTER_AREA)

# #Capture the video
# capture = cv2.VideoCapture(vid_path0)
# capture2 = cv2.VideoCapture(vid_path1)
# while True:
#     isTrue,frame=capture.read()
#     cv2.imshow('Video',frame)
#     isTrue1,frame1=capture2.read()
#     frame_resized=rescale(frame1,0.5)
#     cv2.imshow('VideoResized',frame_resized)
#     if cv2.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv2.destroyAllWindows()


blank=np.zeros((500,500,3),dtype='uint8')
# blank[100:200,300:400]= 255,0,0
# Draw rectangle
# cv2.rectangle(blank,(0,0),(250,250),(0,0,255),thickness=-2)

#Draw circle
# cv2.circle(blank,(250,250),100,(255,255,0),thickness=-1)

# Draw a line
# cv2.line(blank,(100,200),(200,100),(255,0,255),thickness=10)

#Write text
# cv2.putText(blank,"Blank",(100,100),cv2.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),thickness=2)
# cv2.imshow('blank',blank)

# #converting image into grayscale
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)

# Blur image
# blur=cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
# cv2.imshow('blur',blur)

#Edge Cascade
# cas=cv2.Canny(img,100,200)
# cv2.imshow('cas',cas)
# cas=cv2.Canny(blur,100,200)
# cv2.imshow('cas',cas)

# #Dilating images
# dilated=cv2.dilate(cas,(3,3),iterations=2)
# cv2.imshow('dilated',dilated)

# #eroding
# eroded=cv2.erode(dilated,(3,3),iterations=2)
# cv2.imshow('eroded',eroded)

# #Resize
# resized=cv2.resize(img,(500,500))
# cv2.imshow('resized',resized)

# #Cropping
# cropped=img[10:200,20:200]
# cv2.imshow('cropped',cropped)

# #Translation
# def translate(img,x,y):
#     transMat=np.float32([[1,0,x],[0,1,y]])
#     dimensions=(img.shape[1],img.shape[0])
#     return cv2.warpAffine(img,transMat,dimensions)
# translated=translate(img, 20, 25)
# cv2.imshow('translated',translated)

# #Rotation
# def rotate(img,ang,rotPoint=None):
#     (height,width)=img.shape[:2]
#     if rotPoint == None:
#         rotPoint=(width//2,height//2)
#     rotMat=cv2.getRotationMatrix2D(rotPoint,ang,1.0)
#     dimensions=(width,height)
#     return cv2.warpAffine(img,rotMat,dimensions)
# rotated=rotate(img,-90)
# cv2.imshow('rotated',rotated)

# #Flip image
# v_flip=cv2.flip(img,0)
# h_flip=cv2.flip(img,1)
# vh_flip=cv2.flip(img,-1)
# cv2.imshow('v_flip',v_flip) 
# cv2.imshow('h_flip',h_flip) 
# cv2.imshow('vh_flip',vh_flip) 

#Contours
# contours,heiracrchy=cv2.findContours(cas,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# print(str(len(contours)) + ' countours found !')
# ret,thresh=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
# cv2.imshow('thresh',thresh) 
# contours,heiracrchy=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
# print(str(len(contours)) + ' countours found !')

# Draw contours
# blank=np.zeros(img.shape,dtype='uint8')
# cv2.imshow('blank',blank)
# cv2.drawContours(blank,contours,-1,(255,255,255),1)
# cv2.imshow('Contours_Drawn',blank)

# Convert BGR to HRV(Hue Saturation Value)
# hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
# cv2.imshow('hsv',hsv)

# Convert BGR to LAB
# lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
# cv2.imshow('lab',lab)

# Convert BGR to RGB
# RGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cv2.imshow('RGB',RGB)
# plt.imshow(RGB)
# plt.show()

# Convert HSV to BGR
# hsv_bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
# plt.imshow(hsv_bgr)
# plt.show()

# Convert HSV to BGR
# lab_bgr=cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
# plt.imshow(lab_bgr)
# plt.show()

#Split image in Blue, Green and Red
b,g,r=cv2.split(img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
#print(img.shape,b.shape,g.shape,r.shape)

#Merge images by colors
merged=cv2.merge([b,g,r])
cv2.imshow('merged',merged)

blank=np.zeros(img.shape[:2],dtype='uint8')
b_merged=cv2.merge([b,blank,blank])
cv2.imshow('b_merged',b_merged)
g_merged=cv2.merge([blank,g,blank])
cv2.imshow('g_merged',g_merged)
r_merged=cv2.merge([blank,blank,r])
cv2.imshow('r_merged',r_merged)


cv2.waitKey(0)