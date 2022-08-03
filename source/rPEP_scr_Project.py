import sys
import time
from time import localtime, strftime
import random

class rPEP_scr_Project():
    def __init__(self):
        self.base_path = '/home/mcalvert/'
        self.base_name = 'rPEP_scr'
        self.lib_path = self.base_path + 'lib/'

        #define tools from Keith's drive
        self.base_lib = '/home/kabush/lib/'
        self.path_tools_kablab = (self.base_lib + 'kablab/')
        self.path_tools_nifti = (self.base_lib + 'nifti/')
        self.path_atlas = '/home/kabush/atlas'

        #define project name
        self.path_name = self.base_name

        #define workspace
        self.path_home = (self.base_path + 'workspace/')
        self.path_bids = (self.path_home + 'bids/rPEP/')
        self.path_data = (self.path_home + 'data/' + self.path_name + '/')
        self.path_code = (self.path_home + 'code/rPEP/')
        self.path_log = (self.path_code + 'log/')
        self.path_fig = (self.path_code + 'fig/')
        self.path_tmp = (self.path_code + 'tmp/')

        #subject lists
        self.path_subj_list = (self.path_code + 'subj_lists/')

        # logging
        self.dt = time.gmtime()
        self.formatOut = strftime("%Y%m%d%H%M%S", localtime())
        # print(formatOut)
        self.path_logfile = (self.path_log + 'logfile_' + self.formatOut + '.txt')

        # Derivatives output directory
        self.path_physio_name = (self.path_data + 'physio/')
        self.path_betas_name = (self.path_data + 'beta_series/scr_ex_beta/')

# testing to see if the class Project did what it was supposed to do ##
pj = rPEP_scr_Project()