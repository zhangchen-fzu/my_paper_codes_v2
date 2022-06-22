# #中文词语抽取
# import pynlpir
# from collections import Counter
# import re
# import pandas as pd
# import itertools
# import os
# pynlpir.open()
#
# # 加载停用词、停用词性表
# stop_poss=['时间词','时间词性语素','方位词','动词"是"','动词"有"','代词','人称代词','指示代词','时间指示代词','处所指示代词','谓词性指示代词',
#          '疑问代词','时间疑问代词','处所疑问代词','谓词性疑问代词','代词性语素','数词','数量词','干支','量词','动量词','时量词','副词',
#            '连词','并列连词','助词',"'着'","了／喽","过","的／底","地","得","所","等／等等／云云","一样／一般／似的／般",
#          "的话","来讲／来说／而言／说来","之","连",'叹词','语气词','拟声词','字符串','Email字符串','微博会话分隔符','表情符合','网址URL',
#          '非语素字','标点符号','左括号','右括号','左引号','右引号','句号','问号','叹号','逗号','分号','顿号','冒号','省略号','破折号',
#           '百分号千分号','单位符号']
# stop_words = set([line.strip() for line in open(r'G:\my paper\zhstoplist.txt',encoding='utf-8').readlines()])
# #
# #分词、词性标注
# subdirs = os.walk(r'D:\my paper xiugai\zh稍改进文本之后的语料\zh')
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'txt':
#             wordlist = []  ##一篇文档的分词和磁性标注
#             with open(d + os.sep + fn, "r", encoding="utf-8") as p:
#                 for eachline in p:
#                     for i in pynlpir.segment(eachline,pos_english=False,pos_names='child'):
#                         wordlist.append(i)
#             word=[]
#             pos=[]
#             for i in range(len(wordlist)):
#                 word.append(wordlist[i][0])
#                 pos.append(wordlist[i][1])
#             df = {"word": word, "pos": pos}
#             segandpos_result = pd.DataFrame(df)  ##一篇文章的csv
#             segandpos_result.to_csv(r'D:\my paper xiugai\分词词性标注之后的语料\zh\{}.csv'.format(fn[0:-4]),index=False,encoding='utf-8')
# #
# #去除停用词和停用词性
# # subdirs = os.walk(r'D:\my paper xiugai\分词词性标注之后的语料\zh')
# # # for d, s, fns in subdirs:
# # #     for fn in fns:
# # #         if fn[-3:] == 'csv':
# # #             segandpos_result=pd.read_csv(d + os.sep + fn)
# # #             with open(r'D:\my paper xiugai\去除停用词词性之后的语料\zh\{}.txt'.format(fn[0:-4]), 'w', encoding='utf-8') as f1:
# # #                 without_stopwords_wordlist = []
# # #                 for i in range(len(segandpos_result)):
# # #                         if segandpos_result['word'][i] in stop_words or segandpos_result['pos'][i] in stop_poss or segandpos_result['pos'][i]==None:
# # #                             without_stopwords_wordlist.append('\n')
# # #                         else:
# # #                             without_stopwords_wordlist.append(segandpos_result['word'][i])
# # #                 f1.write(' '.join(without_stopwords_wordlist))
# # #                 f1.write('\n')
#
# #原子词步长法
# # def aswExtract(path):
# #     with open(path, encoding='utf-8') as file:
# #         awsList = []
# #         for line in file:
# #             awsList.append(line.split())
# #     return awsList
# #
# # def getChild(listA, b, argv):
# #     a = ''
# #     ChildList = []
# #     for i in range(0, b - argv + 1):
# #         ChildList.append(a.join(listA[i:i + argv]))
# #     return ChildList
# #
# # subdirs = os.walk(r'D:\my paper xiugai\去除停用词词性之后的语料\zh')
# # for d, s, fns in subdirs:
# #     for fn in fns:
# #         if fn[-3:] == 'txt':
# #             atomic_method = []
# #             with open(d + os.sep + fn, "r", encoding="utf-8") as f1:
# #                 eachline_split = []  #二维列表
# #                 for line in f1:
# #                     # line=line.strip()
# #                     eachline_split.append(line.split())
# #                 for aws in eachline_split:
# #                     temp = []
# #                     b = len(aws)
# #                     for argv in range(1, b + 1):
# #                         a=getChild(aws, b, argv)
# #                         temp.append(a)
# #                     atomic_method.append([j for k in temp for j in k])
# #             # print(atomic_method)
# #             # 统计词频
# #             atomicfreq= {}
# #             for x in atomic_method:
# #                 r = Counter(x)
# #                 for key, value in r.items():
# #                     atomicfreq[key] = atomicfreq.get(key, 0) + value
# #             f = pd.DataFrame(pd.Series(atomicfreq), columns=['freq'])
# #             f = f.reset_index().rename(columns={'index': 'word'})
# #             output = f.sort_values(by=['freq'], ascending=False)
# #             output.to_csv(r'd:\my paper xiugai\提取原子词之后的语料\zh\{}.csv'.format(fn[0:-4]), index=False, encoding='utf-8')
#
# #按长度排序&只取频率大于1的
# # subdirs = os.walk(r'D:\my paper xiugai\提取词之后的语料\zh')
# # for d, s, fns in subdirs:
# #     for fn in fns:
# #         if fn[-3:] == 'csv':
# #             data=pd.read_csv(d + os.sep + fn,encoding='utf-8')
# #             data1=data[data['freq']>1]  ##筛选频率大于1的词语
# #             lens=[]
# #             segwords=[]
# #             for i in range(len(data1)):
# #                 segword=[]
# #                 for m,_ in pynlpir.segment(data1['word'][i],pos_english=False,pos_names='child'):
# #                     segword.append(m)
# #                 a=[' '.join(segword)]
# #                 segwords.append(a)
# #                 lens.append(len(segword))
# #             lens=pd.DataFrame(lens,columns=['len'])
# #             segwords=pd.DataFrame(segwords,columns=['segword'])
# #             data_result=pd.concat([data1,lens,segwords],axis=1)
# #             data_result1= data_result.sort_values(by=['len'], ascending=False)
# #             data_result1.to_csv(r'D:\my paper xiugai\筛选词串频率大于一之后的语料\zh\{}.csv'.format(fn[0:-4]), index=False, encoding='utf-8')
#
#  #去子串
# subdirs = os.walk(r'D:\my paper xiugai\筛选词串频率大于一之后的语料\zh')
# for d, s, fns in subdirs:
#     for fn in fns:
#         if fn[-3:] == 'csv':
#             data=pd.read_csv(d + os.sep + fn,encoding='utf-8')
#             for i in range(0,len(data)):
#                 for j in range(0,i):
#                     if data['word'][i] in data['word'][j]:
#                         data['freq'][i] = data['freq'][i] - data['freq'][j]
#                     else:
#                         continue
#             word_fre_len_1_delchild=data.sort_values(by=["freq"],ascending=False)
#             word_fre_len_1_delchild1=word_fre_len_1_delchild[word_fre_len_1_delchild['freq']>1]
#             word_fre_len_1_delchild1.to_csv(r'D:\my paper xiugai\去子串之后的语料库\zh\{}.csv'.format(fn[0:-4]),encoding='utf-8',index=False)
#             print(fns.index(fn))

