# ##改进中文文本开头第一行的“联 合 国”问题！！
# import os
# subdirs = os.walk(r'D:\my paper xiugai\1去掉标题信息之后的语料\zh')
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\2es处理序号zh处理联合国\zh\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         eachline=eachline.strip()
#                         if eachline=="联 合 国":
#                             eachline='联合国'
#                             f2.write(eachline+'\n')
#                         else:
#                             f2.write(eachline+'\n')
# print("完成中文文本的改进")