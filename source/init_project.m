%% ----------------------------------------
%% Maegan Calvert, PhD (2021)
%% Keith Bush, PhD (2021)
%% Univ. of Arkansas for Medical Sciences
%% Brain Imaging Research Center (BIRC)
%%
%% ----------------------------------------
%% Initialize project param structure
proj = struct();

%% ----------------------------------------
%% Link Library Tools

base_lib = '/home/kabush/lib/';

proj.path.tools.kablab = [base_lib,'kablab/'];
addpath(genpath(proj.path.tools.kablab));

proj.path.tools.nifti = [base_lib,'nifti/'];
addpath(genpath(proj.path.tools.nifti));

%% ----------------------------------------
%% Link Atlases Path
proj.path.atlas = ['/home/kabush/atlas'];

%% ----------------------------------------
%% Project Name
proj.path.name = 'rPEP';
proj.path.home = '/home/mcalvert/workspace/';

%% ----------------------------------------
%% Workspace (code,bids,derivatives,...)
proj.path.bids = [proj.path.home,'bids/rPEP/'];
proj.path.bids_name = [proj.path.bids, 'sub-'];
proj.path.data = [proj.path.home,'data/',proj.path.name,'/'];
proj.path.code = [proj.path.home,'code/',proj.path.name,'/'];
proj.path.derives = [proj.path.data, 'derivatives/'];
proj.path.log =[proj.path.code,'log/']; 
proj.path.fig = [proj.path.code,'fig/'];
proj.path.tmp = [proj.path.code,'tmp/'];

%% Subject Lists
proj.path.subjs = [proj.path.code, 'subj_lists/rPEP_subj_list.txt'];

%% Logging (creates a unique time-stampted logfile)
formatOut = 'yyyy_mm_dd_HH:MM:SS';
t = datetime('now');
ds = datestr(t,formatOut);
proj.path.logfile = [proj.path.log,'logfile_',ds,'.txt'];

%% ----------------------------------------
%% Derivatives output directory (All top-level names)
proj.path.mri.name = 'mri/';
proj.path.physio.name = 'physio/';
proj.path.betas.name = 'beta_series/';
proj.path.trg.name = 'target/';
proj.path.mvpa.name = 'mvpa/';
proj.path.analysis.name = 'analysis/';
proj.path.haufe.name = 'haufe/';

%% ----------------------------------------
%% Specific Data Paths
proj.path.fmriprep = [proj.path.derives, 'fmriprep/'];
proj.path.mri_clean = [proj.path.derives, proj.path.mri.name, 'mri_clean/'];
proj.path.mri.gm_mask = [proj.path.derives, proj.path.mri.name, 'gm_mask/'];


%% ----------------------------------------
%% Project Parameter Definitions

%% SCR Paths %%%
proj.path.physio.scr_clean = [proj.path.data,proj.path.physio.name,'scr_clean/'];
proj.path.betas.scr_ex_beta = [proj.path.data,proj.path.betas.name,'scr_ex_beta/'];
%% Data source
proj.param.studies = {'rPEP'}; %base_name};

%% Clean build the directories as it runs
proj.flag.clean_build = 1;

%% MRI fmriprep post-processing params
proj.param.mri.tasks = {'identify','modulate'};
proj.param.mri.Nscans = [2,2];
proj.param.mri.Nvol = [167,228];
proj.param.mri.TR = 2;
proj.param.mri.stim_t = 2;
proj.param.mri.FD_thresh = .5;
proj.param.mri.anat_space = 'MNI152NLin2009cAsym';
proj.param.mri.bold_space = proj.param.mri.anat_space; %,'_res-native'];
proj.param.mri.desc = 'preproc_bold';
proj.param.mri.gm_prob = .7;
proj.param.mri.fwhm = 8.0;
proj.param.mri.temp_hz = .0078;




%%% SCR Analysis Parameters
proj.param.betas.hirez = 20;
proj.param.physio.scr.filt_med_samp = 0.01; %(Bach 2015)
proj.param.physio.scr.filt_high = 0.0159;   %halfway between .05 and
                                            %.0159
                                            %(Staib 2015)
proj.param.physio.scr.filt_low = 5;
proj.param.physio.scr.filt_type = 2; 
%% ----------------------------------------
%% Seed random number generator
rng(1,'twister');

%% ----------------------------------------
%% Write out initialized project structure
save('proj.mat','proj');
