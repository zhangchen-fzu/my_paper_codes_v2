#中文词语抽取
# import pynlpir
# # # from collections import Counter
# # # import re
# # # import pandas as pd
# # # # import itertools
# # # import os
# pynlpir.open()
# a=pynlpir.segment('威海市辖区',pos_english=False,pos_names='child')
# for i in a:
#     print(i)
#
# import jieba
# cut=jieba.cut('枣庄台儿庄区')
# a=[]
# for i in cut:
#     a.append(i)
# print(a)
# print(a)
# # # # print([i for i in cut])
# import treetaggerwrapper as tter
# tagger = tter.TreeTagger(TAGLANG='es')
# tags = tagger.tag_text("L' économie")
# tags2 = tter.make_tags(tags, allow_extra=True)
# print(tags2)
# # a=[]
# for i in tags2:
#     a.append(i[2])
# print(' '.join(a))
# # # # # poss=[]
# for i in tags2:
#     poss.append(i[1])
# print(poss)
# print(' '.join(poss))

# import treetaggerwrapper as tter
# tagger = tter.TreeTagger(TAGLANG='es')
# words=[]  ['con', 'durante', 'hasta', 'contra', 'en', 'sobre', 'por', 'sin', 'desde']
# with open(r'G:\my paper\esstoplist.txt',encoding='utf-8') as f:
#     for word in f:
#         word=word.strip()
#         # print(word)
#         tags = tagger.tag_text(word)
#         tags2 = tter.make_tags(tags, allow_extra=True)
#         # print(tags2)
#         for j in tags2:
#             if j[1]=='PREP':
#                 words.append(j[0])
# print(words)
# import re
# each_line='la delincuencia cibernética'
# each_line = re.sub(r"^la de\s", '',each_line)
# print(each_line)
# a='Adad'
# if ord('A') <= ord(a[0]) <= ord('Z'):
# #     print("首字母大写！")
# # with open(r'c:\Users\admin\Desktop\1.txt', 'w', encoding='utf-8') as f1:
# #     a=['ada','sd','\n','sfwea','weQ','\n','dwed','wefw']
# #     f1.write(' '.join(a))
# import re
# each_line1='de'
# each_line1 = re.sub("^de la\s", '', each_line1)
# each_line1 = re.sub("^la de\s", '', each_line1)
# each_line1 = re.sub("^el de\s", '', each_line1)
# each_line1 = re.sub("^de el\s", '', each_line1)
# each_line1 = re.sub("^la el\s", '', each_line1)
# each_line1 = re.sub("^el la\s", '', each_line1)
# each_line1 = re.sub("^De la\s", '', each_line1)
# each_line1 = re.sub("^La de\s", '', each_line1)
# each_line1 = re.sub("^El de\s", '', each_line1)
# each_line1 = re.sub("^De el\s", '', each_line1)
# each_line1 = re.sub("^La el\s", '', each_line1)
# each_line1 = re.sub("^El la\s", '', each_line1)
# each_line1 = re.sub("^de\s", '', each_line1)
# each_line1 = re.sub("^del\s", '', each_line1)
# each_line1 = re.sub("^en\s", '', each_line1)
# each_line1 = re.sub("^ser\s", '', each_line1)
# each_line1 = re.sub("^haber\s", '', each_line1)
# each_line1 = re.sub("^la\s", '', each_line1)
# each_line1 = re.sub("^el\s", '', each_line1)
# each_line1 = re.sub("^De\s", '', each_line1)
# each_line1 = re.sub("^Del\s", '', each_line1)
# each_line1 = re.sub("^En\s", '', each_line1)
# each_line1 = re.sub("^Ser\s", '', each_line1)
# each_line1 = re.sub("^Haber\s", '', each_line1)
# each_line1 = re.sub("^La\s", '', each_line1)
# each_line1 = re.sub("^El\s", '', each_line1)
#
# each_line1 = re.sub("\sde la$", '', each_line1)
# each_line1 = re.sub("\sla de$", '', each_line1)
# each_line1 = re.sub("\sel de$", '', each_line1)
# each_line1 = re.sub("\sde el$", '', each_line1)
# each_line1 = re.sub("\sla el$", '', each_line1)
# each_line1 = re.sub("\sel la$", '', each_line1)
# each_line1 = re.sub("\sDe la$", '', each_line1)
# each_line1 = re.sub("\sLa de$", '', each_line1)
# each_line1 = re.sub("\sEl de$", '', each_line1)
# each_line1 = re.sub("\sDe el$", '', each_line1)
# each_line1 = re.sub("\sLa el$", '', each_line1)
# each_line1 = re.sub("\sEl la$", '', each_line1)
# each_line1 = re.sub("\sde$", '', each_line1)
# each_line1 = re.sub("\sdel$", '', each_line1)
# each_line1 = re.sub("\sen$", '', each_line1)
# each_line1 = re.sub("\sser$", '', each_line1)
# each_line1 = re.sub("\shaber$", '', each_line1)
# each_line1 = re.sub("\sla$", '', each_line1)
# each_line1 = re.sub("\sel$", '', each_line1)
# each_line1 = re.sub("\sDe$", '', each_line1)
# each_line1 = re.sub("\sDel$", '', each_line1)
# each_line1 = re.sub("\sEn$", '', each_line1)
# each_line1 = re.sub("\sSer$", '', each_line1)
# each_line1 = re.sub("\sHaber$", '', each_line1)
# each_line1 = re.sub("\sLa$", '', each_line1)
# each_line1 = re.sub("\sEl$", '', each_line1)
# each_line1 = re.sub("^el$", '', each_line1)
# each_line1 = re.sub("^El$", '', each_line1)
# each_line1 = re.sub("^de$", '', each_line1)
# each_line1 = re.sub("^De$", '', each_line1)
# each_line1 = re.sub("^la$", '', each_line1)
# each_line1 = re.sub("^La$", '', each_line1)
# each_line1 = re.sub("^del$", '', each_line1)
# each_line1 = re.sub("^Del$", '', each_line1)
# each_line1 = re.sub("^en$", '', each_line1)
# each_line1 = re.sub("^En$", '', each_line1)
# print(each_line1)
# import nltk
# a='dkwd wrjfim efj, aweji wejieaw; aoeow weala.'
# b=nltk.word_tokenize(a)
# print(b)
# with open(r'D:\my paper xiugai\es\with_stopword_huanyuan.txt','r',encoding='utf-8') as f:
#     with open(r'D:\my paper xiugai\es\with_stopword_huanyuan1.txt','w',encoding='utf-8') as f1:
#         for i in f:
#             if i!='.'+'\n':
#                 f1.write(i)
# print("wancheng")
# with open(r'd:\my paper xiugai\es\with_stopword_huanyuan1.txt','r',encoding='utf-8') as f:
#     with open(r'd:\my paper xiugai\es\with_stopword_huanyuan2.txt','w', encoding='utf-8') as f2:
#         for i in f:
#             i=i.strip()
#             f2.write(' '+i+'\n')
# print("wancheng")pr
# a=16
# print()
# word=[]
# pos=[]
# huanyuan=[]
# with open(r'C:\Users\admin\Desktop\1.txt',encoding='utf-8') as f:
#     for i in f:
#         a=i.split()
#         print(a)
#         word.append(a[0])
#         pos.append(a[1])
#         if '|' in a[2]:
#             print(a[2][:a[2].find('|')])
# a=['dwd','qweq','weq']
# print(a[:-1])
# bb=['SJDW WAEHUWA WERAWK AWW']
# word_new=[]
# for i in range(len(bb)):
#     a=bb[i].split()
#     if a[0]!='PREP' and a[-1]!='PREP':
#         word_new.append(bb[i])
#     else:
#         if a[0]!='PREP' and a[-1]=='PREP':
#             word_new.append(a[:-1])
#         else:
#             if a[0]=='PREP' and a[-1]!='PREP':
#                 word_new.append(a[1:])
#             else:
#                 if a[0]=='PREP' and a[-1]=='PREP':
#                     word_new.append(a[1:-1])
# print(word_new)
# import pandas as pd
# a=[['tru','rtgtr','weq'],['q','jyg'],['eq']]
# b=[]
# for i in range(len(a)):
#     b.append(' '.join(a[i]))
# b=pd.DataFrame(b,columns=['term'])
# print(b)
# with open(r'd:\my paper xiugai\es1\with_stopword_huanyuan.txt','r') as f:
#     with open(r'd:\my paper xiugai\es1\with_stopword_huanyuan2.txt','w') as f2:
#         for eachline in f:
#             eachline=eachline.strip()
#             if eachline!='.':
#                 f2.write(eachline+'\n')

