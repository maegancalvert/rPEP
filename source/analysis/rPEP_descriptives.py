import pandas as pd
from rPEP.source.rPEP_Project import rPEP_Project
import re
import numpy as np
from scipy import stats

p = rPEP_Project()

### Split function ###
def split(part_num):
    return [char for char in part_num]

### Open participants tsv file ###
fh = open(p.path_bids + 'participants.tsv')
pd.set_option("display.max_rows", None, "display.max_columns", None)
df = pd.read_csv(fh, delimiter='\t')

### Define race coding ###
df.loc[(df['race'] == 1), 'Race'] = 'White'
df.loc[(df['race'] == 2), 'Race'] = 'Black'
df.loc[(df['race'] == 3), 'Race'] = 'Asian'
df.loc[(df['race'] == 4), 'Race'] = 'Native American'
df.loc[(df['race'] == 5), 'Race'] = 'Hispanic, Latino'
df.loc[(df['race'] == 6), 'Race'] = 'Pacific Islander'
df.loc[(df['race'] == 7), 'Race'] = 'Other'

### Open clinical data ###
fh = open(p.path_data + 'RPEP_clinical_data.csv')
df1 = pd.read_csv(fh, delimiter=',')

### Only include these columns ###
df2 = df1[['rpep_participantid', 'dcf_age', 'dcf_race', 'dcf_education', 'dcf_handedness', 'dcf_psychotropic_meds',
                      'dcf_drug_user', 'dcf_fam_hist_diag', 'dcf_fam_hist_drugs', 'physicalassult_1', 'physicalassult_1a',
                      'physicalassult_2', 'physicalassult_2a', 'physicalassult_3', 'physicalassult_3a',
                      'physicalassult_4', 'physicalassult_4a', 'physicalassult_5', 'physicalassult_5a',
                      'physicalabuse_1', 'physicalabuse_2', 'physicalabuse_3', 'physicalabuse_4', 'physicalabuse_5',
                      'physicalabuse_6', 'physicalabuse_7', 'physicalabuse_8', 'physicalabuse_9', 'physicalabuse_10',
                      'physicalabuse_11', 'sexualassult_1', 'sexualassult_2', 'sexualassult_3', 'sexualassult_4',
                      'sexualassult_5', 'domesticviolence_1', 'domesticviolence_2', 'domesticviolence_3',
                      'domesticviolence_4', 'domesticviolence_5', 'domesticviolence_6', 'communityviolence_1',
                      'communityviolence_2', 'communityviolence_3', 'communityviolence_4', 'communityviolence_5',
                      'communityviolence_6', 'bdi2_1', 'bdi2_2', 'bdi2_3', 'bdi2_4', 'bdi2_5', 'bdi2_6', 'bdi2_7',
                      'bdi2_8', 'bdi2_9', 'bdi2_10', 'bdi2_11', 'bdi2_12', 'bdi2_13', 'bdi2_14', 'bdi2_15', 'bdi2_16',
                      'bdi2_17', 'bdi2_18', 'bdi2_19', 'bdi2_20', 'bdi2_21','ctq_1', 'ctq_2', 'ctq_3', 'ctq_4', 'ctq_5',
                      'ctq_6', 'ctq_7', 'ctq_8', 'ctq_9', 'ctq_10', 'ctq_11', 'ctq_12', 'ctq_13', 'ctq_14', 'ctq_15',
                      'ctq_16', 'ctq_17', 'ctq_18', 'ctq_19', 'ctq_20', 'ctq_21', 'ctq_22', 'ctq_23', 'ctq_24', 'ctq_25',
                      'ctq_26', 'ctq_27', 'ctq_28', 'ders_1_rs', 'ders_2_rs', 'ders3', 'ders4', 'ders5', 'ders_6_rs',
                      'ders_7_rs', 'ders_8_rs', 'ders9', 'ders_10_rs', 'ders11', 'ders12', 'ders13', 'ders14',
                      'ders15', 'ders16', 'ders_17_rs', 'ders18', 'ders19', 'ders_20_rs', 'ders21', 'ders_22_rs',
                      'ders23', 'ders_24_rs', 'ders25', 'ders26', 'ders27', 'ders28', 'ders29', 'ders30', 'ders31',
                      'ders32', 'ders33', 'ders_34_rs', 'ders35', 'ders36', 'panas_1', 'panas_2', 'panas_3', 'panas_4',
                      'panas_5', 'panas_6', 'panas_7', 'panas_8', 'panas_9', 'panas_10', 'panas_11', 'panas_12',
                      'panas_13', 'panas_14', 'panas_15', 'panas_16', 'panas_17', 'panas_18', 'panas_19', 'panas_20',
                      'pcl_1', 'pcl_2', 'pcl_3', 'pcl_4', 'pcl_5', 'pcl_6', 'pcl_7', 'pcl_8', 'pcl_9', 'pcl_10',
                      'pcl_11', 'pcl_12', 'pcl_13', 'pcl_14', 'pcl_15', 'pcl_16', 'pcl_17', 'pcl_18',
                      'pcl_19', 'pcl_20','sud_alcohol_life', 'sud_alcohol_pastmonth', 'sud_sed_hyp_anx_life','sud_sed_hyp_anx_pastmonth',
                      'sud_cannabis_life', 'sud_cannabis_pastmonth', 'sud_stimulants_life', 'sud_stimulants_pastmonth',
                      'sud_opioid_life', 'sud_opioid_pastmonth', 'sud_cocaine_life', 'sud_cocaine_pastmonth', 'sud_hall_pcp_life',
                      'sud_hall_pcp_pastmonth', 'sud_poly_drug_life', 'sud_poly_drug_pastmonth', 'sud_other_life', 'sud_other_pastmonth',
                      'bipolar1_lifetime', 'bipolar1_pastmonth', 'bipolar2_lifetime2', 'bipolar2_pastmonth', 'otherbipolar_lifetime',
                      'otherbipolar_pastmonth', 'mdd_lifetime', 'mdd_pastmonth', 'dysthymic_lifetime', 'depressivenos_lifetime',
                      'depressivenos_pastmonth', 'mooddisordergmc_lifetime', 'mooddisordergmc_pastmonth',
                      'substanceinducedmood_lifetime', 'substanceinducedmood_pastmonth', 'primarypsychotic_lifetime',
                      'primarypsychotic_pastmonth', 'panicdisorder_lifetime', 'panic_life_agoraphobia', 'panicdisorder_pastmonth',
                      'panicdisorder_pastmonth_ag', 'awopd_lifetime', 'awopd_pastmonth', 'social_lifetime', 'socialphobia_pastmonth',
                      'specificphobia_lifetime', 'specificphobia_pastmonth', 'ocd_lifetime', 'ocd_pastmonth', 'ptsd_lifetime',
                      'ptsd_pastmonth', 'gad_lifetime', 'anxietydisordergmc_lifetime', 'anxietydisordergmc_pastmonth',
                      'substanceinducedanxiety_lifetime', 'substanceinducedanxiety_pastmonth', 'anxietydisordernos_lifetime',
                      'anxietydisordernos_pastmonth', 'borderline_pastmonth',]]

