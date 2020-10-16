import cv2
import dropbox
import time
import random

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite()method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    #release the camera
    videoCaptureObject.release()
    #close all the windows that might be opened during the process
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "V6B5KxFUJb0AAAAAAAAAAYzJKdV_RfIH21V2rG3FETWCIIu5k9ZbCQLjWa0H75us"
    file = img_name
    file_from = file
    file_to="/testfolder/"+(img_name)

    dbx = dropbox.Dropbox(access_token)

    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()-start_time)>=300):
            name = take_snapshot()
            upload_file(name)

main()