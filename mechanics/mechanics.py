from os import name
import random as rn

names=[]
surnames=[]
counts=[]

hju=2
with open("male.txt",'r') as m:
    # for line in m:
    #     names.append(line)
    names=m.read().splitlines()
with open("surnames.txt",'r') as s:
    # for line in s:
    #     surnames.append(line)
    surnames=s.read().splitlines()
with open("rng.txt",'r') as r:
    # for line in r:
    #     counts.append(line)
    counts=r.read().splitlines()
with open("staff.sql",'w') as staff:
    for count in counts:
        if(rn.randint(2,4)==2):
            a=2
        else:
            a=3
        staff.write("INSERT INTO mechanics VALUES (\'"+str(count)+"\',\'"+str(a)+"\',\'"+names[rn.randint(0,2942)]+" "+surnames[rn.randint(0,151670)]+"\',\'"+str(hju)+"\');\n")
        hju+=1