### Create a new dataframe so can use only subject number ###
df3 = df2
df3.insert(1, 'sub', value=0, allow_duplicates=False)

### Participant numbers are coded differently in the csv file from red cap. Parse those participant names so they are all ###
### the same and can be compared ###
subj_list = list()
num_subjs_list = list()
x = '_'
y = ' '
z = '00'
sub_cnt = 0

for sub_id in df2['rpep_participantid']:
    if x in sub_id:
        x2 = sub_id.split('_')
        x3 = x2[1]
        x4 = split(x3)
        if z in x3:
            x5 = x4[2]
            subj_list.append(x5)
            sub_cnt = sub_cnt + 1
            df3.loc[df2['rpep_participantid'].str.contains(x5, regex=False), 'sub'] = x5
        else:
            x5 = re.findall(('0[0-9][0-9]'), x3)
            x5 = str(x5)
            # print(x5)
            x6 = split(x5)
            # print(x6)
            x7 = x6[3] + x6[4]
            # print(x7)
            sub_cnt = sub_cnt + 1
            subj_list.append(x7)
            df3.loc[df2['rpep_participantid'].str.contains(x7, regex=False), 'sub'] = x7
    elif y in sub_id:
        y2 = sub_id.split()
        y3 = y2[1]
        y4 = re.findall(('0[0-9][0-9]'), y3)
        y4 = str(y4)
        y5 = split(y4)
        y6 = y5[3]+y5[4]
        subj_list.append(y6)
        sub_cnt = sub_cnt + 1
        df3.loc[df2['rpep_participantid'].str.contains(y6, regex=False), 'sub'] = y6

