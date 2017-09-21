#!/usr/bin/python

import string

games = []
with open("sample.txt","r") as f:
    for line in f.readlines():
        games.append(line)

for g in games:
    p1, p2 = g.split(':')

def results():
    allResults = ""
    for g in games:
        p1, p2 = g.split(':')
        allResults+=str(Game(p1,p2))


def getSum(list):
    sum = 0
    numlist = []
    for v in list:
        if v[1].isdigit() == True:
            numlist.append(v[1])
    print "numbers: ", numlist
    for v in list:
        print "original: ", v[1]
        num = str(v[1])
        print "num: ", num
        if num.isdigit() == True:
            sum = sum + int(v[1])
    return sum

def closest(p1,p2):
     player1 = getSum(p1)
     player2 = getSum(p2)
     pl1 = 8 - player1
     pl2 = 8 - player2
     winner = min(pl1,pl2)
     if pl1 == pl2:
         return "draw"
     elif winner == pl1:
         return "p1"
     elif winner == pl2:
        return "p2"

alphabet = ['A','B','C']
colours = ['r','b','g','y']
token = ['A','B','C','9','8','7','6','5','4','3','2','1']

def findLowestLetterInList(list):
    letters = {}
    i = 0
    for l in list:
        lowest = alphabet.index("A")
        let = alphabet.index(l)
        letters[let] = l  
        i = i + 1

    winner = min(letters.keys())
    ans = letters[winner]
    return ans

def lowestletter(p1,p2):
    player1 = findLowestLetterInList(p1)
    player2 = findLowestLetterInList(p2)
    lowest = alphabet.index("A")
    pl1 = alphabet.index(player1)
    pl2 = alphabet.index(player2)
    winner = min(pl1, pl2)
    if pl1 == pl2:
        print "draw"
        return "draw"
    elif winner == pl1:
        return "p1"
        print "p1"
    elif winner == pl2:
        return "p2"
        print "p2"

print lowestletter(['A'], ['B','C'])

def highestScores(p1, p2):
    highestcp1 = findHighest(p1,0,colours)
    highestscp1 = findHighest(p1,1,token)

    highestcp2 = findHighest(p2,0,colours)
    highestscp2 = findHighest(p2,1,token)
    
    highest = [highestscp1,highestscp2]
    finalcol = findHighest(highest)
    finalwinner = findHighest(finalcol)
    print "final", finalwinner
    if finalwinner == highestscp1:
        return "p1"
    elif finalwinner == highestscp2:
        return "p2"

def findHighest(list,x,valuelist):
    values = {}
    for l in list:
        i =  valuelist.index(l[x])
        values[i] = l[x]
    highest = min(values.keys())
    winner = values[highest]
    final = []
    for l in list:
        if winner in l:
            final.append(l) 
    return final

def Game(p1,p2):
    round1 = closest(p1,p2)
    if round1 == "p1":
        return 0
    elif round1 == "p2":
        return 1
    elif round1 == "draw":
        round2 = lowestletter(p1,p2)
        if round1 == "p1":
            return 0
        elif round1 == "p2":
            return 1
        elif round1 == "draw":
            round3 = highestScores(p1,p2)
            if round1 == "p1":
                return 0
            elif round1 == "p2":
                return 1
print "Game: "
print "expected: 0 - p1"
print Game(['r1','b2','bA'], ['gA'])

print results()
