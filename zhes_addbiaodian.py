##zh预处理：为每行后面添加标点（软换行符可能会导致一行接一行的连接）
# import os
# import pynlpir
# pynlpir.open()
# subdirs = os.walk(r'D:\my paper xiugai\3es人名圈小a的处理\zh')   # os.walk读取每个子目录下的文件
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\4zhes加标点\zh\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         eachline=eachline.strip()
#                         word=[]
#                         a = pynlpir.segment(eachline, pos_english=False, pos_names='child')
#                         for i in a:
#                             word.append(i[0])
#                         if word[-1]=='。' or word[-1]=='，' or word[-1]=='？' or word[-1]=='！' or word[-1]=='；' or word[-1]=='：':
#                             f2.write(eachline+'\n')
#                         else:
#                             f2.write(eachline+'。'+'\n')
# print("标点添加完毕！")

# es预处理：为每行后面添加标点（软换行符可能会导致一行接一行的连接）
# import os
# import nltk
# subdirs = os.walk(r'D:\my paper xiugai\3es人名圈小a的处理\32es圈小a')   # os.walk读取每个子目录下的文件
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\4zhes加标点\es\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         eachline=eachline.strip()
#                         a=nltk.word_tokenize(eachline)
#                         if a[-1]=='.' or a[-1]=='?' or a[-1]==';' or a[-1]==':' or a[-1]==',' or a[-1]=='!':
#                             f2.write(eachline+'\n')
#                         else:
#                             f2.write(eachline+'.'+'\n')
# print("标点添加完毕！")


# es预处理：新的加标点方式，取词的时候要把“JUHAO”加到停用词中
# import os
# import nltk
# subdirs = os.walk(r'D:\my paper xiugai\es背景语料库\4es人名圈小a的处理\圈小a')   # os.walk读取每个子目录下的文件
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\es背景语料库\5es加标点\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         eachline=eachline.strip()
#                         f2.write(eachline+' JUHAO'+'\n')
# print("标点添加完毕！")


