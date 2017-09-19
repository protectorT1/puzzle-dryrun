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

alphabet = 

def lowestABC(p1, p2):
     
