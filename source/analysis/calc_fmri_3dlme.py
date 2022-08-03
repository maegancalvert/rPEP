import os
from rPEP.source.rPEP_Project import rPEP_Project
from rPEP.source.Gather_events_data import Events_Path_dict
import pandas as pd

pd.set_option('display.max_columns', None, 'display.max_rows', None)

p = rPEP_Project()

########## objects to create paths by subject directories ###
fs = '/func/sub-'
mod1 = '_task-modulate1'
mod2 = '_task-modulate2'
nifti = '_bold.nii.gz'

subj_dict = Events_Path_dict()

### Now create a new dataframe with only the data you need ###
df_subj_dict = pd.DataFrame()
df_all = pd.DataFrame()
df_all2 = pd.DataFrame()

### For each subject in the dictionary, the object is defined by subject, task, etc. Then save those into a dataframe ###
path1_dict = dict()
path2_dict = dict()
path1_vols_list = list()
path2_vols_list = list()

for s in subj_dict:

        sub = subj_dict[s]
        trial_type_mod1 = subj_dict[s]['modulate1']['trial_type']
        trial_type_mod2 = subj_dict[s]['modulate2']['trial_type']
        path_mod1 = subj_dict[s]['path1']
        path_mod2 = subj_dict[s]['path2']
        vols1 = subj_dict[s]['vols1']
        for v in vols1:
            path1_dict = [s, (str(path_mod1 + "'" + '[' + str(v) + ']' + "'" + ' \\'))]
            path1_vols_list.append(path1_dict)
        vols2 = subj_dict[s]['vols2']
        for v in vols2:
            path2_dict = [s, (str(path_mod2 + "'" + '[' + str(v) + ']' + "'" + ' \\'))]
            path2_vols_list.append(path2_dict)
        df_all['trial_type_mod1'] = trial_type_mod1
        df_all['trial_type_mod2'] = trial_type_mod2
        df_all['sub'] = s
        df_all2 = pd.concat([df_all2, df_all])

### Save the paths and volumes dictionary into a dataframe ###

### First reset index because will not be able to combine dataframes without resetting index ###
df_all3 = df_all2.reset_index(drop=True)
### create dataframe with the paths and volumes then name columns###
path1_df = pd.DataFrame(path1_vols_list)
path1_df.columns=['sub_path1', 'path_vol1']

path2_df = pd.DataFrame(path2_vols_list)
path2_df.columns = ['sub_path2', 'path_vol2']

### Add columns to dataframe###
df_all_path1 = pd.concat([df_all3,path1_df], axis=1, sort=True)
df_all_paths = pd.concat([df_all_path1,path2_df], axis=1, sort=True)

### Use pd melt to stack the trial types into one column ###
df_copy1 = df_all_paths.copy()
df2 = pd.melt(df_copy1, id_vars=['sub'], value_vars=['trial_type_mod1','trial_type_mod2'])
df3 = df2.rename(columns={"variable": "run_t", "value": "trial_type"})
df4 = df3.replace(to_replace=['trial_type_mod1', 'trial_type_mod2'],value=[1,2])
df4.columns = ['sub', 'run_t', 'trial_type']

### Use pd melt to stack the paths into one column ###
df_copy3 = df_all_paths.copy()
df8 = pd.melt(df_copy3, id_vars=['sub'], value_vars=['path_vol1','path_vol2'])
df9 = df8.rename(columns={"variable": "run_p", "value": "path"})
df10 = df9.replace(to_replace=['path_vol1', 'path_vol2'],value=[1,2])
df10.columns = ['sub_p', 'run_p', 'path']

### Concat dataframes ###
df_all = pd.concat([df4, df10], axis=1)
print(df_all['sub'].head)

## Create new column called Feedback based on trial type ###
df_all.loc[(df_all['trial_type'] == 'stims_rst'), 'feedback'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'instr_fba'), 'feedback'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'instr_fbs'), 'feedback'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'instr_aro'), 'feedback'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'instr_sup'), 'feedback'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'stims_aro'), 'feedback'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'stims_sup'), 'feedback'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'stims_fba'), 'feedback'] = 'ON'
df_all.loc[(df_all['trial_type'] == 'stims_fbs'), 'feedback'] = 'ON'
print(df_all.shape)

### Keep the following feedback columns ###
all = df_all[['sub', 'run_t', 'feedback', 'path']]
a = all.rename(columns={"sub": "Subj", "run_t": "run", "feedback": "feedback", "path":"InputFile"})
b = a.dropna()
c = b[['Subj', 'feedback', 'InputFile']]
print(c.shape)
print(c.head())
c.to_csv(p.path_data + 'feedback_path_.csv')
print('saved feedback path csv')

