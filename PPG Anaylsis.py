# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Task: PPG Anaylsis of various UEFA Leagues
Date: 07/03/23
"""

#Modules Used
import pandas as pd
import matplotlib.pyplot as plt
import statistics


#Generate visual and numerical statistics around PPG
def dataAnalysis():
    
    df = footballData() #Set df to processed dataframe
    ppg = df['PPG']
    
    
    ## Graphical Analysis of Data
    
    plt.hist(ppg,bins=16) #Graph the PPG Data to a histogram
    plt.grid() #Display a grid on the graph
    plt.show() #Print the graph to console
    
    
    ## Numerical Statistics of Data
    
    ppgMean = statistics.mean(ppg) #Calculate the mean of the ppg
    ppgMedian = statistics.median(ppg) #Calculate the median of the ppg
    ppgStd = statistics.stdev(ppg) #Calculate the standard deviation of the ppg
    
    print('----------------------')
    print('Numerical  Statistics')
    print('')
    print('PPG Mean:   ',round(ppgMean,6))
    print('PPG Median: ',round(ppgMedian,6))
    print('PPG Stdev:  ',round(ppgStd,6))
    print('----------------------')
    
    
#Process in data, and automatically add PPG coloumn
def footballData():
    
    data = pd.read_csv('All Leagues Final.csv') #Import the selected data
    data['PPG'] = data['Pts'] / data['Pld'] #Add a Points Per Game coloumn to data
    
    return data