### Wanted to create a check of the script, but did not work the way I planned; tried if/then statements also did not work because can not evaluate two truth statements###
df3.loc[(df3['rpep_participantid'].str.contains(x5, regex=False)) & (df3['sub'].str.contains(x5, regex=False)), 'Status'] = 'Correct'
df3.loc[(~df3['rpep_participantid'].str.contains(x5, regex=False)) & (df3['sub'].str.contains(x5, regex=False)), 'Status'] = 'Error'
df3.loc[(df3['rpep_participantid'].str.contains(x7, regex=False)) & (df3['sub'].str.contains(x7, regex=False)), 'Status'] = 'Correct'
df3.loc[(~df3['rpep_participantid'].str.contains(x7, regex=False)) & (df3['sub'].str.contains(x7, regex=False)), 'Status'] = 'Error'
df3.loc[(df3['rpep_participantid'].str.contains(y6, regex=False)) & (df3['sub'].str.contains(y6, regex=False)), 'Status'] = 'Correct'
df3.loc[(~df3['rpep_participantid'].str.contains(y6, regex=False)) & (df3['sub'].str.contains(y6, regex=False)), 'Status'] = 'Error'

### sub in dataframes df and df3 are not the same type. Must be saved as int###
df['sub']=df['sub'].astype(int)
df3['sub'] = df3['sub'].astype(int)

for id in df['sub']:
    str_id = str(id)
    sub_cnt = 0
    #print(id)
    for sub_id in df3['sub']:
        str_sub_id = str(sub_id)
        #print(str_sub_id)
        if(str_id==str_sub_id):
            #print(str_sub_id)
            df4 = df3.merge(df, on=['sub'], how='left')
        else:
            continue

## want to drop all rows and columns will all NaN
df.dropna(axis=0, how='all', inplace=True)
df.dropna(axis=1, how='all', inplace=True)

### Save to csv ###
df4.to_csv(p.path_data + 'rPEP_clinical_merged.csv')

### Open clinical merge ###
fh = open(p.path_data + 'rPEP_clinical_merged.csv')
df5 = pd.read_csv(fh, delimiter=',')

### Score relevant scales ###
df5.insert(0, 'PCL_score', value=0, allow_duplicates=False)
df5.insert(0, 'CTQ_score', value=0, allow_duplicates=False)
df5.insert(0, 'DERS_Total', value=0, allow_duplicates=False)
df5.insert(0, 'DERS_Nonacceptance', value=0, allow_duplicates=False)
df5.insert(0, 'DERS_Goals', value=0, allow_duplicates=False)
df5.insert(0, 'DERS_Impulse', value=0, allow_duplicates=False)
df5.insert(0, 'DERS_Aware', value=0, allow_duplicates=False)
df5.insert(0, 'DERS_Strategies', value=0, allow_duplicates=False)
df5.insert(0, 'DERS_Clarity', value=0, allow_duplicates=False)
df5.insert(0, 'Positive_Affect', value=0, allow_duplicates=False)
df5.insert(0, 'Negative_Affect', value=0, allow_duplicates=False)

