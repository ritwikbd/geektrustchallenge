# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 08:51:17 2021

@author: ritwi
"""

import pandas as pd
import sys

def get_confs():
    conf_file=pd.read_csv("confs.txt",delimiter='=')
    confs_dict= dict(zip(conf_file['keys'],conf_file['values']))
    return confs_dict

def read_command(command_instance):
    """
    Arguments taken: 1 dataframe. Returns 1 Dictionary
    This function reads the input file, parses the commands to identify the command keword and arguments and returns it in the form of a list
    """
    command_keyword=command_instance['allfields'][0]
    command_args=command_instance['allfields'][1:]
    return {command_keyword:command_args}


def get_commands(input_file_path):
    """
    Arguments taken: 1 string. Returns 1 List
    This function reads the input file, parses the commands to identify the command keword and arguments and returns it in the form of a list
    """
    command_set=pd.read_csv(input_file_path, header= None)
    command_set['allfields']=command_set[0].str.split(' ')
    command_set.drop(columns=0,inplace=True)
    parsed_commands=list(command_set.apply(lambda x: read_command(x),axis=1))
    return parsed_commands



if __name__ == '__main__':
    confs=get_confs()
    print(confs)
    #input_file=sys.argv[1]
    input_file="input1.txt"
    commands=get_commands(input_file)
    
    for action in commands:
        print(action)
    