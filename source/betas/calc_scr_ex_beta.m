%%========================================
%%========================================
%% Maegan Calvert, PhD (2021)
%% Keith Bush, PhD (2021)
%% Univ. of Arkansas for Medical Sciences
%% Brain Imaging Research Center (BIRC)
%%
%%========================================
%%========================================

%% Load in path data
load(init_proj)

%% Set-up Directory Structure for SCR
if(proj.flag.clean_build)
     disp(['Removing ',proj.path.betas.scr_ex_beta]);
     eval(['! rm -rf ',proj.path.betas.scr_ex_beta]);
     betas = 'ex_betas';
     disp(['Creating ',proj.path.betas.scr_ex_beta]);
     eval(['! mkdir ',proj.path.betas.scr_ex_beta]);
end

%% Create the subjects to be analyzed

f = fopen(proj.path.subjs);
subjs = textscan(f,'%s'); % issue is that textscan opens string as a cell array within a cell
subjs = subjs{1};         % so here we convert to a single cell array of strings
fclose(f);

%% Define the task and type details
task = proj.param.mri.tasks{2}; %modulate
Nscans = proj.param.mri.Nscans(2); %number of scans
n_tr = proj.param.mri.Nvol(2); %using modulate1, but have same amount of volumes for modulate 2; if code was written differently, could be more simple
TR = proj.param.mri.TR;
stim_t = proj.param.mri.stim_t;

%% Fit beta series for each subject
for i=1:numel(subjs)
      
    %% extract subject info
    name = subjs{i};
   
    %% debug
    %logger(['sub:',name],proj.path.logfile);

    %% Initizlize scr beta structure
    ex_betas = struct();

    for j = 1:Nscans

        %% Load bids events files for the taskn
        filename = [proj.path.bids_name, name,'/func/sub-', name,'_task-',task,num2str(j),'_events.tsv'];
        events = tdfread(filename); 

        %% Construct onset times for regression
        onset = [];
        duration = [];
        trial_type = [];

        for k = 1:numel(events.onset)
            if exist(filename)
                
                type = events.trial_type(k,:);
                onset = [onset;events.onset(k)];    
                duration = [duration;events.duration(k)];
                trial_type = [trial_type;events.trial_type(k,:)];
            else
                if isempty(filename)
                    continue
                end
            end
            
        end
        
        %%% DEBUG to FIX CRASHING
        good_ids = find(onset<n_tr*2);
        onset = onset(good_ids);
        duration = duration(good_ids);
        trial_type = trial_type(good_ids,:);
            
                            
        [prime_ex other_ex] = scr_dsgn_preprocv2(proj,n_tr,onset,duration);
        plot(prime_ex);
        drawnow;
      
        %% LSS of scr signal (Mumford, 2012)
        ex_betas.(['mod',num2str(j)]) = [];
        path = [proj.path.physio.scr_clean,'rPEP_',name,'_',task,num2str(j),'.mat']
        load(path);
    
        for k=1:size(prime_ex, 1)
            mdl_ex = regstats(scr,[prime_ex(k,:)',other_ex(k,:)']);
            ex_betas.(['mod',num2str(j)]) = [ex_betas.(['mod',num2str(j)]),mdl_ex.beta(2)];
        end

        %% Create table that includes betas, trial_type
        if length(trial_type)== length(ex_betas.(['mod',num2str(j)])');
            T = table(trial_type,ex_betas.(['mod',num2str(j)])');
        else 
            trial_type2 = length(trial_type(:,-1));
            T = table(trial_type2,ex_betas.(['mod',num2str(j)]));
        end
        
        %% Save individual betas
        save([proj.path.betas.scr_ex_beta,'sub-',name,(['_mod',num2str(j)]),'ex_betas.mat'],'ex_betas');
        writetable(T,[proj.path.betas.scr_ex_beta,'sub-',name,(['_mod',num2str(j)]), 'ex_betas.csv'],'Delimiter','\t');
    [i j k]
    end
end




  