# stop=['c','cc','d','e','m','mq','o','q','qv','qt','r','rr','rz','rzt','rzs','rzv','ry','ryt','rys','ryv','rg','u','uzhe','ule','uguo','ude1',
#       'ude2','ude3','usuo','udeng','uyy','udh','uzhi','uls','ulian','w','wkz','wky','wyz','wyy','wj','ww','wt','wd','wf','wn','wm','ws','wp',
#       'wb','wh','x','xx','xu','y']
#['cc', 'd', 'e', 'm', 'mq', 'o', 'q', 'qv', 'qt', 'r', 'rr', 'rz', 'rzt', 'rzs', 'rzv', 'ry', 'ryt', 'rys', 'ryv', 'rg', 'u', 'uzhe', 'ule', 'uguo', 'ude1', 'ude2', 'ude3', 'usuo', 'udeng', 'uyy', 'udh', 'uls', 'uzhi', 'ulian', 'w', 'wkz', 'wky', 'wyz', 'wyy', 'wj', 'ww', 'wt', 'wd', 'wf', 'wn', 'wm', 'ws', 'wp', 'wb', 'wh', 'x', 'xx', 'xu', 'y']
#
# import pandas as pd
# data=pd.read_excel(r'D:\my paper xiugai\jieba_stopwords.xlsx',usecols=[0]).values.tolist()
# import itertools
# data=list(itertools.chain.from_iterable(data))
# print(data)
# import pandas as pd
# data=pd.read_excel(r'd:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq_frebig1_pos_delprep.xlsx')
# word=[]
# seg=[]
# for i in range(len(data)):
#     word.append(data['word'][i])
#     seg.append(data['word_seg'][i])
# word=pd.DataFrame(word,columns=['word'])
# seg=pd.DataFrame(seg,columns=['word_seg'])
# data1=pd.concat([word,seg],axis=1)
# data1.to_csv(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq_frebig1_pos_delprep.csv',index=False,encoding='utf-8')
# # import pandas as pd
# # import re
# # data=pd.read_csv(r'd:\my paper xiugai\es1\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela4.csv',encoding='utf-8')
# # for i in range(len(data)):
# #     data['term'][i] = re.sub("\stener$", '', str(data['term'][i]))
# #     data['term'][i] = re.sub("^tener\s", '', str(data['term'][i]))
# # data.to_csv(r'd:\my paper xiugai\es1\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela5.csv',index=False,encoding='utf-8')
# import re
# with open(r'D:\my paper xiugai\2es处理序号zh处理联合国\es\2012_td_b_ex_55__4.txt','r',encoding='utf-8') as f:
#     with open(r'D:\my paper xiugai\2es处理序号zh处理联合国\es\1.txt','w',encoding='utf-8') as f2:
#         for eachline in f:
#             eachline = eachline.strip()
#             if re.search("Sr. ", eachline) != None and re.search("Sra. ", eachline) == None:
#                 eachline = re.sub("Sr. ", 'Sr.', eachline)
#                 f2.write(eachline + '\n')
#             else:
#                 if re.search("Sr. ", eachline) == None and re.search("Sra. ", eachline) != None:
#                     eachline = re.sub("Sra. ", 'Sra.', eachline)
#                     f2.write(eachline + '\n')
#                 else:
#                     if re.search("Sr. ", eachline) != None and re.search("Sra. ", eachline) != None:
#                         eachline = re.sub("Sra. ", 'Sra.', eachline)
#                         eachline = re.sub("Sr. ", 'Sr.', eachline)
#                         f2.write(eachline + '\n')
#                     else:
#                         if re.search("Sr. ", eachline) == None and re.search("Sra. ", eachline) == None:
#                             eachline = eachline
# #                             f2.write(eachline + '\n')
# import nltk
# a='仅供参考。'
# b=nltk.word_tokenize(a)
# print(b)
# with open(r'D:\my paper xiugai\shiyan\all_es.txt','r',encoding='utf-8') as f:
#     with open(r'D:\my paper xiugai\shiyan\all_es_juhao.txt','w',encoding='utf-8') as f2:
#         for eachline in f:
#             eachline=eachline.strip()
#             f2.write(eachline+' JUHAO'+'\n')

