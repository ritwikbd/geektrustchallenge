# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 08:51:17 2021

@author: ritwi
"""

import pandas as pd

def read_command(command_instance):
    command_keyword=command_instance['allfields'][0]
    command_args=command_instance['allfields'][1:]
    return {command_keyword:command_args}


def get_commands():
    command_set=pd.read_csv("input1.txt", header= None)
    command_set['allfields']=command_set[0].str.split(' ')
    command_set.drop(columns=0,inplace=True)
    parsed_commands=list(command_set.apply(lambda x: read_command(x),axis=1))
    return parsed_commands



if __name__ == '__main__':
    commands=get_commands()
    for action in commands:
        print(action)