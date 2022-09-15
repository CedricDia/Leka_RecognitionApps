import pandas as pd
from sklearn.tree import DecisionTreeClassifier  # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split  # Import train_test_split function
from sklearn.model_selection import StratifiedKFold 
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn import preprocessing
from statistics import mean
from sklearn import metrics  # Import scikit-learn metrics module for accuracy calculation
from sklearn import tree
from scipy.io import arff
import re
import sys
import numpy as np
import os
import logging

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import *
import pydotplus
from sklearn.tree import export_graphviz


def isLeaf(src_str):
    r = re.match("[0-9]+ \[label=\"", src_str)
    s = re.search("\\\\n", src_str)
    if (r != None and s == None):
        return True
    else:
        return False


def printClassName(src_str, dt_file):
    r = re.search("[0-9]+ \[label=\"", src_str)
    s = re.search("\"\] ;", src_str)
    t = re.search("\\\\n", src_str)
    if (r != None and s != None and t == None):
        print(src_str[r.end():s.start()], end="", file=dt_file)


def printCondition(src_str, dt_file):
    r = re.search("[0-9]+ \[label=\"", src_str)
    s = re.search("\\\\n", src_str)
    if (r != None and s != None):
        print(src_str[r.end():s.start()], end="", file=dt_file)


def getNodeNum(src_str):
    r = re.match("[0-9]+", src_str)
    if (r != None):
        return int(r.group(0))
    else:
        print("on rentre ici pardi")
        return ""


def getNextLineIndex(src_list, node_num):
    tmp = []
    i = len(src_list) - 1
    for line in reversed(src_list):
        if (getNodeNum(line) == int(node_num)):
            return i
        i -= 1
    return -1


def isNodeInfo(src_str):
    if (re.match('[0-9]+ -> [0-9]+[ ]+;', src_str) != None):
        return True
    else:
        return False


def oppOperator(src_str):
    src_str = src_str.replace("<=", ">")
    src_str = src_str.replace(">=", "<")
    return src_str


def formatTree(line, indent, dt_file):
    # Init to zeros, will store n_nodes and n_leaves
    size = np.array([0, 0])
    # If the first line is just node connection info line, skip it
    if (isNodeInfo(line[0])):
        line = line[1:]

    # Add this node
    size[0] += 1

    # If the first line is a leaf, print its name with \n, otherwise only \n
    if (isLeaf(line[0])):
        print(": ", end="", file=dt_file)
        printClassName(line[0], dt_file)
        print("", file=dt_file)
        return np.array([1, 1])
    else:
        print("", file=dt_file)

    nIndex = getNodeNum(line[0])  # Get node index
    splitIndex = getNextLineIndex(line[1:], nIndex)  # Get split index

    if (len(line[1:splitIndex]) > 0):
        # Print original condition
        print("|   " * indent, end="", file=dt_file)
        printCondition(line[0], dt_file)
        size += formatTree(line[1:splitIndex], indent + 1, dt_file)  # Call recursively for the first part of original tree

    if (len(line[splitIndex - 1:]) > 0):
        # Print opposite condition
        print("|   " * indent, end="", file=dt_file)
        printCondition(oppOperator(line[0]), dt_file)
        size += formatTree(line[splitIndex - 1:], indent + 1, dt_file)  # Call recursively for the second part of original tree

    return size

def isolate_feature_used(line):
    return line.split("label=\"")[1].split(" ")[0]


def isolate_feature_CV(tree, arff_calculus):
    for line in tree:
        r = re.search(r"(?<= )+\w+", line)
        #print(r.group())
        if r is not None:
            if("F" in line):
                feature = r.group()
                if not  feature in arff_calculus.features_used_for_tree:
                    arff_calculus.features_used_for_tree.append(feature)