#中文词语抽取
import pynlpir
from collections import Counter
import re
import pandas as pd
import itertools
pynlpir.open()
import jieba.posseg as posseg
stop_poss=['时间词','时间词性语素','方位词','动词"是"','动词"有"','代词','人称代词','指示代词','时间指示代词','处所指示代词','谓词性指示代词',
         '疑问代词','时间疑问代词','处所疑问代词','谓词性疑问代词','代词性语素','数词','数量词','干支','量词','动量词','时量词','副词',
           '连词','并列连词','助词',"'着'","了／喽","过","的／底","地","得","所","等／等等／云云","一样／一般／似的／般",
         "的话","来讲／来说／而言／说来","之","连",'叹词','语气词','拟声词','字符串','Email字符串','微博会话分隔符','表情符合','网址URL',
         '非语素字','标点符号','左括号','右括号','左引号','右引号','句号','问号','叹号','逗号','分号','顿号','冒号','省略号','破折号',
          '百分号千分号','单位符号']
stop_words = set([line.strip() for line in open(r'G:\my paper\zhstoplist.txt',encoding='utf-8').readlines()])


# 分词、词性标注
# wordlist=[]
# with open(r'D:\my paper xiugai\4zhes加标点\zh\all_zh.txt','r',encoding='utf-8') as alltext:
#     for eachline in alltext:
#         eachline=eachline.strip()
#         for i in pynlpir.segment(eachline,pos_english=False,pos_names='child'):
#             wordlist.append(i)
# word=[]
# pos=[]
# for i in range(len(wordlist)):
#     word.append(wordlist[i][0])
#     pos.append(wordlist[i][1])
# df = {"word": word, "pos": pos}
# segandpos_result = pd.DataFrame(df)
# segandpos_result.to_csv(r'd:\my paper xiugai\zh\segandpos_result.csv',index=False,encoding='utf-8')


