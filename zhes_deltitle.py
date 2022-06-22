##zh预处理：删除中问前6行联合国套话
# import os
# subdirs = os.walk(r'D:\my paper xiugai\原版本200篇语料\zh_text')   # os.walk读取每个子目录下的文件
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\1去掉标题信息之后的语料\zh\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     text=[]
#                     for eachline in p:
#                         text.append(eachline)
#                     for i in range(len(text)):
#                         if i!=1 and i!=2 and i!=3 and i!=4 and i!=5:
#                             f2.write(text[i])
# print("无法对齐的题目已删除完毕！")

##es预处理：删除中问前6行联合国套话
# import os
# subdirs = os.walk(r'D:\my paper xiugai\es背景语料库\1yuan_es')   # os.walk读取每个子目录下的文件
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\es背景语料库\2去掉标题信息之后的语料\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     text=[]
#                     for eachline in p:
#                         text.append(eachline)
#                     for i in range(len(text)):
#                         if i!=1 and i!=2 and i!=3 and i!=4 and i!=5:
#                             f2.write(text[i])
# print("无法对齐的题目已删除完毕！")