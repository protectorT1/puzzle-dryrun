#!/usr/bin/python

import string

games = []
with open("sample.txt","r") as f:
    for line in f.readlines():
        games.append(line)

def results():
    allResults = ""
    p1 = []
    p2 = []
    for g in games:
        pl1, pl2 = g.split(':')
        p1 = pl1.split(',')
        p2 = pl2.split(',')
        print "p1: ", p1
        print "p2: ", p2
        allResults+=str(Game(p1,p2))
        print "all: ",allResults
    return allResults


def getSum(list):
    sum = 0
    i = 1
    print "list: ", type(list)
    for v in list:
        print "v: ", type(v)
        print "v1: ", v[1]
        print "v after: ", v
        num = str(v[1])
        if num.isdigit() == True:
            print "num: ",num
            sum = sum + int(num)
            print "sum: ", sum
            print "i before: ", i
            i = i + 1
            print "i after: ", i
    return sum

def closest(p1,p2):
     player1 = getSum(p1)
     print "player1 sum done"
     player2 = getSum(p2)
     print "player2 sum done"
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
    clist = []
    for l in list:
        if l[1].isalpha() == True:
            clist.append(l)
    if clist != []:
        for l in clist:
            lowest = alphabet.index("A")
            let = alphabet.index(l[1])
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
    print "player1 ", player1, " player2: ", player2 
    if player1 == '' and player2 == '':
        return "draw"
    if player1 == '' and player2 != '':
        return "p2"
    elif player2 == '' and player1 != '':
        return "p1"
    elif player1 != '' and player2 != '':
        pl1 = alphabet.index(player1)
        pl2 = alphabet.index(player2)
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
    
    highest = [highestscp1,highestscp2]
    print "highest", highest
    finalcol = findHighest(highest,0,colours)
    finalwinner = findHighest(finalcol)
    if finalwinner == highestscp1:
        return "p1"
    elif finalwinner == highestscp2:
        return "p2"

def findHighest(list,x,valuelist):
    values = {}
    for l in list:
        print "l", l
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
    print "round winner: "
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

# print Game(['g6'],['y6'])
print closest(['g6'],['y6'])
print lowestletter(['g6'],['y6'])
print highestScores(['g6'],['y6'])


# print "results: ", results()
