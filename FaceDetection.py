import cv2

cap = cv2.VideoCapture(0)
i=0

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while (cap.isOpened()):

    ret, frame = cap.read()

    if ret == False:
        break

    path='E:\SEM4\PYTHON PROGRAM\FaceDetectionSystem\Video Frames\image'+str(i)+'.jpg'
    cv2.imwrite(path,frame)
    i+=1

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=6,
        minSize=(30, 30)
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("frame", frame)
    #cv2.imshow("gray",gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()