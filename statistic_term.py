import pandas as pd
data=pd.read_csv(r'd:\my paper xiugai\术语提取a术语对生成\es\es_term_value_dc_dr_delzero.csv',encoding='utf-8')
lens=[]
for i in range(len(data)):
    lens.append(len(data['term'][i].split()))
lens=pd.DataFrame(lens,columns=['lens'])
data1=pd.concat([data,lens],axis=1)
data1.to_csv(r'd:\my paper xiugai\术语提取a术语对生成\es\es_term_value_dc_dr_delzero_lens.csv',index=False,encoding='utf-8')