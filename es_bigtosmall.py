# # es开头的序号删掉
# import os
# import re
# subdirs = os.walk(r'D:\my paper xiugai\es背景语料库\2去掉标题信息之后的语料')
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\es背景语料库\3es处理序号\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         word=eachline.split()
#                         words=[]
#                         for i in range(len(word)):
#                             if i==0:
#                                 # print(word[i])
#                                 if re.search("^\d+\.", word[0]) ==None and re.search("^[a-zA-Z]\)", word[0]) ==None and re.search("^[i]*\.",word[0])==None and re.search("^[I]*\.",word[0])==None and re.search("^IV\.",word[0])==None and re.search("^[a-zA-Z]\.", word[0]) ==None and re.search("^V\.",word[0])==None and re.search('^[i]*\)',word[0])==None:
#                                     words.append(word[0])
#                             else:
#                                 words.append(word[i])
#                         line=' '.join(words)
#                         if line:
#                             # print(line)
#                             f2.write(line+'\n')
# print("完成")

# #一句话开头的字符串大写变小写,要想让所有的开头字母由大写变成小写的前提是把西语所有的开头序号去掉
# import os
# import re
# subdirs = os.walk(r'D:\my paper xiugai\es背景语料库\5es加标点')
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\es背景语料库\6大变小\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         word=eachline.split()
#                         words=[]
#                         for i in range(len(word)):
#                             if i==0:
#                                 words.append(word[i].lower())
#                             else:
#                                 words.append(word[i])
#                         line=' '.join(words)
#                         f2.write(line+'\n')
# print("完成")

##还原文本的形成
# import os
# import re
# with open(r'D:\my paper xiugai\es背景语料库\tree_back_huanyuan.txt',encoding='utf-8') as f:
#     with open(r'D:\my paper xiugai\es背景语料库\final_huanyuan_rusult.txt', 'w', encoding='utf-8') as f3:
#         for eachword in f:
#             d=eachword.strip().split()
#             words_list1_pos = []
#             if d[2]== '<unknown>' or d[2] == '@card@' or d[2] == '@ord@' or (ord('A') <= ord(d[0][0]) <= ord('Z')): ##未识别或是句中首字母大写的词
#                 word_lemma = d[0]
#                 if d[0]!='JUHAO':
#                     f3.write(word_lemma+' ')
#                 else:
#                     f3.write('\n')
#             else:
#                 if d[0] in ["el", "los","El","Los"]:
#                     word_lemma = 'el'
#                     if d[0] != 'JUHAO':
#                         f3.write( word_lemma + ' ')
#                     else:
#                         f3.write('\n')
#                 else:
#                     if d[0] in ["las", "la","La","Las"]:
#                         word_lemma = 'la'
#                         if d[0] != 'JUHAO':
#                             f3.write( word_lemma + ' ')
#                         else:
#                             f3.write('\n')
#                     else:
#                         if '|' not in d[2]:
#                             word_lemma = d[2]
#                         else:
#                             word_lemma=d[2][:d[2].find('|')]
#                         if d[0] != 'JUHAO':
#                             f3.write(word_lemma + ' ')
#                         else:
#                             f3.write('\n')
