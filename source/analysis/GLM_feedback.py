import pandas as pd
import statsmodels.api as sm
import numpy as np
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
from statsmodels.formula.api import ols
import statsmodels.iolib as smlib
from scipy import stats
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from rPEP.source.rPEP_Project import rPEP_Project
from io import StringIO


def prsquared(self):
    return 1 - self.llf / self.llnull

def model_params(self):
    paramsname_list = []
    paramsnum_list = []

    for items in self[0]:
        paramsname_list.append(items)
    for items in self[2]:
        paramsname_list.append(items)
    for items in self[1]:
        paramsnum_list.append(items)
    for items in self[3]:
        paramsnum_list.append(items)
    df3 = pd.DataFrame()
    df3['param_name'] = paramsname_list
    df3['param_num'] = paramsnum_list
    return(df3)

p = rPEP_Project()

###Open the intermediate data file ###
fh = open(p.data_frame)
df1 = pd.read_csv(fh, sep=',', index_col=0)
pd.set_option('display.max_columns', None, 'display.max_rows', None)
print(df1.head())

############################# Descriptives for clinical trials paperwork ##############################################

### Feedback On Only ###
# feedbackon_df = pd.DataFrame()
# feedbackon_df = df1.query('feedbackcst == "1"')[['feedback', 'group']]
#
# ### Feedback Off Only ###
# feedbackoff_df = pd.DataFrame()
# feedbackoff_df = df1.query('feedbackcst == "0"')[['feedback', 'group']]
#
# # print('feedback on', feedbackon_df.describe())
# # print('feedback off', feedbackoff_df.describe())
#
# ### feedback on with ptsd###
# feedbackon_ptsd_df = pd.DataFrame()
# feedbackon_ptsd_df = feedbackon_df.query('group == "1"')[['feedback']]
# # print('feedback on PTSD', feedbackon_ptsd_df.describe())
#
# feedbackoff_ptsd_df = pd.DataFrame()
# feedbackoff_ptsd_df = feedbackoff_df.query('group == "1"')[['feedback']]
# #print('feedback off PTSD', feedbackoff_ptsd_df.describe())
#
# feedbackon_control_df = pd.DataFrame()
# feedbackon_control_df = feedbackon_df.query('group == "0"')[['feedback']]
# #print('feedback on control', feedbackon_control_df.describe())
#
# feedbackoff_control_df = pd.DataFrame()
# feedbackoff_control_df = feedbackoff_df.query('group == "0"')[['feedback']]
# # print('feedback off control', feedbackoff_control_df.describe())

################################################# GLM #################################################################

# scat = sns.lmplot(x='feedback', y='arouse_sup', data=df1, hue='group', palette='Set2')
# plt.show()
#
# scat1 = sns.lmplot(x='feedback', y='arouse_sup', data=df1, hue='feedbackcst', palette='Set2')
# plt.show()


# #### Direct Effects Only GLM ######
# md = smf.glm('feedback ~ arouse_sup + feedbackcst + run + group', df1)
# mdf = md.fit()
# mds_aic = mdf.aic
# mds = mdf.summary()
# print(mds)
# print(mds_aic)
# print(prsquared(mdf))
#
# # scat = sns.scatterplot(x='feedbackcst', y='feedback', data=df1, hue=df1.group, palette='Set2')
# # scat.set_title('Interaction Feedback OFF/ON and PTSD')
# # plt.show()
# #
# # scat = sns.scatterplot(x='feedbackcst', y='feedback', data=df1, hue=df1.arouse_sup, palette='Set2')
# # scat.set_title('Interaction Feedback OFF/ON and Arouse/Suppress ')
# # plt.show()
# #
# # scat = sns.scatterplot(x='group', y='feedback', data=df1, hue=df1.arouse_sup, palette='Set2')
# # scat.set_title('Interaction PTSD and Arouse/Suppress')
# # plt.show()
# #
# # scat = sns.scatterplot(x='group', y='feedback', data=df1, hue=df1.feedbackcst, palette='Set2')
# # scat.set_title('Interaction PTSD and Feedback OFF/ON')
# # plt.show()
#
# # # ### GLM probing interactions ###
md2 = smf.glm('feedback ~ arouse_sup + feedbackcst + group + arouse_sup:feedbackcst + arouse_sup:group + feedbackcst:group', df1)
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)
print(mds2_aic)
print(prsquared(mdf2))