# # #去除停用词和停用词性
# segandpos_result=pd.read_csv(r'd:\my paper xiugai\zh\segandpos_result.csv',encoding='utf-8')
# with open(r'd:\my paper xiugai\zh\without_stopwords_wordlist.txt', 'w', encoding='utf-8') as f1:
#     without_stopwords_wordlist = []
#     for i in range(len(segandpos_result)):
#         if segandpos_result['word'][i] in stop_words or segandpos_result['pos'][i] in stop_poss or segandpos_result['pos'][i]==None:
#             without_stopwords_wordlist.append('\n')
#         else:
#             without_stopwords_wordlist.append(segandpos_result['word'][i])
#     f1.write(' '.join(without_stopwords_wordlist))
#     f1.write('\n')


# # #原子词步长法
# def aswExtract(path):
#     with open(path, encoding='utf-8') as file:
#         awsList = []
#         for line in file:
#             awsList.append(line.split())
#     return awsList
# def getChild(listA, b, argv):
#     a = ''
#     ChildList = []
#     for i in range(0, b - argv + 1):
#         ChildList.append(a.join(listA[i:i + argv]))
#     return ChildList
# atomic_method=[]
# with open(r'd:\my paper xiugai\zh\without_stopwords_wordlist.txt', 'r',encoding='utf-8') as f1:
#     eachline_split = []  #二维列表
#     for line in f1:
#         eachline_split.append(line.split())
#     for aws in eachline_split:
#         temp = []
#         b = len(aws)
#         for argv in range(1, b + 1):
#             a=getChild(aws, b, argv)
#             temp.append(a)
#         atomic_method.append([j for k in temp for j in k])
# # print(atomic_method)
# #统计词频
# atomicfreq= {}
# for x in atomic_method:
#     d = Counter(x)
#     for key, value in d.items():
#         atomicfreq[key] = atomicfreq.get(key, 0) + value
# f = pd.DataFrame(pd.Series(atomicfreq), columns=['freq'])
# f = f.reset_index().rename(columns={'index': 'word'})
# output = f.sort_values(by=['freq'], ascending=False)
# output.to_csv(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq.csv', index=False, encoding='utf-8')
# #只取频率大于1的
# data=pd.read_csv(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq.csv',encoding='utf-8')
# data1=data[data['freq']>1]
# data1.to_csv(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq_frebig1.csv', index=False, encoding='utf-8')


# ##对介词开头和结尾词的处理,手动处理！！！
# import pandas as pd
# import pynlpir
# pynlpir.open()
# data=pd.read_csv(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq_frebig1.csv',encoding='utf-8')
# poss=[]
# words=[]
# for i in range(len(data)):
#     pos=[]
#     word=[]
#     a = pynlpir.segment(data['word'][i],pos_english=False,pos_names='child')
#     for j in a:
#         pos.append(j[1])
#         word.append(j[0])
#     poss.append(' '.join(pos))
#     words.append(' '.join(word))
# poss=pd.DataFrame(poss,columns=['pos'])
# words=pd.DataFrame(words,columns=['word_seg'])
# poss1=pd.concat([data,poss,words],axis=1)
# poss1.to_csv(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq_frebig1_pos.csv',index=False,encoding='utf-8')

##除去介词之后按长度排序！！
# data=pd.read_excel(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq_frebig1_pos_delprep.xlsx')
# lens=[]
# for i in range(len(data)):
#     lens.append(len(data['word_seg'][i].split()))
# lens=pd.DataFrame(lens,columns=['lens'])
# data2=pd.concat([data,lens],axis=1)
# data2=data2.sort_values(by=['lens'],ascending=False)
# data2.to_csv(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq_frebig1_pos_delprep_lens.csv',index=False,encoding='utf-8')


# # #去子串 39990
# data=pd.read_excel(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq_frebig1_pos_delprep_lens_del10.xlsx')
# for i in range(0,len(data)):
#     if i%1000==0:
#         print(i)
#     length=data['lens'][i]
#     for j in range(0,i):
#         if data['lens'][j]>length:
#             if data['word'][i] in data['word'][j]:
#                 data['freq'][i] = data['freq'][i] - data['freq'][j]
#             else:
#                 continue
# word_fre_len_1_delchild=data.sort_values(by=["lens"],ascending=False)
# word_fre_len_1_delchild1=word_fre_len_1_delchild[word_fre_len_1_delchild['freq']>1]
# word_fre_len_1_delchild1.to_csv(r'D:\my paper xiugai\zh\without_stopwords_wordlist_atomicfreq_frebig1_pos_delprep_lens_del10_delchild.csv',encoding='utf-8',index=False)
# print("提词完毕！")
