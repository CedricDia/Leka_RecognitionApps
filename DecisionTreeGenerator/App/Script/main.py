import os, datetime
from ucf_converter import *

import command_parameters
from command_parameters import *

current_directory = os.getcwd().replace('Script', 'Trees')
current_directory = os.path.join(current_directory, datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
os.makedirs(current_directory)

from mlc_script_log import *
logger = Logger(current_directory, "")
logging.info("Current directory: " + current_directory)

import external_tools

arff_filename = os.path.join(current_directory, "features.arff")

# private import:
import mlc_configurator
from mlc_configurator import *
import decision_tree_generator
from decision_tree_generator import generateDecisionTree
from decision_tree_generator import generate_subset_of_ARFF
import mlc_test
from mlc_test import *    
from arff_generator import *

device_name = "LSM6DSOX"    ## list of supported devices available with mlc_configurator.get_devices()



#####
# ARGUMENTS MANAGE
# Parsing argument
cmd_checking = cmd_parameters()
window_length, mlc_odr, accelerometer_odr, accelerometer_fs, gyroscope_fs, gyroscope_odr, input_type, _name, motion_duration, ml_algo, k_fold = cmd_checking.check_args_value()


#############################
ucf_filename = os.path.join(current_directory, _name +".ucf")
h_filename = os.path.join(current_directory, _name +".h")



result_names  = [] # leave empty here
result_values = [] # leave empty here
datalog_results = [] # leave empty here

# Load class names (folder names) from Logs folder
direct = os.listdir("../Logs/")
print ("available classes = ", direct)

#filenames = next(os.walk(direct), (None, None, []))[1] # 2: Get all files | 1: Get all directories
class_names = list(filter(lambda file: not("DS_Store") in file, direct))

# For each class (folder), load all data (files in the folder)
datalogs = []
datalogs_split_by_class = []
for class_name in class_names:
    datalogs_i = os.listdir("../Logs/" + class_name +"/")
    print(class_name, " --> data logs: ", datalogs_i)
    datalogs_i = list(filter(lambda file: not("DS_Store") in file, datalogs_i))
    datalogs_split_by_class.append(datalogs_i)
    for datalog_i in datalogs_i:
        datalogs.append("../Logs/" + class_name + "/" + datalog_i)
        datalog_results.append(class_name)
print("All data logs: ", datalogs)
print("All data logs 0: ", datalogs[0])


# Assign results and values for decision tree 1:
result_names.append(  class_names )
result_values.append( list(range(0, len(class_names), 1)) )

    # Can't be used at the moment
# Assign results and values for decision tree 2:
result_names.append(  [] )
result_values.append( [] )
# Assign results and values for decision tree 3:
result_names.append(  [] )
result_values.append( [] )
# Assign results and values for decision tree 4:
result_names.append(  [] )
result_values.append( [] )
# Assign results and values for decision tree 5:
result_names.append(  [] )
result_values.append( [] )
# Assign results and values for decision tree 6:
result_names.append(  [] )
result_values.append( [] )
# Assign results and values for decision tree 7:
result_names.append(  [] )
result_values.append( [] )
# Assign results and values for decision tree 8:
result_names.append(  [] )
result_values.append( [] )
    #


dectree_filenames = []
for i in range(0,8): 
    if not result_names[i]:
        break
    else: 
        dectree_filenames.append(os.path.join(current_directory, "dectree{}.txt".format(i+1)))
n_decision_trees = i
logging.info('n_decision_trees = %d' % (n_decision_trees))


############

arff_calculus = Arff_generator()

    #empty because our tests were bad with features calculate on filtered data
filters_list = []

mlc_configurator.arff_generator( arff_calculus=arff_calculus,
               device_name = device_name, 
               datalogs = datalogs, 
               results = datalog_results, 
               mlc_odr = mlc_odr, 
               input_type = input_type, 
               accelerometer_fs = accelerometer_fs, 
               accelerometer_odr = accelerometer_odr, 
               gyroscope_fs = gyroscope_fs, 
               gyroscope_odr = gyroscope_odr, 
               n_decision_trees = n_decision_trees, 
               window_length = window_length,
               filters_list = filters_list,  
               arff_filename = arff_filename, 
               current_directory = current_directory)




###########################



if (n_decision_trees == 1):
    dectree_accuracy, dectree_nodes = decision_tree_generator.generateDecisionTree(
                                                        arff_filename = arff_filename, 
                                                        dectree_filename = dectree_filenames[0],
                                                        arff_calculus = arff_calculus,
                                                        ml_algo = ml_algo,
                                                        k_fold = k_fold)
else:
    for i in range(n_decision_trees) :
        arff_filename_i = arff_filename + str(i+1)
        decision_tree_generator.generate_subset_of_ARFF( arff_filename = arff_filename, 
                                                         arff_subset_filename = arff_filename_i, 
                                                         classes_subset = result_names[i] )
        logging.info("\n# Decision Tree %d:" %(i+1))
        dectree_accuracy, dectree_nodes = decision_tree_generator.generateDecisionTree( 
                                               arff_filename = arff_filename_i, 
                                               dectree_filename = dectree_filenames[i],
                                               arff_calculus = arff_calculus )



###################

# Meta-classifiers
# metaclassifierX_values contains the end counter values of the meta classifier associated to the decision tree 'X'
# 4 end counter values are available in LSM6DSOX (the first 4 values in "metaclasifierX_values")
# 8 end counter values are available in LSM6DSRX/ISM330DHCX (the 8 values in "metaclasifierX_values")
# values allowed for end counters are from 0 to 14
metaclassifier1_values = "0,0,0,0,0,0,0,0"
metaclassifier2_values = "0,0,0,0,0,0,0,0"
metaclassifier3_values = "0,0,0,0,0,0,0,0"
metaclassifier4_values = "0,0,0,0,0,0,0,0"
metaclassifier5_values = "0,0,0,0,0,0,0,0"
metaclassifier6_values = "0,0,0,0,0,0,0,0"
metaclassifier7_values = "0,0,0,0,0,0,0,0"
metaclassifier8_values = "0,0,0,0,0,0,0,0"
metaclassifier_values = [metaclassifier1_values, metaclassifier2_values, metaclassifier3_values, metaclassifier4_values, metaclassifier5_values, metaclassifier6_values, metaclassifier7_values, metaclassifier8_values]

mlc_configurator.ucf_generator( arff_calculus = arff_calculus,
                                device_name = device_name, 
                                arff_filename = arff_filename, 
                                dectree_filenames = dectree_filenames,
                                result_names = result_names, 
                                result_values = result_values, 
                                metaclassifier_values = metaclassifier_values, 
                                ucf_filename = ucf_filename, 
                                current_directory = current_directory )
                                
convert_ucf_to_h(_name, ucf_filename, h_filename)
