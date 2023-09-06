# -*- coding: utf-8 -*-
import sys,os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication
from Ui_map_assistant import Ui_MainWindow  #导入你写的界面类
from functools import partial
import cv2 as cv
import numpy as np
import data
class MyMainWindow(QMainWindow,Ui_MainWindow): #这里也要记得改
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)

dir='D:\workplace\maps\dwrg_maps'
#填入你的目录

rb_list=[]
def rb_slot(text,rb_list,flag):
    if flag:
        rb_list.append(text)
        print("rb_list",rb_list)
    else:
        rb_list.remove(text)
def cv_imread(path):
    #import cv2 as cv
    img=cv.imdecode(np.fromfile(path,dtype=np.uint8),-1)
    return img

def ysf_slot(myWin):
    
    gb=getattr(myWin,rb_list[0]+"_2")
    
    grid=gb.findChild(QtWidgets.QGridLayout,rb_list[0]+"_2_killer")
    killer_born=[]
    for c in range(grid.count()):
        cb=grid.itemAt(c).widget()
        if cb.isChecked():
            killer_born.append(cb.text())
    # print(killer_born)
    if len(killer_born)>1 or len(killer_born)==0:
        # QtWidgets.QMessageBox.information(myWin,"ERROR","不要选两个")
        print("two born")
        return
    path=(dir+"\\"+rb_list[0]+"\\"+killer_born[0]+"ysf.png")
    # path=[]
    # for kb in killer_born:
    #     path.append(dir+"\\"+rb_list[0]+"\\"+kb)
    # imgs=[]
    # for p in path:
    #     imgs.append(cv.imread(p))
    
    img=cv_imread(path)
    winname=killer_born[0]+"ysf"
    cv.namedWindow(winname,0)
    cv.moveWindow(winname, 0, 150)
    cv.resizeWindow(winname, 300, 300)
    cv.imshow(winname,img)
    
    video_path=dir+"\\video\\"+rb_list[0]+"\\"+data.ysf[rb_list[0]][killer_born[0]]+".mp4"
    # print(video_path)
    cap = cv.VideoCapture(video_path)
    while cap.isOpened():
        ret, frame = cap.read()
        if  not ret:
            # cap.release()
            break
        cv.namedWindow("ysfv",0)
        cv.resizeWindow("ysfv", 400, 300)
        cv.imshow("ysfv", frame)
        
        if cv.waitKey(18) & 0xFF == 27:
            # cap.release()
            break
        

        
    print("break")
    cv.waitKey(0)#第一次暂停 第二次退出
    cap.release()
    cv.destroyAllWindows()
    
def tf_slot(myWin):
    gb=getattr(myWin,rb_list[0]+"_2")
    
    grid=gb.findChild(QtWidgets.QGridLayout,rb_list[0]+"_2_killer")
    killer_born=[]
    for c in range(grid.count()):
        cb=grid.itemAt(c).widget()
        if cb.isChecked():
            killer_born.append(cb.text())
    if len(killer_born)>1 or len(killer_born)==0:
        print("two born")
        return
    path=(dir+"\\"+rb_list[0]+"\\"+killer_born[0]+"ysf.png")

    
    img=cv_imread(path)
    winname=killer_born[0]+"ysf"
    cv.namedWindow(winname,0)
    # cv.moveWindow(winname, 0, 150)
    cv.resizeWindow(winname, 300, 300)
    cv.imshow(winname,img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    
def cellar_slot():
    path=dir+"\\cellar\\"+rb_list[0]+".jpg"
    img=cv_imread(path)
    cv.namedWindow("cellar",0)
    cv.resizeWindow("cellar", 300, 300)
    cv.imshow("cellar",img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def which_map(cb):
    #遍历查找符合条件的所有地图
    mapdic=getattr(data,rb_list[0])
    cb=set(cb)
    maplist=[]
    for k,v in mapdic.items():
        if set(v).issuperset(cb):#cb 是否是该出生集合的子集
            maplist.append(k)
            print(k,v)
    return maplist

def human_slot(myWin):
    gb=getattr(myWin,rb_list[0]+"_2")
    grid=gb.findChild(QtWidgets.QGridLayout,rb_list[0]+"_2_human")
    human_born=[]
    for c in range(grid.count()):
        cb=grid.itemAt(c).widget()
        if cb.isChecked():
            human_born.append(cb.text())
    print(human_born)
    if len(human_born)==0:
        print("born is 0")
        return
    maplist=which_map(human_born)

    if len(maplist)>1:
        i=0
        for m in maplist:
            p=dir+"\\"+rb_list[0]+"\\"+m+".png"
            # imgs.append(cv_imread(p))
            imgs=cv_imread(p)
            cv.namedWindow(m,0)
            cv.resizeWindow(m, 300, 300)
            cv.moveWindow(m, 300*i, 150)
            cv.imshow(m,imgs)
            i=+1
        cv.waitKey(0)
        cv.destroyAllWindows()
    elif len(maplist)==1:
        path=dir+"\\"+rb_list[0]+"\\"+maplist[0]+".png"
        imgs=cv_imread(path)
        cv.namedWindow("human",0)
        cv.resizeWindow("human", 300, 300)
        cv.imshow("human",imgs)
        cv.waitKey(0)
        cv.destroyAllWindows()
    else:
        print("no match")
        return

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        myWin = MyMainWindow()
        myWin.show()
        #加入信号和槽连接
        
        radioButtons=myWin.maps.findChildren(QtWidgets.QRadioButton)
        for rb in radioButtons:
            rb.toggled['bool'].connect(partial(rb_slot,rb.objectName(),rb_list))
    
        myWin.ysf.clicked.connect(partial(ysf_slot, myWin))
        myWin.human.clicked.connect(partial(human_slot, myWin))
        myWin.cellar.clicked.connect(cellar_slot)
        myWin.ysf_2.clicked.connect(partial(tf_slot, myWin))
        # print(app.exec_())
        os._exit(app.exec_())
        
        
    except Exception as e:
        repr(e)
        exit(0)
    finally:
        sys.exit(app.exec_())

   
    
