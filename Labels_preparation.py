import os
import numpy as np
import pandas as pd
import csv 
labels_input = '/media/amrgaballah/Seagate Backup Plus Drive/IEMOCAP/labels/'
output = '/media/amrgaballah/Seagate Backup Plus Drive/IEMOCAP/labels_pre/'
if not os.path.exists(output):
    os.makedirs(output)
for path1 in os.listdir(labels_input):
    path2 = os.path.join(labels_input,path1)
    f = open(path2, "r")
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
    df = pd.DataFrame([sub.split(";") for sub in out2])
    df.to_csv(output+path1.split('.')[0]+'.csv', index=False)
