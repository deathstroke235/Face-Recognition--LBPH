import cv2
import sys
cpt = 0

vidStream = cv2.VideoCapture(0)
while True:
    
    ret, frame = vidStream.read() # read frame and return code.
    
    cv2.imshow("test window", frame) # show image in window
    
    cv2.imwrite("C:/Users/SAFI UDDIN/Desktop/face/train-images/0/image%04i.jpg" %cpt, frame)    #Give path to  train-images/0/ and keep image%04i.jpg as it is in this line. Your images will be stored at train-images/0/ folder
    cpt += 1
    
        

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break
        
vidStream.release()
cv2.destroyAllWindows()