### Testing simple interaction effects using ANOVA ###
lm = smf.ols('feedback ~ arouse_sup', data=df1).fit()
print(lm.summary())

lm1 = smf.ols('feedback ~ arouse_sup + arouse_sup:feedbackcst', data=df1).fit()
print(lm1.summary())

lm2 = smf.ols('feedback ~ arouse_sup + feedbackcst', data=df1).fit()
print(lm2.summary())

lm3 = smf.ols('feedback ~ arouse_sup * feedbackcst', data=df1).fit()
print(lm3.summary())

# effect of feedbackcst on slope or intercept #
table1 = anova_lm(lm, lm3)
print(table1)
# effect of feedbackcst on intercept #
table2 = anova_lm(lm, lm2)
print(table2)
# effect of feedbackcst on slope #
table3 = anova_lm(lm, lm1)
print(table3)
# effect of feedbackcst on slope and intercept #
table4 = anova_lm(lm1, lm3)
print(table4)

lm = smf.ols('feedback ~ arouse_sup', data=df1).fit()
print(lm.summary())

lm1 = smf.ols('feedback ~ arouse_sup + arouse_sup:group', data=df1).fit()
print(lm1.summary())

lm2 = smf.ols('feedback ~ arouse_sup + group', data=df1).fit()
print(lm2.summary())

lm3 = smf.ols('feedback ~ arouse_sup * group', data=df1).fit()
print(lm3.summary())

# effect of group on slope or intercept #
table1 = anova_lm(lm, lm3)
print(table1)
# effect of group on intercept #
table2 = anova_lm(lm, lm2)
print(table2)
# effect of group on slope #
table3 = anova_lm(lm, lm1)
print(table3)
# effect of group on slope and intercept #
table4 = anova_lm(lm1, lm3)
print(table4)
 ### Interactions using ANCOVA but not able to use between group variable ###
# ancova = sm.stats.AnovaRM(df1, depvar='feedback', subject='group', within=['arouse_sup', 'feedbackcst'], aggregate_func='mean')
# print(ancova.fit())

### Testing simple effects via Robinson et al., 2013 ###

### PTSD only dataframe ###
ptsd_df = pd.DataFrame()
ptsd_df = df1.query('group == 1')[['sub','feedbackcst', 'group', 'arouse_sup', 'feedback']]
ptsd_df.to_csv(p.path_data + 'ptsd_hyp.csv')

df_list = []

