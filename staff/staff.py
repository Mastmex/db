import random as rn


counts=[]


with open("rng.txt",'r') as r:
    counts=r.read().splitlines()

with open("staff1.sql",'w') as s:
    for count in counts:
        
        s.write("INSERT INTO staff (team_number) VALUES (\'"+ str(1) +"\');\n")
