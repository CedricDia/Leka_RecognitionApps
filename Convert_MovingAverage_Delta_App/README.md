

<H2 align="center">APPLICATION – Convert Moving Average and Delta </H2>


# Introduction

This document is intended to provide information about the _Convert App used_ to automatically calculate the moving average and the difference between 2 data from a log file.

This application was developed with python language and uses mainly the library QT to design GUI.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Convert_MovingAverage_Delta_App/Screens/interface.png" align="center" height="80%" width="80%" /> <br>
  <i>Figure 1. Interface of the application</i>
</p>

# How it works

  
## Import a File

At first, you have to select which logs file you want to transform.

To do this, just click on the browse button of the line 'File to transform' and select the file.

    
### Format file

It can have the following extensions: .txt or .csv.

The file must be like this example figure 2 i.e., 6 data columns with at the first line a headline and a dot for each decimal data.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image3.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 2. Example of a file log</i>
</p>
  
## Select the destination folder

When you run the application, the destination folder will automatically be generated to be in the file Ouputs present in the application folder.

You can change this path easily by clicking on the browse button of the line 'Path where the file will be registered'.

  
## Generate a moving average file

If you want to generate a single moving average, you have to choose on how much samples N you want to calculate this.

The formula to get the moving average is the following:

To select this N, you must type it in the case on the right top corner at the line 'Range:'

Then click on the green button 'Generate'. The algorithm will calculate the moving average on the first N data for each column (from index 0), then increment by one the index, calculate the average between index 1 and index+N, the repeat this until the end of the file. The result of this is stocked in an array then writing in a file.

The name of the created file will be ORIGINAL\_FILE\_NAME-average-Range\_N.csv

Note: If you want to generate rapidly 3 moving average files on 4, 8 and 16 samples, you can click on the orange button 'Generate [sample – 4/8/16]'.

If it works, a green message will appear 'File created successfully!', and if it doesn't then a red message 'File not created, [the reason]'.

  
## Generate a delta file

If you want to generate a delta file, you must click on the blue button 'Generate delta file'.

Delta corresponds to the difference between 2 data:

Click on this button will generate a file where the delta is calculated for each column until arriving at the end of the file.

The new file name will be: ORIGINAL\_FILE\_NAME -Cedric-delta.csv

  
## Note

The Record\_IMU\_App application can automatically generate moving average after each recording but the line in the script find\_com.py is commented by default. The script present in Record\_IMU\_App is better because it's more secure than Convert\_App with the manage different possible bugs.



_Author: Diavorini Cédric_
_Mail: diavorini.Cedric.dev@gmail.com_

