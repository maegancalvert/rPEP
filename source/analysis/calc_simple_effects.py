import pandas as pd
import numpy as np
import scipy.stats


### Estimates gathered from
estimate_feedback = np.array([0.07, -0.02, 0.35, 0.14, 0.10, 0.31])
stand_error_feedback = np.array([0.02, 0.01, 0.12, 0.09, 0.01, 0.02])
no_obs_feedback = np.array([3360, 3733, 3360, 3733, 3713, 3380])

estimate_scr = np.array([0.02, 0.01, -0.01, 0.01, 0.02, 0.01, 0.01, 0.01])
stand_error_scr = np.array([0.004, 0.003, 0.01, 0.01, 0.03, 0.003, 0.003, 0.003])
no_obs_scr = np.array([3360, 3345, 3360, 3345, 3511, 3374, 3511, 3374])

### See Robinson et al., 2013 Tests of Moderation Effects ###
### t=B diff/SE pooled ###
### Step 1 difference in estimates ###
diff_est_feedback = np.array(estimate_feedback[0] - estimate_feedback[1])
diff_est_feedback = np.append(diff_est_feedback, (estimate_feedback[2]-estimate_feedback[3]))
diff_est_feedback = np.append(diff_est_feedback, (estimate_feedback[4]-estimate_feedback[5]))
print('difference in the estimates')
print(diff_est_feedback)

### Step 2a: standard error * number of observations ###
calc1_se_feedback = np.array(stand_error_feedback[0]*no_obs_feedback[0])
calc1_se_feedback = np.append(calc1_se_feedback, (stand_error_feedback[1]*no_obs_feedback[1]))
calc1_se_feedback = np.append(calc1_se_feedback, (stand_error_feedback[2]*no_obs_feedback[2]))
calc1_se_feedback = np.append(calc1_se_feedback, (stand_error_feedback[3]*no_obs_feedback[3]))
calc1_se_feedback = np.append(calc1_se_feedback, (stand_error_feedback[4]*no_obs_feedback[4]))
calc1_se_feedback = np.append(calc1_se_feedback, (stand_error_feedback[5]*no_obs_feedback[5]))
print(calc1_se_feedback)

### Step 2b: add step2a for each simple effect comparison###
calc2_se_feedback = np.array(calc1_se_feedback[0]+calc1_se_feedback[1])
calc2_se_feedback = np.append(calc2_se_feedback, (calc1_se_feedback[2]+calc1_se_feedback[3]))
calc2_se_feedback = np.append(calc2_se_feedback, (calc1_se_feedback[4]+calc1_se_feedback[5]))
print(calc2_se_feedback)

### Step 2c: add number of observations from each effect###
calc3_se_feedback = np.array(no_obs_feedback[0]+no_obs_feedback[1])
calc3_se_feedback = np.append(calc3_se_feedback, (no_obs_feedback[2]+no_obs_feedback[3]))
calc3_se_feedback = np.append(calc3_se_feedback, (no_obs_feedback[4]+no_obs_feedback[5]))
print(calc3_se_feedback)

### Step 2d: divide step2b by step2c minus 2 ###
calc4_se_feedback = np.array(calc2_se_feedback[0]/(calc3_se_feedback[0]-2))
calc4_se_feedback = np.append(calc4_se_feedback, calc2_se_feedback[1]/(calc3_se_feedback[1]-2))
calc4_se_feedback = np.append(calc4_se_feedback, calc2_se_feedback[2]/(calc3_se_feedback[2]-2))
print(calc4_se_feedback)

### Don't think I actually need this step - will check with Keith ###
# ### Step 2e: square root product of Step2d; this is the SE pooled###
# calc5_se_feedback = np.sqrt(calc4_se_feedback)
# print(calc5_se_feedback)

t_value_feedback = np.array(diff_est_feedback[0]/calc4_se_feedback[0])
t_value_feedback = np.append(t_value_feedback, (diff_est_feedback[1]/calc4_se_feedback[1]))
t_value_feedback = np.append(t_value_feedback, (diff_est_feedback[2]/calc4_se_feedback[2]))
print('T values')
print(t_value_feedback)

p_value1 = scipy.stats.t.sf(abs(t_value_feedback[0]), df=calc3_se_feedback[0])
# print(p_value1)
p_value2 = scipy.stats.t.sf(abs(t_value_feedback[1]), df=calc3_se_feedback[1])
# print(p_value2)
p_value3 = scipy.stats.t.sf(abs(t_value_feedback[2]), df=calc3_se_feedback[2])
# print(p_value3)

print('Feedback Simple Effects')
print('Feedback by Engage/Disengage condition', 't', t_value_feedback[0], 'SE pooled',calc4_se_feedback[0],
       'no obs', calc3_se_feedback[0],  'p', p_value1)
print('Group by Engage/Disengage condition', 't', t_value_feedback[1], 'SE pooled',calc4_se_feedback[1],
      'no obs', calc3_se_feedback[1],  'p', p_value2)
