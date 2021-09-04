# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 08:51:17 2021

Assumptions:    Balances are always floored to the nearest integers.
                The rebalancing happens on 6th (June) and 12th (December) month.
                The allocation always happens from January, and SIP from February.
@author: ritwik
"""

import pandas as pd
import sys

portfolio={'current_balance':[0,0,0],
           'current_month':1,
           'last_rebalance':[0,0,0]
           }



def allocate_fn(args):
    #logic
    #print(args)
    return 66

def change_fn(args):
    #logic
    #print(args)
    return 92

def sip_fn(args):
    #logic
    #print(args)
    return 23

def balance_fn(args):
    #logic
    #print(args)
    return 51

def rebalance_fn(args):
    #logic
    #print(args)
    return 49


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


def get_service(action_item):
    comm_key=list(action.values())[0]
    switcher={
                "ALLOCATE":allocate_fn(comm_key),
                "CHANGE":change_fn(comm_key),
                "SIP":sip_fn(comm_key),
                "BALANCE":balance_fn(comm_key),
                "REBALANCE":rebalance_fn(comm_key),
        }
    print(list(action.keys())[0])
    print(switcher.get(list(action.keys())[0]))
    


if __name__ == '__main__':
    confs=get_confs()
    #input_file=sys.argv[1]
    input_file="input1.txt"
    commands=get_commands(input_file)
    
    for action in commands:
        get_service(action)
    