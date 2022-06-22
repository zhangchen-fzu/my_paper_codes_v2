import treetaggerwrapper as tter
import pandas as pd
import re
import os
from collections import Counter
import numpy as np

# 加载停用词、停用词性表
tagger = tter.TreeTagger(TAGLANG='es')
word_dict = {}
stop_words = set([line.strip() for line in open(r'G:\my paper\esstoplist.txt',encoding='utf-8').readlines()])
pos_deleted = set(['ALFP', 'ALFS', 'BACKSLASH', 'CC', 'CCAD', 'CCNEG', 'CM', 'CODE','COLON', 'CQUE', 'CSUBF', 'CSUBI', 'CSUBX', 'DASH', 'DM', 'DOTS', 'FO', 'INT', 'ITJN', 'LP', 'ORD', 'PERCT', 'PPC', 'PPO', 'PPX',  'QT', 'QU', 'REL', 'RP', 'SE', 'SEMICOLON', 'SLASH', 'SYM', 'UMMX', 'CARD', 'FS'])  # 根据停用词性表，删除无用原子词
#词性标注+词形还原
# words_list_pos = []
# words_list_huanyuan = []
# with open(r'D:\my paper xiugai\es\tree_huanyuan.txt',encoding='utf-8') as f:
#     with open(r'D:\my paper xiugai\es\with_stopword_huanyuan.txt', 'w', encoding='utf-8') as f3:
#         for eachword in f:
#             d=eachword.strip().split()
#             words_list1_pos = []
#             if d[2]== '<unknown>' or d[2] == '@card@' or d[2] == '@ord@' or (ord('A') <= ord(d[0][0]) <= ord('Z')): ##未识别或是句中首字母大写的词
#                 word_lemma = d[0]
#                 if d[0]!='.':
#                     f3.write(word_lemma+' ')
#                 else:
#                     f3.write(word_lemma+'\n')
#                 words_list_huanyuan.append(word_lemma)
#                 words_list_pos.append(d[1])
#             else:
#                 if d[0] in ["el", "los","El","Los"]:
#                     word_lemma = 'el'
#                     if d[0] != '.':
#                         f3.write( word_lemma + ' ')
#                     else:
#                         f3.write(word_lemma + '\n')
#                     words_list_huanyuan.append(word_lemma)
#                     words_list_pos.append(d[1])
#                 else:
#                     if d[0] in ["las", "la","La","Las"]:
#                         word_lemma = 'la'
#                         if d[0] != '.':
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
#                         if d[0] != '.':
#                             f3.write(word_lemma + ' ')
#                         else:
#                             f3.write(word_lemma + '\n')
#                         words_list_huanyuan.append(word_lemma)
#                         words_list_pos.append(d[1])
# with open(r'D:\my paper xiugai\es\without_stopword_huanyuan.txt', 'w', encoding='utf-8') as f1:
#     words_list_without_stopwords=[]
#     df = {"term": words_list_huanyuan, "pos": words_list_pos}
#     words_pos_DF = pd.DataFrame(df)
#     for i in range(0, len(words_pos_DF)):
#         if words_pos_DF['term'][i] in stop_words or words_pos_DF['pos'][i] in pos_deleted:
#             words_list_without_stopwords.append('\n')
#         else:
#             words_list_without_stopwords.append(words_pos_DF['term'][i])
#     f1.write(' '.join(words_list_without_stopwords))


