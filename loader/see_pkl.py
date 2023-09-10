# import pickle
# import pandas as pd
# f = open('/nfs/home/luorui/Tag2Pix/Tag2Pix-master/loader/tag_dump.pkl','rb')
# data = pickle.load(f)
# pd.set_option('display.width',None)
# pd.set_option('display.max_rows',None)
# pd.set_option('display.max_colwidth',None)
# print(data)
# inf=str(data)
# ft = open('test1.csv', 'w')
# ft.write(inf)

import pickle

path='/nfs/home/luorui/Tag2Pix/Tag2Pix-master/loader/tag_dump.pkl'

#path='/root/……/aus_openface.pkl' pkl文件所在路径

f=open(path,'rb')

data=pickle.load(f)

print(data)

print(len(data))