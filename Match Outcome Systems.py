# -*- coding: utf-8 -*-
"""
Author: Jack Bellamy
Date: 08/03/23
Task: Match Outcome Systems
"""

#Modules Used
import random
import matplotlib.pyplot as plt

#Function will generate frequency of each match Outcome depending on system used
def outcomeStats():
    
    intAmount = 10000 #Simulation amount for each system
    uniform = False #Determine if the team 'strengths' are uniformly random or a biased generation between 0 and 1
    
    for i in range(1,4): #Iterate through each match outcome system
        ints = 0
        wins = 0
        draws = 0
        losses = 0
        
        while ints < intAmount:
            outcome = matchOutcomes(i,uniform) #Generate match outcome
            if outcome == 'Win':
                wins += 1
            elif outcome == 'Draw':
                draws += 1
            elif outcome == 'Loss':
                losses += 1
            ints += 1
            
            
        totalGames = wins + draws + losses
        winPer = wins / totalGames #Calculate relative frequency of wins
        drawPer = draws / totalGames #Calculate relative frequency of draws
        lossPer = losses / totalGames #Calculate relative frequency of losses
        ppg = ((wins * 3) + (draws * 1)) / totalGames
        
        #Numerical statistics output
        print('----------------------')
        print('Numerical  Statistics')
        print('')
        print('System',i)
        print('Win%:   ',round(winPer,6))
        print('Draw%:  ',round(drawPer,6))
        print('Loss%:  ',round(lossPer,6))
        print('Point Avg:',round(ppg,6))
        print('----------------------')
        print('')
    
        

#Loop through teams with random strength
def matchOutcomes(system,uniform):
    
    teamAmount = 20 #Amount of teams to generate
    teams = genTeams(teamAmount,uniform) #Generate teams for results system
       
    #Loop through combinations of teams possible
    for x in range(0,len(teams)): 
        for y in range(0,len(teams)):
            if x != y: #Check if team isn't itself
                if system == 1:
                    result = outcomeOne(teams[x][1],teams[y][1])    
                    return result
                elif system == 2:
                    result = outcomeTwo(teams[x][1],teams[y][1])
                    return result
                elif system == 3:
                    result = outcomeThree(teams[x][1],teams[y][1])
                    return result
    
#Generate teams for system
def genTeams(n,uniform):
    
    teams = []
    
    for x in range(0,n):
        tProb = probSystem(uniform) #Generate team 'strength' 
        teams.append([x+1,tProb])
    return teams
    
#Generate team 'stength' using certain mmethod    
def probSystem(uniformRandom):
    
    if uniformRandom == True:
        probability = random.random()
        return probability
    else:
        probability = random.normalvariate(0.457,0.144) #Mu and Sigma come from 'PPG Anaylsis.py', and are the PPG Mean and Stdev divided by 3
        if probability < 0:
            probability = 0
        elif probability > 1:
            probability = 1
        return probability


### Outcome Systems
  
def outcomeOne(p1,p2):
    
    t1 = p1 ; t2 = p2 ; r = random.random() + 0.25
    
    if t1 + t2 < r:
        return 'Draw'
    
    elif t1 + t2 + r < 1.85:
        return 'Win'
    
    elif t1 + t2 + r > 1.85:
        return 'Loss'
    
def outcomeTwo(p1,p2):
    
    #r from team probs is changed to a statis 'r'
    
    r = 0.18
    
    if p1 > p2 + r:
        return 'Win'
    elif p2 > p1 + r:
        return 'Loss'
    else:
        return 'Draw'
        
def outcomeThree(p1,p2):
    
    r = random.random()
    d = 0.125
    t1 = abs(p1-r) ; t2 = abs(p2-r)
    
    if abs(t1-t2) < d:
        return 'Draw'
    else:
        if t1 < t2:
            return 'Win'
        else:
            return 'Loss'

