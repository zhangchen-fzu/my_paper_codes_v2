##笛卡尔积
# import itertools
# import pandas as pd

# zh_term=[]
# data=pd.read_csv(r'D:\my paper xiugai\zh\zh_term_value_dc_dr_delzero.csv',encoding='utf-8')
# for i in range(len(data)):
#     zh_term.append(data['word'][i])
# zh_all_line_term=[]  #有多少句话就有多少个[]存在，二维列表
# with open(r'D:\my paper xiugai\4zhes加标点\zh\all_zh.txt','r',encoding='utf-8') as zh_file:
#     for eachline in zh_file:
#         zh_each_line_term=[]
#         for j in range(len(zh_term)):
#             if str(zh_term[j]) in str(eachline):
#                 zh_each_line_term.append(zh_term[j])
#         zh_all_line_term.append(zh_each_line_term)
# print("1")

# es_term=[]
# trans=[]
# data=pd.read_excel(r'D:\my paper xiugai\es\es_term_value_dc_dr_delzero_trans.xlsx')
# for i in range(len(data)):
#     es_term.append(data['term'][i])
#     trans.append(data['trans'][i])
# es_all_line_term=[]  #有多少句话就有多少个[]存在
# with open(r'D:\my paper xiugai\shiyan\大文本的还原\5add_space.txt','r',encoding='utf-8') as es_file:
#     for eachline in es_file:
#         es_each_line_term=[]
#         for j in range(len(es_term)):
#             if ' '+str(es_term[j])+' ' in str(eachline):
#                 es_each_line_term.append((es_term[j],trans[j]))
#         es_all_line_term.append(es_each_line_term)
# print("2")
# all_dicard=[]  #三维列表
# for i in range(len(zh_all_line_term)):
#     if zh_all_line_term[i]!=[] and es_all_line_term[i]!=[]:
#         dicard=[]
#         for j in zh_all_line_term[i]:
#             for k in es_all_line_term[i]:
#                 dicard.append([j,k[0],k[1]])
#         all_dicard.append(dicard)
# all_dicard=list(itertools.chain.from_iterable(all_dicard))  #二维列表
# zh=[]
# es=[]
# trans1=[]
# for i in range(len(all_dicard)):
#     zh.append(all_dicard[i][0])
#     es.append(all_dicard[i][1])
#     trans1.append(all_dicard[i][2])
# zh=pd.DataFrame(zh,columns=['zh_term'])
# es=pd.DataFrame(es,columns=['es_term'])
# trans1=pd.DataFrame(trans1,columns=['trans'])
# result=pd.concat([zh,es,trans1],axis=1)
# result.to_csv(r'D:\my paper xiugai\candidate_termpair.csv',encoding='utf-8',index=False)
# print("笛卡尔积计算候选术语完成！")

##按中文排序
# import pandas as pd
# data=pd.read_csv(r'd:\my paper xiugai\candidate_termpair.csv',encoding='utf-8')
# data1=data.sort_values(by=['zh_term'])
# data1.to_csv(r'd:\my paper xiugai\candidate_termpair_rank.csv',index=False,encoding='utf-8')

##去重
import pandas as pd
import itertools
data3=pd.read_csv(r'D:\my paper xiugai\candidate_termpair_rank.csv',encoding='utf-8')
data=pd.read_csv(r'D:\my paper xiugai\candidate_termpair_rank.csv',encoding='utf-8',usecols=[0]).values.tolist()
data_zh_term=list(set(list(itertools.chain.from_iterable(data))))
for i in range(len(data_zh_term)):
    group_data=data3[data3.zh_term==data_zh_term[i]]
    group_data = group_data.reset_index()
    group_data = group_data.drop(columns='index')
    group_data.drop_duplicates(inplace=True)
    group_data.to_csv(r'D:\my paper xiugai\candidate_termpair_rank_quchong.csv', header=0, mode='a', index=False)



