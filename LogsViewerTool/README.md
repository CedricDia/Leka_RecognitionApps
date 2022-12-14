

<H2 align="center">APPLICATION – LOGS VIEWER TOOL</H2>

#


# Introduction

This document is intended to provide information about the _Logs Viewer Tool used_ to visualize data recording with the _Record IMU application_.

This application was developed with python language and uses mainly the library QT to design GUI.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image1.png" align="center" height="80%" width="80%" /> <br>
  <i>Figure 1. Logs Viewer Tool Interface</i>
</p>


# Run application

## On a terminal

Check if you have python installed. If it is the case, launch a terminal and go to the path where python's files are located, then type this line:

**Example** :

….\LogsViewerTool\> python ./main.py


# How it works

When you run the application, you arrive on this page:

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image2.png" align="center" height="80%" width="80%" /> <br>
  <i>Figure 2. Interface by default</i>
</p>

As you can see, no graphs are plotted.

  
## Import a File

    
### Format file

Be careful, the file imported must look like this:

- File's extension: _ **.csv** _or _ **.txt** _.
- The name of the file must be like this :

**yyyy\_MM\_dd-HH\_mm\_ss-ODR\_valueHz-Shape\_Name-suffix.csv or .txt**

- The file has 6 columns separated by a _ **tabulation** _.
- First Line of the file is the _ **headline** _, each column has a **title** with **unity**.
- Each column of the other lines must be a **value** (with a _ **dot** _ if it's decimal).

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image3.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 3. Example of a file log</i>
</p>

    
### Choose the file !

To import a file, click on the orange button:

<p align="right">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image4.PNG" align="center" height="15%" width="15%" /> <br>
  <i>Figure 4. Button "import"</i>
</p>
It will open a new tab where you can choose the file to analyze.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image5.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 5. Import File</i>
</p>

You can select the file that you want, but it's preferable to open the 'basic file', (i.e. the one without average or delta in his name). Indeed, in this application when you select a basic file to open, the application will automatically open the same files with average and delta in their name. The different files must be in the same repository as the basic file.

_ **For instance** __: Select the file: '[…]-26Hz-Right-First.csv', then click on the Open Button. Application will automatically open:_

- '_[…]-26Hz-Right-First-average-Range\_4.csv'_
- '_[…]-26Hz-Right-First-average-Range\_8.csv'_
- '_[…]-26Hz-Right-First-average-Range\_16.csv'_
- '_[…]-26Hz-Right-First-delta.csv'_

_All these files can be plotted on the graph as we will see just below._

**Note:** _The last repository's path that you opened to select a file is saved in the file config.json. If you close the application, the path is preserved._

  
## Visualize curves

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image6.png" align="center" height="80%" width="80%" /> <br>
  <i>Figure 6. Interface after import a file</i>
</p>

Once you open a file, a curve appears. As you probably saw, the **component** _"Acc\_x"_ is selected and the **checkbox** _"Raw Data"_ is checked at the left by default. The blue curve then corresponds to the graph of raw data of the accelerometer on X axis.

As you can see on the bottom of the page, you can observe these informations:

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image7.png" align="center" height="60%" width="60%" /> <br>
  <i>Figure 7. Informations given</i>
</p>

These are calculated with the **ODR\_valueHz** and **the number of lines in the raw data file.**

**Time recording = Samples number \* 1/ODR\_valueHz**

**Here:** 790\*1/26 = 30.38s

    
### ![Shape3](RackMultipart20220914-1-z6q0vw_html_aa9768843f3a272.gif)Components

When you click on the components bar a new tab is opened figure 7.

<p align="right">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image8.PNG" align="center" height="10%" width="10%" /> <br>
  <i>Figure 8. Components Onglet</i>
</p>

You can observe only one component at a time.

Each component is automatically added to the selection in function of each columns.

- 'A\_\*' corresponds to _Accelerometer_
- 'G\_\*' corresponds to _Gyroscope_
- 'M\_\*' corresponds to Magnetometer

**For instance** : _for the file showed above at figure 3, in components tab we will just find A\_\* and G\_\* componenents because we don't have magnetometer columns here._

This is therefore very flexible.


**For instance:** _If your file contains only these components and that you have a column F\_X corresponding to an other external tools, it will be added to the components selection._

<p align="left">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image10.PNG" align="center" height="20%" width="20%" /> <br>
  <i>Figure 9. New selection</i>
</p>
<p align="right">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image9.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 10. Example of a file with different columns</i>
</p>

**Note** _ **:** _ _For developers, if you want to add an other component like 'F\_', and you want to change the ordinate and the title of the graph, you just need to add a condition in Component class, in the_ _ **page\_graph.py** _ _and specify the self.title and self.ordinate corresponding_.

    
### Data Type

Checking a box will plot the data corresponding to the name of the checkbox.

<p align="left">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image11.PNG" align="center" height="20%" width="20%" /> <br>
  <i>Figure 11. Data type section</i>
</p>

If the corresponding file doesn't exist, then the checkbox is inactive.

You can check one or several boxes at the same time. Each box checked shows a specific curve. Thereby, you can superimpose curves in the same graph in order to compare them.

The order of the boxes defines on which plane the curve will be. "Raw Data" curve will be on the first plane, "Average 4" curve will be between the first plane and the "average 8 plane", etc.

The average is done on a number of samples, per example '8'. Therefore, in order to remove the delay and to align with raw data's curve caused by the average, the application automatically adds n 0 (n is the difference between the number of lines of Raw data and the number of lines after average).

**Note:** If you want to add a 'Data Type' in the boxes list, it's easy. In page\_graph.py, just add the name of the type in "self.type\_data\_to\_show".

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image12.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 12. Different data files</i>
</p>

**For instance** __: If I want to add the possibility to visualize data treated by a lowpass filter. Just add the file corresponding in the repository where the file with raw data is located._

_The name of this new file must have the same pattern as the raw data file._

_Namefile: Data-Time-ODR-Suffix-xxxx.csv_

_(xxxx is here 'lowpass\_filter')_

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image13.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 13. Array with data type (page\_graph.py)</i>
</p>

_And had "-lowpass\_filter in the array just like below:_

<p align="right">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image14.PNG" align="center" height="20%" width="20%" /> <br>
  <i>Figure 14. Data type section with a new line</i>
</p>

_If you run the application, you can see that a new choice "lowpass filter" is possible to check. The name of the line corresponds to the element that you added to the array where '-' and '\_' are replace by a space._

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image15.png" align="center" height="80%" width="80%" /> <br>
  <i>Figure 15. Accelerometer (axis Y) showed with average on 8 and 16 samples</i>
</p>

    
### Change view

If you want to zoom on an area of the graph, you just have to put the mouse's cursor where you want to zoom and scroll.

If you click on the graph and maintain this, you can translate it where you want.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image16.png" align="center" height="80%" width="80%" /> <br>
  <i>Figure 16. Graph zoomed</i>
</p>


Click on the button represented figure 17 to reset the view as default
<p align="right">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image17.png" align="center" height="15%" width="15%" /> <br>
  <i>Figure 17. Reset view button</i>
</p>
    
### Play with Pages

If you want to observe different data in order to compare them for example, you can do it with page management.

<p align="left">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image18.png" align="center" height="15%" width="15%" /> <br>
  <i>Figure 18. Add Page button</i>
</p>

On the right top corner of the application, you can see a button "Add page". It allows you to add a new empty page with a graph section.

When you import a file, the title of the page is updated.

To switch the page shows, just click on the top bar with the page's names.
<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image19.PNG" align="center" height="40%" width="40%" /> <br>
  <i>Figure 19. Pages toolbar</i>
</p>


If you want to remove a page, click on this button
<p align="right">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image20.png" align="center" height="15%" width="15%" /> <br>
  <i>Figure 20. 'Remove Page' button</i>
</p>

_An alert message will then appear, click on "Yes" to remove the page, or "No" else._

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image21.png" align="center" height="40%" width="40%" /> <br>
  <i>Figure 21. 'Delete Page' Alert 1</i>
</p>

_If you try to delete the only page present on your app, you receive this information message:_

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image22.png" align="center" height="40%" width="40%" /> <br>
  <i>Figure 22. 'Delete Page' Alert 2</i>
</p>
    
### Quit the application

If you want to close the application, you can click on:

- File\>Exit.
- Press Echap
- Click on the red cross as usual

An alert is showed to confirm than you really want to close the application

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/LogsViewerTool/Screens/image23.png" align="center" height="40%" width="40%" /> <br>
  <i>Figure 22. 'Quit the app' Alert</i>
</p>

#

_Author: Diavorini Cédric_
_Mail: diavorini.Cedric.dev@gmail.com_