# import os
# import re
# subdirs = os.walk(r'D:\my paper xiugai\shiyan\小文本的还原\3huanyuan_list')
# for q, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\shiyan\小文本的还原\4huanyuan_result\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f3:
#                 with open(q + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachword in p:
#                         d = eachword.strip().split()
#                         words_list1_pos = []
#                         if d[2] == '<unknown>' or d[2] == '@card@' or d[2] == '@ord@' or (ord('A') <= ord(d[0][0]) <= ord('Z')):  ##未识别或是句中首字母大写的词
#                             word_lemma = d[0]
#                             if d[0] != 'JUHAO':
#                                 f3.write(word_lemma + ' ')
#                             else:
#                                 f3.write('\n')
#                         else:
#                             if d[0] in ["el", "los", "El", "Los"]:
#                                 word_lemma = 'el'
#                                 if d[0] != 'JUHAO':
#                                     f3.write(word_lemma + ' ')
#                                 else:
#                                     f3.write('\n')
#                             else:
#                                 if d[0] in ["las", "la", "La", "Las"]:
#                                     word_lemma = 'la'
#                                     if d[0] != 'JUHAO':
#                                         f3.write(word_lemma + ' ')
#                                     else:
#                                         f3.write('\n')
#                                 else:
#                                     if '|' not in d[2]:
#                                         word_lemma = d[2]
#                                     else:
#                                         word_lemma = d[2][:d[2].find('|')]
#                                     if d[0] != 'JUHAO':
#                                         f3.write(word_lemma + ' ')
#                                     else:
#                                         f3.write('\n')
#

