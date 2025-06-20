import sys
import pandas as pd 
import numpy as np
#np.set_printoptions(threshold=sys.maxsize)


sensor = (1,2,3,4,5,6,7) 


def read_int(FileName,x):

    #print(FileName)

    xlen = len(FileName)
    ending = FileName[xlen-4:xlen]

    if ending=='.int':
        FileName = FileName[0:xlen-4]


    with open(FileName+ending,"rb") as f:
        f.read()
        filesize = f.tell()
       # print(filesize)
       

    f.close()


    with open('0002.int',"rb") as f:

    # the first 4 junk buffer
        
        leer = np.frombuffer(f.read(4),dtype=np.single)
        #print(leer)
    # the  24 buffer give information about file
        datei = np.frombuffer(f.read(24),dtype=np.uint32)
        #print(datei)

        f.seek(76)
    # read the number of sensor in file 
        lvek = np.frombuffer(f.read(4),dtype=np.uint32)
        #print(lvek)
     
    # then 4 times the number of sensors are skipped to read a control parameter:
  
        f.seek(84+lvek[0]*4)

        filetype = np.frombuffer(f.read(4),dtype=np.uint)
        #print(filetype)

        if filetype != 12:

    # start time is read (is not equal to 0 as we have been cut off from the simulation for the first 50 s
            t0 = np.frombuffer(f.read(4),dtype=np.single)
            #print(t0)

    # comes the parameter for the step size of the simulation

            dt = np.frombuffer(f.read(4),dtype=np.single)
            #print(dt)

            pos_fak = f.tell()
            #print(pos_fak)

            fak = []
 
            for n in x:
                f.seek(pos_fak + 4*(n-1))
                fak.append(np.frombuffer(f.read(4),dtype=np.single))
                
            f.seek(pos_fak+lvek[0]*4)
            position = f.tell()
    # the length of the sensors is calculated:
            RecordCount = round((filesize-position)/lvek[0]/2)
            #print(RecordCount)

            raw_ts_int = np.empty([len(x),RecordCount])
            print(raw_ts_int)
            #print("Type:",type(raw_ts_int))
            print(raw_ts_int.shape)

            for n in range(RecordCount):

                for m, sensor_ in enumerate(x):

                    f.seek(position+2*sensor_+(lvek[0]*2)*n-2)
                    raw_ts_int[m,n] = np.frombuffer(f.read(2),dtype=np.int16)*fak[m]

            df = pd.DataFrame(raw_ts_int)

            print(df)
                    
    f.close()


read_int("0001.int",sensor)









        