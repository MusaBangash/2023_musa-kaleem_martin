import read_data as rd
import os
import pandas as pd
from pathlib import Path
import numpy as np
import feather

sensor=(1,2,3,4,5,7,8,9,10)

folder_path= r'C:\Users\musab\OneDrive\Desktop\Test'
merg_df=pd.DataFrame()

list_of_files=os.listdir(folder_path)
#number=[]
for file_name in list_of_files:

    #if '.int' in file_name:
    if file_name[-4:] == '.int': 
     print(file_name)

     rd.read_int(file_name,sensor)
     new_name=file_name[:-4]+'.feather'
     rd.df.to_csv(new_name)
     
    
     #df=rd.df.rename(columns={1:'1'})
     #feather.write_dataframe(rd.df,'data.feather')
    # exp_data=rd.df.to_feather('yaw_0.feather')
     
       

  










#rd.read_int("0001.int", sensor)