### Score measures ###
for sub in df5['sub']:

    df5['PCL_score'] = (df5['pcl_1'] + df5['pcl_2'] + df5['pcl_3'] + df5['pcl_4'] + df5['pcl_5'] + df5['pcl_6']
                        + df5['pcl_7'] +df5['pcl_8'] + df5['pcl_9'] + df5['pcl_10'] + df5['pcl_11'] + df5['pcl_12']
                        + df5['pcl_13'] + df5['pcl_14'] + df5['pcl_15'] + df5['pcl_16'] + df5['pcl_17']
                        + df5['pcl_18'] + df5['pcl_19'] + df5['pcl_20'])
    df5['CTQ_score'] = (df5['ctq_1']+df5['ctq_2']+df5['ctq_3']+df5['ctq_4']+df5['ctq_5']
                        +df5['ctq_6']+df5['ctq_7']+df5['ctq_8']+df5['ctq_9']+df5['ctq_10']+df5['ctq_11']
                        +df5['ctq_12']+df5['ctq_13']+df5['ctq_14']+df5['ctq_15']+df5['ctq_16']+df5['ctq_17']
                        +df5['ctq_18']+df5['ctq_19']+df5['ctq_20']+df5['ctq_21']+df5['ctq_22']+df5['ctq_23']
                        +df5['ctq_24']+df5['ctq_25']+df5['ctq_26']+df5['ctq_27']+df5['ctq_28'])
    df5['DERS_Total'] = (df5['ders_1_rs']+df5['ders_2_rs']+df5['ders3']+df5['ders4']+df5['ders5']+df5['ders_6_rs']
                         +df5['ders_7_rs']+df5['ders_8_rs']+df5['ders9']+df5['ders_10_rs']+df5['ders11']+df5['ders12']
                         +df5['ders13']+df5['ders14']+df5['ders15']+df5['ders16']+df5['ders_17_rs']+df5['ders18']+df5['ders19']+df5['ders_20_rs']
                         +df5['ders21']+df5['ders_22_rs']+df5['ders23']+df5['ders_24_rs']+df5['ders25']+df5['ders26']
                         +df5['ders27']+df5['ders28']+df5['ders29']+df5['ders30']+df5['ders31']+df5['ders32']
                         +df5['ders33']+df5['ders_34_rs']+df5['ders35']+df5['ders36'])
    df5['DERS_Nonacceptance']=(df5['ders11']+df5['ders12']+df5['ders21']+df5['ders23']+df5['ders29'])
    df5['DERS_Goals']=(df5['ders13']+df5['ders18']+df5['ders_20_rs']+df5['ders26']+df5['ders33'])
    df5['DERS_Impulse'] =(df5['ders3'] + df5['ders14'] + df5['ders19'] + df5['ders_24_rs'] + df5['ders27']+ df5['ders32'])
    df5['DERS_Aware'] = (df5['ders_6_rs'] + df5['ders_2_rs'] + df5['ders_10_rs'] + df5['ders_17_rs'] + df5['ders_8_rs'] + df5['ders_34_rs'])
    df5['DERS_Strategies'] = (df5['ders16'] + df5['ders15'] + df5['ders31'] + df5['ders35'] + df5['ders28'] + df5['ders_22_rs']+df5['ders36']+df5['ders30'])
    df5['DERS_Clarity'] = (df5['ders5'] + df5['ders4'] + df5['ders9'] + df5['ders_7_rs'] + df5['ders_1_rs'])
    df5['Positive_Affect'] = (df5['panas_1']+df5['panas_3']+df5['panas_5']+df5['panas_9']+df5['panas_10']+df5['panas_12']+df5['panas_14']+df5['panas_16']+df5['panas_17']+df5['panas_19'])
    df5['Negative_Affect'] = (df5['panas_2'] + df5['panas_4'] + df5['panas_6'] + df5['panas_7'] + df5['panas_8']
                              + df5['panas_11'] + df5['panas_13'] + df5['panas_15'] + df5['panas_18'] + df5['panas_20'])

### Save to csv ###
df5.to_csv(p.path_data + 'rPEP_clinical_scored.csv')

### open csv ###
fh = open(p.path_data + 'rPEP_clinical_scored.csv')
df6 = pd.read_csv(fh, sep=',', index_col=0)

### Descriptive statistics ###
pd.set_option("display.max_rows", None, "display.max_columns", None)
desc_df = df6[['age', 'group', 'Race']]