def formatTreeCV(_tree_, dt_file_, n_nodes, n_leaves):
    index = 0
    index_ = []
    classes = []
    
    #print(_tree_)
    for line in _tree_:
        if("class:" in line):
            c = line.split("class:")
            ind = index - 1
            index_.append(ind)
            classes.append(c[1])
        index += 1
    
    for z in range(len(index_)):
        _tree_[index_[z]] = _tree_[index_[z]].strip('\n')
        _tree_[index_[z]] = _tree_[index_[z]] + ":" + classes[z]
        
    
    for lin in _tree_:
        lin = lin.replace('---', '  ')
        lin = lin[4:]
        
        if("class:" not in lin):
            dt_file_.write(lin)
    
    """
    # Save to file
    n_nodes = tr.tree_.node_count
    n_leaves = tr.get_n_leaves()
    #dt_file_.write(tr)
    """
   
    print('\nNumber of Leaves  : \t', n_leaves, file=dt_file_)
    print('\nSize of the Tree : \t', n_nodes, file=dt_file_)

    return n_nodes, n_leaves


def saveTreeCV(tree_, dt_file_, feature_name):
    tr = tree.export_text(tree_, feature_names = feature_name)
    #print(tr)
    
    # Save to file
    dt_file_.write(tr)
   


def printTree(dot_tree, dt_file, arff_calculus):
    new_tree = []

    # Preprocess the tree
    for line in dot_tree.split("\n"):
        r = re.search("[0-9]+\\\\n\[([0-9]+[,]?[ ]?)+\]\\\\n", line)
        s = re.search("\[labeldistance=[0-9]+\.?[0-9]*, labelangle=-?[0-9]+, headlabel=\"(False|True)\"\]", line)
        if (r != None):
            line = line[:r.start()] + line[r.end():]
            if("F" in line and "_on_" in line):
                feature = isolate_feature_used(line)
                if not feature in arff_calculus.features_used_for_tree:
                    arff_calculus.features_used_for_tree.append(feature)
        if (s != None):
            line = line[:s.start()] + line[s.end():]
        new_tree.append(line)

    # Print in Weka format
    size_tree, n_leaves = formatTree(new_tree[3:-1], 0, dt_file)

    print('\nNumber of Leaves  : \t', n_leaves, file=dt_file)
    print('\nSize of the Tree : \t', size_tree, file=dt_file)

    n_nodes = n_leaves - 1

    return n_nodes, n_leaves


def data_split_algo(X, y):
    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                        random_state=1)  # 70% training and 30% test

    # Create Decision Tree classifer object
    clf = tree.DecisionTreeClassifier(random_state=1, max_depth=256)  # You can specify the max depth by passing argument for example: max_depth=3

    # Train Decision Tree Classifer
    clf = clf.fit(X_train, y_train)

    # Predict the response for test dataset
    y_pred = clf.predict(X_test)

    

    return clf, X_train, X_test, y_train, y_test, y_pred


def cross_validation_algo(X, y, k_fold):
    #Stratified cross validation
    clf = tree.DecisionTreeClassifier()
    skf = StratifiedKFold(n_splits=k_fold, shuffle=True, random_state=1)
    lst_accu_stratified = []
    lst_rec_stratified = []
    lst_f1_stratified = []
    lst_mse_stratified = []

    scaler = preprocessing.MinMaxScaler()
    x_scaled = scaler.fit_transform(X)
    

    for train_index, test_index in skf.split(X, y):
        X_train, X_test = x_scaled[train_index], x_scaled[test_index]
        y_train, y_test = y[train_index], y[test_index]
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        label_encoder = LabelEncoder()
        y_test_enc = label_encoder.fit_transform(y_test)
        y_pred_enc = label_encoder.fit_transform(y_pred)

        scaler = StandardScaler()
        y_test_scaler = scaler.fit_transform(y_test_enc.reshape(-1, 1))
        y_pred_scaler = scaler.fit_transform(y_pred_enc.reshape(-1, 1))

        lst_accu_stratified.append(clf.score(X_test, y_test))
        lst_rec_stratified.append(recall_score(y_test, y_pred, average='weighted'))
        lst_f1_stratified.append(f1_score(y_test, y_pred, average ='weighted'))
        lst_mse_stratified.append(mean_squared_error(y_test_scaler, y_pred_scaler, squared=True))

    #Predict the response for test dataset
    print('list accu : ', lst_accu_stratified)
    print('list recall :', lst_rec_stratified)
    print('list f1 :', lst_f1_stratified)
    print('list mse :', lst_mse_stratified)
    print('Overall accuracy', mean(lst_accu_stratified)*100, '%')
    
    
    return clf, X_train, X_test, y_train, y_test, lst_accu_stratified, lst_rec_stratified, lst_f1_stratified, lst_mse_stratified


