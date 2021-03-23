import os
import numpy as np
import pandas as pd
import csv 
labels = '/media/amrgaballah/Seagate Backup Plus Drive/IEMOCAP/labels'
f = open(path, "r")
out = []
for line in f:
    
   
    if line.startswith('['):

        out.append(line.rstrip())

# print(out)    
f.close()

out2 = []
for i in out:
    a = i.replace("\t", ";")
    out2.append(a)
print(out2)    
df = pd.DataFrame(out2)
df.to_csv('/home/amrgaballah/Desktop/csvfile11.csv', index=False)
