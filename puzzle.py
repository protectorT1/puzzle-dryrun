#!/usr/bin/python

import string

games = []
with open("SAPchallenge.txt","r") as f:
    for line in f.readlines():
        games.append(line)

def results():
    allResults = ""
    p1 = []
    p2 = []
    i = 0
    for g in games:
        pl1, pl2 = g.split(':')
        p1 = pl1.split(',')
        p2 = pl2.split(',')
        allResults+=str(Game(p1,p2))
        print "ROUND FINISHED: "
        i = i + 1
    print "NoOfRounds: ", i
    return allResults

def getSum(list):
    sum = 0
    for v in list:
        for i in v:
            num = str(i)
            if num.isdigit() == True:
                sum = sum + int(num)
    return sum

def closest(p1,p2):
     player1 = getSum(p1)
     player2 = getSum(p2)
     ply1 = abs(player1) - 8
     ply2 = abs(player2) -8
     pl1 = abs(ply1)
     pl2 = abs(ply2)
     winner = min(pl1,pl2)
     if pl1 == pl2:
         return "draw"
     elif winner == pl1:
         return "p1"
     elif winner == pl2:
        return "p2"

colours = ['r','b','g','y']
token = ['A','B','C','9','8','7','6','5','4','3','2','1']

def findLowestLetterInList(list):
    letters = {}
    i = 0
    clist = []
    for l in list:
        if l[1].isalpha() == True:
            clist.append(l)
    if clist != []:
        for l in clist:
            let = token.index(l[1])
            letters[let] = l[1]
            i = i + 1
        winner = min(letters.keys())
        ans = letters[winner]
    else:
        ans = ''
    return ans

def lowestletter(p1,p2):
    player1 = findLowestLetterInList(p1)
    player2 = findLowestLetterInList(p2)
    if player1 == '' and player2 == '':
        return "draw"
    if player1 == '' and player2 != '':
        return "p2"
    elif player2 == '' and player1 != '':
        return "p1"
    elif player1 != '' and player2 != '':
        pl1 = token.index(player1)
        pl2 = token.index(player2)
        winner = min(pl1, pl2)
        if pl1 == pl2:
            return "draw"
        elif winner == pl1:
            return "p1"
        elif winner == pl2:
            return "p2"

def highestScores(p1, p2):
    highestcp1 = findHighest(p1,0,colours)
    highestscp1 = findHighest(p1,1,token)
    highestcp2 = findHighest(p2,0,colours)
    highestscp2 = findHighest(p2,1,token)
    highest = [] 
    for i in highestscp1:
        highest.append(i)
    for i in highestscp2:
        highest.append(i)
    finalcol = findHighest(highest,0,colours)
    if len(finalcol) > 1:
        finalwinner = findHighest(finalcol,0,colours)
    else:
        finalwinner = finalcol
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
    result = roundresult(1,round1)
    if result == "draw":
        round2 = lowestletter(p1,p2)
        result = roundresult(2,round2)
        if result == "draw":
            round3 = highestScores(p1,p2)
            result = roundresult(3,round3)
    return result

def roundresult(roundno, result):
    round = "round", roundno
    if result == "p1":
        print "p1 wins ", round
        return 0
    elif result == "p2":
        print "p2 wins ", round
        return 1
    elif result == "draw":
        print "draw ", round
        return "draw"

print results()
