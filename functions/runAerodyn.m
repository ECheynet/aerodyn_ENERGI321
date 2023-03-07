function [status] = runAerodyn(filename)
% The function [status] = runAerodyn(filename) runs the aerodyn model and
% move the output files in an output folder named "outputFiles"
% 
% Author: E Cheynet - UiB - 15/03/2022

%% Run Aerodyn
command=['./bin/AeroDyn_Driver_x64 ',filename,'.dvr'] ;   

if ismac
    % check https://www.hsph.harvard.edu/liming-liang/software/mac/
    status = system(['wine ',command]);% Code to run on Mac platform
elseif isunix
    status = system(['wine ',command]); % Code to run on Linux platform
elseif ispc
    status = system(command);  %Zero means it worked!
else
    disp('Platform not supported')
end

%% Move the output files in a specific folder
if ~exist('outputFiles','dir'), mkdir('outputFiles'); end
movefile('*.out','outputFiles')

end

