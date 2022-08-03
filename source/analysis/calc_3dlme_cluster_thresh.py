from rPEP.source.rPEP_Project import rPEP_Project
import pandas as pd
import os

pd.set_option('display.max_columns', None, 'display.max_rows', None)
pd.set_option('display.max_colwidth', -1)

p = rPEP_Project()

### Get the median x, y, z parameters ###
with open(p.path_data + 'smooth_params_total.txt', 'r') as fh:
    for line in fh:
        split = line.split(',')
        print(split[2])

### Run AFNI's 3dClustSim ###
os.system('3dClustSim -acf ' + split[0] + ' ' + split[1] + ' ' + split[2] + ' ' + '-nxyz 54 64 50 -pthr 0.001 -athr 0.05 -mask '+
    p.path_mri_gm_mask + 'group_gm_mask.nii -prefix ' + p.path_data + 'clust_size_feedbackXarouse')
