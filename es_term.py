import pandas as pd
import itertools
import os
import math

##筛选
# data=pd.read_csv(r'D:\法语处理\fr\60000-80000.csv')
# data1=data[data['freq']>1]
# data1.to_csv(r'D:\法语处理\fr\quzichuan_result.csv',index=False,encoding='utf-8')


# ###dc
data=pd.read_excel(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_pos_delprep_lens_del10_delchild.xlsx',usecols=[0],encoding='utf-8').values.tolist()
data=list(itertools.chain.from_iterable(data))
term_value=[]  #dc
for i in range(len(data)):
    # print(i)
    count = 0  #df
    each_text_count = []  #tf
    subdirs = os.walk(r'D:\my paper xiugai\shiyan\小文本的还原\5huanyuanadd_space')   #文档集
    for d, s, fns in subdirs:
        for fn in fns:
            if fn[-3:] == 'txt':
                    with open(d + os.sep + fn, "r", encoding="utf-8") as p:
                        text_content=p.read()
                        if ' '+ str(data[i])+' ' in text_content:
                            each_text_count.append(text_content.count(' '+str(data[i])+' '))
                            count+=1
    a=0
    for i in range(len(each_text_count)):
        b=each_text_count[i]/sum(each_text_count)
        c = b * math.log(1 / b)
        a+=c
    term_value.append(a)
data1=pd.read_excel(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_pos_delprep_lens_del10_delchild.xlsx')
term_value=pd.DataFrame(term_value,columns=['dc'])
data2=pd.concat([data1,term_value],axis=1)
data2.to_csv(r'D:\my paper xiugai\es\es_term_value_dc.csv',index=False,encoding='utf-8')
print("术语度计算完毕！")


###dr
# data=pd.read_excel(r'D:\my paper xiugai\es\without_stopwords_huanyuan_deldela_freq_freqbig1_deldela_pos_delprep_lens_del10_delchild.xlsx',usecols=[0]).values.tolist()
# data=list(itertools.chain.from_iterable(data))
# def freq(data,path):
#     with open(path, "r", encoding="utf-8") as p:
#         text = p.read()
#         all_tfs = []  #存放每个词语的词频
#         for i in range(len(data)):
#             if ' '+data[i]+' ' in text:
#                 all_tfs.append(text.count(' '+data[i]+' '))
#             else:
#                 all_tfs.append(0)
#     return all_tfs
# all_tfs_domain=freq(data,r'D:\my paper xiugai\shiyan\大文本的还原\5add_space.txt')  #说明：es_alltext.txt是为了提词而形成的并且和中文的已对齐每句前未加空格，es_alltext1.txt是为了计算词频而形成的，每句前后都加了空格
# all_tfs_notdomain=freq(data,r'D:\my paper xiugai\es背景语料库\9add_space.txt')  #和上面的长度应保持一致为data的长度
# drs=[]
# for i in range(len(all_tfs_domain)):
#     dr=(math.log((all_tfs_domain[i]/200)/((all_tfs_notdomain[i]+1e-8)/477)))
#     drs.append(dr)
# data1=pd.read_csv(r'D:\my paper xiugai\es\es_term_value_dc.csv')
# drs=pd.DataFrame(drs,columns=['dr'])
# data2=pd.concat([data1,drs],axis=1)
# data2.to_csv(r'D:\my paper xiugai\es\es_term_value_dc_dr.csv',index=False,encoding='utf-8')
# print("术语度计算完毕！")


###筛选
# data=pd.read_excel(r'D:\my paper xiugai\es\es_term_value_dc_dr.xlsx')
# data1=data[data['dc']>0]
# data2=data1[data1['dr']>0]
# data2.to_csv(r'D:\my paper xiugai\es\es_term_value_dc_dr_delzero.csv',index=False,encoding='utf-8')
# print("完成！")

###dc和dr合并排序
# data=pd.read_csv(r'D:\my paper xiugai\es\es_term_value_dc_dr_delzero.csv',encoding='utf-8')
# dr_dc=[]
# for i in range(len(data)):
#     a=(0.95*data['dr'][i])+(0.05*data['dc'][i])
#     dr_dc.append(a)
# dr_dc=pd.DataFrame(dr_dc,columns=['0.95dr_0.05dc'])
# data2=pd.concat([data,dr_dc],axis=1)
# data2=data2.sort_values(by=["0.95dr_0.05dc"],ascending=False)
# data2.to_csv(r'D:\my paper xiugai\es\es_term_value_dc_dr_delzero_drdcchengji.csv',index=False,encoding='utf-8')
# print("术语度计算完毕！")




# # all_tfs_domain=pd.DataFrame(all_tfs_domain,columns=['all_tfs_domain'])
# # all_tfs_notdomain=pd.DataFrame(all_tfs_notdomain,columns=['all_tfs_notdomain'])
# # data1=pd.concat([all_tfs_domain,all_tfs_notdomain],axis=1)
# # data1.to_csv(r'C:\Users\admin\Desktop\1.csv',index=False,encoding='utf-8')