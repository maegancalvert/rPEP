import pandas as pd
from rPEP.source.rPEP_Project import rPEP_Project
import statsmodels.formula.api as smf


p = rPEP_Project()

### Testing simple effects as suggested in Robinson et al., 2013 ###

### Create list of model parameters ###
df_list = []

### Open CSVs ###
fh = open(p.path_data + 'Engage_conditions.csv')
engage = pd.read_csv(fh, sep=',', index_col=0)
fh1 = open(p.path_data + 'Disengage_conditions.csv')
disengage = pd.read_csv(fh1, sep=',', index_col=0)
fh2 = open(p.path_data + 'Control_only.csv')
control = pd.read_csv(fh2, sep=',', index_col=0)
fh3 = open(p.path_data + 'PTSD_only.csv')
PTSD = pd.read_csv(fh3, sep=',', index_col=0)

pd.set_option('display.max_columns', None, 'display.max_rows', None)

### --------------------------------------------------------------------- ###

### Simple Effects feedback ON and OFF in Engage condition only ###

### --------------------------------------------------------------------- ###
md2 = smf.mixedlm('feedback ~ feedbackcst', engage, groups=engage['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)
del(md2, mdf2, mds2_aic, mds2)

### ---------------------------------------------------------------------- ###
fh = open(p.path_data + 'Engage_conditions.csv')
df1 = pd.read_csv(fh, sep=',', index_col=0)
pd.set_option('display.max_columns', None, 'display.max_rows', None)
print(df1.head())

### --------------------------------------------------------------------- ###

### Simple Effects feedback ON and OFF in Disengage condition only ###

### --------------------------------------------------------------------- ###
md2 = smf.mixedlm('feedback ~ feedbackcst', disengage, groups=disengage['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)
del(md2, mdf2, mds2_aic, mds2)

### --------------------------------------------------------------------- ###

### Simple Effects feedback ON and OFF in the Engage condition only ###

### --------------------------------------------------------------------- ###

md2 = smf.mixedlm('feedback ~ group', engage, groups=engage['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)
del(md2, mdf2, mds2_aic, mds2)

### --------------------------------------------------------------------- ###

### Simple effects feedback ON and OFF in the Disengage condition only ###

### --------------------------------------------------------------------- ###
md2 = smf.mixedlm('feedback ~ group', disengage, groups=disengage['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)
del(md2, mdf2, mds2_aic, mds2)

### --------------------------------------------------------------------- ###

### Simple effects in the Engage vs Disengage Conditions in the Control group ###

### --------------------------------------------------------------------- ###
md2 = smf.mixedlm('feedback ~ arouse_sup', control, groups=control['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)
del(md2, mdf2, mds2_aic, mds2)

### --------------------------------------------------------------------- ###

### Simple effects in the Engage vs Disengage Conditions in the PTSD group ###

### --------------------------------------------------------------------- ###
md2 = smf.mixedlm('feedback ~ arouse_sup', PTSD, groups=PTSD['sub'])
mdf2 = md2.fit()
mds2_aic = mdf2.aic
mds2 = mdf2.summary()
print(mds2)
del(md2, mdf2, mds2_aic, mds2)

