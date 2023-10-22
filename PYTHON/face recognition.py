import random
import cv2
import os
import datetime
#2. Initialize the classifier:
a1=input("enter the video stream url,file name or 0,1,2 for camera access :-")
if a1.isdigit()==True:
        
    try:
        video_capture = cv2.VideoCapture(int(a1))
    # Check if camera opened successfully
    except :
        print("Unable to read video feed")
        exit()
    cascPath=os.path.dirname(cv2.__file__)+"/data/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    #3. Apply faceCascade on webcam frames: 
    # Default resolutions of the frame are obtained.The default resolutions are system dependent.
    # We convert the resolutions from float to integer.
    frame_width = int(video_capture.get(3))
    frame_height = int(video_capture.get(4))
    x0 = (datetime.datetime.now())
    x1=str(x0.day)+"-"+str(x0.month)+"-"+str(x0.year)+"_"+str(x0.hour)+':'+str(x0.minute)+":"+str(x0.second)
    a="C:\\Users\\utkar\\Desktop\\videos\\"+input("enter file name for recording to be saved:- ")+".avi"
    file=cv2.VideoWriter(a,cv2.VideoWriter_fourcc('M','J','P','G'),5, (frame_width,frame_height))
    while True:
    # Capture frame-by-frame
        ret, frames = video_capture.read()
        if ret == True:
            x0 = (datetime.datetime.now())
            if x0.day==1:
                a="st"
            elif x0.day==2:
                a="nd"
            elif x0.day==3:
                a="rd"
            else:
                a="th"
            x1=(x0.strftime("%d"+a+" %B %Y"))+"_"+str(x0.hour)+':'+str(x0.minute)+":"+str(x0.second)
            cv2.putText(frames,x1,(50,150),cv2.FONT_ITALIC,1,(255,0,0),2)
            
    # Write the frame into the file 'video1.mp4'
            gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

            faces = faceCascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE
            )

    # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 0), 2)
                file.write(frames)
                exkey=(27,32,ord("q"))
                if cv2.waitKey(1) & 0xFF== ord("c"):
                    img="C:\\Users\\utkar\\Desktop\\videos\\images\\img-"+str(random.choice(range(1,999999)))+".png"
                    cv2.imwrite(img,frames)
                elif cv2.waitKey(1) & 0xFF in exkey:
                    break          
            
    # Display the resulting frame
            cv2.imshow('Video', frames)
            exkey=(27,32,ord("q"))
            if cv2.waitKey(10) & 0xFF in exkey:
                break
        else:
            break
#4. Release the capture frames:
    video_capture.release()
else:
    video_capture = cv2.VideoCapture(a1)
    while True:
        ret, frames = video_capture.read()
        if ret==True:
            cv2.imshow('Video', frames)
            exkey=(27,32,ord("q"))
            if cv2.waitKey(10) & 0xFF in exkey:
                break
        
    video_capture.release()
cv2.destroyAllWindows()