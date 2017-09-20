import string
games = []
with open("sample.txt","r") as f:
    for line in f.readlines():
        games.append(line)
print games

for g in games:
    p1, p2 = g.split(':')
print "p1 list:"
print p1

print "p2 list:"
print p2


def closest(p1,p2):
     pl1 = 8 - p1
     pl2 = 8 - p2
     print "values"
     print pl1
     print pl2
     winner = min(pl1,pl2)
     print winner
     if pl1 == pl2:
         return "draw"
     elif winner == pl1:
         return "p1"
     elif winner == pl2:
        return "p2"

print closest(4,4)

alphabet = list(string.uppercase)

def lowestletter(p1,p2):
    print alphabet
    print "p1: ", p1, "p2: ", p2
    lowest = alphabet.index("A")
    print lowest
    pl1 = alphabet.index(p1)
    print "pl1: ", pl1
    pl2 = alphabet.index(p2)
    print "pl2: ", pl2
    winner = min(pl1, pl2)
    print winner
    if pl1 == pl2:
        print "draw"
        return "draw"
    elif winner == pl1:
        print "pl1 wins"
        return "p1"
    elif winner == pl2:
        print "pl2 wins"
        return "p2"


lowestletter('A', 'C')

