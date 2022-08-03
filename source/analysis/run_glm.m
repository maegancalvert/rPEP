%% ----------------------------------------
%% Maegan Calvert, PhD (2021)
%% Keith Bush, PhD (2021)
%% Univ. of Arkansas for Medical Sciences
%% Brain Imaging Research Center (BIRC)
%%
%% ----------------------------------------

%%% Read data from feedback file %%%
T = readtable([proj.path.data, 'GLM_feedback_arous_contrasts_demo_.csv']);
trg = T.feedback;

%%% Read data from scr betas file %%%
T = readtable([proj.path.data, 'GLM_physio_arouse_contrasts_demo.csv']);
trg = T.beta;

%%% No longer using fba/fbs and suppress %%%
% fba = T.stims_fba;
% fbs = T.stims_fbs;
% sup = T.suppress;

%%% Variables using %%%
fbcst = T.feedbackcst;
aro = T.arouse_sup;
run = T.run;
grp = T.group;
rce = T.race;
sub = T.sub;

%%% Format subject id but do not need %%%
%sbj = [];
%for i = 1:size(sub_str,1)
%    cll = sub_str(i,:);
%    str = cll{1};
%    pcs = strsplit(str,'-');
%    id = str2num(pcs{2});
%    sbj = [sbj;id];
%end

%%% Double precision %%%
trg = double(zscore(trg));
fb = double(fbcst);
aro = double(aro);
run = double(run);
grp = double(grp);
rce = double(rce);
sbj = double(sub);

%% Generate categories
cdn_cat = categorical(aro);
fb_cat = categorical(fb);
run_cat = categorical(run);
grp_cat = categorical(grp);
rce_cat = categorical(rce);

%%% Put all data into a table that Matlab can use %%%
tbl = table(trg,cdn_cat,fb_cat,run_cat,grp_cat,rce_cat,sbj,...
            'VariableNames',...
            {'trg','cdn','fb','run','grp','rce','sbj'});
        
%%% Feedback GLM %%% 
mdlx = fitlm(tbl,['trg ~ 1 + cdn + fb + grp +'...
                     'fb:cdn + grp:cdn + fb:grp + fb:grp:cdn'])
 
%%% SCR GLM %%%
mdlx = fitlm(tbl,['trg ~ -1 + cdn + fb + grp + rce +' ...
                     'fb:cdn + grp:cdn + fb:grp:cdn'])
 
%%% Plot interactions for Feedback %%%  
figure(1)
set(gcf,'color','w');
plotInteraction(mdlx,'cdn','fb','predictions');
title('Interaction between Arousal and Feedback')
xlabel('Feedback (on/off)');
ylabel('Hyperplane Distance');
% 
figure(2)
plotInteraction(mdlx,'cdn','grp','predictions');
title('Interaction between Arousal and PTSD')
xlabel('PTSD (present/absent)');
ylabel('Hyperplane Distance');


%%% Plot interactions for SCR %%%
figure(1)
set(gcf,'color','w');
plotInteraction(mdlx,'cdn','fb','predictions');
title('Interaction between arousal and scr')
xlabel('Feedback (on/off)');
ylabel('SCR-beta');

figure(2)
plotInteraction(mdlx,'cdn','grp','predictions');
title('Interaction between arousal and PTSD')
xlabel('PTSD (present/absent)');
ylabel('SCR_beta');

figure(3)
plotInteraction(mdlx,'fb','grp','predictions');
title('Interaction between PTSD and feedback')
xlabel('PTSD (on/off)');
ylabel('SCR_beta');

%%% Feedback Fixed Effects GLM with interactions and R-squared %%%
mdl_fe = fitlme(tbl,['trg ~ 1 + cdn + fb + grp + run +' ...
                    'cdn:fb + grp:cdn + fb:grp + fb:grp:cdn'])
mdl_fe.Rsquared.Ordinary

%%% SCR Fixed Effects GLM with interactions and R-squared %%%
mdl_fe = fitlme(tbl,['trg ~ 1 + cdn + fb + run + grp + rce + ' ... 
                    'fb:cdn + grp:cdn + fb:grp:cdn + rce:cdn'])
mdl_fe.Rsquared.Adjusted

%%%Feedback Random Effects GLM and R-squared %%%
mdl_re = fitlme(tbl,['trg ~ 1 + cdn + fb + run + grp + '...
                    'fb:cdn + grp:cdn + fb:grp + fb:grp:cdn +' ...
                    '(cdn|sbj) + (fb|sbj)'])
mdl_re.Rsquared.Adjusted

%%% SCR Random Effects GLM and R-squared %%%
mdl_re = fitlme(tbl,['trg ~ -1 + cdn + fb + run + grp + rce + '...
                    'fb:cdn + grp:cdn + fb:grp + fb:grp:cdn + fb:grp:cdn:rce +' ... 
                    '(-1 + cdn|sbj) + (fb|sbj)'])
mdl_re.Rsquared.Adjusted

mdl_re = fitlme(tbl,['trg ~ 1 + cdn + fb + run + grp + '...
                    'fb:cdn + grp:cdn + fb:grp + fb:grp:cdn + ' ...
                    '(cdn|sbj) + (fb|sbj)'])
mdl_re.Rsquared.Adjusted

%%% Compare models for either feedback or SCR %%%
fe_vs_re = compare(mdl_fe,mdl_re);

mdl = mdl_fe;
re = 0;    
if(fe_vs_re.pValue<0.05);
    mdl=mdl_re;
    re = 1;
    disp('  ---Random effects matter');
    [~,~,RE] = randomEffects(mdl);
end

[~,~,FE] = fixedEffects(mdl_fe);
[~,~,FErdm] = fixedEffects(mdl_re);
[~,~,RE] = randomEffects(mdl_re);


%%% Feedback Write Table of Estimates, Standard Errors, T-stat, DF, pValue %%%
writetable(dataset2table(FE),[proj.path.log,'feedback_fixed_effects_out.txt'])
writetable(dataset2table(FErdm),[proj.path.log, 'feedback_fixedrdm_effects_out.txt'])
writetable(dataset2table(RE),[proj.path.log, 'feedback_random_effects_out.txt'])

%%% SCR Write Table of Estimates, Standard Errors, T-stat, DF, pValue %%%
writetable(dataset2table(FE),[proj.path.log, 'SCR_fixed_effects_out.txt'])
writetable(dataset2table(FErdm),[proj.path.log, 'SCR_fixedrdm_effects_out.txt'])
writetable(dataset2table(RE),[proj.path.log, 'SCR_random_effects_out.txt'])



