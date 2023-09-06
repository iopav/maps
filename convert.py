import data
# input="""
# 大房
# 中场 两板一窗 两车 雪人
# 大房窗口左
# 月亮门 中场 集装箱 集装箱
# 大房角落
# 月亮门 油罐 中场 南门
# 集装箱
# 木屋 圣诞树 南门 大门
# 木屋窗口
# 月亮门废墟 油罐 大房 两板一窗
# 木屋入口
# 月亮门废墟 月亮门 楼梯 两板一窗
# 圣诞门
# 木屋 中场 两板一窗 大房
# 油罐
# 圣诞树 中场 大房 大房角落
# 月亮门废墟
# 木屋 中场 楼梯 两车
# """
# dict={}
# input1=list(filter(None,input.split("\n")))
# # print(input1)
# for i in range(0,len(input1),2):
#     dict[input1[i]]=input1[i+1].split(" ")
# print(dict)

# exit(0)
#人类出生点
hospital={'小树林', '鸟笼', '医院', '正门废墟', '木屋', '小门', '无敌废墟', '三板', '女神像'}
military_factory={'厂房', '备注：厂房外附近分布同，均匀分布正弧形', '备注：均匀分布中场反弧形', '木屋', '中场', '小门', '大门'}
mr={'人皇桥', '月亮河', '三连废墟', '二站台', '马戏团', '三站台', '双滑梯', '鬼屋废墟', '鬼屋', '终点站', '好木马', '坏木马', '鬼屋桥'}
rc={'木屋', '大门', '红地毯', '小门废墟', '墓地废墟', '大推', '教堂', '小推', '墓地', '中推'}
v={'大船', '船尾', '海边废墟', '厕所', '船头', '木屋废墟', '木屋', '玉米地', '小船', '大门废墟', '双十一', '中场'}
rio={'两车', '月亮门废墟', '木屋', '大房角落', '油罐', '大门', '楼梯', '雪人', '南门', '中场', '两板一窗', '大房', '月亮门', '集装箱', '圣诞树'}
town={'红蝶楼', '一版一窗', '二站', '四站房', '大门废墟', '三板废墟', '三站', '人皇机', '墓地', '饰伞屋', '红蝶桥', ' 湖边两板一窗', '湖边废墟', '假门房', '居酒屋'}
cs={'裁缝铺', '花店', '古树', '关公像', '剧场', '狮子楼', '酒楼', '洗浴', '烧饼铺', '雨伞门', '一窗一板', '醉芳庭', '御景轩'}

import os,pinyin
# maps="军工厂,红教堂,圣心医院,湖景村,月亮河,冰工厂,永眠镇"
# # en=["military_factory","red_church","hospital","village","moon_river","rio_memory","town"]
# en=["military_factory","red_church","hospital","village","moon_river"]
en=["rio_memory","town","chinese_street"]
# m=maps.split(",")
# # w="village"

# for w in en:
#     d=getattr(data,w)
#     print("public static final String[] {}_cn={{{}}};".format(w,d.keys()))
    
# en=["rio_memory","town","chinese_street"]

# for w in en:
#     d=getattr(data,w)
#     print("public static final String[] {}={{{}}};".format(w,list(map(lambda x:pinyin.get(x,format="strip"),d.keys()))))
# for w in en:
#     d=getattr(data,w)
#     for i in d.keys():
#         v=d[i]
#         print("public static final String [] {}_{}={{ {} }}".format(w,pinyin.get(i,format="strip"),v))
# p=r"D:\workplace\funes_\360FloatWindowDemo\app\src\main\assets\dwrg_maps\town"
# dir=os.listdir(p)
# for f in dir:
#     os.rename(p+"\\"+f,p+"\\"+pinyin.get(f,format="strip"))


n=139
count=0
print("""<TableLayout
    android:id="@+id/rio_memory_killer"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:visibility="gone">""")
print(""" <TableRow
            android:layout_width="match_parent"
            android:layout_height="match_parent" >""")
for i in data.rio_memory.keys():
# for i in cs:
    print("""<CheckBox
                android:id="@+id/checkBox{}"
                android:layout_width="match_parent"
                android:layout_height="wrap_content"
                android:text="{}"
                android:tag="{}" />""".format(n,i,pinyin.get(i,format="strip")))
    count+=1
    if count % 4 ==0:
        print(r"""</TableRow>
        <TableRow
            android:layout_width="match_parent"
            android:layout_height="match_parent">
        
        """)
    n+=1
print(r"</TableRow>")
print("</TableLayout>")
print(n)


# a=[]
# for i in data.chinese_street.values():
#     a=a+i
# print(set(a))
# b=[]
# for j in data.red_church.values():
#     b=b+j
# print(set(b))
# print(data.hospital.keys())



