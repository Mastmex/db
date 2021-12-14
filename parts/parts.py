import random as rn
partstype=["Front wing","Back wing", "Engine", "Gear box", "Suspension","Body"]
library="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def f():
    return(library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)]+library[rn.randint(0,25)])
def g():
    return(str(rn.randint(1,9))+str(rn.randint(1,9))+str(rn.randint(1,9))+str(rn.randint(1,9))+str(rn.randint(1,9)))

with open("parts.sql",'w')as p:
    for id,name in enumerate(partstype):
        p.write("INSERT INTO parts (part_type,car_num) VALUES (\'"+name+""+"\',\'66\');\n")
    for id,name in enumerate(partstype):
        p.write("INSERT INTO parts (part_type,car_num) VALUES (\'"+name+""+"\',\'15\');\n")
