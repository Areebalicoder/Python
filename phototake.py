import cv2 as cv
import dropbox
import time
import random

st=time.time()

def takepic():
  number=random.randint(0,100)
  videoCaptureO= cv.VideoCapture(0)
  result= True
  while (result):
    ret,frame=videoCaptureO.read()
    iname="img"+str(number)+".png"
    cv.imwrite(iname,frame)
    st=time.time
    result=False
  return iname
  print("Snapshottaken")
  
  videoCaptureO.release()
  cv.destoryAllWindows()

def uploadfile(iname):
    access_token = "upn2DAkr8GoAAAAAAAAAAYlIAoWfZAM3z4nCFRNN9wqER6W3wl2rBqC75ZVM2rev"
    file=iname
    file_from=file
    file_to="/test/"+(iname)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploded")

def main():
    while(True):
        if ((time.time()-st)>=5):
            name=takepic()
            uploadfile(name)

main()


