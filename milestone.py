import numpy as np
import cv2

img_file="MoonAndSun.jpeg"
# img=cv2.imread(img_file)
# px=img[940,500]
# print(px)
#
# blue=img[100, 100, 0]
# print(blue)
#
# img[100,100]= [255,255,255]
# print(img[100,100])


# img=cv2.imread(img_file,cv2.IMREAD_COLOR)
# alpha_img= cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
# gray_img= cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
#
# print("RGB Shape :", img.shape)
# print("ARGB Shape: ", alpha_img.shape)
# print("GRAY SCALE Shape :", gray_img.shape)
#
# # Datatype
# print("image datatype: ",img.dtype)
# # Size -----multiplacation of RGB Values----
# print("imgae size: ", img.size)


# img_raw= cv2.imread(img_file)
# roi= cv2.selectROI(img_raw)
# print(roi)
#
# # cropping selected ROI from the raw(given) image
#
# roi_cropped=img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
# cv2.imshow("ROI cropped image",roi_cropped)
# cv2.imwrite("cropped.jpeg",roi_cropped)
# cv2.waitKey(0)
# cv2.destroAllWindows()


# img= cv2.imread(img_file)
# r,g,b= cv2.split(img)
# cv2.imshow("Green part of the image", g)
# cv2.imshow("Red part of the image", r)
# cv2.imshow("Blue part of the image", b)
# img1=cv2.merge((r,g,b))
# cv2.imshow("Image after merging part of three color",img1)
# cv2.waitKey(0)


# color_change=cv2.cvtColor(img,cv2.COLOR_RGB2LAB)
# cv2.imshow("Color changed from RGB2LAB",color_change)
# cv2.waitKey(0)


# scr1=cv2.imread("MoonAndSun.jpeg",cv2.IMREAD_COLOR)
# scr2=cv2.imread("cropped.jpeg",cv2.IMREAD_COLOR)
#
# img1=cv2.resize(scr1,(800,600))
# img2=cv2.resize(scr2,(800,600))
#
# blended_image=cv2.addWeighted(img1,1,img2,.5,.0)
# cv2.imshow("Blende image",blended_image)
# cv2.waitKey(0)


# img=cv2.imread(img_file)
# k_sharpened=np.array([[-1,-1,-1],
#                       [-1,9,-1],
#                       [-1,-1,-1]])
# sharpened=cv2.filter2D(img,-1,k_sharpened)
#
# cv2.imshow("Original image",img)
# cv2.imshow("Filtered image",sharpened)
# cv2.waitKey(0)


# img=cv2.imread(img_file, cv2.IMREAD_COLOR)
# ret, thresh= cv2.threshold(img,127,255,cv2.THRESH_BINARY)
# cannyimage=cv2.Canny(img,50,100)
#
# cv2.imshow("Original image", img)
# cv2.imshow("Threshold image",thresh)
# cv2.imshow("Canny image", cannyimage)
# cv2.waitKey(0)


from matplotlib import pyplot as plt
# -----2:23 hr.min---- start from the video