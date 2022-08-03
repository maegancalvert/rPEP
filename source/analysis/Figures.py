import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from rPEP.source.rPEP_Project import rPEP_Project
from rPEP.source.Gather_events_data import Events_Path_dict

p = rPEP_Project()

subj_dict = Events_Path_dict()

### Read in dataframe with participant data ###
fh = open(p.data_frame)
df = pd.read_csv(fh, sep=',', index_col=0)
pd.set_option('display.max_columns', None, 'display.max_rows', None)

df4_participants = pd.read_csv(p.path_subj_list, sep='\t', header=0, dtype={'sub':'string'})

### Read in subject dictionary to get number of vols per run ###
df_vols = pd.DataFrame()
df_vols_all = pd.DataFrame()
for s in subj_dict:
    df_vols['vols1'] = pd.Series(subj_dict[s]['vols1'])
    df_vols['vols2'] = pd.Series(subj_dict[s]['vols2'])
    df_vols['trial_type_1'] = pd.Series(subj_dict[s]['modulate1']['trial_type'])
    df_vols['feedback1'] = pd.Series(subj_dict[s]['modulate1']['feedback'])
    df_vols['trial_type_2'] = pd.Series(subj_dict[s]['modulate2']['trial_type'])
    df_vols['feedback2'] = pd.Series(subj_dict[s]['modulate2']['feedback'])
    df_vols['sub'] = s
    df_vols_all = pd.concat([df_vols_all, df_vols])

### Set contrasts ###
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_rst'), 'feedbackcst_1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_fin'), 'feedbackcst_1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'instr_fba'), 'feedbackcst_1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'instr_fbs'), 'feedbackcst_1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'instr_aro'), 'feedbackcst_1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'instr_sup'), 'feedbackcst_1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_aro'), 'feedbackcst_1'] = -1
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_sup'), 'feedbackcst_1'] = -1
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_fba'), 'feedbackcst_1'] = 1
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_fbs'), 'feedbackcst_1'] = 1

df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_rst'), 'feedbackcst_2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_fin'), 'feedbackcst_2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'instr_fba'), 'feedbackcst_2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'instr_fbs'), 'feedbackcst_2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'instr_aro'), 'feedbackcst_2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'instr_sup'), 'feedbackcst_2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_aro'), 'feedbackcst_2'] = -1
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_sup'), 'feedbackcst_2'] = -1
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_fba'), 'feedbackcst_2'] = 1
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_fbs'), 'feedbackcst_2'] = 1

df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_rst'), 'tr_recode1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_fin'), 'tr_recode1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'instr_fba'), 'tr_recode1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'instr_fbs'), 'tr_recode1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'instr_aro'), 'tr_recode1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'instr_sup'), 'tr_recode1'] = 0
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_aro'), 'tr_recode1'] = 1
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_sup'), 'tr_recode1'] = -1
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_fba'), 'tr_recode1'] = 1
df_vols_all.loc[(df_vols_all['trial_type_1'] == 'stims_fbs'), 'tr_recode1'] = -1

df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_rst'), 'tr_recode2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_fin'), 'tr_recode2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'instr_fba'), 'tr_recode2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'instr_fbs'), 'tr_recode2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'instr_aro'), 'tr_recode2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'instr_sup'), 'tr_recode2'] = 0
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_aro'), 'tr_recode2'] = 1
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_sup'), 'tr_recode2'] = -1
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_fba'), 'tr_recode2'] = 1
df_vols_all.loc[(df_vols_all['trial_type_2'] == 'stims_fbs'), 'tr_recode2'] = -1

df_vols_2 = df_vols_all.reset_index()

### Merge dataframes ###

for id in df_vols_2['sub']:
    for sub_id in df4_participants['sub']:
        if(id==sub_id):
            df_vols_grp = df_vols_2.merge(df4_participants, on='sub',how='left')

### Set palette for seaborn ###

palette = sns.color_palette("gnuplot2_r")
sns.set_palette(palette)

### Hyperplane Distances rt-fmri-nf figure ###
### Run 3 ###
sns.set_theme(style='white', palette=palette)
sns.lineplot(x='vols1', y='feedbackcst_1', data=df_vols_grp, color=palette[3], label='Feedback ON/OFF')
sns.lineplot(x='vols1', y='tr_recode1', data=df_vols_grp,ls='dashed', dashes=[(10,10)], color=palette[5], label='Engage vs Disengage')
sns.lineplot(x='vols1', y='feedback1', data=df_vols_grp, color=palette[0-1], hue='group')
plt.title("Hyperplane Distances by TR, Feedback, and Condition for Run 3")
plt.xlabel('Volumes')
plt.ylabel('Hyperplane Distances')
plt.yticks([-1,1],['Feedback OFF \n Disengage','Feedback ON \n Engage'])
plt.legend(labels=['Feedback ON/OFF', 'Engage vs Disengage', 'Hyperplane Control','Hyperplane PTSD'], loc=1)
plt.savefig(p.path_fig + 'Run3.png')
plt.show()

