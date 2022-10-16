import cv2
#
# # img=cv2.imread("MoonAndSun.jpeg", 0)
# # cv2.imshow("Original image", img)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()
#
#
# #abc=cv2.VideoCapture(0)
#
# # while (True):
# #     ret, frames =abc.read()
# #     cv2.imshow("abc",frames)
# #     if cv2.waitKey(1) & 0xFF == ord("q"):
# #         break
# #         abc.release()
# # cv2.destroyAllWindows()
#
#
# cap=cv2.VideoCapture(0)
#
# if(cap.isOpened()==False):
#     print("Camera Couldn't Open...")
#
# frame_width=int(cap.get(3))
# frame_height=int(cap.get(4))
#
# #  Video Coded.....encoders and decoders
#
# video_cod=cv2.VideoWriter_fourcc(*"XVID")
# video_output=cv2.VideoWriter("Capured_video.mp4",video_cod,30,(frame_width,frame_height))
#
# while (True):
#     ret, frame = cap.read()
#
#     if ret == True:
#         video_output.write(frame)
#         cv2.imshow("frame",frame)
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         break
# cap.release()
# video_output.release()
# cv2.destroyAllWindows()
# print("The Video was saved successfully...")


cap= cv2.VideoCapture("Capured_video.mp4")
while (True):
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()