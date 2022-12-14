function [CNVgen] = convolve_scr(NEVgen,kernel)
%
%%-Description
%% This function takes in a matrix of generated neural events and
%% parameters describing the SCR function and convolves the neural
%% events and SCR function neural events
%    
%%-Parameters
%% NEVgen - true neural events generated by the model
%% kernel - data sequence representation the kernel to convolve

%%Compute number of ROIS
    [N,Bn] = size(NEVgen);
    
    %% Calc simulation steps related to simulation time
    Bk = numel(kernel); 
    
    %% Allocate Memory to store model brfs
    CNVgen = zeros(N,Bn+Bk-1);
    
    %% Convert neural events to indices
    for curr_node = 1:N

        %% Superimpose all kernels into one time-series
        for i = 1:numel(NEVgen(curr_node,:))
            CNVgen(curr_node,i:(i+Bk-1)) = NEVgen(curr_node,i)*kernel + CNVgen(curr_node,i:(i+Bk-1));
        end
    
    end

    %% Trim the excess Bk-1 time-points from result
    CNVgen = CNVgen(:,1:Bn);
    
end