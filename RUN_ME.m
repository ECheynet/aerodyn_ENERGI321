clearvars;clc;close all;
addpath('./functions') ; % add the folder function to the path
filename = 'driver_EX1'; % driver_EX1.dvr
%% Run the AeroDyn model 
% The model is run 85 times. SO there are 85 outputs, which are stored in
% the folder outputFiles 
[status] = runAerodyn(filename);
%% Read output data
%  The output data are read and stored in a single variable
tic
[data] = readOutput(filename);
toc


T = readtable([filename,'.dvr'],'FileType','text','NumHeaderLines',19);

%%
clf;close all;
figure
plot(T.Pitch,data.Cd,'linewidth',1.2)
grid on
%% Plot Cp, Ct and Cq as a function of the mean wind speed

%% PLot T, P and Q as a function of the mean wind speed
