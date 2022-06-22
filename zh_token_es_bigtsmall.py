import pynlpir
import itertools
import pandas as pd
# pynlpir.open()
# wordlist=[]
# data=pd.read_csv(r'D:\my paper xiugai\人工标记\candidate_termpair_rank_quchong_labels0_labeled.csv',usecols=[0]).values.tolist()
# data=list(itertools.chain.from_iterable(data))
# tokens=[]
# for i in range(len(data)):
#     token=[]
#     for j in pynlpir.segment(data[i]):
#         token.append(j[0])
#     tokens.append(' '.join(token))
# tokens=pd.DataFrame(tokens,columns=['zh_term'])
# data1=pd.read_csv(r'D:\my paper xiugai\人工标记\candidate_termpair_rank_quchong_labels0_labeled.csv',usecols=[1]).values.tolist()
# data1=list(itertools.chain.from_iterable(data1))
# data1=pd.DataFrame(data1,columns=['es_term'])
# data2=pd.read_csv(r'D:\my paper xiugai\人工标记\candidate_termpair_rank_quchong_labels0_labeled.csv',usecols=[2]).values.tolist()
# data2=list(itertools.chain.from_iterable(data2))
# data2=pd.DataFrame(data2,columns=['trans'])
# data3=pd.read_csv(r'D:\my paper xiugai\人工标记\candidate_termpair_rank_quchong_labels0_labeled.csv',usecols=[3]).values.tolist()
# data3=list(itertools.chain.from_iterable(data3))
# data3=pd.DataFrame(data3,columns=['biaoqian'])
# reslut=pd.concat([tokens,data1,data2,data3],axis=1)
# reslut.to_csv(r'D:\my paper xiugai\人工标记\labeled_all_token.csv',index=False,encoding='utf-8')
# print("中文分词完成！")



# import itertools
# data=pd.read_csv(r'D:\my paper xiugai\人工标记\labeled_all_token.csv')
# small=[]
# for i in range(len(data)):
#     small.append(data['es_term'][i].lower())
# small = pd.DataFrame(small, columns=['es_term'])
#
# data1=pd.read_csv(r'D:\my paper xiugai\人工标记\labeled_all_token.csv',usecols=[0]).values.tolist()
# data1=list(itertools.chain.from_iterable(data1))
# data1=pd.DataFrame(data1,columns=['zh_term'])
#
# data2=pd.read_csv(r'D:\my paper xiugai\人工标记\labeled_all_token.csv',usecols=[2]).values.tolist()
# data2=list(itertools.chain.from_iterable(data2))
# data2=pd.DataFrame(data2,columns=['trans'])
#
# data3=pd.read_csv(r'D:\my paper xiugai\人工标记\labeled_all_token.csv',usecols=[3]).values.tolist()
# data3=list(itertools.chain.from_iterable(data3))
# data3=pd.DataFrame(data3,columns=['biaoqian'])
#
# result=pd.concat([data1,small,data2,data3],axis=1)
# result.drop_duplicates(inplace=True)
# # result=result.sort_values(by=['zh_term'],ascending=False)
# result.to_csv(r'D:\my paper xiugai\人工标记\labeled_all_token_bigtsmall.csv',index=False,encoding='utf-8')
# print("西语大小写转换完毕！")