# ### Create new column called Arouse based on trial type ###
df_all.loc[(df_all['trial_type'] == 'stims_rst'), 'arouse'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'instr_fba'), 'arouse'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'instr_fbs'), 'arouse'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'instr_aro'), 'arouse'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'instr_sup'), 'arouse'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'stims_aro'), 'arouse'] = 'ON'
df_all.loc[(df_all['trial_type'] == 'stims_sup'), 'arouse'] = 'OFF'
df_all.loc[(df_all['trial_type'] == 'stims_fba'), 'arouse'] = 'ON'
df_all.loc[(df_all['trial_type'] == 'stims_fbs'), 'arouse'] = 'OFF'
print(df_all.shape)

### Keep the following arouse columns and put into a new dataframe ###
all1 = df_all[['sub', 'run_t', 'arouse', 'path']]
a1 = all1.rename(columns={"sub": "Subj", "run_t": "run", "arouse": "arouse", "path":"InputFile"})
b1 = a1.dropna()
c1 = b1[['Subj', 'arouse', 'InputFile']]
print(c1.shape)
print(c1.head())
c1.to_csv(p.path_data + 'arouse_path_.csv')
print('saved arouse path csv')

### Keep the feedback and arouse columns and put into a new dataframe ###
all2 = df_all[['sub', 'run_t', 'feedback', 'arouse', 'path']]
a2 = all2.rename(columns={"sub": "Subj", "run_t": "run", "feedback": "feedback", "arouse": "arouse", "path":"InputFile"})
b2 = a2.dropna()
c2 = b2[['Subj', 'feedback', 'arouse', 'InputFile']]
print(c2.shape)
print(c2.head())
c2.to_csv(p.path_data + 'feedback_arouse_path_.csv')
print('saved feedback arouse path csv')

### Create an AFNI script for the 3dlme ###
### Feedback (ON vs OFF) by Condition (Engage vs Disengage) ###

with open('/home/mcalvert/workspace/code/rPEP/source/analysis/lme_rPEP_feedbackXarouse_script', 'w') as f:
    f.write(str('#! /bin/csh\n'))
    f.write(str('\n'))
    f.write(str("3dLME -prefix FBXArouse -jobs 16 \\"))
    f.write(str("      -resid lme_FBxArouse_resid \\"))
    f.write(str("      -model 'feedback*arouse' \\"))
    f.write(str("      -ranEff '~1' \\"))
    f.write(str("      -mask /project/data/clean/bush/rPEP/derivatives/pipeline/mri/mri_gm_mask/group_gm_mask.nii \\"))
    f.write(str("      -num_glt 4 \\"))
    f.write(str("      -gltLabel  1  feedback  -gltCode  1  'feedback : 1*ON -1*OFF' \\"))
    f.write(str("      -gltLabel  2  arouse  -gltCode  2  'arouse : 1*ON -1*OFF' \\"))
    f.write(str("      -gltLabel  3  feedback_arouse_on  -gltCode  3  'feedback : 1*ON -1*OFF arouse : 1*ON' \\"))
    f.write(str("      -gltLabel  4  feedback_arouse_off  -gltCode  4  'feedback : 1*ON -1*OFF arouse : -1*OFF' \\"))
    f.write(str("      -dataTable \  Subj feedback arouse InputFile \\"))
    count = -1

    with open('/home/mcalvert/workspace/data/rPEP/feedback_arouse_path_.csv') as fh:
        for line in fh:
            if not line.startswith(","):
                if count <= 7080:
                    line2 = line.rstrip()
                    line3 = line2.split(',')
                    newline = line3[1:5]
                    str_nl = ' '.join(newline)
                    str_l = (str(' ' + str_nl))
                    count = count + 1
                    if not count == 7081:
                        f.write(str(str_l))
                    elif count == 7081:
                        last_line = str_l.rstrip('\\')
                        f.write(str(last_line))
                    elif count >= 7082:
                        break
            else:
                continue
        print(count)
        f.write(str('\n'))
        f.write(str(" \\"))
f.close()
print(count)

### Feedback X Arouse bashscript ###
os.system('chmod u+x /home/mcalvert/workspace/code/rPEP/source/analysis/lme_rPEP_feedbackXarouse_script')
os.system('./lme_rPEP_feedbackXarouse_script')
