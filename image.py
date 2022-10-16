import cv2

image_path="MoonAndSun.jpeg"

image=cv2.imread(image_path)
# cv2.imshow("sample image",image)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# directory=r"D:\openCV"

# filename="savesImage.png"
# cv2.imwrite(filename,image)
# print("Image Successfully Saved...")

# print(image.shape)

#gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Original Image",image)
# cv2.imshow("Gray Image",gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#  -----Unable to convert from gray to rgb-----

#color=cv2.cvtColor(gray,cv2.COLOR_GRAY2RGB)
# cv2.imshow("Original Image",gray)
# cv2.imshow("Color Image",color)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# resize=cv2.resize(image,(800,700))

#text="Moon And Sun"
#cordinates=(100,100)
#font=cv2.FONT_HERSHEY_SIMPLEX
#fontScale=1.7
# color=(255,250,250)
# thickness=2
# start_point=(100,100)
# end_point=(250,250)
# centre_cordinates=(120,100)
# axisLength=(100,50)
# angle=30
# startAngle=0
# endAngle=360
#radius=200
#image=cv2.putText(image,text,cordinates,font,fontScale,color,thickness)
#image=cv2.line(image,start_point,end_point,color,thickness)
#image=cv2.circle(image,centre_cordinates,radius,color,thickness)
#image=cv2.rectangle(image,start_point,end_point,color,thickness)
# -----Ellipse Running Problem-----
# image=cv2.ellipse(image,centre_cordinates,axisLength,startAngle,endAngle,color,thickness)
#
# cv2.imshow("Original Image",image)
# #cv2.imshow("Resized Image",resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()