with open('/home/mcalvert/workspace/results/rPEP/Clinical_descriptives.txt', 'a') as f:
    print(desc_df['age'].describe(), file=f)
    print('/n',desc_df['group'].value_counts(), file=f)
    print(desc_df.groupby(['group']).describe(), file=f)
    print(desc_df.groupby(['Race', 'group']).count(), file=f)
    print(desc_df['Race'].value_counts(), file=f)

### SCID coding : 0 = absent, 1 = subthreshold, 2 = threshold,  or 0= absent, 1 = present
    print(df5['sud_alcohol_life'].value_counts(), file=f)
    print(df5['sud_alcohol_pastmonth'].value_counts(), file=f)
    print(df5['sud_sed_hyp_anx_life'].value_counts(), file=f)
    print(df5['sud_sed_hyp_anx_pastmonth'].value_counts(), file=f)
    print(df5['sud_cannabis_life'].value_counts(), file=f)
    print(df5['sud_cannabis_pastmonth'].value_counts(), file=f)
    print(df5['sud_stimulants_life'].value_counts(), file=f)
    print(df5['sud_stimulants_pastmonth'].value_counts(), file=f)
    print(df5['sud_opioid_life'].value_counts(), file=f)
    print(df5['sud_opioid_pastmonth'].value_counts(), file=f)
    print(df5['sud_cocaine_life'].value_counts(), file=f)
    print(df5['sud_cocaine_pastmonth'].value_counts(), file=f)
    print(df5['sud_hall_pcp_life'].value_counts(), file=f)
    print(df5['sud_hall_pcp_pastmonth'].value_counts(), file=f)
    print(df5['sud_poly_drug_life'].value_counts(), file=f)
    print(df5['sud_poly_drug_pastmonth'].value_counts(), file=f)
    print(df5['sud_other_life'].value_counts(), file=f)
    print(df5['sud_other_pastmonth'].value_counts(), file=f)
    print(df5['bipolar1_lifetime'].value_counts(), file=f)
    print(df5['bipolar1_pastmonth'].value_counts(), file=f)
    print(df5['bipolar2_lifetime2'].value_counts(), file=f)
    print(df5['bipolar2_pastmonth'].value_counts(), file=f)
    print(df5['otherbipolar_lifetime'].value_counts(), file=f)
    print(df5['otherbipolar_pastmonth'].value_counts(), file=f)
    print(df5['mdd_lifetime'].value_counts(), file=f)
    print(df5['mdd_pastmonth'].value_counts(), file=f)
    print(df5['dysthymic_lifetime'].value_counts(), file=f)
    print(df5['depressivenos_lifetime'].value_counts(), file=f)
    print(df5['depressivenos_pastmonth'].value_counts(), file=f)
    print(df5['mooddisordergmc_lifetime'].value_counts(), file=f)
    print(df5['mooddisordergmc_pastmonth'].value_counts(), file=f)
    print(df5['substanceinducedmood_lifetime'].value_counts(), file=f)
    print(df5['substanceinducedmood_pastmonth'].value_counts(), file=f)
    print(df5['primarypsychotic_lifetime'].value_counts(), file=f)
    print(df5['primarypsychotic_pastmonth'].value_counts(), file=f)
    print(df5['panicdisorder_lifetime'].value_counts(), file=f)
    print(df5['panic_life_agoraphobia'].value_counts(), file=f)
    print(df5['panicdisorder_pastmonth'].value_counts(), file=f)
    print(df5['panicdisorder_pastmonth_ag'].value_counts(), file=f)
    print(df5['awopd_lifetime'].value_counts(), file=f)
    print(df5['awopd_pastmonth'].value_counts(), file=f)
    print(df5['social_lifetime'].value_counts(), file=f)
    print(df5['socialphobia_pastmonth'].value_counts(), file=f)
    print(df5['specificphobia_lifetime'].value_counts(), file=f)
    print(df5['specificphobia_pastmonth'].value_counts(), file=f)
    print(df5['ocd_lifetime'].value_counts(), file=f)
    print(df5['ocd_pastmonth'].value_counts(), file=f)
    print(df5['ptsd_lifetime'].value_counts(), file=f)
    print(df5['ptsd_pastmonth'].value_counts(), file=f)
    print(df5['gad_lifetime'].value_counts(), file=f)
    print(df5[ 'anxietydisordergmc_lifetime'].value_counts(), file=f)
    print(df5['anxietydisordergmc_pastmonth'].value_counts(), file=f)
    print(df5['substanceinducedanxiety_lifetime'].value_counts(), file=f)
    print(df5['substanceinducedanxiety_pastmonth'].value_counts(), file=f)
    print(df5['anxietydisordernos_lifetime'].value_counts(), file=f)
    print(df5['anxietydisordernos_pastmonth'].value_counts(), file=f)
    print(df5['borderline_pastmonth'].value_counts(), file=f)

