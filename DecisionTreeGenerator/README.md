
<H2 align="center">APPLICATION – DECISION TREE GENERATOR</H2>


# Introduction

This document is intended to provide information about the decision\_tree folder containing scripts used to manage the data logs collected from the 3D accelerometer and 3D gyroscope of the IMU LSM6DSOX (ST Microelectronics product) with the Record\_APP.


<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/DecisionTreeGenerator/Screens/steps_MLC.png" align="center" height="80%" width="80%" /> <br>
  <i>Figure 1. Main steps for designing a project using the MLC feature of the lsm6dsox module</i>
</p>

This application was developed in order to facilitate the 3 steps of the whole motion recognition procedure design (step 2 to 4).

This application was developed in python language and uses sklearn library to design the decision tree.

#

# 1- Run the application

## a. From the CLI

From the command line interface (CLI) run the following command :

…/App\_python/decision\_tree/Scripts $\> python3 main.py _-n_ ucf\_filename

Note : _The argument required to run the program corresponds to the .ucf file and .h file's name._

##

#

#

# 2 - How it works

In this section, we will explain how the scripts contained in the decision\_tree folder work.

<p align="center">
<img src="https://github.com/CedricDia/Leka_RecognitionApps/blob/main/DecisionTreeGenerator/Screens/schema.png" align="center" height="80%" width="80%" /> <br>
  <i>Figure 2. Procedure of the DecisionTreeTool</i>
</p>

As described in the previous schema, the DecisionTreeTool starts using the inertial module unit's logs contained in a folder ../Logs. This folder contains the different classes of the project (1 class/folder).

**Example** : if we have only 3 classes [idle, up, down] it will be as following :

| ../Logs/idle
  ../Logs/up
  ../Logs/down |
| --- |

##

## a. Creation of the .arff file

The first script called arff\_generator.py, is used to create a text file called ARFF\_generation. This file contains the features selected to perform the machine learning algorithm and the associated data. Using the Unico tool, one can only choose 36 features maximum to generate a decision tree with the right configurations according to the chosen device. This script has been created in order to select more than 36 features. In fact, with arff\_generator.py, one can choose as many features as wished.

As shown in the schema in figure 2, the second step of the procedure of designing a decision tree for the LSM6DSOX IMU consists of creating a file containing all the features selected to create the X vector of our machine learning problem. These features are stocked in a file with the .arff extension. This file contains the selected features with their corresponding data.

##

## b. Creation of the decision tree

Once the .arff file is created, the next step is to design an algorithm of machine learning using the decision tree classifier. For that, we use the sklearn python library. The script used is decision\_tree\_generator.py.

First, we need to create 2 vectors : X and y. The X vector refers to the dataset and corresponds to the features (from the features.arff) and the y vector will contain the corresponding labels (classes). Each example corresponds to a class.

Example :

X1 = (O.OO1, …… , 9.87) here we have 1 example with n features X(1, n)

y1 = 2 : here we have the corresponding label

Then, we use the DecisionTreeClassifier() to create the classifier.

### Data split algorithm

This consists of dividing our dataset into 2 groups : the learning base + the validation base (80% or 70%) and the testing base (20% or 30%).

Note : _To select this method run the following command_

| $python main.py -ml\_algo 1 |
| --- |

###


### Cross validation algorithm (k-folds)

This algorithm consists of dividing our dataset into k sub-groups (folds) : k-1 will be the learning + validation base and 1 will be the testing base. The idea is to train the model k times at each training the testing base won't be the same so the model will train on the whole database. The overall accuracy is the mean of the k accuracies obtained from each training.

Note : _To select this method run the following command by setting the -ml\_algo to 2. To choose the k number of folds add the argument -k k\_numberI_.

| $python main.py _-ml\_algo_ 2 _-k_ k\_number |
| --- |

## c. Creation of the Unico Configuration File (.ucf file)

Once the decision tree is generated, we call the ucf\_generator() method from the mlc\_configurator.py script to create the file containing the registers' configuration of the lsm6dsox module according to the tree. This method calls Unico in background to complete the creation of the "unico configuration file" (.ucf).

This file contains a structure which is composed of 2 sections one for the registers' addresses and the other one for the data they contain.

##

## d. Creation of the header (.h file)

Once the unico configuration file is created, we call the convert\_ucf\_to\_h method from the ucf\_converter.py script to convert the .ucf file to a header file, readable by a simple script in c or c++.

## e. Configuration

The following table describes the arguments which can be added to the command before running the program.

| Arguments | Indication | Required |
| --- | --- | --- |
| --Window\_length (-wl) | Size of the window length (must be between 1 and 255) | False (default value 50) |
| --Mlc\_odr (-mlc\_odr) | Output data rate of the MLC (must be initialized to : 12.5 Hz, 26 Hz, 52 Hz or 104 Hz) | False (default value 26 Hz) |
| --Accelerometer\_odr (-acc\_odr) | Output data rate of the accelerometer (Hz) (must be initialized to : 12.5, 26, 52, 104, 208, 416, 833, 1666, 3332 or 6664) | False (default value 26 Hz) |
| --Accelerometer\_fs (-acc\_fs) | Linear acceleration measurement range (g) (must be initialized to 2, 4, 8 or 16) | False |
| --Gyroscope\_odr (-gyr\_odr) | Output data rate of the gyroscope (Hz) (must be initialized to : 12.5, 26, 52, 104, 208, 416, 833, 1666, 3332 or 6664) | False (default value 26 Hz) |
| --Gyroscope\_fs (-gyr\_fs) | Angular rate measurement range (dps) (must be initialized to 125, 250, 500, 1000 or 2000) | False |
| --Input\_type (-it) | Module use for input data :- 1 : accelerometer+gyroscope mode- 2 : accelerometer\_only mode | False |
| --Name (-n) | Name of the .ucf and .h files | True |
| --Motion\_duration (-duration) | Duration of 1 pure motion (s) (must be initialized to 1, 1.5 or 2) | False (default value 1.5s) |
| --K\_Fold (-k) | Number of folds for cross validation method (must be initalized to 5, 6, 7, 8, 9 or 10) | False (default value 10) |
| --ML\_algorithm (-ml\_algo) | Machine learning algorithm to use to generate the decision tree classifier (2 methods available) :- 1 : data split - 2 : cross validation | True |

To run the program, we need to add two required arguments :

- name of the .ucf and .h files : -n or --Name
- algorithm to generate the decision tree classifier : -ml\_algo or --ML\_Algorithm

**Note :** This part of the program is contained in the command\_parameters.py.

_Author: Bennamane Camelia_