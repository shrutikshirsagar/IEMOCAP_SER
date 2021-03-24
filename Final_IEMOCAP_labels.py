import numpy as np
import pandas as pd
import os

file1 = '/media/amrgaballah/Seagate Backup Plus Drive/IEMOCAP/labels_pre/'
out_cols = ['filename', 'valence','Arousal', 'Dominance'] 
final_vec = np.empty((0, 4))
for filename in os.listdir(file1):
    df = pd.read_csv(os.path.join(file1,filename))
    print(df.shape)
    df2 = df.iloc[:,1]
    df1 = df.iloc[:,3]

    df4 = df.iloc[:,3].map(lambda x: x.lstrip('[').rstrip(']'))


    a = pd.DataFrame([sub.split(",") for sub in df4])
    print(a.shape)

    out_vec = np.hstack((df2[:, None],a))
    final_vec = np.vstack((final_vec,out_vec))
df22 = pd.DataFrame(final_vec, columns = out_cols)
df22.to_csv('/media/amrgaballah/Seagate Backup Plus Drive/IEMOCAP/'+ 'final_labels.csv', index=False)