scid_df = df6[['sub', 'sud_alcohol_life', 'sud_alcohol_pastmonth', 'sud_sed_hyp_anx_life','sud_sed_hyp_anx_pastmonth',
                      'sud_cannabis_life', 'sud_cannabis_pastmonth', 'sud_stimulants_life', 'sud_stimulants_pastmonth',
                      'sud_opioid_life', 'sud_opioid_pastmonth', 'sud_cocaine_life', 'sud_cocaine_pastmonth', 'sud_hall_pcp_life',
                      'sud_hall_pcp_pastmonth', 'sud_poly_drug_life', 'sud_poly_drug_pastmonth', 'sud_other_life', 'sud_other_pastmonth',
                      'bipolar1_lifetime', 'bipolar1_pastmonth', 'bipolar2_lifetime2', 'bipolar2_pastmonth', 'otherbipolar_lifetime',
                      'otherbipolar_pastmonth', 'mdd_lifetime', 'mdd_pastmonth', 'dysthymic_lifetime', 'depressivenos_lifetime',
                      'depressivenos_pastmonth', 'mooddisordergmc_lifetime', 'mooddisordergmc_pastmonth',
                      'substanceinducedmood_lifetime', 'substanceinducedmood_pastmonth', 'primarypsychotic_lifetime',
                      'primarypsychotic_pastmonth', 'panicdisorder_lifetime', 'panic_life_agoraphobia', 'panicdisorder_pastmonth',
                      'panicdisorder_pastmonth_ag', 'awopd_lifetime', 'awopd_pastmonth', 'social_lifetime', 'socialphobia_pastmonth',
                      'specificphobia_lifetime', 'specificphobia_pastmonth', 'ocd_lifetime', 'ocd_pastmonth', 'gad_lifetime',
                      'anxietydisordergmc_lifetime', 'anxietydisordergmc_pastmonth',
                      'substanceinducedanxiety_lifetime', 'substanceinducedanxiety_pastmonth', 'anxietydisordernos_lifetime',
                      'anxietydisordernos_pastmonth', 'borderline_pastmonth']]

scid_df2 = scid_df.fillna('0')
scid_df3 = scid_df2.replace(to_replace='na', value='0')
scid_df4 = scid_df3.astype(dtype='int', copy=True, errors='ignore')

### For each participant, iterate over each column in the SCID data. Each data point is put in a list to use later. ###
### Because participant ID is a column, only take items 1 through end in the list ###
### Sum the list. Any value besides zero will indicate that there is a lifetime diagnosis. After each object is used ###
### have to return the value to zero ###
z = list()
rowlist = list()
sumlist = list()
for index, row in scid_df4.iterrows():
    for r in row:
        z.append(r)
    rowlist = (z[1:])
    z *= 0
    y = sum(rowlist)
    rowlist *= 0
    sumlist.append(y)

df5.insert(0, 'any_lifetime_diagnosis', sumlist)
df5.loc[(df5['any_lifetime_diagnosis'] == 0), 'Any'] = 0
df5.loc[(df5['any_lifetime_diagnosis'] >= 1), 'Any'] = 1

