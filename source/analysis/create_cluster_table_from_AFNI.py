import pandas as pd
from rPEP.source.rPEP_Project import rPEP_Project

p = rPEP_Project()

arouse_ON = 'FBXArouse_ON'
arouse_OFF = 'FBXArouse_OFF'

fh = open(p.path_data + arouse_ON + '.1D', 'r')
df = pd.DataFrame(columns=['Voxels', 'CMx', 'CMy', 'CMz', 'PeakX', 'PeakY', 'PeakZ'])

count=0
cnt_list = []

for line in fh:
    # print(line)
    if line.startswith(' '):
        n = line.split()
        df_len = len(df)
        df.loc[df_len] = n
        count = count+1
        cnt_list.append(count)
    else:
        continue

df2 = df.drop(labels=['CMx', 'CMy', 'CMz'], axis = 1)
df2['count'] = cnt_list

df2.to_csv(p.path_data + arouse_ON + 'AFNI.csv')

fh1 = open(p.path_data + arouse_OFF + '.1D', 'r')
df1 = pd.DataFrame(columns=['Voxels', 'CMx', 'CMy', 'CMz', 'PeakX', 'PeakY', 'PeakZ'])

count1 = 0
cnt1_list = []
for line in fh1:
    # print(line)
    if line.startswith(' '):
        n = line.split()
        df_len = len(df1)
        df1.loc[df_len] = n
        count1 = count1 + 1
        cnt1_list.append(count1)
    else:
        continue

df3 = df1.drop(labels=['CMx', 'CMy', 'CMz'], axis = 1)
df3['count'] = cnt1_list

df3.to_csv(p.path_data + arouse_OFF + 'AFNI.csv')