### Simple effects feedback by arouse in PTSD ###
md2 = smf.mixedlm('feedback ~ arouse_sup', ptsd_df, groups=ptsd_df['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()

### add summary info to df list ###
name = 'hyperplane distance by arouse/suppress in PTSD group'
df_list.append(name)
PTSD_se_fbarosup_mparams_df = mds2.tables[0]
params = model_params(PTSD_se_fbarosup_mparams_df)
params.to_csv(p.path_results + 'PTSD_se_fbarosup_mparams_df.csv')
df_list.append(params)
PTSD_se_fbarosup_est_df = mds2.tables[1]
PTSD_se_fbarosup_est_df.to_csv(p.path_results + 'PTSD_se_fbarosup_est_df.csv')
df_list.append(PTSD_se_fbarosup_est_df)
del(md2, mdf2, mds2_aic, mds2)

### Control only dataframe ###
control_df = pd.DataFrame()
control_df = df1.query('group == 0')[['sub','feedbackcst', 'group', 'arouse_sup', 'feedback']]
control_df.to_csv(p.path_data + 'control_hyp.csv')

### Simple effects feedback by arouse in Control ###
md2 = smf.mixedlm('feedback ~ arouse_sup', control_df, groups=control_df['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()

### add summary info to df list ###
name = 'hyperplane distance by arouse/suppress in control group'
df_list.append(name)
Control_se_fbarosup_mparams_df = mds2.tables[0]
params = model_params(Control_se_fbarosup_mparams_df)
params.to_csv(p.path_results + 'Control_se_fbarosup_mparams_df.csv')
df_list.append(params)
Control_se_fbarosup_est_df = mds2.tables[1]
Control_se_fbarosup_est_df.to_csv(p.path_results + 'Control_se_fbarosup_est_df.csv')
df_list.append(Control_se_fbarosup_est_df)
del(md2, mdf2, mds2_aic, mds2)

### Simple Effects feedback by feedback contrast in PTSD ###
md2 = smf.mixedlm('feedback ~ feedbackcst', ptsd_df, groups=ptsd_df['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()

### add summary info to df list ###
name = 'hyperplane distance by feedbackcst in PTSD group'
df_list.append(name)
PTSD_se_fbfb_mparams_df = mds2.tables[0]
params = model_params(PTSD_se_fbfb_mparams_df)
params.to_csv(p.path_results + 'PTSD_se_fbfb_mparams_df.csv')
df_list.append(params)
PTSD_se_fbfb_est_df = mds2.tables[1]
PTSD_se_fbfb_est_df.to_csv(p.path_results + 'PTSD_se_fbfb_est_df.csv')
df_list.append(PTSD_se_fbfb_est_df)
del(md2, mdf2, mds2_aic, mds2)

### Simple Effects feedback by feedbackcst in Control ###
md2 = smf.mixedlm('feedback ~ feedbackcst', control_df, groups=control_df['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()

### add summary info to df list ###
name = 'hyperplane distance by feedbackcst in Control group'
df_list.append(name)
Control_se_fbfb_mparams_df = mds2.tables[0]
params = model_params(Control_se_fbfb_mparams_df)
params.to_csv(p.path_results + 'Control_se_fbfb_mparams_df.csv')
df_list.append(params)
Control_se_fbfb_est_df = mds2.tables[1]
Control_se_fbfb_est_df.to_csv(p.path_results + 'Control_se_fbfb_est_df.csv')
df_list.append(Control_se_fbfb_est_df)
del(md2, mdf2, mds2_aic, mds2)

### Create dataframe with arouse only ###
arouse_df = pd.DataFrame()
arouse_df = df1.query('arouse_sup == 1')[['sub','feedbackcst', 'group', 'arouse_sup', 'feedback']]
arouse_df.to_csv(p.path_data + 'arouse_hyp.csv')

### Create dataframe with only suppress ###
sup_df = pd.DataFrame()
sup_df = df1.query('arouse_sup == 0')[['sub','feedbackcst', 'group', 'arouse_sup', 'feedback']]
sup_df.to_csv(p.path_data + 'sup_hyp.csv')

### Simple Effects feedback by feedback contrast in arouse only ###
md2 = smf.mixedlm('feedback ~ feedbackcst', arouse_df, groups=arouse_df['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()

### add summary info to df list ###
name = 'hyperplane distance by feedbackcst in arouse condition'
df_list.append(name)
Arouse_se_fbfb_mparams_df = mds2.tables[0]
params = model_params(Arouse_se_fbfb_mparams_df)
params.to_csv(p.path_results + 'Arouse_se_fbfb_mparams_df.csv')
df_list.append(params)
Arouse_se_fbfb_est_df = mds2.tables[1]
Arouse_se_fbfb_est_df.to_csv(p.path_results + 'Arouse_se_fbfb_est_df.csv')
df_list.append(Arouse_se_fbfb_est_df)
del(md2, mdf2, mds2_aic, mds2)

### Simple effects feedback by feedback contrast in suppress only ###
md2 = smf.mixedlm('feedback ~ feedbackcst', sup_df, groups=sup_df['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### add summary info to df list ###
name = 'hyperplane distance by feedbackcst in suppress condition'
df_list.append(name)
Suppress_se_fbfb_mparams_df = mds2.tables[0]
params = model_params(Suppress_se_fbfb_mparams_df)
params.to_csv(p.path_results + 'Suppress_se_fbfb_mparams_df.csv')
df_list.append(params)
Suppress_se_fbfb_est_df = mds2.tables[1]
Suppress_se_fbfb_est_df.to_csv(p.path_results + 'Suppress_se_fbfb_est_df.csv')
df_list.append(Suppress_se_fbfb_est_df)
del(md2, mdf2, mds2_aic, mds2)

### Simple effects feedback by Group in Arouse only ###
md2 = smf.mixedlm('feedback ~ group', arouse_df, groups=arouse_df['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### add summary info to df list ###
name = 'hyperplane distance by group in arouse condition'
df_list.append(name)
arouse_se_fbgroup_mparams_df = mds2.tables[0]
params = model_params(arouse_se_fbgroup_mparams_df)
params.to_csv(p.path_results + 'arouse_se_fbgroup_mparams_df.csv')
df_list.append(params)
arouse_se_fbgroup_est_df = mds2.tables[1]
arouse_se_fbgroup_est_df.to_csv(p.path_results + 'arouse_se_fbgroup_est_df.csv')
df_list.append(arouse_se_fbgroup_est_df)
del(md2, mdf2, mds2_aic, mds2)

### Simple effects feedback by Group in Suppress only ###
md2 = smf.mixedlm('feedback ~ group', sup_df, groups=sup_df['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)

### add summary info to df list###
name = 'hyperplane distance by group in suppress condition'
df_list.append(name)
suppress_se_fbgroup_mparams_df = mds2.tables[0]
params = model_params(suppress_se_fbgroup_mparams_df)
params.to_csv(p.path_results + 'suppress_se_fbgroup_mparams_df.csv')
df_list.append(params)
suppress_se_fbgroup_est_df = mds2.tables[1]
suppress_se_fbgroup_est_df.to_csv(p.path_results + 'suppress_se_fbgroup_est_df.csv')
df_list.append(suppress_se_fbgroup_est_df)
del(md2, mdf2, mds2_aic, mds2)


# # # # # # ## Multi-level Model for Individual Subject Grouping ###
# md3 = smf.mixedlm('feedback ~ arouse_sup + feedbackcst + run + group', df1, groups=df1['sub'])
# mdf3 = md3.fit()
# mds3_aic = mdf3.aic
# mds3 = mdf3.summary()
# print(mds3)
# print(mds3_aic)
# print(mdf3.pvalues)
#
# # # # # # # ### Multi-level Model for Individual Subjects and interactions ###
# endog = df1['feedback']
# exog = [df1['arouse_sup'], df1['feedbackcst'], df1['run'], df1['group']]
# group = df1['group']
#
# md4 = smf.mixedlm('feedback ~ 1 + arouse_sup + feedbackcst + run + group + arouse_sup:feedbackcst + arouse_sup:group + feedbackcst:group + arouse_sup:feedbackcst:group', df1, groups=df1['sub'])
# cmd4 = smf.mixedlm
# mdf4 = md4.fit()
# mds4 = mdf4.summary()
# mds4_aic = mdf4.aic
# print(mds4)
# print(mds4_aic)
# print(mdf4.pvalues)
# print(mdf4.params)


# # ### Save output to file ###
# # f = open('/home/mcalvert/workspace/results/rPEP/GLM_feedback.txt', 'w')
# # f.write(str(mds))
# # f.write(str('\n'))
# # f.write(str(mds_aic))
# # f.write(str('\n'))
# # f.write(str(mds1))
# # f.write(str('\n'))
# # f.write(str(mds1_aic))
# # f.write(str('\n'))
# # f.write(str(mds2))
# # f.write(str('\n'))
# # f.write(str(mds2_aic))
# # f.write(str('\n'))
# # f.write(str('\n'))
# # f.write(str('Multi-level Model for Individual Subjects convergence warning'))
# # f.write(str(mds3))
# # f.write(str('\n'))
# # f.write(str(mds3_aic))
# # f.write(str('\n'))
# # f.write(str('Multi-level Model for Individual Subjects and interactions is on the boundary of the parameter space'))
# # f.write(str('\n'))
# # f.write(str(mds4))
# # f.write(str('\n'))
# # f.write(str(mds4_aic))
# # f.write(str('\n'))
# # f.write(str(mdf4.pvalues))
# # f.write(str('Multi-level Model for Individual Subjects, interactions, and controling for main effects is on the boundary of the parameter space'))
# # f.write(str('\n'))
# # f.write(str('\n'))
# # f.write(str(mds5))
# # f.write(str('\n'))
# # f.write(str(mds5_aic))
# # f.write(str('\n'))
# # f.write(str(mdf5.pvalues))
# # f.close()
# # #
# # #
# # #  ########################################################################################################################

rabbit_df = pd.DataFrame()
rabbit_df = df1.query('group == 1')[['sub','group','suppress', 'feedback']]

rabbit_df2 = pd.DataFrame()
rabbit_df2 = df1.query('group == 0')[['sub', 'group', 'suppress', 'feedback']]