### Hyperplane Distances rt-fmri-nf figure ###
### Run 4 ###
sns.set_theme(style='white', palette=palette)
sns.lineplot(x='vols1', y='feedbackcst_2', data=df_vols_grp, color=palette[3], label='Feedback ON/OFF')
sns.lineplot(x='vols1', y='tr_recode2', data=df_vols_grp,ls='dashed', dashes=[(10,10)], color=palette[5], label='Engage vs Disengage')
sns.lineplot(x='vols1', y='feedback2', data=df_vols_grp, color=palette[0-1], hue='group')
plt.title("Hyperplane Distances by TR, Feedback, and Condition for Run 4")
plt.xlabel('Volumes')
plt.ylabel('Hyperplane Distances')
plt.yticks([-1,1],['Feedback OFF \n Disengage','Feedback ON \n Engage'])
plt.legend(labels=['Feedback ON/OFF', 'Engage vs Disengage', 'Hyperplane Control','Hyperplane PTSD'],loc=1)
plt.savefig(p.path_fig + 'Run4.png')
plt.show()


### Change color palette ###
palette2=sns.color_palette('magma', 7)
colors = [palette2[0], palette2[4]]
# sns.palplot(palette2)
# sns.palplot(colors)

### Interactions by Hyperplane Distances ###
scat = sns.lmplot(x='feedback', y='arouse_sup', data=df, hue='group', palette=colors, legend=False)
scat.set(title="Hyperplane Distances by Disengage versus Engage Separated by Group",
         xlabel='Hyperplane Distance',
        ylabel='Condition')
plt.legend(labels=['Control', 'PTSD'], loc=2)
plt.yticks([0,1],['Disengage','Engage'])
plt.show()
scat.savefig(p.path_fig + 'HyperplaneXConditionforGroup.png')
plt.clf()

scat1 = sns.lmplot(x='feedback', y='arouse_sup', data=df, hue='feedbackcst', palette=colors, legend=False)
scat1.set(title="Hyperplane Distances by Disengage versus Engage Separated by Feedback OFF and ON",
          xlabel='Hyperplane Distance',
        ylabel='Condition')
plt.yticks([0,1],['Disengage','Engage'])
plt.legend(labels=['Feedback OFF', 'Feedback ON'], loc=2)
plt.show()
scat1.savefig(p.path_fig + 'HyperplaneXConditionforFeedback.png')
plt.clf()

### SCR interactions ###
fh = open(p.path_data + 'GLM_physio_arouse_contrasts_demo.csv')
df1 = pd.read_csv(fh, sep=',', index_col=0)

scat2 = sns.lmplot(x='beta', y='arouse_sup', data=df1, hue='feedbackcst', palette=colors, legend=False)
scat2.set(title= "SCR by Disengage versus Engage Separated by Feedback OFF and ON",
          xlabel='Skin Conductance Response',
        ylabel='Condition')
plt.yticks([0,1],['Disengage','Engage'])
plt.legend(labels=['Feedback OFF', 'Feedback ON'], loc=2)
plt.show()
scat2.savefig(p.path_fig + 'SCRXConditionforFeedback.png')

scat3 = sns.lmplot(x='beta', y='feedbackcst', data=df1, hue='group', palette=colors, legend=False)
scat3.set(title="SCR by Feedback OFF and ON Separated by Group",
          xlabel='Skin Conductance Response',
        ylabel='Feedback')
plt.yticks([0,1],['OFF','ON'])
plt.legend(labels=['Control', 'PTSD'], loc=2)
plt.show()
scat3.savefig(p.path_fig + 'SCRXFeedbackforGroup.png')

scat4 = sns.lmplot(x='beta', y='arouse_sup', data=df1, hue='group', palette=colors, legend=False)
scat4.set(title="SCR by Disengage versus Engage Separated by Group",
         xlabel='Skin Conductance Response',
        ylabel='Condition')
plt.yticks([0,1],['Disengage','Engage'])
plt.legend(labels=['Control', 'PTSD'], loc=2)
plt.show()
scat4.savefig(p.path_fig + 'SCRXConditionforGroup.png')
