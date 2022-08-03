from rPEP.source.rPEP_Project import rPEP_Project
import numpy as np
import os
import glob
import re

p = rPEP_Project()
resid1 = '_task-modulate1.scaled.resid.nii'
resid2 = '_task-modulate2.scaled.resid.nii'

### new build ###

if os.path.exists(p.path_data + 'mod1_resid.txt'):
    os.system('rm -rf' + p.path_data + 'mod1_resid.txt')

if os.path.exists(p.path_data + 'mod2_resid.txt'):
    os.system('rm -rf' + p.path_data + 'mod2_resid.txt')

### Create the files that afni will send the output to ###
os.system('touch' + p.path_data + 'mod1_resid.txt')
os.system('touch' + p.path_data + 'mod2_resid.txt')

### Read the subjects ###
txt = open(p.path_subjs)

### Subjs had a right hard return, so need to strip that before using ###
for t in txt:
    s_t = t.rstrip()

### Find files in the directory that match the pattern and then check for a full match with the ###
### subject number. This script assesses both modulate 1 and modulate 2 ###
    for filepath in glob.glob((p.path_mri_clean + 'sub-*/' + 'sub-*' + resid1), recursive=True):
        if re.fullmatch(filepath, (p.path_mri_clean + 'sub-' + s_t + '/' + 'sub-' + s_t + resid1)):
            print('True')
            os.system('3dFWHMx -detrend -input ' + filepath + ' -acf >>  ' + p.path_data + 'mod1_resid.txt')
            print('saving resid' + s_t)
        else:
            continue
    for filepath2 in glob.glob((p.path_mri_clean + 'sub-*/' + 'sub-*' + resid2), recursive=True):
        if re.fullmatch(filepath2, (p.path_mri_clean + 'sub-' + s_t + '/' + 'sub-' + s_t + resid2)):
            os.system('3dFWHMx -detrend -input ' + filepath2 + ' -acf >>  ' + p.path_data + 'mod2_resid.txt')
            print('saving resid2' + s_t)
        else:
            continue

### Read the AFNI output for the residual text file we created ###
### Created lists to keep the acf values [x, y, z] from different subjects together ###
with open(p.path_data + 'mod1_resid.txt', 'r') as fh:
    acf_x = []
    acf_y = []
    acf_z = []
    acf_combined = []
    acf = []
### Parse the textfile to be useable ###
    for line in fh:
        strip_lead_return = line.strip('\n')
        if strip_lead_return.startswith('0 0 0 '):
            continue
        else:
            sep_xyz = strip_lead_return.splitlines(True)
            acf_xyz = list(sep_xyz)
            for element in acf_xyz:
                parts = element.split(',')
                parts2 = element.replace(' ', ',')
                parts3 = parts2.split(',')
                if float(parts3[1]) > float('0'):
                    acf_x.append(parts3[1])
                    acf_y.append(parts3[3])
                    acf_z.append(parts3[5])
                    acf_combined.append(parts3[9])

### lists need to be changed to numpy arrays. Have to specify astype() ###
acf_x_array = np.array(acf_x).astype(np.float)
acf_y_array = np.array(acf_y).astype(np.float)
acf_z_array = np.array(acf_z).astype(np.float)
acf_combined_array = np.array(acf_combined).astype(np.float)

### use values from each participant to create the median residual values of the acf ###
median_acf_x_mod1 = np.median(acf_x_array, axis=0)
median_acf_y_mod1 = np.median(acf_y_array, axis=0)
median_acf_z_mod1 = np.median(acf_z_array, axis=0)
median_acf_combined_mod1 = np.median(acf_combined_array, axis=0)

### Write the median acf values to a text file to be used in the calc_3dlme_cluster_thresh.py ###
### Order is x, y, z, and combined ###
mod1_file = (p.path_data + 'smooth_params_mod1.txt')
with open(mod1_file, 'w') as fh:
    fh.write(str(median_acf_x_mod1) + ',')
    fh.write(str(median_acf_y_mod1) + ',')
    fh.write(str(median_acf_z_mod1) + ',')
    fh.write(str(median_acf_combined_mod1) + ',')
    fh.close()

### Use same process for the modulate 2 residuals ###
with open(p.path_data + 'mod2_resid.txt', 'r') as fh:
    acf2_x = []
    acf2_y = []
    acf2_z = []
    acf2_combined = []
    acf2 = []
    for line2 in fh:
        strip_lead_return2 = line2.strip('\n')
        if strip_lead_return2.startswith('0 0 0 '):
            continue
        else:
            sep_xyz2 = strip_lead_return2.splitlines(True)
            acf_xyz2 = list(sep_xyz2)
            for element2 in acf_xyz2:
                parts4 = element2.split(',')
                parts5 = element2.replace(' ', ',')
                parts6 = parts5.split(',')
                if float(parts6[1]) > float('0'):
                    acf2_x.append(parts6[1])
                    acf2_y.append(parts6[3])
                    acf2_z.append(parts6[5])
                    acf2_combined.append(parts6[9])

### Creating numpy arrays ###
acf2_x_array = np.array(acf2_x).astype(np.float)
acf2_y_array = np.array(acf2_y).astype(np.float)
acf2_z_array = np.array(acf2_z).astype(np.float)
acf2_combined_array = np.array(acf2_combined).astype(np.float)

### Creating median acf values ###
median_acf2_x_mod2 = np.median(acf2_x_array, axis=0)
median_acf2_y_mod2 = np.median(acf2_y_array, axis=0)
median_acf2_z_mod2 = np.median(acf2_z_array, axis=0)
median_acf2_combined_mod2 = np.median(acf2_combined_array, axis=0)

### Write text file to be used in calc_3dlme_cluster_thresh.py ###
mod2_file = (p.path_data + 'smooth_params_mod2.txt')
with open(mod2_file, 'w') as fh:
    fh.write(str(median_acf2_x_mod2) + ',')
    fh.write(str(median_acf2_y_mod2) + ',')
    fh.write(str(median_acf2_z_mod2) + ',')
    fh.write(str(median_acf2_combined_mod2) + ',')
    fh.close()

###  Concat arrays to have total acf from both mod1 and mod2 ###
total_acf_x = np.concatenate((acf2_x_array, acf_x_array), axis=0)
total_acf_y = np.concatenate((acf2_y_array, acf_y_array), axis=0)
total_acf_z = np.concatenate((acf2_z_array, acf_z_array), axis=0)
total_acf_combined = np.concatenate((acf_combined_array, acf2_combined_array), axis=0)

### Write a file of the total acf values from mod1 and mod2 ###
### This was done differently to be more concise. Median values are just written ###
### into the text file rather than creating an object to hold the value. ###
total_file = (p.path_data + 'smooth_params_total.txt')
with open(total_file, 'w') as fh:
    fh.write(str(np.median(total_acf_x, axis=0)) + ',')
    fh.write(str(np.median(total_acf_y, axis=0)) + ',')
    fh.write(str(np.median(total_acf_z, axis=0)) + ',')
    fh.write(str(np.median(total_acf_combined, axis=0)) + ',')
    fh.close()