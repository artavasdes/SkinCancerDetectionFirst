import cv2

input = cv2.VideoCapture(0)   
   
#Code exits after 'x' is pressed
while not(cv2.waitKey(1) & 0xFF == ord( 'x' )):   
    ret, frame = input.read()   
 
    if ret:   
        cv2.imshow( "video output", frame )     
    
input.release()   
cv2.destroyAllWindows()   