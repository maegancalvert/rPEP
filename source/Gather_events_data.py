import pandas as pd
from rPEP.source.rPEP_Project import rPEP_Project
from rPEP.source.rPEP_scr_Project import rPEP_scr_Project
import glob
import re

p = rPEP_Project()
pj = rPEP_scr_Project()
column_list = list()

### Function (used below) to extract the file contents of the identify 1 runs and create a dataframe using those contents ###
def identify1_events(filename):
    df = pd.read_csv(filename, sep='\t')
    df.insert(loc=0, column='identify1_events', value=1, allow_duplicates=True)
    identify1_events = df
    return(identify1_events)

### Function (used below) to extract the file contents of the identify 2 runs and create a dataframe using those contents ###
def identify2_events(filename):
    df1 = pd.read_csv(filename, sep='\t')
    df1.insert(loc=0, column='identify2_events', value=2, allow_duplicates=True)
    identify2_events = df1
    return(identify2_events)

### Function (used below) to extract the file contents of the modulate 1 runs and create a dataframe using those contents ###
def modulate1_events(filename):
    df2 = pd.read_csv(filename, sep='\t')
    df2.insert(loc=0, column='modulate1', value=1, allow_duplicates=True)
    modulate1_events = df2
    return(modulate1_events)

### Function (used below) to extract the file contents of the modulate 1 scr betas and create a dataframe using those contents ###
def modulate1_events_physio(filename):
    df2_physio = pd.read_csv(filename, sep='\t', header=0)
    modulate1_events_physio = df2_physio
    return (modulate1_events_physio)

### Function (used below) to extract the file contents of the modulate 2 runs and create a dataframe using those contents ###
def modulate2_events(filename):
    df3 = pd.read_csv(filename, sep='\t')
    df3.insert(loc=0, column='modulate2', value=2, allow_duplicates=True)
    modulate2_events = df3
    return(modulate2_events)

### Function (used below) to extract the file contents of the modulate 2 physio and create a dataframe using the scr beta contents ###
def modulate2_events_physio(filename):
    df3_physio = pd.read_csv(filename, sep='\t', header=0)
    modulate2_events_physio = df3_physio
    return (modulate2_events_physio)


subjs_list = list()
subj_dict = dict()
num_subjs_list = list()

### For each file in the directory, append the subject number to the subject list ###
for filepath in glob.glob((p.path_bids + '/sub-*'), recursive=True):
    file_split = filepath.split('/')
    subjs = file_split[6]
    subjs_list.append(subjs)
    #print(subjs)

### Take off the strings before the '-' and append the subject number to the list ###
for s in subjs_list:
    numslst = s.split('-')
    nums = numslst[1]
    num_subjs_list.append(nums)

### Collect all the data (identify1, identify2, modulate1, modulate2, and bids paths) from the individual subject directories ###
### Will need paths for AFNI 3dlme ###

