# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Task: PPG Anaylsis of various UEFA Leagues, and Match Outcome Anaylsis
Date: 07/03/23
"""

#Modules Used
import pandas as pd
import matplotlib.pyplot as plt
import statistics


#Run ppgAnalysis() for the statistics on the Points Per Game for the dataset
#Run matchAnalysis() for the statistics on the Win%, Draw%, Loss% for the dataset


#Generate visual and numerical statistics around PPG
def ppgAnalysis():
    
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
    
    
def matchAnalysis():
    
    df = footballData() #Set df to processed dataframe
    win = df['Win%']
    draw = df['Draw%']
    loss = df['Loss%']
    
    ## Graphical Analysis of Data
    
    plt.hist(win,bins=12) #Graph the Win% Data to a histogram
    plt.title('Win Percentage')
    plt.grid() #Display a grid on the graph
    plt.show() #Print the graph to console
    plt.clf() #Clear the figure
    
    plt.hist(draw,bins=12) #Graph the Draw% Data to a histogram
    plt.title('Draw Percentage')
    plt.grid() #Display a grid on the graph
    plt.show() #Print the graph to console
    plt.clf() #Clear the figure
    
    plt.hist(loss,bins=12) #Graph the Loss% Data to a histogram
    plt.title('Loss Percentage')
    plt.grid() #Display a grid on the graph
    plt.show() #Print the graph to console
    
    
    ## Numerical Analysis of Data
    
    winMean = statistics.mean(win) #Calculate the mean of the win%
    winMedian = statistics.median(win) #Calculate the mean of the win%
    winStd = statistics.stdev(win) #Calculate the mean of the win%
    
    drawMean = statistics.mean(draw) #Calculate the mean of the draw%
    drawMedian = statistics.median(draw) #Calculate the mean of the draw%
    drawStd = statistics.stdev(draw) #Calculate the mean of the draw%
    
    lossMean = statistics.mean(loss) #Calculate the mean of the loss%
    lossMedian = statistics.median(loss) #Calculate the mean of the loss%
    lossStd = statistics.stdev(loss) #Calculate the mean of the loss%
    
    print('-----------------------')
    print('Numerical  Statistics')
    print('')
    print('Win% Mean:    ',round(winMean,6))
    print('Win% Median:  ',round(winMedian,6))
    print('Win% Stdev:   ',round(winStd,6))
    print('')
    print('Draw% Mean:   ',round(drawMean,6))
    print('Draw% Median: ',round(drawMedian,6))
    print('Draw% Stdev:  ',round(drawStd,6))
    print('')
    print('Loss% Mean:   ',round(lossMean,6))
    print('Loss% Median: ',round(lossMedian,6))
    print('Loss% Stdev:  ',round(lossStd,6))
    print('-----------------------')
    
    
#Process in data, and automatically add PPG coloumn
def footballData():
    
    data = pd.read_csv('All Leagues 4.csv') #Import the selected data
    data['PPG'] = data['Pts'] / data['Pld'] #Add a Points Per Game coloumn to data
    data['Win%'] = data['W'] / data['Pld'] #Add a Win Percentage coloumn to data
    data['Draw%'] = data['D'] / data['Pld'] #Add a Draw Percentage coloumn to data
    data['Loss%'] = data['L'] / data['Pld'] #Add a Loss Percentage coloumn to data
    
    return data
