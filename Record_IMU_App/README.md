

<H2 align="center">APPLICATION – Record IMU LSM6DSOX </H2>


# Introduction

This document is intended to provide information about the Record IMU application used to record data from the LSM6DSOX module from ST Microelectronics.

This application was developed in order to facilitate the procedure of capture of the 3D accelerometer and 3D gyroscope data with the right format needed for the recognition of motion's project.

This application was developed in python language and uses Qt library to design the GUI.

# 1 - Run the application

## a. From the CLI

- …/App\_Python/Record\_App $ python3 main.py


##

#



# 2 - How it works

## a. Configuration

When you run the application, you first arrive at the main window as shown on the figure below.

Before starting using the recording application, you need to configure the settings.

- Go to **File** \> **Preferences :** to set the recordings files' path

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic1.PNG" align="center" height="80%" width="80%" /> <br>
  <i>Figure 1. Setting the recordings files' path</i>
</p>

- Go to **Tools** \> **Port** : to choose the COM port for the card
- 
<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic2.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 2. Setting the COM port</i>
</p>

**Figure 2 :** Setting the COM port

- Go to **Tools** \> **ODR** : to choose the Output Data Rate for the recording

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic3.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 3. Setting the ODR</i>
</p>

- Go to **Tools** \> **Time recording** : to choose the duration of the recording (5s, 10s, 20s, 30s and 60s)

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic4.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 4. Setting the time recording</i>
</p>

- Go to **Tools** \> **Time per movement**** :** to choose the duration of one motion (1s, 1.5s, or 2s)

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic5.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 5. Setting the duration of one movement</i>
</p>

**Note:** _The last repository's path that you opened to configure the recordings files' path is saved in the file config.json. If you close the application, the path is preserved._

## b. Start the recordings

### Main window

Once the previous configurations are done, you can start the recordings. First, you need to choose the classes you want to record. There is a top bar, where the available classes are displayed.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic6.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 6. Available classes on the top bar of the main window</i>
</p>

The chosen classes are displayed on the window as shown on figure 5. You can add as many classes as you want. In this example, only 2 classes are selected : "diagonal\_up\_right" and "square\_clockwise". For each class, you can add a suffix (figure 7) to customize the name of your file which will appear in the "File name" section of the window. The filename is created according to the date and hour of the recording.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic7.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 7. Suffix section to customize the filename</i>
</p>

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic8.PNG" align="center" height="80%" width="80%" /> <br>
  <i>Figure 8. Main window of the Record\_IMU\_app</i>
</p>

- Sections of the main window :
  - **Name Class** : is the name of the class (motion) that will be recorded
  - **Suffix** : to customize the name of the file
  - **Filename** : date\_hour\_class\_ODR\_suffix.csv
  - **Record button** : to switch on the recording window
  - **Status** : is for the status of the recording (green color at the end of the recording)
  - **Clear recording** : is for deleting the recording and start a new one
  - **Delete line** : is for deleting the corresponding recording line

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/alert.png" align="center" height="60%" width="60%" /> <br>
  <i>Figure 9. 'Delete Line' Alert</i>
</p>

**Note** : _The "delete line" button will not clear the recording but delete the line on the panel of the window._

###

### Recording window

To start the recording you have to click on the "REC" button.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic9.PNG" align="center" height="80%" width="80%" /> <br>
  <i>Figure 10. Recording button on the main window</i>
</p>

A new window is displayed and manages the recording session. Once you are ready to start, click on the green "Ready" button on the right side of the screen.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic10.PNG" align="center" height="50%" width="50%" /> <br>
  <i>Figure 11. Ready button on the recording window to start the recording</i>
</p>

Then, a countdown of 5 seconds is triggered before the recording starts and after that, a timer (according to the chosen duration during the configuration) is started. Then, you'll have to perform the movements shown on the screen.

The IMU data will be registered in a file at the end of the recording (to keep the real-time capture of data).

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic11.PNG" align="center" height="60%" width="60%" /> <br>
  <i>Figure 12. Example of a created logs' file</i>
</p>

At the end of the timer, the main window is automatically displayed with the updated information. Now, you can see the complete name of the created file and you also have information about the status of the recording (figure 13).

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/Record_IMU_App/Screens/pic12.PNG" align="center" height="60%" width="60%" /> <br>
  <i>Figure 13. Updated main window</i>
</p>


#

_Author: Bennamane Camelia_
