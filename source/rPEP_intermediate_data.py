import pandas as pd
from rPEP_Project import rPEP_Project

p = rPEP_Project()

### ----------------------------------------------------------------- ###

### Hyperplane Distances ###

### ----------------------------------------------------------------- ###

### Open the Hyperplane data file and delete all NANs ###
fh = open(p.path_data + 'GLM_feedback_suppress_arouse_mod1_2.csv')
df1 = pd.read_csv(fh, sep=',', index_col=0)
pd.set_option('display.max_columns', None, 'display.max_rows', None)

### Code trial type into seperate columns ###
df1.loc[(df1['trial_type'] == 'stims_rst'), 'stims_rst'] = '1'
df1.loc[(df1['trial_type'] != 'stims_rst'), 'stims_rst'] = '0'
df1.loc[(df1['trial_type'] == 'instr_fba'), 'instr_fba'] = '1'
df1.loc[(df1['trial_type'] != 'instr_fba'), 'instr_fba'] = '0'
df1.loc[(df1['trial_type'] == 'instr_fbs'), 'instr_fbs'] = '1'
df1.loc[(df1['trial_type'] != 'instr_fbs'), 'instr_fbs'] = '0'
df1.loc[(df1['trial_type'] == 'instr_aro'), 'instr_aro'] = '1'
df1.loc[(df1['trial_type'] != 'instr_aro'), 'instr_aro'] = '0'
df1.loc[(df1['trial_type'] == 'instr_sup'), 'instr_sup'] = '1'
df1.loc[(df1['trial_type'] != 'instr_sup'), 'instr_sup'] = '0'
df1.loc[(df1['trial_type'] == 'stims_fba'), 'stims_fba'] = '1'
df1.loc[(df1['trial_type'] != 'stims_fba'), 'stims_fba'] = '0'
df1.loc[(df1['trial_type'] == 'stims_fbs'), 'stims_fbs'] = '1'
df1.loc[(df1['trial_type'] != 'stims_fbs'), 'stims_fbs'] = '0'
df1.loc[(df1['trial_type'] == 'stims_aro'), 'stims_aro'] = '1'
df1.loc[(df1['trial_type'] != 'stims_aro'), 'stims_aro'] = '0'
df1.loc[(df1['trial_type'] == 'stims_sup'), 'stims_sup'] = '1'
df1.loc[(df1['trial_type'] != 'stims_sup'), 'stims_sup'] = '0'

### Code trial type into Arouse Vs Suppress Columns ###
df1.loc[(df1['trial_type'] == 'stims_rst'), 'arouse_sup'] = '0'
df1.loc[(df1['trial_type'] == 'instr_fba'), 'arouse_sup'] = '0'
df1.loc[(df1['trial_type'] == 'instr_fbs'), 'arouse_sup'] = '0'
df1.loc[(df1['trial_type'] == 'instr_aro'), 'arouse_sup'] = '0'
df1.loc[(df1['trial_type'] == 'instr_sup'), 'arouse_sup'] = '0'
df1.loc[(df1['trial_type'] == 'stims_aro'), 'arouse_sup'] = '1'
df1.loc[(df1['trial_type'] == 'stims_sup'), 'arouse_sup'] = '0'
df1.loc[(df1['trial_type'] == 'stims_fba'), 'arouse_sup'] = '1'
df1.loc[(df1['trial_type'] == 'stims_fbs'), 'arouse_sup'] = '0'

### Code trial type into Suppress columns ###
df1.loc[(df1['trial_type'] == 'stims_rst'), 'suppress'] = '0'
df1.loc[(df1['trial_type'] == 'instr_fba'), 'suppress'] = '0'
df1.loc[(df1['trial_type'] == 'instr_fbs'), 'suppress'] = '0'
df1.loc[(df1['trial_type'] == 'instr_aro'), 'suppress'] = '0'
df1.loc[(df1['trial_type'] == 'instr_sup'), 'suppress'] = '0'
df1.loc[(df1['trial_type'] == 'stims_aro'), 'suppress'] = '0'
df1.loc[(df1['trial_type'] == 'stims_sup'), 'suppress'] = '1'
df1.loc[(df1['trial_type'] == 'stims_fba'), 'suppress'] = '0'
df1.loc[(df1['trial_type'] == 'stims_fbs'), 'suppress'] = '1'

### Code trial type into Feedback On Off Columns ###
df1.loc[(df1['trial_type'] == 'stims_rst'), 'feedbackcst'] = '0'
df1.loc[(df1['trial_type'] == 'instr_fba'), 'feedbackcst'] = '0'
df1.loc[(df1['trial_type'] == 'instr_fbs'), 'feedbackcst'] = '0'
df1.loc[(df1['trial_type'] == 'instr_aro'), 'feedbackcst'] = '0'
df1.loc[(df1['trial_type'] == 'instr_sup'), 'feedbackcst'] = '0'
df1.loc[(df1['trial_type'] == 'stims_aro'), 'feedbackcst'] = '0'
df1.loc[(df1['trial_type'] == 'stims_sup'), 'feedbackcst'] = '0'
df1.loc[(df1['trial_type'] == 'stims_fba'), 'feedbackcst'] = '1'
df1.loc[(df1['trial_type'] == 'stims_fbs'), 'feedbackcst'] = '1'

#print(df1['trial_type'].unique())
df1.to_csv(p.path_data + 'GLM_feedback_suppress_arouse_contrasts.csv')

### Add demographic variables of interest ###
fh1 = open(p.path_bids + 'participants.tsv')
df2 = pd.read_csv(fh1, sep='\t') #, index_col=0)
pd.set_option('display.max_columns', None, 'display.max_rows', None)

### replace control ptsd with integers for GLM ###
df3 = df2.replace(to_replace=['control', 'ptsd'],value=[0,1])

### Select columns of interest and put into dataframe ###
selected_columns = []
selected_columns = df3[['sub', 'age', 'sex', 'group', 'race']]

### Create empty dataframe ###
df4 = pd.DataFrame

### Match subject ids in previous dataframes and merge data on matching subject ids###
for id in df1['sub']:
    str_id = id
    #print(id)
    for sub_id in df3['sub']:
        #print(sub_id)
        if(str_id==sub_id):
            df4 = df1.merge(selected_columns, on='sub',how='left')
#print(df4.isna().sum())

df5 = df4.dropna(axis=0, how='any')
#print(df5.count())

df5.to_csv(p.path_data + 'GLM_feedback_arous_contrasts_demo_.csv')

### Create dataframes for simple slopes testing ###
### Only engage conditions in this dataframe ###
arouse = df5.query('arouse_sup == "1"')[['sub', 'run', 'feedbackcst', 'group', 'feedback']]
arouse.to_csv(p.path_data + 'Engage_conditions.csv')

### Only disengage conditions in this dataframe ###
suppress = df5.query('arouse_sup == "0"')[['sub', 'run', 'feedbackcst', 'group', 'feedback']]
suppress.to_csv(p.path_data + 'Disengage_conditions.csv')

### Only with the control conditions in this dataframe ###
control = df5.query('group == 0')[['sub', 'arouse_sup', 'feedbackcst', 'feedback']]
control.to_csv(p.path_data + 'Control_only.csv')

### Only with the PTSD conditions in this dataframe ###
ptsd = df5.query('group == 1')[['sub', 'arouse_sup', 'feedbackcst', 'feedback']]
ptsd.to_csv(p.path_data + 'PTSD_only.csv')

