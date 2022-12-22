
import cv2
cam=cv2.VideoCapture("C:/Users/10/Desktop/New folder (2)/ali.mp4")
detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('haarcascade_eye.xml')
while (True):
    ret,img=cam.read()
    #img=cv2.resize(img,(600,300))
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ####---------------face---------------###
    faces=detector.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        ###------eye detection-----###
        face_only=img[y:y+h,x:x+w]
        eyes=eye.detectMultiScale(face_only,1.3,5)
        for(ex,ey,ew,eh) in eyes:
             #cv2.rectangle(face_only,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            eyex=int((ex-(0.25*ex))+(ew/2))
            eyey=int((ey)+(eh))
            cv2.putText(face_only,"x",(eyex,eyey),cv2.FONT_HERSHEY_COMPLEX,4,(255,0,0),4)
             
        
        cv2.imshow('frame',img)
    

    if cv2.waitKey(20) &0xFF ==ord('q'):
        break
    
        
cam.release()
cv2.destroyAllWindows()
