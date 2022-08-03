import sys
import time
from time import localtime, strftime
import random

class rPEP_Project():
    def __init__(self):
        self.base_path = '/home/mcalvert/'
        self.base_name = 'rPEP'

        #define tools from Keith Bush's drive
        self.base_lib = '/home/kabush/lib/'
        self.path_tools_kablab = (self.base_lib + 'kablab/')
        self.path_tools_nifti = (self.base_lib + 'nifti/')
        self.path_atlas = '/home/kabush/atlas'

        #define project name
        self.path_name = self.base_name

        #define workspace
        self.path_home = (self.base_path + 'workspace/')
        self.path_data = (self.path_home + 'data/' + self.path_name + '/')
        self.path_results = (self.path_home + 'results/' + self.path_name + '/')
        self.path_derives = '/project/data/clean/bush/rPEP/derivatives/'
        self.path_bids = (self.path_home + 'bids/' + self.path_name + '/')
        self.path_code = (self.path_home + 'code/' + self.path_name + '/')
        self.path_afni = (self.path_code)
        self.path_log = (self.path_code + 'log/')
        self.path_fig = (self.path_code + 'fig/')
        self.path_tmp = (self.path_code + 'tmp/')

        #subject lists
        self.path_subj_list = (self.path_bids + 'participants.tsv')
        self.path_subjs = (self.path_code + 'subj_lists/rPEP_subj_list.txt')

        # logging
        self.dt = time.gmtime()
        self.formatOut = strftime("%Y%m%d%H%M%S", localtime())
        # print(formatOut)
        self.path_logfile = (self.path_log + 'logfile_' + self.formatOut + '.txt')

        # Derivatives output directory
        self.path_mri_name = 'mri/'
        self.path_physio_name = 'physio/'
        self.path_betas_name = 'betas/'
        self.path_analysis_name = 'analysis/'


        # Preprocessing data
        self.path_fmriprep = (self.path_derives + 'fmriprep/')
        self.path_mri_clean = (self.path_derives + 'pipeline/mri/mri_clean/')
        self.path_mri_gm_mask = (self.path_derives + 'pipeline/mri/mri_gm_mask/')

        # Data source
        self.param_studies = ['rPEP']

        ### Data frame ###
        self.data_frame = (self.path_data + 'GLM_feedback_arous_contrasts_demo_.csv')

        ### Cluster Masks ###
        self.cluster_mask_on = (self.path_data + 'FBArouse_ON+tlrc.HEAD ')
        self.cluster_mask_off = (self.path_data + 'FBArouse_OFF+tlrc.HEAD')

        # Clean build the directories as it runs
        self.flag_clean_build = 1

        # MRI fmriprep post-processing parameters
        self.param_mri_tasks = ['identify', 'modulate'] #this experiment had two 2 modulate and 2 expiremental runs#

        # print(type(param_mri_tasks))
        self.param_mri_Nscans = [2, 2]
        self.param_mri_Nvol = [167, 224]
        self.param_mri_TR = 2
        self.param_mri_stim_t = 2
        self.param_mri_FD_thresh = 0.5
        self.param_mri_anat_space = 'MNI152NLin2009cAsym'
        self.param_mri_bold_space = self.param_mri_anat_space  # + 'res-native' *** TICKET *** fmriprep changed naming convention
        self.param_mri_desc = 'preproc_bold'
        self.param_mri_gm_prob = 0.7
        self.param_mri_fwhm = 8.0
        self.param_mri_temp_hz = 0.0078


        # #MRI fmriprep post-processing list of dictionaries. This list of dictionaries allows us to iterate over every item in the dictionary and all###
        ### items in the dictionary are stored together ####

    keys = ['Tasks', 'Nscans', 'Nvol']
    values1 = ['identify', 'modulate']
    values2 = ['2', '2']
    values3 = ['167', '224']
    values = [values1, values2, values3]
    ### I created different dictionary structures because of the way the script iterates over the items ###
    ### tnv is a zip dictionary. In the fmriprep_process_fmri file we use a structure closest to this structure ###
    tnv = zip(values1, values2, values3)
    ### ltnv is a list of dictionaries ###
    ltnv = list(tnv)
    ### is another dictionary which specifies the key, value pairs ###
    tnv1 = {k: v for k, v in zip(keys, values)}

