import os
import random as rd
from tqdm import tqdm

nth_random_reverse = [0,0,0]
parameters = ["", "-R", "-nr"]
# for x in range(10000, 50001, 10000):
for x in range(10000, 50001, 10000):
    

    
    for y in range(len(parameters)):    
        
        # for z in tqdm(range(rd.randint(1,1000))):
        for z in tqdm(range(100)):
            #linux
            # os.system(f"seq {x} | sort -R | time -o temp -f \"%U\" ./sortIntList")
            
            #mac
            os.system(f"seq {x} | sort {parameters[y]} | gtime -o temp -f \"%U\" ./sortIntList")
            
            rd = open("temp", "r").read()
            nth_random_reverse[y] += float(rd)

        nth_random_reverse[y] /= 10000;

                
            

os.system("rm temp")
print(nth_random_reverse)
#print(sortintlist)
    #print(f"Input size:{x}, Initial Order: {y}, Number of Runs: {z}\nAverage Time for sortIntList: , Average Time for sort ")
