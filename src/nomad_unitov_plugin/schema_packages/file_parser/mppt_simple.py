#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:48:09 2024

@author: a2853
"""
import pandas as pd
import numpy as np
from io import StringIO


def get_value(val):
    try:
        return float(val)
    except:
        return None


def read_mppt_file(filedata):
    filedata = filedata.replace("²", "^2")

    df = pd.read_csv(
        StringIO(filedata),
        skiprows=0,s
        nrows=41,
        header=None,
        sep='\t',
        index_col=0,
        engine='python',
        encoding='unicode_escape').T
    
    df_curve = pd.read_csv(
        StringIO(filedata),
        skiprows=42,
        sep='\t',
        encoding='unicode_escape',
        engine='python')
    df_curve = df_curve.dropna(how='any', axis=0)

    print(df.T,df_curve)

    mppt_dict = {}
    mppt_dict['total_time'] = get_value(df['Test duration (hours)'].iloc[0]*60*60)
    mppt_dict['step_size'] = get_value(df['JV interval (min)'].iloc[0]*60)
    mppt_dict['time_per_track'] = get_value(df['track delay (s)'].iloc[0])
    mppt_dict['active_area'] = get_value(df['Cell Area (cm2)'].iloc[0])
    #mppt_dict['voltage'] = get_value(df.iloc[4, 0])

    mppt_dict['time_data'] = np.array(df_curve["Time (hours)"], dtype=np.float64)
    mppt_dict['voltage_data'] = np.array(df_curve["V (V)"], dtype=np.float64)
    mppt_dict['current_density_data'] = np.array(df_curve["J (mAcm-2)"], dtype=np.float64)
    mppt_dict['power_data'] = np.array(df_curve["P (mWcm-2)"], dtype=np.float64)

    return mppt_dict

import os,io;
abs_path = os.path.dirname(os.path.abspath(__file__))+'\\';
file = io.open(abs_path+r"..\..\..\..\tests\data\example_measurement\001_Tracking.txt", "r",encoding='windows-1252') 
print(read_mppt_file(file.read()))


# file = "/home/a2853/Documents/Projects/nomad/hysprintlab/mppt/0a4d713aea22a9edaf1ac8b98fd5e44e.20211129_ re_02-2.mppt.txt"
# with open(file, 'br') as f:
#     en = chardet.detect(f.read())["encoding"]
# read_mppt_file(file, en)