def Events_Path_dict():

    ########## objects to create paths by subject directories ###
    sr = '.scaled.resid.nii'
    mod1 = '_task-modulate1'
    mod2 = '_task-modulate2'

    path_dict1 = dict()
    path_dict2 = dict()
    path_list1 = list()
    path_list2 = list()

    ### For every item in the subject list, go through the file names and if the file name matches take the contents of that ###
    ### file and put it into a dataframe ###
    for s in num_subjs_list:

        for filepath1 in glob.glob((p.path_bids + 'sub-*' + '/func' + '/*identify1*events.tsv'), recursive=True):
            if re.fullmatch(filepath1, (p.path_bids + 'sub-' + s + '/func/' + 'sub-' + s + '_task-identify1_events.tsv')):
                identify1_df = identify1_events(filepath1)
            else:
                continue
        for filepath2 in glob.glob((p.path_bids + 'sub-*' + '/func' + '/*identify2*events.tsv'), recursive=True):
            if re.fullmatch(filepath2,(p.path_bids + 'sub-' + s + '/func/' + 'sub-' + s + '_task-identify2_events.tsv')):
                identify2_df = identify2_events(filepath2)
            else:
                continue
        for filepath3 in glob.glob((p.path_bids + 'sub-*' + '/func' + '/*modulate1*events.tsv'), recursive=True):
            if re.fullmatch(filepath3, (p.path_bids + 'sub-' + s + '/func/' + 'sub-' + s + '_task-modulate1_events.tsv')):
                modulate1_df = modulate1_events(filepath3)
            else:
                continue
        for filepath4 in glob.glob((p.path_bids + 'sub-*' + '/func' + '/*modulate2*events.tsv'), recursive=True):
            if re.fullmatch(filepath4, (p.path_bids + 'sub-' + s + '/func/' + 'sub-' + s + '_task-modulate2_events.tsv')):
                modulate2_df = modulate2_events(filepath4)
            else:
                continue
        for filepath7 in glob.glob((pj.path_betas_name + 'sub-' + s + '_mod1ex_betas.csv'), recursive=True):
            if re.fullmatch(filepath7, (pj.path_betas_name + 'sub-' + s + '_mod1ex_betas.csv')):
                modulate1_scr_betas_df = modulate1_events_physio(filepath7)
            else:
                continue
        for filepath8 in glob.glob((pj.path_betas_name + 'sub-' + s + '_mod2ex_betas.csv'), recursive=True):
            if re.fullmatch(filepath8, (pj.path_betas_name + 'sub-' + s + '_mod2ex_betas.csv')):
                modulate2_scr_betas_df = modulate2_events_physio(filepath8)
            else:
               continue

        for filepath in glob.glob((p.path_mri_clean + 'sub-' + s + '/' + 'sub-' + s + mod1 + sr), recursive=True):
            if re.fullmatch(filepath, (p.path_mri_clean + 'sub-' + s + '/' + 'sub-' + s + mod1 + sr)):
                path1 = (p.path_mri_clean + 'sub-' + s + '/' + 'sub-' + s + mod1 + sr)
                path_dict1 = (path1)
                path_list1.append(path_dict1)
            else:
                continue
        for filepath2 in glob.glob((p.path_mri_clean + 'sub-' + s + '/' + 'sub-' + s + mod2 + sr), recursive=True):
            if re.fullmatch(filepath2, (p.path_mri_clean + 'sub-' + s + '/' + 'sub-' + s + mod2 + sr)):
                path2 = (p.path_mri_clean + 'sub-' + s + '/' + 'sub-' + s + mod2 + sr)
                path_dict2 = (path2)
                path_list2.append(path_dict2)
            else:
                continue

     ## Create a dictionary of all the task dataframes ###
        task_path_dict = dict()
        task_path_dict['sub'] = num_subjs_list
        task_path_dict["identify1"] = identify1_df
        task_path_dict["identify2"] = identify2_df
        task_path_dict["modulate1"] = modulate1_df
        vols1_index = modulate1_df.index
        vols1_list = list(vols1_index)
        task_path_dict['vols1'] = vols1_list
        task_path_dict["modulate1_scr_betas"] = modulate1_scr_betas_df
        task_path_dict["modulate2"] = modulate2_df
        vols2_index = modulate2_df.index
        vols2_list = list(vols2_index)
        task_path_dict['vols2'] = vols2_list
        task_path_dict["modulate2_scr_betas"] = modulate2_scr_betas_df
        task_path_dict["path1"] = path_dict1
        task_path_dict["path2"] = path_dict2


    ## For each subject in the subject dictionary, pair the subject to their data ###
        subj_dict[s] = task_path_dict
    return(subj_dict)

subj_dict = Events_Path_dict()


### Now create a new dataframe with only the data you need ###
df_subj_dict = pd.DataFrame()
df_subj_dict_all = pd.DataFrame()
all_tmp_df = pd.DataFrame()

### For each subject in the dictionary, the object is defined by subject, task, etc. Then save those into a dataframe ###
for s in subj_dict:
    trial_type_mod1 = subj_dict[s]['modulate1']['trial_type']
    onset_mod1 = subj_dict[s]['modulate1']['onset']
    duration_mod1 = subj_dict[s]['modulate1']['duration']
    dsgn_onset_mod1 = subj_dict[s]['modulate1']['dsgn_onset']
    dsgn_duration_mod1 = subj_dict[s]['modulate1']['dsgn_duration']
    feedback_mod1 = subj_dict[s]['modulate1']['feedback']
    transparency_mod1 = subj_dict[s]['modulate1']['transparency']
    trial_type_mod2 = subj_dict[s]['modulate2']['trial_type']
    onset_mod2 = subj_dict[s]['modulate2']['onset']
    duration_mod2 = subj_dict[s]['modulate2']['duration']
    dsgn_onset_mod2 = subj_dict[s]['modulate2']['dsgn_onset']
    dsgn_duration_mod2 = subj_dict[s]['modulate2']['dsgn_duration']
    feedback_mod2 = subj_dict[s]['modulate2']['feedback']
    transparency_mod2 = subj_dict[s]['modulate2']['transparency']
    df_subj_dict['trial_type_mod1'] = trial_type_mod1
    df_subj_dict['onset_mod1'] = onset_mod1
    df_subj_dict['duration_mod1'] = duration_mod1
    df_subj_dict['dsgn_onset_mod1'] = dsgn_onset_mod1
    df_subj_dict['dsgn_duration_mod1'] = dsgn_duration_mod1
    df_subj_dict['feedback_mod1'] = feedback_mod1
    df_subj_dict['transparency_mod1'] = transparency_mod1
    df_subj_dict['trial_type_mod2'] = trial_type_mod2
    df_subj_dict['onset_mod2'] = onset_mod2
    df_subj_dict['duration_mod2'] = duration_mod2
    df_subj_dict['dsgn_onset_mod2'] = dsgn_onset_mod2
    df_subj_dict['dsgn_duration_mod2'] = dsgn_duration_mod2
    df_subj_dict['feedback_mod2'] = feedback_mod2
    df_subj_dict['transparency_mod2'] = transparency_mod2
    df_subj_dict['sub'] = s
    df_subj_dict_all = pd.concat([df_subj_dict_all, df_subj_dict])