print('Condition by Group','t', t_value_feedback[2], calc4_se_feedback[2], 'SE pooled',
      'no obs', calc3_se_feedback[2],  'p', p_value3)

diff_est_scr = np.array(estimate_scr[0] - estimate_scr[1])
diff_est_scr = np.append(diff_est_scr, (estimate_scr[2]-estimate_scr[3]))
diff_est_scr = np.append(diff_est_scr, (estimate_scr[4]-estimate_scr[5]))
diff_est_scr = np.append(diff_est_scr, (estimate_scr[6]-estimate_scr[7]))
print('Difference in SCR estimates')
print(diff_est_scr)

calc1_se_scr = np.array(stand_error_scr[0]*no_obs_scr[0])
calc1_se_scr = np.append(calc1_se_scr, (stand_error_scr[1]*no_obs_scr[1]))
calc1_se_scr = np.append(calc1_se_scr, (stand_error_scr[2]*no_obs_scr[2]))
calc1_se_scr = np.append(calc1_se_scr, (stand_error_scr[3]*no_obs_scr[3]))
calc1_se_scr = np.append(calc1_se_scr, (stand_error_scr[4]*no_obs_scr[4]))
calc1_se_scr = np.append(calc1_se_scr, (stand_error_scr[5]*no_obs_scr[5]))
calc1_se_scr = np.append(calc1_se_scr, (stand_error_scr[6]*no_obs_scr[6]))
calc1_se_scr = np.append(calc1_se_scr, (stand_error_scr[7]*no_obs_scr[7]))
# print(calc1_se_scr)

calc2_se_scr = np.array(calc1_se_scr[0]+calc1_se_scr[1])
calc2_se_scr = np.append(calc2_se_scr, (calc1_se_scr[2]+calc1_se_scr[3]))
calc2_se_scr = np.append(calc2_se_scr, (calc1_se_scr[4]+calc1_se_scr[5]))
calc2_se_scr = np.append(calc2_se_scr, (calc1_se_scr[6]+calc1_se_scr[7]))
# print(calc2_se_scr)

calc3_se_scr = np.array(no_obs_scr[0]+no_obs_scr[1])
calc3_se_scr = np.append(calc3_se_scr, (no_obs_scr[2]+no_obs_scr[3]))
calc3_se_scr = np.append(calc3_se_scr, (no_obs_scr[4]+no_obs_scr[5]))
calc3_se_scr = np.append(calc3_se_scr, (no_obs_scr[6]+no_obs_scr[7]))
# print(calc3_se_scr)

calc4_se_scr = np.array(calc2_se_scr[0]/(calc3_se_scr[0]-2))
calc4_se_scr = np.append(calc4_se_scr, calc2_se_scr[1]/(calc3_se_scr[1]-2))
calc4_se_scr = np.append(calc4_se_scr, calc2_se_scr[2]/(calc3_se_scr[2]-2))
calc4_se_scr = np.append(calc4_se_scr, calc2_se_scr[3]/(calc3_se_scr[3]-2))
# print(calc4_se_scr)

# calc5_se_scr = np.sqrt(calc4_se_scr)

t_value_scr = np.array(diff_est_scr[0]/calc4_se_scr[0])
t_value_scr = np.append(t_value_scr, (diff_est_scr[1]/calc4_se_scr[1]))
t_value_scr = np.append(t_value_scr, (diff_est_scr[2]/calc4_se_scr[2]))
t_value_scr = np.append(t_value_scr, (diff_est_scr[3]/calc4_se_scr[3]))
# print(t_value_scr)

# print(t_value_scr[0], calc3_se_scr[0])
# print(t_value_scr[1], calc3_se_scr[1])
# print(t_value_scr[2], calc3_se_scr[2])
# print(t_value_scr[3], calc3_se_scr[3])


### q = significance ###
p_value1 = scipy.stats.t.sf(abs(t_value_scr[0]), df=calc3_se_scr[0])
# print(p_value1)
p_value2 = scipy.stats.t.sf(abs(t_value_scr[1]), df=calc3_se_scr[1])
# print(p_value2)
p_value3 = scipy.stats.t.sf(abs(t_value_scr[2]), df=calc3_se_scr[2])
# print(p_value3)
p_value4 = scipy.stats.t.sf(abs(t_value_scr[3]), df=calc3_se_scr[3])
# print(p_value4)

print('SCR Simple Effects')
print('Feedback by Engage/Disengage condition', 't', t_value_scr[0], 'SE pooled', calc4_se_scr[0],
      'no obs', calc3_se_scr[0],  'p', p_value1)
print('Group by Engage/Disengage condition', 't', t_value_scr[1], 'SE pooled', calc4_se_scr[1],
      'no obs',calc3_se_scr[1],  'p', p_value2)
print('Condition by Group', 't', t_value_scr[2], 'SE pooled', calc4_se_scr[2],
      'no obs', calc3_se_scr[2], 'p', p_value3)
print('Feedback by Group', 't', t_value_scr[3], 'SE pooled', calc4_se_scr[3],
      'no obs',calc3_se_scr[3], 'p', p_value4)