# words_list_pos = []
# words_list_huanyuan = []
# with open(r'D:\my paper xiugai\shiyan\tree_hy.txt',encoding='utf-8') as f:
#     with open(r'D:\my paper xiugai\shiyan\shiyan_result.txt', 'w', encoding='utf-8') as f3:
#         for eachword in f:
#             d=eachword.strip().split()
#             words_list1_pos = []
#             if d[2]== '<unknown>' or d[2] == '@card@' or d[2] == '@ord@' or (ord('A') <= ord(d[0][0]) <= ord('Z')): ##未识别或是句中首字母大写的词
#                 word_lemma = d[0]
#                 if d[0]!='JUHAO':
#                     f3.write(word_lemma+' ')
#                 else:
#                     f3.write(word_lemma+'\n')
#                 words_list_huanyuan.append(word_lemma)
#                 words_list_pos.append(d[1])
#             else:
#                 if d[0] in ["el", "los","El","Los"]:
#                     word_lemma = 'el'
#                     if d[0] != 'JUHAO':
#                         f3.write( word_lemma + ' ')
#                     else:
#                         f3.write(word_lemma + '\n')
#                     words_list_huanyuan.append(word_lemma)
#                     words_list_pos.append(d[1])
#                 else:
#                     if d[0] in ["las", "la","La","Las"]:
#                         word_lemma = 'la'
#                         if d[0] != 'JUHAO':
#                             f3.write( word_lemma + ' ')
#                         else:
#                             f3.write( word_lemma + '\n')
#                         words_list_huanyuan.append(word_lemma)
#                         words_list_pos.append(d[1])
#                     else:
#                         if '|' not in d[2]:
#                             word_lemma = d[2]
#                         else:
#                             word_lemma=d[2][:d[2].find('|')]
#                         if d[0] != 'JUHAO':
#                             f3.write(word_lemma + ' ')
#                         else:
#                             f3.write(word_lemma + '\n')
#                         words_list_huanyuan.append(word_lemma)
#                         words_list_pos.append(d[1])