### Have to combine columns into one using pd.melt. Cannot just use the dataframe you created ###
### with pd.melt. Use a copy of the df so you do not change the original dataframe. Create a name for this new column ###
### then replace the values with intergers to be used in the GLM. Then rename all columns ###

### Combine the feedback columns ###

df_copy = df_subj_dict_all.copy()
pd.set_option("display.max_rows", None, "display.max_columns", None)
df = pd.melt(df_copy, id_vars=['sub'], value_vars=['feedback_mod1','feedback_mod2'])
df1 = df.rename(columns={"variable": "run_f", "value": "feedback"})
df2 = df1.replace(to_replace=['feedback_mod1', 'feedback_mod2'],value=[0,1])
df2.columns = ['sub_f', 'run_f', 'feedback']

### Combine the trial type columns ###
df_copy1 = df_subj_dict_all.copy()
df3 = pd.melt(df_copy1, id_vars=['sub'], value_vars=['trial_type_mod1','trial_type_mod2'])
df4 = df3.rename(columns={"variable": "run_t", "value": "trial_type"})
df5 = df4.replace(to_replace=['trial_type_mod1', 'trial_type_mod2'],value=[0,1])
df5.columns = ['sub_t', 'run_t', 'trial_type']

### Combine the onset columns ###
df_copy2 = df_subj_dict_all.copy()
df6 = pd.melt(df_copy2, id_vars=['sub'], value_vars=['onset_mod1','onset_mod2'])
df7 = df6.rename(columns={"variable": "run_o", "value": "onset"})
df8 = df7.replace(to_replace=['onset_mod1', 'onset_mod2'],value=[0,1])
df8.columns = ['sub_o', 'run_o', 'onset']

### Combine the duration columns ###
df_copy3 = df_subj_dict_all.copy()
df9 = pd.melt(df_copy2, id_vars=['sub'], value_vars=['duration_mod1','duration_mod2'])
df10 = df9.rename(columns={"variable": "run_d", "value": "duration"})
df11 = df10.replace(to_replace=['duration_mod1', 'duration_mod2'],value=[0,1])
df11.columns = ['sub_d', 'run_d', 'duration']

### Combine the dsgn onset columns ###
df_copy4 = df_subj_dict_all.copy()
df12 = pd.melt(df_copy4, id_vars=['sub'], value_vars=['dsgn_onset_mod1','dsgn_onset_mod2'])
df13 = df12.rename(columns={"variable": "run_do", "value": "dsgn_onset"})
df14 = df13.replace(to_replace=['dsgn_onset_mod1', 'dsgn_onset_mod2'],value=[0,1])
df14.columns = ['sub_do', 'run_do', 'dsgn_onset']

### Combine the dsgn duration columns ###
df_copy5 = df_subj_dict_all.copy()
df15 = pd.melt(df_copy5, id_vars=['sub'], value_vars=['dsgn_duration_mod1','dsgn_duration_mod2'])
df16 = df15.rename(columns={"variable": "run_dd", "value": "dsgn_duration"})
df17 = df16.replace(to_replace=['dsgn_duration_mod1', 'dsgn_duration_mod2'],value=[0,1])
df17.columns = ['sub_dd', 'run_dd', 'dsgn_duration']

