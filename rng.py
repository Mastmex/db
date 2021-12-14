import random as rn



with open("rng.txt",'w') as r:
    for i in range(1000):
        r.write(str(rn.randint(10000,100000)))
        r.write('\n')



