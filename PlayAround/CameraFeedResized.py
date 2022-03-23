import cv2
#Used for determining screen resolution
import ctypes

user32 = ctypes.windll.user32

#Prints out resolution
print("Width", user32.GetSystemMetrics(0))
print("Height", user32.GetSystemMetrics(1))

input = cv2.VideoCapture(0)  

def make_1080p():
    input.set(3,1920)
    input.set(4,1080)

#Sets output of camera to screen 
#resolution of monitor being used
def set_to_screen_res():
    input.set(3, user32.GetSystemMetrics(0))
    input.set(4, user32.GetSystemMetrics(1))
   
#set_to_screen_res()

dsize = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

#Code exits after 'x' is pressed
while not(cv2.waitKey(1) & 0xFF == ord( 'x' )): 
    ret, frame = input.read()   

    resized = cv2.resize(frame, dsize)

    if ret:   
        cv2.imshow( "video output", resized)     
    
input.release()   
cv2.destroyAllWindows()   