### Combine the transparency columns ###
df_copy6 = df_subj_dict_all.copy()
df18 = pd.melt(df_copy6, id_vars=['sub'], value_vars=['transparency_mod1','transparency_mod2'])
df19 = df18.rename(columns={"variable": "run_tp", "value": "transparency"})
df20 = df19.replace(to_replace=['transparency_mod1', 'transparency_mod2'],value=[0,1])
df20.columns = ['sub_tp', 'run_tp', 'transparency']

### Join these dataframes ###
df21 = pd.concat([df2, df5], axis=1, ignore_index=False)
df22 = pd.concat([df21, df8], axis=1, ignore_index=False)
df23 = pd.concat([df22, df11], axis=1, ignore_index=False)
df24 = pd.concat([df23, df14], axis=1, ignore_index=False)
df25 = pd.concat([df24, df17], axis=1, ignore_index=False)
df26 = pd.concat([df25, df20], axis=1, ignore_index=False)

### Check to see if the concat operation worked correctly. Then sort the values, only take columns of interest and then rename them ###
df26.loc[(df26['sub_f'] == df26['sub_t']) & (df26['run_f'] == df26['run_t']), 'Status'] = 'Correct'
sfd = df26.sort_values(by=['sub_f','run_f'])
df_feedback = sfd[['sub_t','run_t', 'trial_type', 'feedback', 'onset', 'duration', 'dsgn_onset', 'dsgn_duration', 'transparency']]
df_feedback.columns = ['sub', 'run', 'trial_type', 'feedback', 'onset', 'duration', 'dsgn_onset', 'dsgn_duration', 'transparency']

### Save intermediate data ###
df_feedback.to_csv(p.path_data + 'GLM_feedback_suppress_arouse_mod1_2.csv')

### create a dataframe with only the physio data. Same pattern as above. ###
df_subj_dict1 = pd.DataFrame()
df_subj_dict_all1 = pd.DataFrame()
all_tmp_df1 = pd.DataFrame()

for s in subj_dict:
    physio1_mod1 = subj_dict[s]['modulate1_scr_betas']['trial_type']
    physio2_mod1 = subj_dict[s]['modulate1_scr_betas']['Var2']
    physio1_mod2 = subj_dict[s]['modulate2_scr_betas']['trial_type']
    physio2_mod2 = subj_dict[s]['modulate2_scr_betas']['Var2']
    df_subj_dict1['scr_trial_type_mod1'] = physio1_mod1
    df_subj_dict1['scr_trial_type_mod2'] = physio1_mod2
    df_subj_dict1['beta_mod1'] = physio2_mod1
    df_subj_dict1['beta_mod2'] = physio2_mod2
    df_subj_dict1['sub'] = s
    df_subj_dict_all1 = pd.concat([df_subj_dict_all1, df_subj_dict1])

### Combine the trial type columns ###
df_copy2 = df_subj_dict_all1.copy()
pd.set_option("display.max_rows", None, "display.max_columns", None)
df6 = pd.melt(df_copy2, id_vars=['sub'], value_vars=['scr_trial_type_mod1', 'scr_trial_type_mod2'])
df6 = df6.rename(columns={"variable": "scr_run", "value": "trial_type"})
df6 = df6.replace(to_replace=['scr_trial_type_mod1', 'scr_trial_type_mod2'],value=[0,1])
df6.columns = ['sub_s', 'scr_run', 'trial_type']

### Combine the beta value columns ###
df_copy3 = df_subj_dict_all1.copy()
pd.set_option("display.max_rows", None, "display.max_columns", None)
df7 = pd.melt(df_copy3, id_vars=['sub'], value_vars=['beta_mod1', 'beta_mod2'])
df7 = df7.rename(columns={"variable": "beta_run", "value": "beta"})
df7 = df7.replace(to_replace=['beta_mod1', 'beta_mod2'],value=[0,1])
df7.columns = ['sub_b', 'beta_run', 'beta']

scr_data = pd.concat([df6, df7], axis=1, join='outer', ignore_index=False)

### Check to see if the concat operation worked correctly. Then sort the values, only take columns of interest and then rename them ###
scr_data.loc[(scr_data['sub_s'] == scr_data['sub_b']) & (scr_data['scr_run'] == scr_data['beta_run']), 'Status'] = 'Correct'
scrd = scr_data.sort_values(by=['sub_s','scr_run'])
df_scr = scrd[['sub_s','scr_run', 'trial_type', 'beta']]
df_scr.columns = ['sub', 'run', 'trial_type', 'beta']

### Save intermediate data ###
df_scr.to_csv(p.path_data + 'GLM_scr_mod1_2.csv')






