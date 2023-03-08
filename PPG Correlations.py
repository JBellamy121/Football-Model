# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Task: Correlation between PPG and other various statistics
Date: 08/03/23
"""

#Modules Used
import pandas as pd
import matplotlib.pyplot as plt
import statistics


#Analysis of correlation between PPG and Goal Difference
def ppgCorrelation():
    
    ## Graphical Analysis of Data
    
    df = footballData() #Set df to processed dataframe
    ppg = df['PPG']
    gf = df['GF']
    ga = df['GA']
    gd = df['GD']
    gRatio = gf / ga #New statisitic of Goals Scored per Goal Conceded
    
    plt.scatter(gd,ppg) #Generator scatter plot of GD vs PPG
    plt.title('PPG correlation with Goal Difference')
    plt.grid() #Display a grid on the graph
    plt.show() #Print the graph to console
    plt.clf() #Clear current plot figure
    
    plt.scatter(gf,ppg) #Generator scatter plot of GD vs PPG
    plt.title('PPG correlation with Goals Scored')
    plt.grid() #Display a grid on the graph
    plt.show() #Print the graph to console
    plt.clf() #Clear current plot figure
    
    plt.scatter(ga,ppg) #Generator scatter plot of GD vs PPG
    plt.title('PPG correlation with Goals Conceded')
    plt.grid() #Display a grid on the graph
    plt.show() #Print the graph to console
    plt.clf() #Clear current plot figure
    
    plt.scatter(gRatio,ppg) #Generator scatter plot of GD vs PPG
    plt.title('PPG correlation with Goal Ratio')
    plt.grid() #Display a grid on the graph
    plt.show() #Print the graph to console
    plt.clf() #Clear current plot figure
    
    
    ## Numerical Statistics of Data
    
    gdStrength = gd.corr(ppg) #Calculates correlation of Goal Difference and PPG
    gfStrength = gf.corr(ppg) #Calculates correlation of Goals Scored and PPG
    gaStrength = ga.corr(ppg) #Calculates correlation of Goals Conceded and PPG
    gRatioStrength = gRatio.corr(ppg) #Calculates correlation of Goal Ratio and PPG
    
    print('------------------------')
    print('Numerical  Statistics')
    print('')
    print('GD Pearson:   ',round(gdStrength,6))
    print('GF Pearson:   ',round(gfStrength,6))
    print('GA Pearson:   ',round(gaStrength,6))
    print('GR Pearson:   ',round(gRatioStrength,6))
    print('------------------------')


    
#Process in data, and automatically add PPG coloumn
def footballData():
    
    data = pd.read_csv('All Leagues Final.csv') #Import the selected data
    data['PPG'] = data['Pts'] / data['Pld'] #Add a Points Per Game coloumn to data
    data['Win%'] = data['W'] / data['Pld'] #Add a Win Percentage coloumn to data
    data['Draw%'] = data['D'] / data['Pld'] #Add a Draw Percentage coloumn to data
    data['Loss%'] = data['L'] / data['Pld'] #Add a Loss Percentage coloumn to data
    
    return data