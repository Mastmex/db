import random as rn
library="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def f():
    return(library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)])
def g():
    return(rn.randint(10000,99999))

with open("./training_station/training_station.sql",'w')as p:
    for i in range(5):
        fh=f()
        gh=g()
        p.write("INSERT INTO training_station VALUES (\'"+str(gh)+"\',\'"+str(i)+"\',\'"+fh+"\',\'5134784\');\n")
