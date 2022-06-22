# es开头的序号删掉
import os
import re
import pandas as pd
subdirs = os.walk(r'D:\法语处理\xgboost结果\36')
for d, s, fns in subdirs:
    for fn in fns:
        if fn[-3:] == 'csv':
            print(d + os.sep + fn)
            data=pd.read_csv(d + os.sep + fn,header=0)
            data.to_csv(r'D:\法语处理\xgboost结果\36\all.csv',mode='a',encoding='utf-8',index=False,header=False)
