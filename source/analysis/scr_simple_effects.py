import pandas as pd
import statsmodels.formula.api as smf
from rPEP.source.rPEP_Project import rPEP_Project

p = rPEP_Project()

### Open the SCR data file and delete all NANs ###
fh = open(p.path_data + "GLM_physio_arouse_contrasts_demo.csv")
physio = pd.read_csv(fh, sep=",", index_col=0)
pd.set_option('display.max_columns', None, 'display.max_rows', None)

### Create Data Frames for each condition ###

PTSD_beta = physio.query('group == 1')[['beta', 'sub', 'feedbackcst', 'arouse_sup']]
Control_beta = physio.query('group == 0')[['beta', 'sub', 'feedbackcst', 'arouse_sup']]
Run1_beta = physio.query('run == 0')[['beta', 'sub', 'feedbackcst', 'arouse_sup', 'group']]
Run2_beta = physio.query('run == 1')[['beta', 'sub', 'feedbackcst', 'arouse_sup', 'group']]
Engage_beta = physio.query('arouse_sup == 1')[['beta', 'sub', 'feedbackcst', 'group']]
Disengage_beta = physio.query('arouse_sup == 0')[['beta', 'sub', 'feedbackcst', 'group']]
Fdbk_on_beta = physio.query('feedbackcst == 1')[['beta', 'sub', 'group', 'arouse_sup']]
Fdbk_off_beta = physio.query('feedbackcst == 0')[['beta', 'sub', 'group', 'arouse_sup']]


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

md2 = smf.mixedlm('beta ~ arouse_sup', PTSD_beta, groups=PTSD_beta['sub'])
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