# # #在去停用词之后的串中删除de、la等开头和结尾的,提前去掉，为了避免原子词步长法提取出更多的以他们开头和结尾的词语
# with open(r'D:\my paper xiugai\es\without_stopword_huanyuan.txt','r', encoding='utf-8') as f1:
#     with open(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela.txt','w', encoding='utf-8') as fn:
#         for each_line1 in f1:
#             each_line1=each_line1.strip()
#             each_line1 = re.sub("^haber de ser\s", '', each_line1)
#             each_line1 = re.sub("^en la\s", '', each_line1)
#             each_line1 = re.sub("^en el\s", '', each_line1)
#             each_line1 = re.sub("^de la\s", '', each_line1)
#             each_line1 = re.sub("^la de\s", '', each_line1)
#             each_line1 = re.sub("^el de\s", '', each_line1)
#             each_line1 = re.sub("^de el\s", '', each_line1)
#             each_line1 = re.sub("^la el\s", '', each_line1)
#             each_line1 = re.sub("^el la\s", '', each_line1)
#             each_line1 = re.sub("^De la\s", '', each_line1)
#             each_line1 = re.sub("^La de\s", '', each_line1)
#             each_line1 = re.sub("^El de\s", '', each_line1)
#             each_line1 = re.sub("^De el\s", '', each_line1)
#             each_line1 = re.sub("^La el\s", '', each_line1)
#             each_line1 = re.sub("^El la\s", '', each_line1)
#             each_line1 = re.sub("^De\s", '', each_line1)
#             each_line1 = re.sub("^Del\s", '', each_line1)
#             each_line1 = re.sub("^En\s", '', each_line1)
#             each_line1 = re.sub("^Haber\s", '', each_line1)
#             each_line1 = re.sub("^Ser\s", '', each_line1)
#             each_line1 = re.sub("^La\s", '', each_line1)
#             each_line1 = re.sub("^El\s", '', each_line1)
#             each_line1 = re.sub("^de\s", '', each_line1)
#             each_line1 = re.sub("^del\s", '', each_line1)
#             each_line1 = re.sub("^en\s", '', each_line1)
#             each_line1 = re.sub("^haber\s", '', each_line1)
#             each_line1 = re.sub("^ser\s", '', each_line1)
#             each_line1 = re.sub("^la\s", '', each_line1)
#             each_line1 = re.sub("^el\s", '', each_line1)
#             each_line1 = re.sub("\shaber ser$", '', each_line1)
#             each_line1 = re.sub("\sde la$", '', each_line1)
#             each_line1 = re.sub("\sla de$", '', each_line1)
#             each_line1 = re.sub("\sel de$", '', each_line1)
#             each_line1 = re.sub("\sde el$", '', each_line1)
#             each_line1 = re.sub("\sla el$", '', each_line1)
#             each_line1 = re.sub("\sel la$", '', each_line1)
#             each_line1 = re.sub("\sen la$", '', each_line1)
#             each_line1 = re.sub("\sDe la$", '', each_line1)
#             each_line1 = re.sub("\sLa de$", '', each_line1)
#             each_line1 = re.sub("\sEl de$", '', each_line1)
#             each_line1 = re.sub("\sDe el$", '', each_line1)
#             each_line1 = re.sub("\sLa el$", '', each_line1)
#             each_line1 = re.sub("\sEl la$", '', each_line1)
#             each_line1 = re.sub("\sDe$", '', each_line1)
#             each_line1 = re.sub("\sDel$", '', each_line1)
#             each_line1 = re.sub("\sEn$", '', each_line1)
#             each_line1 = re.sub("\sSer$", '', each_line1)
#             each_line1 = re.sub("\sHaber$", '', each_line1)
#             each_line1 = re.sub("\sLa$", '', each_line1)
#             each_line1 = re.sub("\sEl$", '', each_line1)
#             each_line1 = re.sub("\sde$", '', each_line1)
#             each_line1 = re.sub("\sdel$", '', each_line1)
#             each_line1 = re.sub("\sen$", '', each_line1)
#             each_line1 = re.sub("\sser$", '', each_line1)
#             each_line1 = re.sub("\shaber$", '', each_line1)
#             each_line1 = re.sub("\sla$", '', each_line1)
#             each_line1 = re.sub("\sel$", '', each_line1)
#             each_line1 = re.sub("^el$", '', each_line1)
#             each_line1 = re.sub("^El$", '', each_line1)
#             each_line1 = re.sub("^de$", '', each_line1)
#             each_line1 = re.sub("^De$", '', each_line1)
#             each_line1 = re.sub("^la$", '', each_line1)
#             each_line1 = re.sub("^La$", '', each_line1)
#             each_line1 = re.sub("^del$", '', each_line1)
#             each_line1 = re.sub("^Del$", '', each_line1)
#             each_line1 = re.sub("^en$", '', each_line1)
#             each_line1 = re.sub("^En$", '', each_line1)
#             each_line1 = re.sub("^haber de ser$", '', each_line1)
#             each_line1 = re.sub("^en la$", '', each_line1)
#             each_line1 = re.sub("^en el$", '', each_line1)
#             each_line1 = re.sub("^de la$", '', each_line1)
#             each_line1 = re.sub("^la de$", '', each_line1)
#             each_line1 = re.sub("^el de$", '', each_line1)
#             each_line1 = re.sub("^de el$", '', each_line1)
#             each_line1 = re.sub("^la el$", '', each_line1)
#             each_line1 = re.sub("^el la$", '', each_line1)
#             each_line1 = re.sub("^De la$", '', each_line1)
#             each_line1 = re.sub("^La de$", '', each_line1)
#             each_line1 = re.sub("^El de$", '', each_line1)
#             each_line1 = re.sub("^De el$", '', each_line1)
#             each_line1 = re.sub("^La el$", '', each_line1)
#             each_line1 = re.sub("^El la$", '', each_line1)
#             fn.write(each_line1)
#             fn.write('\n')