# with open(r'D:\my paper xiugai\shiyan\shiyan_result.txt','r',encoding='utf-8') as f:
#     with open(r'D:\my paper xiugai\shiyan\shiyan_result_finall.txt','w',encoding='utf-8') as f2:
#         for eachline in f:
#             eachline=eachline.strip()
#             a=eachline.split()
#             b=' '.join(a[:-1])
#             f2.write(b+'\n')

# import os
# subdirs = os.walk(r'D:\my paper xiugai\shiyan\小文本的还原\es')   # os.walk读取每个子目录下的文件
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             with open(r'D:\my paper xiugai\shiyan\小文本的还原\add_juhao\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f2:
#                 with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                     for eachline in p:
#                         eachline=eachline.strip()
#                         f2.write(eachline+' JUHAO'+'\n')
# import pandas as pd
# import re
# data4=pd.read_excel(r'C:\Users\admin\Desktop\1.xlsx')
# print(data4)
# index=[]
# for i in range(len(data4)):
#     word=data4['term'][i].split()
#     if word[0]=='de':
#         index.append(i)
# data4=data4.drop(index)
# print(data4)
# import math
# print(math.log(5/0))
# a=[[[1,2,3],[4,5,6]]]
# import itertools
# b=list(itertools.chain.from_iterable(a))
# # print(b)
#
# a=['dw','qweq','qaweq','wqeq']
# for i in range(len(a)):
#     if i<2:
#         print("1",a[i])
#     else:
#         print("2",a[i])

##将trans分离
# import pandas as pd
# data1=pd.read_csv(r'D:\my paper xiugai\验证集\val_token_bigtsmall.csv',encoding='utf-8')
# zh_word=[]
# es_word=[]
# biaoqian=[]
# for i in range(len(data1)):
#     zh_word.append(data1['zh_term'][i])
#     es_word.append(data1['es_term'][i])
#     biaoqian.append(data1['biaoqian'][i])
# zh_word=pd.DataFrame(zh_word,columns=['zh_term'])
# es_word=pd.DataFrame(es_word,columns=['es_term'])
# biaoqian=pd.DataFrame(biaoqian,columns=['biaoqian'])
# data2=pd.concat([zh_word,es_word,biaoqian],axis=1)
# data2.to_csv(r'D:\my paper xiugai\验证集\分成多个xlsx\all.csv',index=False,encoding='utf-8')

# import pandas as pd
# import itertools
# data1=pd.read_csv(r'D:\my paper xiugai\candidate_termpair_rank_quchong.csv',encoding='utf-8',usecols=[0]).values.tolist()
# word1=list(set(list(itertools.chain.from_iterable(data1)))) ##自己的验证集和测试集
#
# data2=pd.read_excel(r'D:\my paper xiugai\训练集\联合国语料库改删排筛负随机tas.xlsx',usecols=[0]).values.tolist()
# word2=list(set(list(itertools.chain.from_iterable(data2))))##学姐的数据用来当训练集
# new_word2=[]
# for i in range(len(word2)):
#     new_word2.append(''.join(word2[i].split()))
# print(len(new_word2))
# a=[]
# for i in range(len(new_word2)):
#     if new_word2[i] not in word1:
#         a.append(new_word2[i])
# print(len(a))

# import pandas as pd
# import treetaggerwrapper as tter
# tagger = tter.TreeTagger(TAGLANG='es')
# data=pd.read_excel(r'D:\my paper xiugai\训练集\联合国语料库改删排筛负随机tas.xlsx')
# huanyuan=[]
# for i in range(len(data)):
#     print(i)
#     a=[]
#     tags = tagger.tag_text(data['es_term'][i])
#     tags2 = tter.make_tags(tags, allow_extra=True)
#     for d in tags2:
#         if d[2]== '<unknown>' or d[2] == '@card@' or d[2] == '@ord@':
#             a.append(d[0])
#         else:
#             a.append(d[2])
#     huanyuan.append(' '.join(a))
# huanyuan=pd.DataFrame(huanyuan,columns=['huanyuan'])
# data1=pd.concat([data,huanyuan],axis=1)
# data1.to_csv(r'D:\my paper xiugai\训练集\huanyuan.csv',index=False,encoding='utf-8')
#
# import pandas as pd
# data=pd.read_excel(r'D:\my paper xiugai\训练集\train_huanyuan.xlsx')
# data=data.drop_duplicates()
# data.to_csv(r'D:\my paper xiugai\训练集\train_huanyuan_quhong.csv',index=False,encoding='utf-8')

# import numpy as np
# initializer = np.random.uniform(-0.2, 0.2)
# a=np.array([initializer]*3)
# print(a)

# a={'sd':[1,2,3],'ad':[4,5,6]}
# with open(r'C:\Users\admin\Desktop\1.txt','w') as p:
#     for i in a:
#         i=i.strip()
#         p.write(i+' ')
#         for j in range(len(a[i])):
#             if j!=2:
#                 p.write(str(a[i][j])+' ')
#             else:
#                 p.write(str(a[i][j])+'\n')
# a=[1,45,2131,12,0]
# b=min(a)
# if b+1 in a and b+2 in a:
#     print("1")
# else:
#     print("0")
# a=[1,2,3,1]
# print(a.count(1))
# a={'sd':'wd','wd':'dwq'}
# # print(a['wd'])
# import numpy as np
# a=[1,3,4,2,7,5]
# a=np.array(a)
# b=np.argsort(a)
# print(b)
# c = b.index(2)
# print(c)
# print(a[c])

# import numpy as np
# import pandas as pd
# import itertools
# ##统计城市信息,找出最大的来补充缺失值
# city=pd.read_csv(r'd:\数据城堡大赛\A榜给选手数据\中间结果\山东省经纬度信息及缺失值补充.csv',usecols=[0]).values.tolist()
# city=list(set(list(itertools.chain.from_iterable(city))))
# lgtd_latd_info=pd.read_csv(r'd:\数据城堡大赛\A榜给选手数据\中间结果\山东省经纬度信息及缺失值补充.csv')
# month_city_max={}
# lastmonth_city_max={}
# for i in range(len(city)):
#     city_info=lgtd_latd_info[lgtd_latd_info.city_info==city[i]]
#     city_info1 = city_info.reset_index()
#     city_info1 = city_info1.drop(columns='index')
#     resid_info=[]
#     lastresid_info=[]
#     for j in range(len(city_info1)):
#         resid_info.append(int(city_info1['month_resid_info'][j]))
#         lastresid_info.append(int(city_info1['lastmonth_resid_info'][j]))
#     max1_index=resid_info.index(max(resid_info))
#     max2_index=lastresid_info.index(max(lastresid_info))
#     if city_info1['qu'][max1_index]=='市辖区':
#         resid_info1=list(np.argsort(resid_info))
#         b=resid_info1[-2]
#         month_city_max[city_info1['city_info'][b]] = city_info1['qu'][b]
#     else:
#         month_city_max[city_info1['city_info'][max1_index]] = city_info1['qu'][max1_index]
#     if city_info1['qu'][max2_index]=='市辖区':
#         lastresid_info1=list(np.argsort(lastresid_info))
#         c = lastresid_info1[-2]
#         lastmonth_city_max[city_info1['city_info'][c]] = city_info1['qu'][c]
#     else:
#         lastmonth_city_max[city_info1['city_info'][max2_index]] = city_info1['qu'][max2_index]
# print(month_city_max)
# print(lastmonth_city_max)
# import pandas as pd
# def get_city_value(bb):
#     value_info = pd.read_csv(r'd:\数据城堡大赛\A榜给选手数据\中间结果\山东省经纬度信息及缺失值补充.csv')
#     lgtd=[]
#     latd=[]
#     for i in range(len(bb)):
#         for j in range(len(value_info)):
#             if bb[i]==value_info['city'][j]:
#                 lgtd.append(value_info['longitude'][j])
#                 latd.append(value_info['latitude'][j])
#     return lgtd,latd
# bb=['德州','济南历下区']
# cc,dd=get_city_value(bb)
# print(cc,dd)
# import pandas as pd
# import itertools
# data=pd.read_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result.csv')
# label=[]
# for i in range(len(data)):
#     label.append(data['label'][i])
# label=pd.DataFrame(label,columns=['label'])
# data1=pd.read_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result.csv')
# data1.drop('label',axis=1, inplace=True)
# data2=pd.concat([data1,label],axis=1)
# data2.to_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result1.csv',index=False,encoding='utf-8')
# import pandas as pd
# data = pd.read_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result2.csv', header=None)
# X = data.iloc[:, 3:20]  ##0-10列为特征
# Y = data.iloc[:, 21]  ##第11列为标签
# print(type(Y))
# print(X,Y)
# import pandas as pd
# data=pd.read_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result1.csv')
# data[['time_feature', 'city_info','resident_month_info','resident_lastmonth_info','x5','x6','label']] = \
#     data[['time_feature', 'city_info','resident_month_info','resident_lastmonth_info','x5','x6','label']].astype(int)
# data[['loaction_longitudes', 'location_latitudes','datausage_month','datausage_lastmonth','x7','x8','x9','x10','x11','x12','x13','x14']] = \
#     data[['loaction_longitudes', 'location_latitudes','datausage_month','datausage_lastmonth','x7','x8','x9','x10','x11','x12','x13','x14']].astype(float)
# # data.to_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result2.csv',index=False,encoding='utf-8')
# data=pd.read_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result2.csv')
# for i in range(1,2):
#     print(type(data['time_feature'][i]))
#     print(type(data['city_info'][i]))
#     print(type(data['resident_month_info'][i]))
#     print(type(data['resident_lastmonth_info'][i]))
#     print(type(data['x5'][i]))
#     print(type(data['x6'][i]))
#     print(type(data['label'][i]))
#     print(type(data['loaction_longitudes'][i]))
#     print(type(data['location_latitudes'][i]))
#     print(type(data['datausage_month'][i]))
#     print(type(data['datausage_lastmonth'][i]))
#     print(type(data['x7'][i]))
#     print(type(data['x8'][i]))
#     print(type(data['x9'][i]))
#     print(type(data['x10'][i]))
#     print(type(data['x11'][i]))
#     print(type(data['x12'][i]))
#     print(type(data['x13'][i]))
#     print(type(data['x14'][i]))
# import pandas as pd
# import itertools
# data=pd.read_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result.csv')
# data1=pd.read_csv(r'D:\数据城堡大赛\A榜给选手数据\train_label.csv')
# label=[]
# for i in range(len(data1)):
#     label.append(data1['label'][i])
# label=pd.DataFrame(label,columns=['label'],dtype='int64')
# data2=pd.concat([data,label],axis=1)
# data2.to_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result1.csv',index=False,encoding='utf-8')
# # import numpy as np
# # data=pd.read_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result11.csv')
# # print(data)
# # x=data[['label','location_latitudes']]
# # x=np.array(x)
# # print(x)
# # print(type(x))
# b=[]
# a=20200523090003
# b.append(int(str(a)[8:12]))
# print(b)
# import pandas as pd
# # data=pd.read_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result1.csv')
# # # data1=data[['time_feature','num_09_17','yon_except_09_17','hour_id_min','hour_id_max','loaction_longitudes','location_latitudes',
# # #             'loact_multi','medio_latitude_diff_guiyi','city_info','resident_month_info','datausage_month','x13','x14',
# # #             'x3_x4_value_latd','city_multi','lastmonth_multi','label']]
# # # data1.to_csv(r'D:\数据城堡大赛\A榜给选手数据\中间结果\feature_result2.csv',index=False,encoding='utf-8')
# #
# # print(data.dtypes)
# data=pd.read_excel(r'C:\Users\admin\Desktop\2.xlsx')
# sub_data=data[['day_id']]
# sub_data1 = sub_data.drop_duplicates()
# print(len(sub_data1))
# import jieba
# a=[1,2,3]
# print(a[-1])
# import pandas as pd
# import itertools
# data=pd.read_csv(r'D:\法语处理\有or没有翻译筛选\candidate_zhfr_termpair_quchong_label_small_token.csv')
# res=pd.read_csv(r'D:\法语处理\有or没有翻译筛选\cosine.csv')
# data1=pd.concat([data,res],axis=1)
# data1.to_csv(r'D:\法语处理\有or没有翻译筛选\candidate_zhfr_termpair_quchong_label_small_token_cos.csv',index=False,encoding='utf-8')

# ##
# import pandas as pd
# data=pd.read_csv(r'D:\数据城堡大赛\B榜给选手数据\submit_B.csv')
# data_sub=data[['id']]
# data1=pd.read_csv(r'D:\数据城堡大赛\result.csv')
# new=pd.concat([data_sub,data1],axis=1)
# # new.to_csv(r'D:\数据城堡大赛\\submit_B1.csv',index=False,encoding='utf-8')
#
#
# def reOrderArray(array):
#     # write code here
#     if array == []:
#         return []
#     indx = -1
#     for i in range(len(array)):
#         if array[i] % 2 == 0:
#             indx = i
#             break
#     if indx == -1:
#         return array
#     indx1=indx
#     for j in range(indx, len(array)):
#         if array[j] % 2 != 0:
#             tmp = array[j]
#             for k in range(j, indx1, -1):
#                 array[k] = array[k - 1]
#             array[indx1] = tmp
#             indx1 += 1
#     return array
#
# a=reOrderArray([1,2,3,4,5,6,7])
# # print(a)
# indx=-1
# indx1=indx
# indx+=1
# print(indx)
# for k in range(4,2,-1):
#     print(k)
# def reOrderArray( array):
#     # write code here
#     odd_count = -1
#     for i in range(len(array)):
#         if array[i] % 2 != 0:
#             odd_count += 1
#             if i > 0:
#                 temp = array[i]
#                 for k in range(i, odd_count, -1):
#                     array[k] = array[k - 1]
#                 array[odd_count] = temp
#     return array
# print(reOrderArray([1,2,3,4,5,6,7]))
# import math
# print(int(math.sqrt(15)))
#
# sequence=[7,4,6,5]
# root=sequence[-1]
# # print(root)
# left=[]
# right=[]
# res=True
# for i in range(len(sequence)):
#     if sequence[i]<root:
#         left.append(sequence[i])
#     elif sequence[i]>root:
#         right=sequence[i:-1]
#         break
# for val in right:
#     if val<root:
#         res=False
#         break
# print(left,right)
# print(res)
# a=['a','c']
# print(''.join(a))
# n=1
# high=n//10

# low=0
# cur=high%10
# cou=0
# base=1
# print(high,cur)
# while cur or high:
#     if cur==0:
#         cou+=high*base
#     elif cur==1:
#         cou+=((high*10)+(low+1))
#     else:
#         cou+=(high+1)*10
#     low = (base * cur) + low
#     cur = high % 10
#     high = high / 10
#     base = base * 10
# print(cou)
#
# numbers=[3,48,12,1]
# for i in range(len(numbers)):
#     for j in range(i+1,len(numbers)):
#         print(numbers[i])
#         str1=str(numbers[i])+str(numbers[j])
#         str2=str(numbers[j])+str(numbers[i])
#         if int(str2)<int(str1):
#             numbers[i],numbers[j]=numbers[j],numbers[i]
#             print(numbers)
# a=" "
# b=a.split(' ')
# print(b)
# print(' '.join(b[::-1]))
# print(2 and 1)