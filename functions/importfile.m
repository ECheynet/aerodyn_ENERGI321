function [data] = importfile(filename, startRow, endRow,formatSpec,delimiter,varargin)

%% GOAL
% extract data from txt files or excel files to store them into matrix

%% INPUT
%  filename:
%           type: string
%           definition: name of the file whose information are extracted
% 
%  startRow:
%           type: integer
%           definition: first row of the file to be read

%  endRow:
%           type: integer
%           definition: last row of the file to be read

%  formatSpec:
%           type: string
%           definition: format of the data to be read.
%           e.g. : formatSpec = ['%f%f%f%s%s%*[^\n]']; 

%  delimiter:
%           type: string
%           definition: symbol used to delimite the columns in the file
%           e.g. : delimiter = '\t'; or delimiter = ',';

%% OUTPUT
%  data:
%           type: matrix [N1 x N2] where N1 and N2 are integers.
%           N1 = endRow-startRow or total number of rows if enRow is not
%           specified
%           N2 = defined by formatSpec.
%           definition: extracted data from the file, stored as a matrix

% Copyright (C) Etienne Cheynet, 2015.
% last modification: 27/01/2015 10:56

%% EXAMPLE
% M = randn(10,5)*10;
% dlmwrite('example.txt',M,'delimiter',',')
% filename='example.txt';
% formatSpec = ['%f%f%f%f%f%*[^\n]'];
% delimiter = ',';
% startRow=1;
% endRow=10;
% [data] = importfile(filename, startRow, endRow,formatSpec,delimiter);
%% Initialize variables.
if nargin<=2
    startRow = 1;
    endRow = inf;
end

if isempty(endRow),
    endRow = inf;
end

if ~exist(filename,'file'),
    error(['Error: ',filename,' does not exist']);
end

if nargin ==6
    WhiteSpace = varargin{1};
else 
    WhiteSpace = [];
end
%% open the text file.
fileID = fopen(filename,'r');

%Read columns of data according to format string.
if isempty(WhiteSpace),
  dataArray = textscan(fileID, formatSpec, endRow(1)-startRow(1)+1, 'Delimiter', delimiter, 'EmptyValue' ,NaN,'HeaderLines', startRow(1)-1, 'ReturnOnError', false);
    for block=2:length(startRow)
        frewind(fileID);
        dataArrayBlock = textscan(fileID, formatSpec, endRow(block)-startRow(block)+1, 'Delimiter', delimiter, 'EmptyValue' ,NaN,'HeaderLines', startRow(block)-1, 'ReturnOnError', false);
        for col=1:length(dataArray)
            dataArray{col} = [dataArray{col};dataArrayBlock{col}];
        end
    end    
else
    dataArray = textscan(fileID, formatSpec, endRow(1)-startRow(1)+1, 'Delimiter', delimiter, 'EmptyValue' ,NaN,'HeaderLines', startRow(1)-1, 'ReturnOnError', false,'whitespace', WhiteSpace);
    for block=2:length(startRow)
        frewind(fileID);
        dataArrayBlock = textscan(fileID, formatSpec, endRow(block)-startRow(block)+1, 'Delimiter', delimiter, 'EmptyValue' ,NaN,'HeaderLines', startRow(block)-1, 'ReturnOnError', false,'whitespace',WhiteSpace);
        for col=1:length(dataArray)
            dataArray{col} = [dataArray{col};dataArrayBlock{col}];
        end
    end
end
% Close the text file.
fclose(fileID);

%% Create output variable
dataArray = cellfun(@(x) num2cell(x), dataArray, 'UniformOutput', false);
data = [dataArray{1:end}];
% if iscell(data)==1,
%     data=cell2mat(data);
% end
end

