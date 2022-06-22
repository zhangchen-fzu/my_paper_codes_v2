##对还原之后的文本首加空格
# import os
# subdirs = os.walk(r'D:\my paper xiugai\shiyan\小文本的还原\4huanyuan_result')   # os.walk读取每个子目录下的文件
# for d, s, fns in subdirs:
#     for fn in fns:
#         with open(r'D:\my paper xiugai\shiyan\小文本的还原\5huanyuanadd_space\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#             with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                 for eachline in p:
#                     eachline=eachline.strip()
#                     f2.write(' '+eachline+'\n')
#
# print("完成！")

##大文本加space
# with open(r'D:\my paper xiugai\es背景语料库\8final_huanyuan_rusult.txt','r',encoding='utf-8') as f1:
#     with open(r'D:\my paper xiugai\es背景语料库\9add_space.txt','w',encoding='utf-8') as f2:
#         for eachline in f1:
#             eachline=eachline.strip()
#             f2.write(' '+eachline+'\n')