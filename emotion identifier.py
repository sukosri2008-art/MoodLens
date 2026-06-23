from deepface import DeepFace
import cv2
cam =  cv2.VideoCapture(0)
while True:
    success,img=cam.read()
    if not success:
        break
    a= DeepFace.analyze(img,actions=['emotion'],enforce_detection=False)
    e=a[0]['dominant_emotion']
    cv2.putText(img,e,(125,125),cv2.FONT_HERSHEY_SIMPLEX,4,(234,234,78),4)
    cv2.imshow("FACIAL EXPRESSION",img)
    if cv2.waitKey(20)== ord('q'):
        break
cam .release()
cv2.destroyAllWindows()