# 原子词步长法
# def aswExtract(path):
#     with open(path, encoding='utf-8') as file:
#         awsList = []
#         for line in file:
#             awsList.append(line.split())
#     return awsList
# def getChild(listA, b, argv):
#     a = ' '
#     ChildList = []
#     for i in range(0, b - argv + 1):
#         ChildList.append(a.join(listA[i:i + argv]))
#     return ChildList
# awsList = aswExtract(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela.txt')
# result = []
# for aws in awsList:
#     temp = []
#     b = len(aws)
#     for argv in range(1, b + 1):
#         temp.append(getChild(aws, b, argv))
#     result.append([j for k in temp for j in k])
# # 统计词频
# wordDict = {}
# for x in result:
#     d = Counter(x)
#     for key, value in d.items():
#         wordDict[key] = wordDict.get(key, 0) + value
# f = pd.DataFrame(pd.Series(wordDict), columns=['freq'])
# f = f.reset_index().rename(columns={'index': 'term'})
# output = f.sort_values(by=['freq'], ascending=False)
# output.to_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq.csv', index=False, encoding='utf-8')
# data=pd.read_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq.csv',encoding='utf-8')
# data1=data[data['freq']>1]
# data1.to_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1.csv', index=False, encoding='utf-8')

# # #删除之前因为词串中间有de、la等而出现的以他们开头的词语的前后缀  删除整个词而非开头的
# data4=pd.read_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1.csv',  encoding='utf-8')

# index=[]
# for i in range(0,len(data4)):
#     word=data4['term'][i].split()
#     if word[0]=='de' or word[0]=='del' or word[0]=='en' or word[0]=='ser' or word[0]=='haber' or word[0]=='la' or word[0]=='el' or word[-1]=='de' or word[-1]=='del' or word[-1]=='en' or word[-1]=='ser' or word[-1]=='haber' or word[-1]=='la' or word[-1]=='el':
#         index.append(i)
# data4=data4.drop(index)
# data4.to_csv(r'd:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela.csv',index=False,encoding='utf-8')


##利用辅助文件，加pos，因为人名、邮箱等词语用python还原不出来，所以要用treetagger软件还原！
# data=pd.read_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela.csv',encoding='utf-8')
# with open(r'D:\my paper xiugai\es\fuzhu_pos.txt','w',encoding='utf-8') as f:
#     for i in range(len(data)):
#         f.write(data['term'][i]+' JUHAO'+'\n')
# poss=[]
# with open(r'D:\my paper xiugai\es\fuzhu_pos_result.txt','r',encoding='utf-8') as f:
#     with open(r'D:\my paper xiugai\es\pos.txt','w',encoding='utf-8') as f1:
#         for eachline in f:
#             a=eachline.split()
#             if a[0]!='JUHAO':
#                 f1.write(a[1]+' ')
#             else:
#                 f1.write('\n')
# pos=[]
# with open(r'D:\my paper xiugai\es\pos.txt','r',encoding='utf-8') as f:
#     for eachline in f:
#         eachline=eachline.strip()
#         pos.append(eachline)
# data=pd.read_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela.csv',encoding='utf-8')
# pos=pd.DataFrame(pos,columns=['pos'])
# data1=pd.concat([data,pos],axis=1)
# data1.to_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_pos.csv',index=False,encoding='utf-8')


##删除介词开头和结尾的词语，并加上长度，按从长到短排列
# data=pd.read_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_pos.csv',encoding='utf-8')
# index=[]
# for i in range(len(data)):
#     poss=data['pos'][i].split()
#     if poss[0]=='PREP' or poss[-1]=='PREP':
#         index.append(i)
# data1=data.drop(index)
# data1.to_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_pos_delprep.csv',index=False,encoding='utf-8')
# data2=pd.read_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_pos_delprep.csv',encoding='utf-8')
# lens=[]
# for j in range(len(data2)):
#     lens.append(len(data2['term'][j].split()))
# lens=pd.DataFrame(lens,columns=['lens'])
# data3=pd.concat([data2,lens],axis=1)
# data3=data3.sort_values(by=['lens'],ascending=False)
# data3.to_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_pos_delprep_lens.csv',index=False,encoding='utf-8')


##去子串步骤  64730
# data7=pd.read_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_lens.csv',encoding='utf-8')
# # for i in range(0,len(data7)):
# #     print(i)
# #     length=data7['lens'][i]
# #     for j in range(0,i):
# #         if length<data7['lens'][j]:
# #             if re.search("\s+"+data7['term'][i]+"\s",data7['term'][j])!=None or re.search("\s+"+data7['term'][i],data7['term'][j])!=None or re.search(data7['term'][i]+"\s",data7['term'][j])!=None:
# #                 data7['freq'][i] = data7['freq'][i] - data7['freq'][j]
# # word_fre_len_1_delchild=data7.sort_values(by=["freq"],ascending=False)
# # word_fre_len_1_delchild1=word_fre_len_1_delchild[word_fre_len_1_delchild['freq']>1]
# # word_fre_len_1_delchild1.to_csv(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_lens.csv',encoding='utf-8',index=False)
# # print("提词完毕！")


##最后的筛选
# data=pd.read_csv(r'D:\my paper xiugai\es\07.csv',encoding='utf-8')
# data1=data[data['freq']>1]
# data1.to_csv(r'D:\my paper xiugai\es\final_result.csv',index=False,encoding='utf-8')