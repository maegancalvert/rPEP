import pandas as pd
import statsmodels.formula.api as smf
from rPEP.source.rPEP_Project import rPEP_Project

p = rPEP_Project()

### Open the SCR data file and delete all NANs ###
fh = open(p.path_data + "GLM_scr_mod1_2.csv")
df1_physio = pd.read_csv(fh, sep=",", index_col=0)
pd.set_option('display.max_columns', None, 'display.max_rows', None)
df2_physio = df1_physio.dropna()

### Add demographic variables of interest ###
fh1 = open(p.path_subj_list)
df3_demo = pd.read_csv(fh1, sep='\t')
pd.set_option('display.max_columns', None, 'display.max_rows', None)
df4_demo = df3_demo.replace(to_replace=['control', 'ptsd'],value=[0,1])

### Integrate SCR data frame with demographic data frame ###
selected_columns = []
selected_columns = df4_demo[['sub', 'age', 'sex', 'group', 'race']]

for id in df4_demo['sub']:
    str_id = str(id)
    sub_cnt = 0
    for sub_id in df2_physio['sub']:
        if(id==sub_id):
            sub_cnt = sub_cnt +1
            df5_combined = df2_physio.merge(selected_columns, on='sub',how='left')
    # print(id, sub_cnt)

### Make sure have the right number of rows for each participant ###
for id in df4_demo['sub']:
    sub_cnt2 = 0
    for sub_id2 in df5_combined['sub']:
        if(id==sub_id2):
            sub_cnt2 = sub_cnt2 + 1
    # print(id, sub_cnt2)

# print(df5_combined.columns)

### All conditions are coded 1s and 0s ###
df5_combined.loc[(df5_combined['trial_type'] == 'stims_aro'), 'arouse_sup'] = '1'
df5_combined.loc[(df5_combined['trial_type'] == 'stims_sup'), 'arouse_sup'] = '0'
df5_combined.loc[(df5_combined['trial_type'] == 'stims_fba'), 'arouse_sup'] = '1'
df5_combined.loc[(df5_combined['trial_type'] == 'stims_fbs'), 'arouse_sup'] = '0'
df5_combined.loc[(df5_combined['trial_type'] == 'stims_rst'), 'arouse_sup'] = '0'
df5_combined.loc[(df5_combined['trial_type'] == 'instr_fba'), 'arouse_sup'] = '1'
df5_combined.loc[(df5_combined['trial_type'] == 'instr_fbs'), 'arouse_sup'] = '0'
df5_combined.loc[(df5_combined['trial_type'] == 'instr_aro'), 'arouse_sup'] = '1'
df5_combined.loc[(df5_combined['trial_type'] == 'instr_sup'), 'arouse_sup'] = '0'

df5_combined.loc[(df5_combined['trial_type'] == 'stims_aro'), 'feedbackcst'] = '0'
df5_combined.loc[(df5_combined['trial_type'] == 'stims_sup'), 'feedbackcst'] = '0'
df5_combined.loc[(df5_combined['trial_type'] == 'stims_fba'), 'feedbackcst'] = '1'
df5_combined.loc[(df5_combined['trial_type'] == 'stims_fbs'), 'feedbackcst'] = '1'
df5_combined.loc[(df5_combined['trial_type'] == 'stims_rst'), 'feedbackcst'] = '0'
df5_combined.loc[(df5_combined['trial_type'] == 'instr_fba'), 'feedbackcst'] = '1'
df5_combined.loc[(df5_combined['trial_type'] == 'instr_fbs'), 'feedbackcst'] = '1'
df5_combined.loc[(df5_combined['trial_type'] == 'instr_aro'), 'feedbackcst'] = '0'
df5_combined.loc[(df5_combined['trial_type'] == 'instr_sup'), 'feedbackcst'] = '0'

df5_combined.to_csv(p.path_data + 'GLM_physio_arouse_contrasts_demo.csv')

### Create Data Frames for each condition ###

PTSD_beta = df5_combined.query('group == "1"')[['beta']]
Control_beta = df5_combined.query('group == "0"')[['beta']]
Run1_beta = df5_combined.query('run == "0"')[['beta']]
Run2_beta = df5_combined.query('run == "1"')[['beta']]
Engage_beta = df5_combined.query('arouse_sup == "1"')[['beta']]
Disengage_beta = df5_combined.query('arouse_sup == "0"')[['beta']]
Fdbk_on_beta = df5_combined.query('feedbackcst == "1"')[['beta']]
Fdbk_off_beta = df5_combined.query('feedbackcst == "0"')[['beta']]

### --------------------------------------------------------------------- ###

### Simple Effects feedback ON and OFF in Engage condition only ###

### --------------------------------------------------------------------- ###

md2 = smf.mixedlm('beta ~ feedbackcst', Engage_beta, groups=Engage_beta['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### --------------------------------------------------------------------- ###

### Simple Effects feedback ON and OFF in Disengage condition only ###

### --------------------------------------------------------------------- ###

md2 = smf.mixedlm('beta ~ feedbackcst', Disengage_beta, groups=Disengage_beta['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### --------------------------------------------------------------------- ###

### Simple effects in the Control vs PTSD groups in the Engage Condition ###

### --------------------------------------------------------------------- ###

md2 = smf.mixedlm('beta ~ group', Engage_beta, groups=Engage_beta['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### --------------------------------------------------------------------- ###

### Simple effects in the Control vs PTSD groups in the Engage Condition ###

### --------------------------------------------------------------------- ###

md2 = smf.mixedlm('beta ~ group', Disengage_beta, groups=Disengage_beta['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### --------------------------------------------------------------------- ###

### Simple effects in the Engage vs Disengage condition in the Control Condition ###

### --------------------------------------------------------------------- ###

md2 = smf.mixedlm('beta ~ arouse_sup', Control_beta, groups=Control_beta['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### --------------------------------------------------------------------- ###

### Simple effects in the Engage vs Disengage condition in the PTSD Condition ###

### --------------------------------------------------------------------- ###

md2 = smf.mixedlm('beta ~ arouse_sup', Disengage_beta, groups=Disengage_beta['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### --------------------------------------------------------------------- ###

### Simple effects in the Feedback On vs Off conditions in the Control Condition ###

### --------------------------------------------------------------------- ###

md2 = smf.mixedlm('beta ~ feedbackcst', Control_beta, groups=Control_beta['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### --------------------------------------------------------------------- ###

### Simple effects in the Feedback On vs Off conditions in the PTSD Condition ###

### --------------------------------------------------------------------- ###

md2 = smf.mixedlm('beta ~ feedbackcst', PTSD_beta, groups=PTSD_beta['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)




