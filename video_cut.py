import cv2 as cv
import os,sys
import warnings

warnings.filterwarnings('ignore')
from moviepy.editor import *

def cut(src,res,s,e):
    if len(e)>0:
        clip = VideoFileClip(src).subclip((s[0],s[1]),(e[0],e[1]))
    else:
        clip = VideoFileClip(src).subclip((s[0],s[1]))

    new_file =  res+"\\"+str(s[0])+"-"+str(s[1])+".mp4"
    clip.write_videofile(new_file)  
      

if __name__ == '__main__':
    name1="moon_river"
    video_path = "D:\workplace\maps\dwrg_maps\\video\\"+name1+".mp4"
    result_video_path = "D:\workplace\maps\dwrg_maps\\video\\"+name1
    if not os.path.exists(result_video_path):
        os.mkdir(result_video_path)
    name = ".mp4"
    time="""00:26
01:46
03:02
04:20
05:46
07:02
08:17"""
    tcl=list(filter(None,time.split("\n")))
    for i in range(0,len(tcl)):
        s=tcl[i].split(":")
        s=list(map(lambda x:int(x),s))
        e=[]
        if i+1 <len(tcl):
            e=tcl[i+1].split(":")
            e=list(map(lambda x:int(x),e))
        print(s,e)
        cut(video_path, result_video_path, s, e)