def generateDecisionTree( arff_filename, dectree_filename, arff_calculus, ml_algo, k_fold):
    data = arff.loadarff(arff_filename)  # <- Write desired file here
    data_set = pd.DataFrame(data[0])
    data_set['class'] = data_set['class'].str.decode('ASCII')
    col_names = list(data_set)

    feature_cols = col_names[:-1]
    class_name = list(set(data_set[col_names[-1]]))
    X = data_set[feature_cols]  # Features
    y = data_set[col_names[-1]]  # Target variable
    
    # ----------------- Cross validation Method ----------------- #

    if(ml_algo == 'cross_validation'):
        clf, X_train, X_test, y_train, y_test, lst_accu_stratified, lst_rec_stratified, lst_f1_stratified, lst_mse_stratified = cross_validation_algo(X, y, k_fold)
        dot_tree = tree.export_graphviz(clf, out_file=None, class_names=clf.classes_, label="none", impurity=False,
                                    feature_names=feature_cols)

    
        feature_name=list(X.columns)
        class_name = list(y_train.unique())

        
        dectree_accuracy = mean(lst_accu_stratified)*100
        dectree_f1 =  mean(lst_f1_stratified)*100
        dectree_recall =  mean(lst_rec_stratified)*100
        dectree_mse =  mean(lst_mse_stratified)*100

        # Save to file
        dt_file = open(dectree_filename, "w")
        saveTreeCV(clf, dt_file, feature_name)

        dt_file.close()
        n_nodes = clf.tree_.node_count
        n_leaves = clf.get_n_leaves()

        # Read file for logging
        with open(dectree_filename, "r") as file_r:
            data_tree = file_r.readlines()

        with open(dectree_filename, "w") as file_w:
            formatTreeCV(data_tree, file_w, n_nodes, n_leaves)

        isolate_feature_CV(data_tree, arff_calculus)

        if n_nodes > 0:
            logging.info("Accuracy:" + str(dectree_accuracy))
            logging.info("F1:" + str(dectree_f1))
            logging.info("Recall:" + str(dectree_recall))
            logging.info("MSE:" + str(dectree_mse))
        
        else: 
            logging.error("ERROR: decision tree empty. Please check selected features")


    #----------------- Data split Method ----------------- #

    elif(ml_algo == 'data_split'):
       
        clf, X_train, X_test, y_train, y_test, y_pred = data_split_algo(X,y)

        # Model Accuracy, how often is the classifier correct?
        dectree_accuracy = metrics.accuracy_score(y_test, y_pred)

        dot_tree = tree.export_graphviz(clf, out_file=None, class_names=clf.classes_, label="none", impurity=False,
                                    feature_names=feature_cols)

        # Save to file
        dt_file = open(dectree_filename, "w")
        n_nodes, n_leaves = printTree(dot_tree, dt_file, arff_calculus)
        dt_file.close()

        # Read file for logging
        text_file = open(dectree_filename, "r")
        file_content = text_file.read()
        text_file.close()
        if n_nodes > 0:
            logging.info("Accuracy:" + str(dectree_accuracy))
            logging.info(file_content)
        else: 
            logging.error("ERROR: decision tree empty. Please check selected features")


    return dectree_accuracy, n_nodes

    


def generate_subset_of_ARFF(arff_filename, arff_subset_filename, classes_subset):
    with open(arff_filename, "r") as input:
        with open(arff_subset_filename, "w") as output:
            data_section_started = False
            for line in input:
                if line.startswith('@attribute class {'):
                    new_line_class = '@attribute class {'
                    for i_class in range(len(classes_subset)):
                        if i_class > 0:
                            new_line_class += ', '
                        new_line_class += classes_subset[i_class]
                    new_line_class += '}\n'
                    output.write(new_line_class)
                else:
                    if line.startswith('@data'):
                        data_section_started = True
                        output.write(line)

                    if (data_section_started == False):
                        output.write(line)
                    else:
                        class_in_line = line.split(', ')[-1]
                        if (class_in_line.rstrip() in classes_subset):
                            output.write(line)
    input.close()
    output.close()
    return