control_df = pd.DataFrame()
control_df = df5.query('group == "control"')[['sub', 'age', 'PCL_score', 'CTQ_score', 'DERS_Total', 'DERS_Nonacceptance', 'DERS_Goals',
                                        'DERS_Impulse', 'DERS_Aware','DERS_Strategies', 'DERS_Clarity', 'Positive_Affect', 'Negative_Affect', 'Any']]
control_df1 = control_df.dropna()


ptsd_df = pd.DataFrame()
ptsd_df = df5.query('group == "ptsd"')[['sub', 'age', 'PCL_score', 'CTQ_score', 'DERS_Total', 'DERS_Nonacceptance', 'DERS_Goals',
                                        'DERS_Impulse', 'DERS_Aware','DERS_Strategies', 'DERS_Clarity', 'Positive_Affect', 'Negative_Affect', 'Any']]
ptsd_df1 = ptsd_df.dropna()

Age_control = np.array(control_df1['age'])
Age_ptsd = np.array(ptsd_df1['age'])
PCL_control = np.array(control_df1['PCL_score'])
PCL_ptsd = np.array(ptsd_df1['PCL_score'])
CTQ_control = np.array(control_df1['CTQ_score'])
CTQ_ptsd = np.array(ptsd_df1['CTQ_score'])
DERS_control = np.array(control_df1['DERS_Total'])
DERS_ptsd = np.array(ptsd_df1['DERS_Total'])
Positive_control = np.array(control_df1['Positive_Affect'])
Positive_ptsd = np.array(ptsd_df1['Positive_Affect'])
Negative_control = np.array(control_df1['Negative_Affect'])
Negative_ptsd = np.array(ptsd_df1['Negative_Affect'])
Any_control = np.array(control_df1['Any'])
Any_ptsd = np.array(ptsd_df1['Any'])

with open('/home/mcalvert/workspace/results/rPEP/Clinical_descriptives.txt', 'a') as f:
    print('\n', 'PCL_score_Control group', control_df1['PCL_score'].describe(), file=f)
    print('\n', 'PCL_score_PTSD group', ptsd_df1['PCL_score'].describe(), file=f)
    print('\n', 'Any counts Control group', control_df1['Any'].value_counts(), file=f)
    print('\n', 'Any counts PTSD group', ptsd_df1['Any'].value_counts(), file=f)
    print('\n', 'equal variance Age', stats.levene(Age_control, Age_ptsd), file=f)
    t_res_age = stats.ttest_ind(Age_control, Age_ptsd, equal_var=True)
    print('\n', 'Age', t_res_age, file=f)
    print('\n', 'equal variance PCL', stats.levene(PCL_control, PCL_ptsd), file=f)
    t_res_pcl = stats.ttest_ind(PCL_control, PCL_ptsd, equal_var=True)
    print('\n', 'PCL', t_res_pcl, file=f)
    print('\n', 'equal variance CTQ', stats.levene(CTQ_control, CTQ_ptsd), file=f)
    t_res_ctq = stats.ttest_ind(CTQ_control, CTQ_ptsd, equal_var=True)
    print('\n', 'CTQ', t_res_ctq, file=f)
    print('\n', 'equal variance DERS', stats.levene(DERS_control, DERS_ptsd, center='mean'), file=f)
    t_res_ders = stats.ttest_ind(DERS_control, DERS_ptsd, equal_var=True)
    print('\n', 'DERS', t_res_ders,file=f)
    print('\n', 'equal variance positive affect', stats.levene(Positive_control, Positive_ptsd),file=f)
    t_res_pos = stats.ttest_ind(Positive_control,Positive_ptsd, equal_var=True)
    print('\n', 'positive affect', t_res_pos, file=f)
    print('\n', 'equal variance negative affect', stats.levene(Negative_control, Negative_ptsd), file=f)
    t_res_neg = stats.ttest_ind(Negative_control, Negative_ptsd, equal_var=False)
    print('\n', 'negative affect', t_res_neg, file=f)
    print('\n', 'equal variance Any', stats.levene(Any_control, Any_ptsd), file=f)
    t_res_any = stats.ttest_ind(Any_control, Any_ptsd, equal_var=False)
    print('\n', 'Any diagnosis', t_res_any, file=f)