# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 16/03/23
Task: Simple Match Outcome System
"""

#Modules used
import numpy as np
import statistics
import random



#Generate mass amount of results for matchOutcome system
def massResults(bufferMax):
    
    teamAmount = 20 #Amount of individual teams
    interations = 150 #Amount of total iterations
    
    #Counts and variables
    winPer   = []
    drawPer  = []
    lossPer  = []
    totalGames = 0
    ints = 0
    
    while ints < interations:
        teamList = genTeams(teamAmount) #Gen unique teamList for each loop
        win = 0
        draw = 0
        loss = 0
        for x in range(0,len(teamList)): #Loop through all teams as 'team1' team
            for y in range(0,len(teamList)): #Loop through all teams as 'team2' team
                if x != y:
                    result = matchOutcome(teamList[x],teamList[y],bufferMax) #Gen matchOutcome for team x and team y
                    if result == 'Win':
                        win += 1
                    elif result == 'Draw':
                        draw += 1
                    elif result == 'Loss':
                        loss += 1             
        
        games = win + draw + loss
        winPer.append(win / games)
        drawPer.append(draw / games)
        lossPer.append(loss / games)
        ints += 1
    
    print(statistics.mean(winPer))
    print(statistics.mean(drawPer))
    print(statistics.mean(lossPer))
    print('')
    print(statistics.stdev(winPer))
    print(statistics.stdev(drawPer))
    print(statistics.stdev(lossPer))
    
    # return [winPer,drawPer,lossPer]         

#Create random match outcome using the teams strength values
def matchOutcome(team1,team2,bufferMax):
    
    strength1 = team1[1] #Get strength value from team1's list
    strength2 = team2[1] #Get strength value from team2's list
    
    buffer = random.uniform(0,bufferMax)
    
    #Logic for generating result of game
    if strength1 > strength2 + buffer:
        return 'Win'
    elif strength2 > strength1 + buffer:
        return 'Loss'
    else:
        return 'Draw'
    
#Generate teams with label and 'strenght' value from normal distribution for 'n' amount of teams
def genTeams(n):
    
    teams = [] #List of teams to be generated
    
    while len(teams) < n:
        strength = 2 * np.random.normal(0,1) #Generate random number from random distribution
        if strength > 0: #Restrict normal distribution to postive values
            team = [len(teams)+1,strength] #Create team list of label and strength value
            teams.append(team) #Append team info to teams list
            
    return teams
            
        