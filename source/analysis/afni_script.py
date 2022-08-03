from rPEP.source.rPEP_Project import rPEP_Project
import pandas as pd

p = rPEP_Project()

#######################################################################################################################

### AFNI Where Am I code ###

#######################################################################################################################
### csh: whereami -coord_file FBArouse_ON.1D'[4,5,6]' -space MNI -atlas Brainnetome_1.0 -atlas MNI_Glasser_HCP_v1.0  >> FBArouse_ON_regions.txt
### csh: whereami -coord_file FBArouse_OFF.1D'[4,5,6]' -space MNI -atlas Brainnetome_1.0 -atlas MNI_Glasser_HCP_v1.0  >> FBArouse_OFF_regions.txt
### These shell scripts create regions, but L/R is not correct. if use -lpi does not correct the error ###

### Can use this shell script to create the clusters and save the cluster mask ###
### Or can use AFNI GUI and save the Mask created ###

### 3dClusterize -nosum -1Dformat -inset FBXArouse+tlrc.HEAD -idat 9 -ithr 9 -NN 1 -clust_nvox 15 -bisided -3.2905 3.2905 -pref_map Clust_mask

### After saving the cluster mask then need to run whereami in the shell ###

### csh: whereami -omask FBArouse_ON+tlrc.HEAD > FBArouse_ON_whereami.txt ###
### csh: whereami -omask FBArouse_OFF+tlrc.HEAD > FBArouse_OFF_whereami.txt ###

### Slides that help with whereami ###
### https://slideplayer.com/slide/7223753/ ###
#######################################################################################################################

file1 = p.path_data + '/FBArouse_ON_whereami.txt'
file2 = p.path_data + '/FBArouse_OFF_whereami.txt'

def read_AFNI_whereami(file):
    value = []
    overlap = []
    b_list = []
    fh = open(file).read().splitlines()
    for index, line in enumerate(fh):
        if "Processing unique value of " in line:
            v = fh[index]
        if "atlas Brainnetome_1.0 " in line:
            b = fh[index+1: index+3]
            b0 = b[0].split('overlap with')
            overlap.append(b0[0])
            value.append(v)
            b0_1 = b0[1].split(',')
            b_list.append(b0_1[0])
            b1 = b[1].split('overlap with')
            overlap.append(b1[0])
            value.append(v)
            if b1[0].startswith('   --'):
                b1_1 = '---'
                b_list.append(b1_1)
                continue
            b1_1 = b1[1].split(',')
            b_list.append(b1_1[0])
    return(overlap, b_list, value)

x, y, z = read_AFNI_whereami(file1)
df = pd.DataFrame(y, columns=['regions'])
df['overlap'] = x
df['value'] = z
df.to_csv(p.path_data + 'FBArouse_ON.csv')
print('saved FBA ON')

x2, y2, z2 = read_AFNI_whereami(file2)
df2 = pd.DataFrame(y2, columns=['regions'])
df2['overlap'] = x2
df2['value'] = z2
df2.to_csv(p.path_data + 'FBArouse_OFF.csv')
print('saved FBA OFF')

#######################################################################################################################

### BrainSpy code ###
### This program has to be run on a windows machine ###
### BrainSpy may not be necessary in future iterations due to the code above ###

#######################################################################################################################
#
# fh = open(r"C:\Users\Clust_table_feedback_AFNI.csv")
# fh = open(r"C:\Users\Clust_table_arousal_AFNI.csv")
# df = pd.read_csv(fh)
# df1 = df.drop(columns=['Unnamed: 0', 'Voxels','count'], axis=1)
# df1.columns = ['PeakX', 'PeakY', 'PeakZ']
#
# ### create new dataframe ###
# df2 = df1
# df3 = df2.astype(int)
#
# ### Write new text file ###
# with open(r"C:\Clust_table2_feedback_AFNI.txt", 'w') as f:
# with open(r"C:\Clust_table_arousal_final_AFNI.txt", 'w') as f:
#     print('\n', file=f)
#     f.close()
# with open(r"C:\Clust_table_arousal_final_AFNI.txt", 'a') as f1:
# # #     print(df3.to_csv(r"C:\Clust_table2_feedback_AFNI.txt",
# # #                  header=False, index=False, sep=','))
#     print(df3.to_csv(r"C:\Users\Clust_table_arousal_final_AFNI.txt",
#                      header=False, index=False, sep=','))
#     f1.close()
# # # f2 = open(r"C:\Clust_table2_feedback_AFNI.txt", 'a')
# f2 = open(r"C:\Clust_table_arousal_final_AFNI.txt", 'a')
# f2.write('***\n')
# f2.close()
#
# ### Review all characters and text from file ###
# # column_line = []
# # with open(r"C:\Clust_table2_feedback_AFNI.txt", 'r') as f3:
# # #with open(r"C:\Clust_table2_arousal_AFNI.txt", 'r') as f3:
# #     lines2 = f3.readlines()
# #     # print(lines2)
# #     f3.close()
#
# ### count lines to make sure file is complete ###
# # fh1 = open(r"C:\Clust_table2_feedback_AFNI.txt")
# # #fh1 = open(r"C:\Clust_table2_arousal_AFNI.txt")
# # count = 0
# # for lines in fh1:
# #     count = 1 + count
# # #     print(lines)
# # print(count)
# ###
#
# ### Using applicatin to label activation regions. Documentation: ###
# #https://github.com/ezPsycho/brainSpy-cli
# #https://github.com/ezPsycho/brainSpy-cli/releases/tag/0.0.1
# ###
#
# ### Have to use Windows command prompt for this step. Application cannot be utilized through automated code. ###
# #C:\Users>brainSpy < C:\Clust_table2_AFNI.txt > out_arousal.txt
# #
# #or open both programs and copy and paste txt file into the application
# os.startfile(r"C:\Application\brainSpy\brainSpy.exe")
# # type -r 3 to query voxels around the coordinate
# # os.startfile(r"C:\Clust_table2_feedback_AFNI.txt")
# os.startfile(r"C:\Clust_table_arousal_final_AFNI.txt")
# ###
#
# ### Open Application output and paste into txt file###
#
# ### Exact MNI Coordinates ###
# #fh2 = open(r"C:\Significant Feedback Cluster regions.txt")
# fh2 = open(r"C:\Significant Arousal Cluster regions final.txt")
# clust_list = []
# count = 0
# for line in fh2:
#     x = line.split()
#     count = count + 1
#     if count >= 3:
#         clust_list.append(x)
#
# clust_df = pd.DataFrame(columns=['X','Y','Z','AAL Label', 'Dist', 'BA#', 'BA Label', 'Dist'])
# for item in clust_list:
#     df_len = len(clust_df)
#     clust_df.loc[df_len] = item
# # clust_df.to_csv(r"C:\Significant Feedback Cluster regions.csv")
# clust_df.to_csv(r"C:\Significant Arousal Cluster regions final.csv")
# print('saved csv')
