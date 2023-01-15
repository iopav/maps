# input="""
# 大推
# 小推 中推 教堂 红地毯
# 红地毯左
# 中推 小推 教堂 墓地
# 教堂内
# 木屋 小门废墟 墓地废墟 大推
# 墓地地窖点
# 大推 教堂 木屋 墓地废墟
# 墓地靠教堂
# 小门废墟 木屋 小推 大推
# 墓地椅子旁
# 小门废墟 墓地废墟 教堂 大门
# """
# dict={}
# input1=list(filter(None,input.split("\n")))
# # print(input1)
# for i in range(0,len(input1),2):
#     dict[input1[i]]=input1[i+1].split(" ")
# print(dict)

# exit(0)
#hospital
#{'小树林', '鸟笼', '医院', '正门废墟', '木屋', '小门', '无敌废墟', '三板', '女神像'}
#military factory
#{'厂房', '备注：厂房外附近分布同，均匀分布正弧形', '备注：均匀分布中场反弧形', '木屋', '中场', '小门', '大门'}
#mr
# {'人皇桥', '', '月亮河', '三连废墟', '二站台', '马戏团', '三站台', '双滑梯', '鬼屋废墟', '鬼屋', '终点站', '好木马', '坏木马', '鬼屋桥'}
#rc
# {'木屋', '大门', '红地毯', '小门废墟', '墓地废墟', '大推', '教堂', '小推', '墓地', '中推'}
#v
# {'大船', '船尾', '海边废墟', '厕所', '船头', '木屋废墟', '木屋', '玉米地', '小船', '大门废墟', '双十一', '中场'}
import data
# a=[]
# for i in data.village.values():
#     a=a+i
# print(set(a))
# b=[]
# # for j in data.red_church.values():
# #     b=b+j
# # print(set(b))
print(data.hospital.keys())


