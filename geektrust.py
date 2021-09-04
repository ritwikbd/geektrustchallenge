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
import time

portfolio={'current_balance':[0,0,0],
           'current_month':1,
           'last_rebalance':[0,0,0],
           'sip':[0,0,0],
           'ratio':[0.0,0.0,0.0]
           }


def logger(log):
    f=open('logs.txt','a')
    f.write(log+ '\n')
    f.close()
    print(log)

def allocate_fn(args):
    try:
        portfolio['current_balance']=list(map(int,args))
        return 0
    except:
        return 1
    
def rebalance_fn(args):
    #logic
    #print(args)
    return 49

def change_fn(args):
    LAST_ELEMENT=-1 #We know that the last element is the month
    try:
        month=args[LAST_ELEMENT]
        change_vector=[float(x.strip('%')) for x in args[:LAST_ELEMENT]]
        for i in range(0,len(portfolio['current_balance'])):
            if month != "JANUARY":
                print(month)
                portfolio['current_balance'][i]=portfolio['current_balance'][i]+portfolio['sip'][i]
            portfolio['current_balance'][i]=int(portfolio['current_balance'][i]+(change_vector[i]/100)*portfolio['current_balance'][i])
            print(portfolio['current_balance'][i],end=' ')
            #print(args[i])
        return 0
    except:
        return 1

def sip_fn(args):
    try:
        portfolio['sip']=list(map(int,args))
        return 0
    except:
        return 1

def balance_fn(args):
    try:
        for investment in portfolio['current_balance']:
            print(investment, end=' ')
        print('')
        return 0
    except:
        return 1


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
    comm_key=list(action.keys())[0]
    comm_args=list(action.values())[0]
    print(comm_key)
    if comm_key=="ALLOCATE":
        exit_code=allocate_fn(comm_args)
        message="Allocation done with exit code "+str(exit_code)
        logger(message)
    elif comm_key=="CHANGE":
        exit_code=change_fn(comm_args)
        print("Change done with exit code ",exit_code)
    elif comm_key=="SIP":
        exit_code=sip_fn(comm_args)
        logger("SIP done with exit code "+str(exit_code))
    elif comm_key=="BALANCE":
        exit_code=balance_fn(comm_args)
        print("Balance done with exit code ",exit_code)
    elif comm_key=="REBALANCE":
        exit_code=rebalance_fn(comm_args)
        print("Rebalance done with exit code ",exit_code)
  

if __name__ == '__main__':
    
    logger("\n\nMy money problem run at "+str(time.asctime()))
    confs=get_confs()
    #input_file=sys.argv[1]
    input_file="input1.txt"
    commands=get_commands(input_file)
    for action in commands:
        get_service(action)
    